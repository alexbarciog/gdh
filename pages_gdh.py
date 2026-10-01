# -*- coding: utf-8 -*-
"""Etapa 2: transforma paginile HTML din snapshot in paginile GDH."""
import os, re, html, shutil, json
import copy_gdh as C

FAQ_ANSWERS = [
    "Retail and dental products. On the retail side: food and beverage, household and personal care, "
    "and health and beauty lines sold through the large store chains. On the dental side: materials, "
    "consumables and equipment for practices, clinics and laboratories.",
    "Send us your range and your monthly production capacity. We tell you which chains we can "
    "realistically place it in, at what volume and on what timeline. If we agree it fits, we buy the "
    "first order and take it to the buyer ourselves.",
    "The country's largest supermarket, drugstore, convenience and cash-and-carry chains, the "
    "independent stores on our delivery routes, and dental practices, clinics, laboratories and "
    "dental depots nationwide.",
    "Nothing. We are not a logistics supplier and we do not invoice the brands we carry. We buy your "
    "product and earn from distributing it, so there are no listing fees, storage charges or delivery "
    "costs coming back to you.",
    "Your product list with pack sizes, barcodes and shelf life, your production capacity per month, "
    "any listings or exclusivity you already hold, and the certifications your category requires. "
    "That is enough for us to walk into a buyer meeting.",
]

# Nu facturam brandurile pe care le distribuim, deci cardurile de pret ale
# sablonului devin niveluri de parteneriat, fara sume.
PRICING_TIERS = ["Market Entry", "National Retail", "Full Category Partnership"]

NAV_LOGO = ('<a href="index.html" class="brand-link g-inline-block" aria-label="GDH — Global Distribution '
            'Holdings, home">{logo}</a>')
FOOT_LOGO = ('<a href="index.html" class="brand-link g-inline-block" aria-label="GDH — Global Distribution '
             'Holdings, home">{logo}</a>')

SCRIPTS = ('<script src="js/gsap.min.js"></script>'
           '<script src="js/ScrollTrigger.min.js"></script>'
           '<script src="js/SplitText.min.js"></script>'
           '<script src="js/lenis.js"></script>'
           '<script src="js/site.js"></script>'
           '<script src="js/animations.js"></script>')

HAMBURGER = ('<svg class="gdh-burger" viewBox="0 0 39 39" width="39" height="39" aria-hidden="true" '
             'fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round">'
             '<path d="M6 13.5h27M6 25.5h27"/></svg>')


def unesc(t):
    return html.unescape(t)


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def apply_copy(doc):
    """Inlocuieste textele doar in nodurile de text, nu in atribute."""
    exact = {k.strip(): v for k, v in C.EXACT}

    def repl(m):
        raw = m.group(1)
        stripped = unesc(raw).strip()
        if not stripped:
            return m.group(0)
        new = exact.get(stripped)
        if new is None:
            new = stripped
            for a, b in C.SUBSTR:
                new = new.replace(a, b)
            if new == stripped:
                return m.group(0)
        lead = raw[:len(raw) - len(raw.lstrip())]
        tail = raw[len(raw.rstrip()):]
        return ">" + lead + esc(new) + tail + "<"

    return re.sub(r">([^<>]+)<", repl, doc)


def strip_webflow(doc):
    # comentariul de salvare din browser + atributele de pe <html>
    doc = re.sub(r"<!--\s*saved from url=.*?-->\s*", "", doc, flags=re.S)
    doc = re.sub(r"<html[^>]*>", '<html lang="en">', doc, count=1)

    # scripturi: tot ce e Webflow / Google / jQuery / GSAP nefolosit
    def kill_script(m):
        tag, body = m.group(0), m.group(2)
        src = re.search(r'src="([^"]*)"', m.group(1) or "")
        src = src.group(1) if src else ""
        bad_src = any(k in src for k in ("webflow", "jquery", "webfont", "review.js",
                                         "gsap", "ScrollTrigger", "SplitText", "lenis.js"))
        bad_body = any(k in body for k in ("WebFont.load", "__WF_REVIEW_BRIDGE", "w-mod-",
                                           "Webflow", "webflow", "new Lenis"))
        return "" if (bad_src or bad_body) else tag

    doc = re.sub(r"(?is)<script([^>]*)>(.*?)</script>", kill_script, doc)

    # widget-ul de suport al template-ului (link-uri WhatsApp / Webflow) pana la </body>
    i = doc.find("LIOWEB PREMIUM TEMPLATE SUPPORT WIDGET")
    if i > 0:
        start = doc.rfind("<!--", 0, i)
        end = doc.rfind("</body>")
        doc = doc[:start] + doc[end:]

    # preconnect / dns-prefetch catre servicii externe
    doc = re.sub(r'<link[^>]+href="https?://[^"]*"[^>]*rel="(?:preconnect|dns-prefetch)"[^>]*>', "", doc)
    doc = re.sub(r'<link[^>]*rel="(?:preconnect|dns-prefetch)"[^>]*>', "", doc)
    doc = re.sub(r'<meta[^>]*name="generator"[^>]*>', "", doc, flags=re.I)
    doc = re.sub(r'<style>\.wf-force-outline-none\[tabindex="-1"\]:focus\{outline:none;\}</style>', "", doc)
    # blocurile <style> pre-randate pentru interactiunile Webflow (IX2)
    doc = re.sub(r"(?is)<style>(?:(?!</style>).)*?w-mod-ix(?:(?!</style>).)*?</style>", "", doc)
    doc = re.sub(r"<!--\s*Smooth Scrolling\s*-->", "", doc)

    # atribute proprii Webflow
    doc = re.sub(r'\s(?:data-w-id|data-wf-[a-z-]*|data-wf--[a-z-]*--variant|data-is-ix2-target|'
                 r'data-animation-type|data-src|data-loop|data-direction|data-autoplay|data-renderer|'
                 r'data-default-duration|data-duration|data-loading|data-easing2|data-easing|data-delay|'
                 r'data-animation|data-collapse|data-nav-menu-open|data-autoplay-limit|data-disable-swipe|'
                 r'data-hide-arrows|data-infinite|data-ix)="[^"]*"', "", doc)
    doc = re.sub(r'\s(?:data-wf-ignore|data-wf-focus-visible)(?==|\s|>)="?[^"\s>]*"?', "", doc)

    # meniul lottie -> hamburger simplu
    doc = re.sub(r'(?s)(<div class="menu-icon"[^>]*>).*?(</div>)', r"\1" + HAMBURGER + r"\2", doc)
    doc = re.sub(r'(?s)<div class="menu-icon"[^>]*>.*?</svg>\s*</div>',
                 '<div class="menu-icon">' + HAMBURGER + "</div>", doc)

    # link-uri externe ramase (template, WhatsApp, Webflow)
    doc = re.sub(r'href="https?://(?:webflow\.com|wa\.me|frevanta\.webflow\.io)[^"]*"', 'href="contact.html"', doc)
    return doc


def rewrite_assets(doc, img_map, prefixes, remote_map):
    """Trece toate caile de resurse pe img/ si scoate folderele snapshot.

    Numele fisierelor din snapshot contin spatii si virgule, deci nu se pot taia
    dupa delimitatori: cautam prefixul folderului si apoi cel mai lung nume de
    fisier cunoscut care se potriveste exact in acel punct.
    """
    names = sorted(img_map, key=len, reverse=True)
    by_first = {}
    for n in names:
        by_first.setdefault(n[0], []).append(n)

    for pref in prefixes:
        pos = 0
        while True:
            i = doc.find(pref, pos)
            if i < 0:
                break
            j = i + len(pref)
            hit = None
            for cand in by_first.get(doc[j:j + 1], ()):
                if doc.startswith(cand, j):
                    hit = cand
                    break
            if hit:
                doc = doc[:i] + img_map[hit] + doc[j + len(hit):]
                pos = i + len(img_map[hit])
            else:
                pos = j

    # cele mai lungi mai intai, ca un URL sa nu inghita prefixul altuia
    for url in sorted(remote_map, key=len, reverse=True):
        doc = doc.replace(url, remote_map[url])
    return doc


def head_common(page, title, desc, og_type="website"):
    """Antetul comun: iconițe, manifest, canonical și cartonașul de partajare.

    og:image trebuie să fie URL absolut — WhatsApp, Discord, Slack și Facebook nu
    rezolvă căi relative și atunci previzualizarea rămâne fără imagine.
    """
    # Cloudflare Pages servește adresele fără „.html" și redirecționează varianta
    # cu extensie, deci canonical și og:url arată direct spre adresa finală.
    url = C.SITE_URL + ("/" if page == "index.html" else "/" + page[:-len(".html")])
    img = C.SITE_URL + "/img/og-image.jpg"
    return (
        '<link rel="canonical" href="%s">'
        '<link rel="icon" href="/favicon.ico" sizes="32x32">'
        '<link rel="icon" href="/img/icon-32.png" type="image/png" sizes="32x32">'
        '<link rel="icon" href="/img/icon-16.png" type="image/png" sizes="16x16">'
        '<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">'
        '<link rel="manifest" href="/site.webmanifest">'
        '<meta name="theme-color" content="#db020d">'
        '<meta name="application-name" content="GDH">'
        '<meta name="apple-mobile-web-app-title" content="GDH">'
        '<meta name="color-scheme" content="light">'
        '<meta property="og:type" content="%s">'
        '<meta property="og:site_name" content="%s">'
        '<meta property="og:locale" content="en_GB">'
        '<meta property="og:url" content="%s">'
        '<meta property="og:title" content="%s">'
        '<meta property="og:description" content="%s">'
        '<meta property="og:image" content="%s">'
        '<meta property="og:image:secure_url" content="%s">'
        '<meta property="og:image:type" content="image/jpeg">'
        '<meta property="og:image:width" content="1200">'
        '<meta property="og:image:height" content="630">'
        '<meta property="og:image:alt" content="%s">'
        '<meta name="twitter:card" content="summary_large_image">'
        '<meta name="twitter:title" content="%s">'
        '<meta name="twitter:description" content="%s">'
        '<meta name="twitter:image" content="%s">'
        '<meta name="twitter:image:alt" content="%s">'
        % (url, og_type, esc(C.SITE_NAME), url, esc(title), esc(desc), img, img, esc(C.OG_ALT),
           esc(title), esc(desc), img, esc(C.OG_ALT)))


def json_ld(page):
    """Datele structurate: doar pe prima pagină, ca să nu se dubleze."""
    if page != "index.html":
        return ""
    import json
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": C.SITE_NAME,
        "alternateName": "GDH",
        "url": C.SITE_URL + "/",
        "logo": C.SITE_URL + "/img/icon-512.png",
        "image": C.SITE_URL + "/img/og-image.jpg",
        "description": C.TITLES["index.html"][1],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Str. Depozitelor 24, Hala D2",
            "addressLocality": "București",
            "addressCountry": "RO",
        },
        "contactPoint": [{
            "@type": "ContactPoint",
            "telephone": "+40213004050",
            "email": "office@gdh-group.com",
            "contactType": "sales",
            "availableLanguage": ["ro", "en"],
        }],
    }
    site = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": C.SITE_NAME,
        "url": C.SITE_URL + "/",
    }
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps([org, site], ensure_ascii=False, separators=(",", ":")))


def head_rewrite(doc, page):
    title, desc = C.TITLES[page]
    doc = re.sub(r"(?s)<title>.*?</title>", "<title>%s</title>" % esc(title), doc, count=1)
    doc = re.sub(r'<meta content="[^"]*" name="description">',
                 '<meta content="%s" name="description">' % esc(desc), doc)
    doc = re.sub(r'<meta content="[^"]*" property="og:title">',
                 '<meta content="%s" property="og:title">' % esc(title), doc)
    doc = re.sub(r'<meta content="[^"]*" name="twitter:title">',
                 '<meta content="%s" name="twitter:title">' % esc(title), doc)
    doc = re.sub(r'<meta content="[^"]*" property="og:description">',
                 '<meta content="%s" property="og:description">' % esc(desc), doc)
    doc = re.sub(r'<meta content="[^"]*" name="twitter:description">',
                 '<meta content="%s" name="twitter:description">' % esc(desc), doc)

    # metaurile vechi de partajare sunt inlocuite in bloc de head_common
    doc = re.sub(r'<meta[^>]*(?:property="og:[^"]*"|name="twitter:[^"]*")[^>]*>', "", doc)
    doc = re.sub(r'<link[^>]*rel="stylesheet"[^>]*>', "", doc)
    doc = re.sub(r'<link[^>]*rel="(?:icon|apple-touch-icon|shortcut icon|manifest|canonical)"[^>]*>', "", doc)
    doc = re.sub(r'<meta[^>]*name="theme-color"[^>]*>', "", doc)

    head_add = ('<link rel="stylesheet" href="css/fonts.css">'
                '<link rel="stylesheet" href="css/site.css">'
                + head_common(page, title, desc)
                + json_ld(page))
    doc = doc.replace("</head>", head_add + "</head>", 1)
    return doc


def body_rewrite(doc, logo_nav, logo_footer, logo_nav_ink=None):
    # datele de contact apar si in atribute (href), nu doar in text
    doc = doc.replace("partners@mastercare.com", "office@gdh-group.com")
    doc = doc.replace("office@gdh-group.com", "office@gdh-group.com")
    doc = doc.replace("tel:+00762079460857", "tel:+40213004050")

    # brand text -> logo; pe paginile interioare bara e albă, deci sigla merge în tuș închis
    if "home-hero-area" not in doc and logo_nav_ink:
        logo_nav = logo_nav_ink
    doc = re.sub(r'<div class="brand-name[^"]*">[^<]*</div>', logo_nav, doc)
    doc = re.sub(r'<a href="[^"]*" class="brand-name[^"]*">[^<]*</a>',
                 '<a href="index.html" class="brand-link g-inline-block" aria-label="GDH home">%s</a>' % logo_footer,
                 doc)
    doc = re.sub(r'<a href="[^"]*" (aria-current="page" )?class="brand-link[^"]*">\s*</a>',
                 lambda m: '<a href="index.html" class="brand-link g-inline-block" aria-label="GDH home">%s</a>'
                 % logo_nav, doc)

    # FAQ: raspunsuri distincte + inchise implicit (JS le deschide)
    idx = [0]

    def faq(m):
        i = idx[0]
        idx[0] += 1
        ans = FAQ_ANSWERS[i] if i < len(FAQ_ANSWERS) else FAQ_ANSWERS[-1]
        return m.group(1) + esc(ans) + m.group(3)

    doc = re.sub(r'(<p class="paragraph-regular" style="color: rgb\(80, 80, 80\);">)(.*?)(</p>)', faq, doc, flags=re.S)

    # formulare: fara actiune externa, trimise prin mailto de site.js
    doc = re.sub(r'<form([^>]*)>', lambda m: '<form%s>' % re.sub(
        r'\s(?:action|method|data-name|redirect|data-redirect)="[^"]*"', "", m.group(1)) + "", doc)
    doc = doc.replace("<form ", '<form data-gdh-form="1" ')

    # marcheaza slider-ele pentru JS-ul propriu
    doc = doc.replace('class="industries-slider-main g-slider"', 'class="industries-slider-main g-slider gdh-slider"')
    doc = doc.replace('class="review-slide-main g-slider"', 'class="review-slide-main g-slider gdh-slider"')
    doc = re.sub(r'(<div[^>]*class="[^"]*g-slider(?![-\w])[^"]*)"', r'\1 gdh-slider"', doc)

    # sari peste navigatie, pentru cei care folosesc tastatura sau cititor de ecran
    doc = doc.replace('<div class="page-wrapper">',
                      '<a class="gdh-skip" href="#gdh-main">Skip to content</a>'
                      '<div class="page-wrapper">', 1)
    doc = doc.replace('<div class="main">', '<div class="main" id="gdh-main" tabindex="-1">', 1)
    if 'id="gdh-main"' not in doc:
        doc = re.sub(r'(<section class="section)', r'<span id="gdh-main" tabindex="-1"></span>\1',
                     doc, count=1)

    # adresele vechi din snapshot -> numele noi, inainte de rewrite_cards,
    # care potriveste cardurile dupa pagina spre care duc
    import inner_gdh as I
    for was, now in I.RENAME.items():
        doc = doc.replace('href="%s"' % was, 'href="%s"' % now)

    doc = rewrite_pricing(doc)
    doc = rewrite_cards(doc)

    # scripturi proprii
    doc = doc.replace("</body>", SCRIPTS + "</body>")
    return doc


def rewrite_cards(doc):
    """Titlurile, rezumatele, etichetele si datele de pe cardurile din liste.

    In sablon aceleasi siruri apar in mai multe locuri — titlul unui card de
    client coincide cu titlul unui card de serviciu, doua carduri au acelasi
    text, etichetele de sector sunt identice pe toate cardurile, iar datele din
    liste au ramas din 2023 desi articolele sunt din 2026. Potrivirea pe text nu
    le poate separa, deci luam fiecare camp dupa pagina spre care duce cardul,
    din aceeasi sursa care scrie si pagina respectiva.

    Listele au doua variante de card, cu clase diferite pentru aceleasi campuri;
    le dam pe amandoua, iar cea care lipseste dintr-un card ramane fara efect.
    """
    import inner_gdh as I

    slots = {}
    for fn, (title, sector, lead, _items) in I.CASES.items():
        slots[fn] = [("case-card-title", 0, title),
                     ("project-name", 0, title),
                     ("project-summary", 0, lead),
                     ("font-1-extra-small", 0, sector),
                     ("font-1-extra-small", 1, "Distribution")]
    for fn, (_cat, date, title, _paras) in I.POSTS.items():
        slots[fn] = [("blog-date-text", 0, date),
                     ("font-1-extra-small(?: is-white)? medium", 0, date),
                     ("font-2-small", 0, title),
                     ("blog-card-title(?: is-white)?", 0, title)]

    def put(seg, cls, nth, value):
        hits = list(re.finditer(r'<(\w+) class="%s">([^<]*)</\1>' % cls, seg))
        if nth >= len(hits):
            return seg
        m = hits[nth]
        return seg[:m.start(2)] + esc(value) + seg[m.end(2):]

    def card_end(i):
        """Sfarsitul elementului <a> care contine link-ul de la pozitia i.

        Fara limita asta, un card ar inghiti tot ce urmeaza pana la urmatorul
        link — inclusiv sectiunea de parteneriat, careia i-ar rescrie numele
        nivelurilor.
        """
        pat = re.compile(r"<(/?)a\b", re.I)
        depth, pos = 0, doc.rfind("<a", 0, i)
        while True:
            m = pat.search(doc, pos)
            if not m:
                return len(doc)
            depth += -1 if m.group(1) else 1
            pos = m.end()
            if depth == 0:
                return pos

    hits = list(re.finditer(r'href="((?:case|post)-[^"]+)"', doc))
    # de la coada spre cap, ca pozitiile deja gasite sa ramana valide
    for i in range(len(hits) - 1, -1, -1):
        m = hits[i]
        if m.group(1) not in slots:
            continue
        stop = card_end(m.start())
        seg = doc[m.end():stop]
        for cls, nth, value in slots[m.group(1)]:
            seg = put(seg, cls, nth, value)
        doc = doc[:m.end()] + seg + doc[stop:]
    return doc


def rewrite_pricing(doc):
    """Numele nivelurilor din cardurile de pret.

    Numele nivelului 2 coincide in snapshot cu titlul unui card de serviciu, deci
    nu poate fi schimbat prin apply_copy fara sa il mute si pe celalalt: il luam
    aici, dupa pozitie. Sumele sunt siruri unice si se schimba in copy_gdh.
    """
    idx = [0]

    def tier(m):
        i = idx[0]
        idx[0] += 1
        if i >= len(PRICING_TIERS):
            return m.group(0)
        return m.group(1) + esc(PRICING_TIERS[i]) + m.group(3)

    return re.sub(r'(<div class="font-1-extra-small[^"]*">)([^<]*)(</div>'
                  r'<div class="pricing-card-bottom">)', tier, doc)


def fetch_remote(src, out, img_map):
    """Aduce local imaginile la care paginile mai trimit direct catre CDN."""
    import build_gdh as B
    import urllib.parse
    urls = set()
    for page in C.TITLES:
        p = os.path.join(src, page)
        if os.path.exists(p):
            doc = open(p, encoding="utf-8").read()
            for u in re.findall(r'https?://[^"\s\']+', doc):
                u = u.rstrip(",);")
                if any(h in u for h in ("website-files.com", "cloudfront.net")):
                    urls.add(u)
    remote = {}
    for u in sorted(urls):
        base = urllib.parse.unquote(u.split("/")[-1].split("?")[0])
        base = re.sub(r"^[0-9a-f]{24}_", "", base)
        new = B.safe_name(base)
        # un URL fara nume de fisier (ex. preconnect catre radacina CDN-ului) ar
        # deveni prefixul tuturor celorlalte si le-ar rupe caile
        if not new or "." not in new:
            continue
        dst = os.path.join(out, "img", new)
        if not os.path.exists(dst):
            try:
                open(dst, "wb").write(B.download(u))
            except Exception as e:
                print("    ! remote esuat", u.split("/")[-1], e)
                continue
        remote[u] = "img/" + new
    print("   imagini aduse de la CDN:", len(remote))
    return remote


def build_pages(src, out, files_dir, img_map, logo_img):
    # sigla e imaginea reală: varianta cu tuș alb pe fundal închis, cea cu tuș
    # negru pe fundal deschis — se alege per pagină în body_rewrite
    # 54 px în bară: sub atât descriptorul „GLOBAL DISTRIBUTION HOLDINGS" devine
    # o dungă gri și sigla nu se mai citește ca în original
    logo_nav = '<span class="brand-mark">%s</span>' % logo_img("light", "gdh-logo gdh-logo--nav", 54)
    logo_nav_ink = '<span class="brand-mark">%s</span>' % logo_img("dark", "gdh-logo gdh-logo--nav", 54)
    logo_footer = '<span class="brand-mark">%s</span>' % logo_img("light", "gdh-logo gdh-logo--footer", 66)
    from build_gdh import w_rename
    remote_map = fetch_remote(src, out, img_map)
    dirs = [d for d in os.listdir(src) if d.endswith("_files") and os.path.isdir(os.path.join(src, d))]
    prefixes = []
    for d in dirs:
        for p in ("./%s/images/" % d, "./%s/" % d, "%s/images/" % d, "%s/" % d):
            prefixes.append(p)
    prefixes.sort(key=len, reverse=True)

    for page in C.TITLES:
        p = os.path.join(src, page)
        if not os.path.exists(p):
            continue
        doc = open(p, encoding="utf-8").read()
        doc = strip_webflow(doc)
        doc = rewrite_assets(doc, img_map, prefixes, remote_map)
        doc = head_rewrite(doc, page)
        doc = w_rename(doc)
        doc = apply_copy(doc)
        doc = body_rewrite(doc, logo_nav, logo_footer, logo_nav_ink)
        doc = re.sub(r"\n{3,}", "\n", doc)
        open(os.path.join(out, page), "w", encoding="utf-8").write(doc)
        print("   ", page, len(doc) // 1024, "KB")
