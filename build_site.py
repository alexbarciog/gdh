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

# Inter Tight tine locul lui Creato Display din referinta (acelasi grotesc
# strans, dar sub licenta OFL); IBM Plex Mono e chiar fontul de etichete al
# referintei. Numele de familie publice sunt ale noastre: 'GDH Sans', 'GDH Mono'.
FONT_CSS = ("https://fonts.googleapis.com/css2?"
            "family=Inter+Tight:wght@400;500;600;700"
            "&family=IBM+Plex+Mono:wght@400;500&display=swap")
FAMILIES = {"Inter Tight": ("GDH Sans", "sans"), "IBM Plex Mono": ("GDH Mono", "plexmono")}


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
    """Inter Tight si IBM Plex Mono, aduse local. Zero cereri catre Google din
    pagina publicata."""
    css = download(FONT_CSS).decode("utf-8")
    blocks = re.findall(r"/\*\s*([a-z-]+)\s*\*/\s*(@font-face\s*\{.*?\})", css, re.S)
    out, files, by_digest = [], {}, {}
    for subset, block in blocks:
        if subset not in ("latin", "latin-ext"):
            continue
        m = re.search(r"url\((https://[^)]+)\)", block)
        fam = re.search(r"font-family:\s*'([^']+)'", block)
        if not m or not fam or fam.group(1) not in FAMILIES:
            continue
        public, stem = FAMILIES[fam.group(1)]
        data = download(m.group(1))
        weight = re.search(r"font-weight:\s*(\d+)", block)
        weight = weight.group(1) if weight else "400"
        # Inter Tight vine ca font variabil: acelasi fisier pentru toate
        # grosimile, deci il salvam o data si il refolosim. Fisierele mono nu
        # poarta cifre in nume, ca assets_gdh.load_fonts sa nu le ia drept sans.
        digest = hashlib.md5(data).hexdigest()
        if digest in by_digest:
            fn = by_digest[digest]
        else:
            if stem == "sans":
                fn = "sans-%s-%s.woff2" % (weight, subset)
            else:
                fn = "%s-%s-%s.woff2" % (stem, "medium" if weight == "500" else "regular", subset)
            open(os.path.join(OUT, "fonts", fn), "wb").write(data)
            files[fn] = len(data)
            by_digest[digest] = fn
        block = block.replace(m.group(0), "url(../fonts/%s)" % fn)
        block = block.replace(fam.group(0), "font-family: '%s'" % public)
        block = block.replace("font-style: normal;", "font-style: normal;\n  font-display: swap;")
        out.append(block)
    open(os.path.join(OUT, "css", "fonts.css"), "w", encoding="utf-8").write(
        "/* Inter Tight + IBM Plex Mono - gazduite local, fara conexiuni externe */\n"
        + "\n".join(out) + "\n")
    log("  fonturi: %d declaratii, %d fisiere (%d KB)"
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
def copy_images():
    """Fotografiile si gradientul, din img_src/ in dist/img."""
    src = os.path.join(SRC, "img_src")
    if not os.path.isdir(src):
        log("  ! img_src lipseste — paginile se randeaza fara fotografii")
        return
    n = 0
    for fn in sorted(os.listdir(src)):
        if fn.startswith(".") or fn == "og-source.png":
            continue      # sursa cartonasului de partajare, decupata separat
        shutil.copy2(os.path.join(src, fn), os.path.join(OUT, "img", fn))
        n += 1
    log("  imagini copiate: %d" % n)


def build_logo():
    import logo_gdh as LG
    meta = LG.build(os.path.join(SRC, "gdh-logo-source.png"), os.path.join(OUT, "img"),
                    os.path.join(SRC, "gdh-mark-source.png"))
    log("  sigla: %dx%d (raport %.3f), verticala %dx%d, steaua %dx%d"
        % (meta["w"], meta["h"], meta["ratio"], meta["stacked"][0], meta["stacked"][1],
           meta["mark"][0], meta["mark"][1]))


def build_brand_assets():
    import assets_gdh as A
    fonts = A.load_fonts(OUT, os.path.join(CACHE, "ttf"))
    A.build_icons(OUT, fonts)
    # Cartonasul de partajare: imaginea de brand din img_src/og-source.png,
    # decupata central la 1200x630. Daca lipseste, il compunem din degradeul
    # bannerului si sigla verticala, ca sa nu apara niciodata sigla veche.
    from PIL import Image
    tw, th = 1200, 630
    supplied = os.path.join(SRC, "img_src", "og-source.png")
    source = supplied if os.path.exists(supplied) else os.path.join(SRC, "img_src", "banner-poster.webp")
    bg = Image.open(source).convert("RGB")
    scale = max(tw / bg.width, th / bg.height)
    bg = bg.resize((round(bg.width * scale), round(bg.height * scale)), Image.LANCZOS)
    left, top = (bg.width - tw) // 2, (bg.height - th) // 2
    card = bg.crop((left, top, left + tw, top + th)).convert("RGBA")
    if source != supplied:
        card = Image.alpha_composite(card, Image.new("RGBA", (tw, th), (0, 0, 0, 96)))
        logo = Image.open(os.path.join(OUT, "img", "gdh-logo-stacked-light.png")).convert("RGBA")
        lh = 330
        logo = logo.resize((round(logo.width * lh / logo.height), lh), Image.LANCZOS)
        card.alpha_composite(logo, ((tw - logo.width) // 2, (th - lh) // 2))
    card.convert("RGB").save(os.path.join(OUT, "img", "og-image.jpg"), "JPEG",
                             quality=88, optimize=True)
    log("  imagine de partajare: %s" % ("img_src/og-source.png" if source == supplied
                                        else "compusa din banner + sigla"))
    A.build_manifest(OUT, C.SITE_NAME, "GDH")
    log("  favicon + iconite + og-image")


# --------------------------------------------------------------------- 5
def load_pages_data():
    try:
        import pages_data_gdh
        pages = pages_data_gdh.PAGES
        for i, entry in enumerate(pages):
            entry["rhythm"] = i % 3
        return pages
    except Exception as e:                       # pragma: no cover
        log("  ! pages_data_gdh lipseste (%s) — se construiesc doar paginile scrise" % e)
        return []


# --------------------------------------------------------------------- 6
def fingerprint():
    """Amprenta continutului in numele fisierelor statice.

    `_headers` le tine un an, ca `immutable`. Daca numele nu se schimba, o
    imagine inlocuita nu mai ajunge niciodata la cine a vazut-o o data — nici
    prin browser, nici prin reteaua Cloudflare. Sigla noua a stat asa doua
    publicari la rand. Cu numele legat de continut, un fisier schimbat capata
    alta adresa si problema nu mai poate aparea.

    favicon.ico ramane la radacina cu numele lui: browserele il cer pe
    conventie, fara sa se uite in HTML.
    """
    renames = {}

    def stamp(sub, name):
        src = os.path.join(OUT, sub, name)
        if not os.path.isfile(src):
            return
        digest = hashlib.md5(open(src, "rb").read()).hexdigest()[:8]
        stem, ext = os.path.splitext(name)
        new = "%s.%s%s" % (stem, digest, ext)
        os.rename(src, os.path.join(OUT, sub, new))
        renames["%s/%s" % (sub, name)] = "%s/%s" % (sub, new)
        if sub in ("css", "js"):
            # copie cu numele vechi, pentru o fila ramasa deschisa pe un build
            # anterior; paginile proaspete trimit la numele cu amprenta
            shutil.copy2(os.path.join(OUT, sub, new), os.path.join(OUT, sub, name))

    for sub in ("css", "js", "img"):
        for name in sorted(os.listdir(os.path.join(OUT, sub))):
            stamp(sub, name)

    # rescriem referintele peste tot: HTML, CSS, manifest, sitemap. Formele
    # relative (img/x.png) si absolute (https://.../img/x.png) contin amandoua
    # sirul "img/x.png", deci o singura inlocuire le prinde pe amandoua.
    targets = []
    for root, _dirs, files in os.walk(OUT):
        if os.sep + ".git" in root:
            continue
        for fn in files:
            if fn.endswith((".html", ".css", ".xml", ".webmanifest", ".txt", ".json")):
                targets.append(os.path.join(root, fn))

    ordered = sorted(renames.items(), key=lambda kv: len(kv[0]), reverse=True)
    for path in targets:
        text = open(path, encoding="utf-8").read()
        before = text
        for old_ref, new_ref in ordered:
            text = text.replace(old_ref, new_ref)
        if text != before:
            open(path, "w", encoding="utf-8").write(text)
    log("  amprenta pe %d fisiere (css/js/img)" % len(renames))


if __name__ == "__main__":
    log("1/7 pregatesc dist/")
    prepare()
    log("2/7 fonturi")
    build_fonts()
    log("3/7 css + js")
    build_css()
    build_js()
    log("4/7 sigla si imagini")
    build_logo()
    copy_images()
    log("5/7 pagini")
    pages = S.build_all(OUT, load_pages_data())
    import seo_gdh
    seo_gdh.check([p for p in pages if p.endswith(".html")])
    log("  titluri si descrieri: %d, toate unice" % len(seo_gdh.SEO))
    S.deploy_files(OUT, pages)
    log("  pagini scrise: %d" % len(pages))
    log("6/7 iconite si imagine de partajare")
    build_brand_assets()
    log("7/7 amprenta")
    fingerprint()
    log("gata -> dist/")
