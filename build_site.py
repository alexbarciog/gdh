# -*- coding: utf-8 -*-
"""Construieste site-ul GDH de la zero, in ./dist.

Nu mai pleaca de la snapshot-ul Webflow: paginile se scriu din componentele din
ui_gdh.py, cu sistemul vizual din theme_gdh.py si continutul din content_gdh.py
plus pages_data_gdh.py.

Ruleaza:  python3 build_site.py
"""
import hashlib
import os
import re
import shutil

import content_gdh as C
import site_gdh as S
import theme_gdh as T
from build_gdh import download          # doar ajutorul de descarcare cu cache

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SRC, "dist")
CACHE = os.path.join(SRC, ".dlcache")

ROBOTO_CSS = ("https://fonts.googleapis.com/css2?"
              "family=Roboto:wght@400;500;600;700&display=swap")


def log(*a):
    print(*a, flush=True)


# --------------------------------------------------------------------- 1
def prepare():
    keep = {".git", ".gitignore", ".gitattributes", ".wrangler"}
    if os.path.exists(OUT):
        for entry in os.listdir(OUT):
            if entry in keep:
                continue
            p = os.path.join(OUT, entry)
            try:
                shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
            except OSError as e:
                log("  ! nu s-a putut sterge", entry, e)
    for d in ("css", "js", "img", "fonts"):
        os.makedirs(os.path.join(OUT, d), exist_ok=True)


# --------------------------------------------------------------------- 2
def build_fonts():
    """Roboto, adus local. Zero cereri catre Google din pagina publicata."""
    css = download(ROBOTO_CSS).decode("utf-8")
    blocks = re.findall(r"/\*\s*([a-z-]+)\s*\*/\s*(@font-face\s*\{.*?\})", css, re.S)
    out, files = [], {}
    for subset, block in blocks:
        if subset not in ("latin", "latin-ext"):
            continue
        m = re.search(r"url\((https://[^)]+)\)", block)
        if not m:
            continue
        data = download(m.group(1))
        weight = re.search(r"font-weight:\s*(\d+)", block)
        weight = weight.group(1) if weight else "400"
        fn = "roboto-%s-%s.woff2" % (weight, subset)
        if fn not in files:
            open(os.path.join(OUT, "fonts", fn), "wb").write(data)
            files[fn] = len(data)
        block = block.replace(m.group(0), "url(../fonts/%s)" % fn)
        block = block.replace("font-family: 'Roboto'", "font-family: 'GDH Roboto'")
        block = block.replace('font-family: "Roboto"', "font-family: 'GDH Roboto'")
        block = block.replace("font-style: normal;", "font-style: normal;\n  font-display: swap;")
        out.append(block)
    open(os.path.join(OUT, "css", "fonts.css"), "w", encoding="utf-8").write(
        "/* Roboto - gazduit local, fara conexiuni externe */\n" + "\n".join(out) + "\n")
    log("  fonturi Roboto: %d declaratii, %d fisiere (%d KB)"
        % (len(out), len(files), sum(files.values()) // 1024))


# --------------------------------------------------------------------- 3
def build_css():
    sheet = T.css()
    # fonturile intra in aceeasi foaie: o cerere in loc de doua
    fonts = open(os.path.join(OUT, "css", "fonts.css"), encoding="utf-8").read()
    open(os.path.join(OUT, "css", "site.css"), "w", encoding="utf-8").write(fonts + sheet)
    os.remove(os.path.join(OUT, "css", "fonts.css"))
    log("  css: %d KB" % ((len(fonts) + len(sheet)) // 1024))


def build_js():
    shutil.copy2(os.path.join(SRC, "site_js_gdh.js"), os.path.join(OUT, "js", "site.js"))
    log("  js: %d KB" % (os.path.getsize(os.path.join(OUT, "js", "site.js")) // 1024))


# --------------------------------------------------------------------- 4
def build_logo():
    import logo_gdh as LG
    meta = LG.build(os.path.join(SRC, "gdh-logo-source.png"), os.path.join(OUT, "img"))
    log("  sigla: %dx%d, marca %dx%d" % (meta["w"], meta["h"], meta["mark"][0], meta["mark"][1]))


def build_brand_assets():
    import assets_gdh as A
    fonts = A.load_fonts(OUT, os.path.join(CACHE, "ttf"))
    A.build_icons(OUT, fonts)
    A.build_og(OUT, fonts,
               C.HOME["title"],
               "Retail distribution · Dental distribution · Shelf execution",
               C.SITE_URL.split("//")[-1], None)
    A.build_manifest(OUT, C.SITE_NAME, "GDH")
    log("  favicon + iconite + og-image")


# --------------------------------------------------------------------- 5
def load_pages_data():
    try:
        import pages_data_gdh
        return pages_data_gdh.PAGES
    except Exception as e:                       # pragma: no cover
        log("  ! pages_data_gdh lipseste (%s) — se construiesc doar paginile scrise" % e)
        return []


# --------------------------------------------------------------------- 6
def fingerprint():
    """Amprenta continutului in numele css/js, ca sa nu ramana cache vechi."""
    renames = {}
    for sub in ("css", "js"):
        for name in sorted(os.listdir(os.path.join(OUT, sub))):
            src = os.path.join(OUT, sub, name)
            if not os.path.isfile(src):
                continue
            digest = hashlib.md5(open(src, "rb").read()).hexdigest()[:8]
            stem, ext = os.path.splitext(name)
            new = "%s.%s%s" % (stem, digest, ext)
            os.rename(src, os.path.join(OUT, sub, new))
            renames["%s/%s" % (sub, name)] = "%s/%s" % (sub, new)
    for fn in os.listdir(OUT):
        if not fn.endswith(".html"):
            continue
        fp = os.path.join(OUT, fn)
        doc = open(fp, encoding="utf-8").read()
        for old, new in renames.items():
            doc = doc.replace(old, new)
        open(fp, "w", encoding="utf-8").write(doc)
    log("  amprenta pe %d fisiere" % len(renames))


if __name__ == "__main__":
    log("1/7 pregatesc dist/")
    prepare()
    log("2/7 fonturi")
    build_fonts()
    log("3/7 css + js")
    build_css()
    build_js()
    log("4/7 sigla")
    build_logo()
    log("5/7 pagini")
    pages = S.build_all(OUT, load_pages_data())
    S.deploy_files(OUT, pages)
    log("  pagini scrise: %d" % len(pages))
    log("6/7 iconite si imagine de partajare")
    build_brand_assets()
    log("7/7 amprenta")
    fingerprint()
    log("gata -> dist/")
