# -*- coding: utf-8 -*-
"""
Build GDH — Global Distribution Holdings.

Ia snapshot-ul Webflow (Frevanta) din folderul curent si produce in ./dist un
site complet static, fara nicio resursa externa si fara nicio urma de Webflow,
gata de urcat pe Cloudflare Pages.

Ruleaza:  python build_gdh.py
"""
import os, re, shutil, html, urllib.request, hashlib, json, sys

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SRC, "dist")
FILES = "Frevanta – Webflow HTML Website Template_files"
CSS_IN = os.path.join(SRC, FILES, "frevanta.webflow.shared.4de84eec5.css")
FONTS_IN = os.path.join(SRC, FILES, "fonts.css")

PAGES = {
    "index.html": "index.html",
    "service.html": "service.html",
    "case-study.html": "case-study.html",
    "blog.html": "blog.html",
    "contact.html": "contact.html",
}

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}
_cache = os.path.join(SRC, ".dlcache")


def log(*a):
    print(*a, flush=True)


def download(url):
    os.makedirs(_cache, exist_ok=True)
    key = hashlib.sha1(url.encode()).hexdigest() + os.path.splitext(url.split("?")[0])[1]
    p = os.path.join(_cache, key)
    if os.path.exists(p):
        return open(p, "rb").read()
    req = urllib.request.Request(url, headers=UA)
    data = urllib.request.urlopen(req, timeout=60).read()
    open(p, "wb").write(data)
    return data


def safe_name(name):
    name = urllib.parse.unquote(name) if hasattr(urllib, "parse") else name
    name = name.replace("–", "-").replace("—", "-")
    name = re.sub(r"[^A-Za-z0-9._-]+", "-", name)
    name = re.sub(r"-{2,}", "-", name).strip("-.")
    return name.lower()


import urllib.parse  # noqa: E402


# --------------------------------------------------------------------------
# 1. structura de iesire
# --------------------------------------------------------------------------
def prepare():
    # OneDrive tine uneori un handle pe folder, deci golim continutul in loc sa
    # stergem folderul in sine
    keep = {".git", ".gitignore", ".gitattributes"}
    if os.path.exists(OUT):
        for entry in os.listdir(OUT):
            if entry in keep:          # dist e si copia de lucru git a site-ului
                continue
            p = os.path.join(OUT, entry)
            try:
                shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
            except OSError as e:
                log("  ! nu s-a putut sterge", entry, e)
    else:
        os.makedirs(OUT)
    for d in ("css", "js", "img", "fonts"):
        os.makedirs(os.path.join(OUT, d), exist_ok=True)


# --------------------------------------------------------------------------
# 2. imagini din snapshot -> dist/img cu nume curate
# --------------------------------------------------------------------------
IMG_MAP = {}


def collect_images():
    roots = [os.path.join(SRC, FILES), os.path.join(SRC, FILES, "images"),
             os.path.join(SRC, "blog_files"), os.path.join(SRC, "blog_files", "images"),
             os.path.join(SRC, "service_files"), os.path.join(SRC, "service_files", "images"),
             os.path.join(SRC, "contact_files"), os.path.join(SRC, "contact_files", "images"),
             os.path.join(SRC, "case-study_files"), os.path.join(SRC, "case-study_files", "images")]
    seen = {}
    for root in roots:
        if not os.path.isdir(root):
            continue
        for fn in os.listdir(root):
            fp = os.path.join(root, fn)
            if not os.path.isfile(fp):
                continue
            ext = os.path.splitext(fn)[1].lower()
            if ext not in (".webp", ".png", ".jpg", ".jpeg", ".svg", ".gif", ".json", ".avif"):
                continue
            # taie prefixul de id webflow (24 hex + _)
            base = re.sub(r"^[0-9a-f]{24}_", "", fn)
            new = safe_name(base)
            if not new:
                new = safe_name(fn)
            digest = hashlib.md5(open(fp, "rb").read()).hexdigest()
            if new in seen and seen[new] != digest:
                stem, e = os.path.splitext(new)
                new = "%s-%s%s" % (stem, digest[:6], e)
            seen[new] = digest
            dst = os.path.join(OUT, "img", new)
            if not os.path.exists(dst):
                shutil.copy2(fp, dst)
            IMG_MAP[fn] = "img/" + new
    log("  imagini copiate:", len(set(IMG_MAP.values())))


# --------------------------------------------------------------------------
# 3. fonturi Google (Inter Tight) -> local, doar latin + latin-ext
# --------------------------------------------------------------------------
def build_fonts():
    css = open(FONTS_IN, encoding="utf-8").read()
    blocks = re.findall(r"/\*\s*([a-z-]+)\s*\*/\s*(@font-face\s*\{.*?\})", css, re.S)
    out = []
    n = 0
    # Google serveste Inter Tight ca font variabil: acelasi fisier pentru toate
    # cele cinci grosimi. Numim fisierul dupa continut, nu dupa grosime, ca sa
    # nu salvam de cinci ori aceiasi octeti (525 KB degeaba).
    files = {}
    for subset, block in blocks:
        if subset not in ("latin", "latin-ext"):
            continue
        m = re.search(r"url\((https://[^)]+)\)", block)
        if not m:
            continue
        data = download(m.group(1))
        fn = "inter-tight-%s-%s.woff2" % (subset, hashlib.md5(data).hexdigest()[:8])
        if fn not in files:
            open(os.path.join(OUT, "fonts", fn), "wb").write(data)
            files[fn] = len(data)
        block = block.replace(m.group(0), "url(../fonts/%s)" % fn)
        block = block.replace("font-style: normal;", "font-style: normal;\n  font-display: swap;")
        out.append(block)
        n += 1
    open(os.path.join(OUT, "css", "fonts.css"), "w", encoding="utf-8").write(
        "/* Inter Tight - gazduit local, fara conexiuni externe */\n" + "\n".join(out) + "\n")
    log("  fonturi Inter Tight: %d declaratii, %d fisiere (%d KB)"
        % (n, len(files), sum(files.values()) // 1024))


# --------------------------------------------------------------------------
# 4. CSS: descarca resursele remote, redenumeste clasele Webflow
# --------------------------------------------------------------------------
def w_rename(text):
    """Redenumeste prefixele de clasa Webflow: w- -> g-, wf- -> gf-."""
    text = re.sub(r"\bwebflow-icons\b", "gdh-icons", text)
    text = re.sub(r"(?<![\w-])w--(?=[a-z])", "g--", text)
    text = re.sub(r"(?<![\w-])w-(?=[a-z])", "g-", text)
    text = re.sub(r"(?<![\w-])wf-(?=[a-z])", "gf-", text)
    return text


def build_css():
    css = open(CSS_IN, encoding="utf-8").read()

    # atentie: unele nume de fisiere contin paranteze codate (%20(1)), deci
    # oprirea la primul ')' ar taia URL-ul in doua
    urls = sorted(set(re.findall(r'url\("(https?://[^"]+)"\)', css)))
    for u in urls:
        try:
            data = download(u)
        except Exception as e:                     # pragma: no cover
            log("  ! nu s-a putut descarca", u, e)
            continue
        base = urllib.parse.unquote(u.split("/")[-1].split("?")[0])
        base = re.sub(r"^[0-9a-f]{24}_", "", base)
        new = safe_name(base)
        sub = "fonts" if new.endswith((".otf", ".ttf", ".woff", ".woff2")) else "img"
        open(os.path.join(OUT, sub, new), "wb").write(data)
        css = css.replace('url("%s")' % u, 'url("../%s/%s")' % (sub, new))
    log("  resurse CSS aduse local:", len(urls))

    # regulile pentru insigna "Made in Webflow" nu au ce cauta aici
    css = re.sub(r"[^{}]*\.w-webflow-badge[^{}]*\{[^}]*\}", "", css)
    # rosul GDH in locul portocaliului din sablon, peste tot in CSS
    # si forma pe 8 cifre, cu alfa (#fe3e0280), nu doar cea pe 6
    css = re.sub(r"#fe3e02([0-9a-f]{2})?\b", lambda m: "#db020d" + (m.group(1) or ""),
                 css, flags=re.I)
    css = re.sub(r"rgba?\(\s*254\s*,\s*62\s*,\s*2\s*", "rgba(219, 2, 13", css)
    css = css.replace("#ffefe6", "#ffe9ea")   # tenta calda a insignei, acordata la rosu
    css = w_rename(css)
    # familia proprie de fonturi, fara referinte la template
    css = css.replace("Generalsans", "GDH Sans")
    css = css.replace("--font-family--general-sans", "--font-family--gdh-sans")
    css = css.replace("--font-family--inter-tight", "--font-family--inter-tight")
    css = re.sub(r"/\*.*?webflow.*?\*/", "", css, flags=re.I | re.S)

    brand = """
/* ---------- GDH brand ---------- */
:root{--gdh-red:#db020d;--gdh-red-dark:#a80209;--gdh-ink:#111111;}
.gdh-logo{display:block;height:auto;width:auto;max-width:100%}
.gdh-logo--nav{height:54px}
.gdh-logo--footer{height:66px}
@media (max-width:767px){
  .gdh-logo--nav{height:44px}
  .gdh-logo--footer{height:56px}
}
.brand-link{display:inline-flex;align-items:center}
.brand-mark{display:inline-flex}
.gdh-hero-mark{height:75px;width:auto}
.gdh-logo-boards{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.gdh-logo-board{border:1px solid rgba(0,0,0,.1);border-radius:18px;padding:32px;
  display:flex;flex-direction:column;gap:18px;align-items:flex-start;justify-content:space-between}
.gdh-logo-board.is-dark{background:#0d0d0d;border-color:#0d0d0d;color:#fff}
.gdh-logo-board.is-mark img{height:96px;width:auto}
.gdh-logo-board img{max-width:100%;height:auto}
@media (max-width:767px){.gdh-hero-mark{height:58px}}
/* paginile interioare scrise de noi: banda inchisa in spatele navigatiei */
.gdh-innernav{background:#0d0d0d}
.gdh-innernav .navbar{position:relative}
.gdh-nav-open{overflow:hidden}
/* pastila de text are inaltime fixa: un text care se rupe pe doua randuri s-ar taia */
.button-text,.footer-text{white-space:nowrap}
/* „Get a Quote" se rupea in doua randuri cand sigla a crescut */
.navlink{white-space:nowrap}
.g-nav-overlay{display:none}
.menu-button{color:#fff}
/* meniul mobil: inainte il deschidea runtime-ul sters, acum il tinem in CSS */
@media screen and (max-width:991px){
  .navbar{position:relative}
  /* panoul portocaliu al șablonului își aduce singur fundalul și colțurile */
  .navbar .nav-menu{display:none!important;position:absolute;top:100%;left:0;right:0;z-index:60}
  .navbar .nav-menu.is-open{display:block!important}
  .navbar .nav-menu-desktop{display:flex;flex-direction:column;align-items:flex-start;gap:14px;width:100%}
  .navbar .menu-button{display:flex!important;align-items:center;justify-content:center;cursor:pointer}
  .navbar .navlink{width:100%}
}
.faq-answer{overflow:hidden;transition:height .35s cubic-bezier(.22,.61,.36,1)}
.gdh-slider{position:relative}
.gdh-slider .g-slider-mask{overflow:hidden}
.gdh-slider-track{display:flex;transition:transform .55s cubic-bezier(.22,.61,.36,1);will-change:transform}
.gdh-dot.is-active{opacity:1}

/* ---------- finisaje ---------- */
html{-webkit-text-size-adjust:100%;text-size-adjust:100%}
img,svg,video{max-width:100%}
::selection{background:var(--gdh-red);color:#fff}
a,button,[role="button"],.faq-top{-webkit-tap-highlight-color:transparent}

/* inel de focus vizibil doar pentru navigarea de la tastatura */
a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible,
select:focus-visible,[tabindex]:focus-visible,.faq-top:focus-visible{
  outline:3px solid var(--gdh-red);outline-offset:3px;border-radius:6px}

/* sari peste navigatie */
.gdh-skip{position:absolute;left:-9999px;top:0;z-index:200;background:var(--gdh-red);
  color:#fff;padding:12px 20px;border-radius:0 0 10px 0;font-weight:600;text-decoration:none}
.gdh-skip:focus{left:0}

/* fisele de statistici din paginile interioare */
.gdh-stat{border:1px solid rgba(0,0,0,.1);border-radius:18px;padding:26px}
.gdh-stat-value{font-size:38px;font-weight:700;color:var(--gdh-red);line-height:1.05}
.gdh-stat-label{margin-top:8px}

@media (max-width:767px){
  /* zone de atins de cel putin 44 px, fara sa miscam nimic din layout */
  .footer-link,.contact-link,.social-link,.navlink,.g-slider-dot{position:relative}
  .footer-link::after,.contact-link::after,.navlink::after{
    content:"";position:absolute;left:0;right:0;top:50%;height:44px;transform:translateY(-50%)}
  /* sablonul pune max-height 1.5rem, deci nu ajunge doar height */
  .social-link{width:44px;height:44px;max-height:44px;display:inline-flex;
    align-items:center;justify-content:center}
  .social-link .social-icon{width:24px;height:24px}
  .service-slide-button,.review-slide-button{min-width:44px;min-height:44px;
    display:inline-flex;align-items:center;justify-content:center}
  .g-slider-dot{width:12px;height:12px}
  .g-slider-dot::after{content:"";position:absolute;inset:-16px}
}
"""
    open(os.path.join(OUT, "css", "site.css"), "w", encoding="utf-8").write(css + brand)


# --------------------------------------------------------------------------
# 5. sigla reala GDH (PNG transparent, pregatit local)
# --------------------------------------------------------------------------
LOGO_SRC = "gdh-logo-source.png"
LOGO_META = {}


def build_logo():
    """Pregătește sigla reală (PNG transparent) în variantele de care e nevoie."""
    import logo_gdh as LG
    meta = LG.build(os.path.join(SRC, LOGO_SRC), os.path.join(OUT, "img"))
    LOGO_META.update(meta)
    log("  siglă: %dx%d (raport %.3f), marcă %dx%d"
        % (meta["w"], meta["h"], meta["ratio"], meta["mark"][0], meta["mark"][1]))


def logo_img(variant, cls, height, alt='GDH — Global Distribution Holdings'):
    """Marcajul <img> pentru siglă, cu dimensiuni ca să nu sară pagina la încărcare."""
    ratio = LOGO_META.get("ratio", 2.3873)
    w = round(height * ratio)
    src = "img/gdh-logo-light.png" if variant == "light" else "img/gdh-logo.png"
    return ('<img src="%s" alt="%s" class="%s" width="%d" height="%d" decoding="async">'
            % (src, alt, cls, w, height))


def extract_block(doc, start_marker):
    """Extrage un <div>/<footer> echilibrat, pornind de la primul marker gasit."""
    i = doc.find(start_marker)
    if i < 0:
        return ""
    start = doc.rfind("<", 0, i)
    tag = re.match(r"<([a-z0-9]+)", doc[start:]).group(1)
    depth = 0
    pos = start
    pat = re.compile(r"<(/?)%s\b[^>]*?(/?)>" % tag, re.I)
    while True:
        m = pat.search(doc, pos)
        if not m:
            return doc[start:]
        if m.group(2) == "/":
            pos = m.end()
            continue
        depth += -1 if m.group(1) else 1
        pos = m.end()
        if depth == 0:
            return doc[start:pos]


HERO_PHOTO = "8a8999ada35854b9d773294bd845c416d4013409-1-.webp"


def build_brand_assets():
    """Iconițele, imaginea de partajare și manifestul — desenate din fonturile locale."""
    import assets_gdh as A
    import copy_gdh as C
    fonts = A.load_fonts(OUT, os.path.join(_cache, "ttf"))
    A.build_icons(OUT, fonts)
    A.build_og(OUT, fonts,
               "Your product, in the country’s biggest chains.",
               "Retail distribution · Dental distribution · Shelf execution",
               C.SITE_URL.split("//")[-1],
               HERO_PHOTO)
    A.build_manifest(OUT, C.SITE_NAME, "GDH")
    log("  favicon.ico + 6 PNG-uri + apple-touch + maskable + og-image.jpg")


def finalize():
    """Copiaza JS-ul, construieste paginile interioare si fisierele de deploy."""
    for js in ("lenis.js", "gsap.min.js", "ScrollTrigger.min.js", "SplitText.min.js"):
        shutil.copy2(os.path.join(SRC, FILES, js), os.path.join(OUT, "js", js))
    shutil.copy2(os.path.join(SRC, "site_js.js"), os.path.join(OUT, "js", "site.js"))
    shutil.copy2(os.path.join(SRC, "animations_js.js"), os.path.join(OUT, "js", "animations.js"))

    index = open(os.path.join(OUT, "index.html"), encoding="utf-8").read()
    nav = extract_block(index, 'class="navbar')
    # navigatia vine din index, deci ar marca "Home" ca pagina curenta peste tot
    nav = nav.replace(' g--current', '').replace(' aria-current="page"', '')
    footer = extract_block(index, 'class="section footer"')
    # iconitele si theme-color vin din head_common; un link catre
    # img/favicon.svg ar da 404, fisierul ala nu se genereaza
    css_head = ('<link rel="stylesheet" href="css/fonts.css">'
                '<link rel="stylesheet" href="css/site.css">')
    import inner_gdh
    pages = inner_gdh.build(OUT, nav, footer, css_head)
    log("  pagini interioare:", len(pages))

    # ---- fisiere pentru Cloudflare Pages
    open(os.path.join(OUT, "_headers"), "w", encoding="utf-8").write(
        "/*\n"
        "  X-Content-Type-Options: nosniff\n"
        "  X-Frame-Options: SAMEORIGIN\n"
        "  Referrer-Policy: strict-origin-when-cross-origin\n"
        "  Permissions-Policy: geolocation=(), microphone=(), camera=()\n"
        "  Content-Security-Policy: default-src 'self'; img-src 'self' data:; "
        "style-src 'self' 'unsafe-inline'; script-src 'self'; font-src 'self'; "
        "form-action 'self'; frame-ancestors 'self'; base-uri 'self'\n"
        "\n/img/*\n  Cache-Control: public, max-age=31536000, immutable\n"
        "\n/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n"
        "\n/css/*\n  Cache-Control: public, max-age=604800\n"
        "\n/js/*\n  Cache-Control: public, max-age=604800\n")
    # adresele vechi raman valide: Cloudflare Pages citeste _redirects
    import inner_gdh as _I
    open(os.path.join(OUT, "_redirects"), "w", encoding="utf-8").write(
        "".join("/%s  /%s  301\n" % (was[:-5], now[:-5])
                for was, now in sorted(_I.RENAME.items())))

    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % __import__("copy_gdh").SITE_URL)

    import copy_gdh as C
    urls = sorted(f for f in os.listdir(OUT) if f.endswith(".html") and f != "404.html")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = C.SITE_URL + ("/" if u == "index.html" else "/" + u[:-5])
        sm.append("  <url><loc>%s</loc></url>" % loc)
    sm.append("</urlset>")
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")

    open(os.path.join(OUT, "README.md"), "w", encoding="utf-8").write(
        "# GDH - Global Distribution Holdings (site generat)\n\n"
        "Folderul asta e **generat**: il rescrie `python3 build_gdh.py` din radacina\n"
        "repo-ului, la fiecare rulare. Nu edita nimic aici, se pierde la urmatorul build.\n"
        "Sursele si instructiunile sunt in `../SURSE.md`.\n\n"
        "Site static, fara nicio resursa externa: fonturile, imaginile, CSS-ul si JS-ul\n"
        "sunt servite de pe acelasi domeniu.\n\n"
        "| | |\n|---|---|\n"
        "| Pagini | %d |\n| Cereri catre alte domenii | 0 |\n"
        "| Fonturi | Inter Tight + GDH Sans, locale |\n"
        "| Animatii | GSAP + ScrollTrigger + SplitText, locale (`js/animations.js`) |\n\n"
        "## Publicare\n\n"
        "Cloudflare Pages e legat la repo, cu build command gol si build output\n"
        "directory `dist`. Fiecare push pe `main` redeployeaza singur.\n\n"
        "`_headers` seteaza cache-ul si o politica CSP care blocheaza orice cerere in\n"
        "afara domeniului. `_redirects` tine in viata adresele vechi.\n"
        % len(urls))


if __name__ == "__main__":
    log("1/8 pregatesc dist/")
    prepare()
    log("2/8 imagini")
    collect_images()
    log("3/8 fonturi")
    build_fonts()
    log("4/8 css")
    build_css()
    log("5/8 sigla reala")
    build_logo()
    log("6/8 pagini principale")
    import pages_gdh
    pages_gdh.build_pages(SRC, OUT, FILES, IMG_MAP, logo_img)
    log("7/8 pagini interioare + deploy")
    finalize()
    log("8/8 iconite, imagine de partajare, manifest")
    build_brand_assets()
    log("gata -> dist/")
