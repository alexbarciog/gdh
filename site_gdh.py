# -*- coding: utf-8 -*-
"""Asambleaza paginile GDH din componente si continut.

Fiecare pagina trece prin `shell()`, care pune antetul, navigatia, subsolul si
metadatele. Continutul vine din content_gdh.py (scris de mana), din
pages_data_gdh.py (paginile de sector si serviciu) si din inner_gdh.py
(programele de client si articolele).
"""
import json
import os

import content_gdh as C
import ui_gdh as U

LOGO_DARK = "img/gdh-logo.png"        # pe fundal deschis
LOGO_LIGHT = "img/gdh-logo-light.png"  # pe fundal inchis

# Slot-uri de imagine: pagina -> fisier din dist/img. O pagina care nu apare
# aici se randeaza curat, fara fotografie. Pentru raft si cabinet stomatologic
# inca nu avem fotografii, deci acele pagini raman fara.
IMAGES = {
    "index.html": "img/warehouse-racking.webp",
    "sectors.html": "img/warehouse-wide.webp",
    "sector-retail.html": "img/fulfilment.webp",
    "sector-grocery.html": "img/packing.webp",
    "sector-convenience.html": "img/sortation.webp",
    "sector-private-label.html": "img/automation.webp",
    "distribution.html": "img/sortation.webp",
    "service-chain-listings.html": "img/planning.webp",
    "service-stock-and-delivery.html": "img/warehouse-racking.webp",
    "service-shelf-execution.html": "img/team.webp",
    "service-sell-out-visibility.html": "img/stock-check.webp",
    "service-returns.html": "img/packing.webp",
    "brands.html": "img/fulfilment.webp",
    "insights.html": "img/planning.webp",
    "about-us.html": "img/team.webp",
    "careers.html": "img/team.webp",
    "locations.html": "img/warehouse-wide.webp",
    "partner-with-us.html": "img/planning.webp",
}


def img(slot):
    return IMAGES.get(slot)


# --------------------------------------------------------------------- shell
def head(page, title, desc, noindex=False):
    url = C.SITE_URL + ("/" if page == "index.html" else "/" + page[:-len(".html")])
    og = C.SITE_URL + "/img/og-image.jpg"
    e = U.esc
    return (
        '<meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>%s</title>'
        '<meta name="description" content="%s">'
        '%s'
        '<link rel="canonical" href="%s">'
        '<link rel="icon" href="/favicon.ico" sizes="32x32">'
        '<link rel="icon" href="/img/icon-32.png" type="image/png" sizes="32x32">'
        '<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">'
        '<link rel="manifest" href="/site.webmanifest">'
        '<meta name="theme-color" content="#00767a">'
        '<meta name="color-scheme" content="light">'
        '<meta property="og:type" content="website">'
        '<meta property="og:site_name" content="%s">'
        '<meta property="og:locale" content="en_GB">'
        '<meta property="og:url" content="%s">'
        '<meta property="og:title" content="%s">'
        '<meta property="og:description" content="%s">'
        '<meta property="og:image" content="%s">'
        '<meta property="og:image:width" content="1200">'
        '<meta property="og:image:height" content="630">'
        '<meta name="twitter:card" content="summary_large_image">'
        '<meta name="twitter:title" content="%s">'
        '<meta name="twitter:description" content="%s">'
        '<meta name="twitter:image" content="%s">'
        % (e(title), e(desc),
           '<meta name="robots" content="noindex">' if noindex else "",
           e(url), e(C.SITE_NAME), e(url), e(title), e(desc), e(og),
           e(title), e(desc), e(og)))


def org_jsonld():
    data = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": C.SITE_NAME,
        "alternateName": "GDH",
        "url": C.SITE_URL + "/",
        "logo": C.SITE_URL + "/img/icon-512.png",
        "description": ("GDH is a distributor of retail and dental products. We buy, stock "
                        "and place products into the country's largest store chains and "
                        "dental practices."),
        "address": {"@type": "PostalAddress",
                    "streetAddress": C.ADDRESS[0],
                    "addressLocality": "București",
                    "addressCountry": "RO"},
        "contactPoint": [{"@type": "ContactPoint",
                          "telephone": C.PHONE.replace(" ", ""),
                          "email": C.EMAIL,
                          "contactType": "sales",
                          "availableLanguage": ["ro", "en"]}],
    }
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps(data, ensure_ascii=False, separators=(",", ":")))


def clip(text, limit=42):
    """Scurteaza pe granita de cuvant, nu in mijlocul lui."""
    text = text.strip()
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(" ,.;:") + "…"


def page_title(headline):
    """Titlul din tab. Sufixul de brand intra doar daca nu impinge peste 62 de
    caractere — altfel Google il taie oricum si pierdem finalul titlului."""
    headline = headline.rstrip(".")
    suffixed = "%s | GDH" % headline
    return suffixed if len(suffixed) <= 62 else headline


def meta_desc(lede, sections=(), floor=70):
    """Descrierea de cautare. Daca lede-ul e prea scurt, imprumutam din prima
    sectiune pana trecem de pragul util."""
    text = lede.strip()
    for item in sections:
        if len(text) >= floor:
            break
        body = item[1] if isinstance(item, (tuple, list)) else item.get("body", "")
        text = (text + " " + body.strip()).strip()
    if len(text) > 180:
        text = text[:177].rsplit(" ", 1)[0] + "…"
    return text


def shell(page, title, desc, body, current="", noindex=False, jsonld=""):
    return (
        '<!DOCTYPE html><html lang="en"><head>%s'
        '<link rel="stylesheet" href="css/site.css">%s</head><body>'
        '<a class="gdh-skip" href="#main">Skip to content</a>'
        '%s%s%s'
        '<main id="main" tabindex="-1">%s</main>'
        '%s<script src="js/site.js" defer></script></body></html>'
        % (head(page, title, desc, noindex), jsonld,
           U.chrome(C.TOPBAR, C.NAV, LOGO_DARK, current), "",
           U.drawer(C.NAV),
           body,
           U.footer(C.FOOTER_NAV, LOGO_LIGHT, C.LEGAL)))


# ----------------------------------------------------------------- fragments
def contact_section():
    c = C.CONTACT
    return U.section(
        U.head_block("Contact", "Get in touch with the commercial desk.")
        + U.contact_band(c["name"], c["role"], c["blurb"], C.EMAIL, C.PHONE),
        variant="grey")


def cta_section(title, text):
    return U.section(
        U.cta_band(title, text,
                   U.btn("Partner with us", "partner-with-us.html"),
                   U.btn("Contact sales", "contact.html", "ghost")),
        variant="grey")


def faq_section(items, title="Questions brands ask us."):
    if not items:
        return ""
    return U.section(U.head_block("FAQ", title)
                     + U.accordion([(i["q"], i["a"]) for i in items]))


def simple_page(page, data, current="", trail=None, noindex=False, extra=""):
    """Pagina de text: antet inchis, sectiuni de proza, indemn."""
    trail = trail or [("Home", "index.html"), (data["kicker"], page)]
    body = (U.pagehead(trail, data["kicker"], data["title"], data["lede"],
                       image=img(page))
            + U.section(U.prose_blocks(data["sections"]))
            + extra
            + cta_section("Send us your range.",
                          "Tell us what you make and which shelves it belongs on."))
    return shell(page, page_title(data["title"]),
                 meta_desc(data["lede"], data["sections"]), body, current, noindex)


# ---------------------------------------------------------------- home page
def home():
    h = C.HOME
    hero = U.hero(h["kicker"], h["title"], h["lede"],
                  [U.btn("Partner with us", "partner-with-us.html"),
                   U.btn("What we do", "distribution.html", "grad")],
                  image=img("index.html"))

    topics = U.section(
        U.head_block("Start here", h["topics_title"]) + U.topics(h["topics"]),
        tight=True)

    features = U.section("".join(
        '<div class="split%s" style="margin-bottom:64px">'
        '<div class="split__media">%s</div><div>%s<h2 class="h1">%s</h2>'
        '<p class="muted" style="margin-top:16px">%s</p>'
        '<div style="margin-top:24px">%s</div></div></div>'
        % (" split--reverse" if i % 2 else "",
           ('<img src="%s" alt="" loading="lazy" decoding="async">' % U.esc(f["image"]))
           if f.get("image") else '<div style="background:var(--g100);aspect-ratio:4/3"></div>',
           U.eyebrow(f["kicker"]), U.esc(f["title"]), U.esc(f["text"]),
           U.link_arrow("Read more", f["href"]))
        for i, f in enumerate(h["features"])), variant="grey")

    sectors = U.section(
        U.head_block("Sectors", h["sectors_title"], h["sectors_lede"])
        + '<div class="grid grid--4">%s</div>' % "".join([
            U.tile("Grocery", "Food and beverage into national grocery chains.",
                   "sector-grocery.html"),
            U.tile("Health & Beauty", "Personal care into drugstore chains and pharmacies.",
                   "sector-health-beauty.html"),
            U.tile("Convenience", "Small-format stores no single brand can serve alone.",
                   "sector-convenience.html"),
            U.tile("Dental", "Materials and consumables into practices and laboratories.",
                   "sector-dental.html"),
        ]))

    services = U.section(
        U.head_block("Distribution", h["services_title"], h["services_lede"],
                     U.link_arrow("See everything we do", "distribution.html"))
        + '<div class="grid grid--4">%s</div>' % "".join([
            U.card("Chain listings", "We take your range to the buyers we already supply.",
                   "service-chain-listings.html", meta="01", image="img/planning.webp"),
            U.card("Stock & delivery", "We buy the stock and supply every depot and store.",
                   "service-stock-and-delivery.html", meta="02",
                   image="img/warehouse-racking.webp"),
            U.card("Shelf execution", "Our people place it, hold the planogram and report back.",
                   "service-shelf-execution.html", meta="03", image="img/team.webp"),
            U.card("Sell-out visibility", "What sold, where, and how fast — back to you.",
                   "service-sell-out-visibility.html", meta="04", image="img/stock-check.webp"),
        ]), variant="grey")

    stats = U.section(
        U.head_block("The network", h["stats_title"]) + U.stats(C.STATS)
        + '<p class="muted" style="margin-top:28px;font-size:.95rem">%s</p>'
        % U.esc(h["stats_note"]), variant="ink", tight=True)

    import inner_gdh as I
    cases = list(I.CASES.items())[:3]
    brands = U.section(
        U.head_block("Brands", "Programmes we run.",
                     align_cta=U.link_arrow("All brands we distribute", "brands.html"))
        + '<div class="grid grid--3">%s</div>' % "".join(
            U.card(t, lead, fn, meta=sector) for fn, (t, sector, lead, _it) in cases))

    posts = list(I.POSTS.items())[:3]
    insights = U.section(
        U.head_block("Insights", "From the commercial desk.",
                     align_cta=U.link_arrow("All insights", "insights.html"))
        + '<div class="grid grid--3">%s</div>' % "".join(
            U.card(title, paras[0][:132].rsplit(" ", 1)[0] + "…", fn, meta="%s · %s" % (cat, date))
            for fn, (cat, date, title, paras) in posts), variant="grey")

    body = (hero + topics + features + sectors + services + stats + brands
            + insights + contact_section()
            + cta_section(h["cta_title"], h["cta_text"]))
    return shell("index.html",
                 "GDH — Global Distribution Holdings | Retail & Dental Distribution",
                 "GDH buys, stocks and distributes retail and dental products into the "
                 "country's largest store chains and dental practices — at no cost to the "
                 "brands we carry.",
                 body, current="", jsonld=org_jsonld())


# ------------------------------------------------- sector / service pages
def data_page(entry, current):
    page = entry["slug"] + ".html"
    trail = [("Home", "index.html"), (entry["kicker"], page)]
    body = U.pagehead(trail, entry["kicker"], entry["title"], entry["lede"],
                      [U.btn("Partner with us", "partner-with-us.html"),
                       U.btn("Contact sales", "contact.html", "on-dark")],
                      image=img(page))
    body += U.section(U.prose_blocks([(s["heading"], s["body"]) for s in entry["sections"]]))
    if entry.get("bullets"):
        body += U.section(
            U.head_block("", "In practice.")
            + '<div class="grid grid--3">%s</div>' % "".join(
                '<div class="tile"><h3 class="h3">%s</h3>'
                '<p class="muted" style="margin-top:10px">%s</p></div>'
                % (U.esc(b["title"]), U.esc(b["text"])) for b in entry["bullets"]),
            variant="grey")
    body += faq_section(entry.get("faq", []))
    body += cta_section("Send us your range.",
                        "We will tell you honestly where it fits and how fast we can start.")
    return shell(page, page_title(entry["title"]),
                 meta_desc(entry["lede"], [(x["heading"], x["body"]) for x in entry["sections"]]),
                 body, current)


# ----------------------------------------------------------- listing pages
def listing(page, kicker, title, lede, cards, current, section_title="All of them."):
    body = (U.pagehead([("Home", "index.html"), (kicker, page)], kicker, title, lede,
                       image=img(page))
            + U.section(U.head_block("", section_title)
                        + '<div class="grid grid--3">%s</div>' % "".join(cards))
            + cta_section("Send us your range.",
                          "Tell us what you make and which shelves it belongs on."))
    return shell(page, page_title(title), meta_desc(lede), body, current)


def article(page, kicker, title, lede, blocks, back, trail_parent, current):
    body = (U.pagehead([("Home", "index.html"), trail_parent, (clip(title), page)],
                       kicker, title, lede, image=img(page))
            + U.section(U.prose_blocks(blocks))
            + U.section(U.btn_row(U.btn(back[0], back[1], "ghost")), tight=True, reveal=False)
            + cta_section("Send us your range.",
                          "Tell us what you make and which shelves it belongs on."))
    return shell(page, page_title(title), meta_desc(lede, [("", b) for _h, b in blocks]),
                 body, current)


# ------------------------------------------------------------- contact page
def contact_page():
    c = C.CONTACT
    form = (
        '<form data-gdh-form="1" data-subject="Distribution enquiry">'
        '<div class="grid grid--2">'
        '<label class="field"><span>Name</span><input name="Name" required></label>'
        '<label class="field"><span>Company</span><input name="Company" required></label>'
        '<label class="field"><span>Email</span><input name="Email" type="email" required></label>'
        '<label class="field"><span>Phone</span><input name="Phone"></label>'
        '</div>'
        '<label class="field"><span>What do you make?</span>'
        '<textarea name="Message" required placeholder="Your range, your monthly capacity, '
        'and the chains or practices you want to reach."></textarea></label>'
        '<button class="btn btn--primary" type="submit">Send message%s</button>'
        '</form>' % U.ARROW)
    aside = (
        '<div>%s<h2 class="h2">Office</h2>'
        '<p class="muted" style="margin-top:12px">%s</p>'
        '<p style="margin-top:16px"><a class="link-arrow" href="mailto:%s">%s</a></p>'
        '<p style="margin-top:16px"><a class="link-arrow" href="tel:%s">%s</a></p></div>'
        % (U.eyebrow("Where we are"), "<br>".join(U.esc(a) for a in C.ADDRESS),
           U.esc(C.EMAIL), U.esc(C.EMAIL),
           U.esc(C.PHONE.replace(" ", "")), U.esc(C.PHONE)))
    body = (U.pagehead([("Home", "index.html"), ("Contact", "contact.html")],
                       c["kicker"], c["title"], c["lede"])
            + U.section('<div class="split" style="align-items:start">%s<div>%s</div></div>'
                        % (aside, form)))
    return shell("contact.html", "Contact | GDH", c["lede"], body, "")


# ----------------------------------------------------------- style guide
def style_guide():
    import theme_gdh as T
    swatches = "".join(
        '<div><div style="height:104px;background:%s;border:1px solid var(--g100)"></div>'
        '<p class="card__meta" style="margin-top:10px">%s</p>'
        '<p class="muted" style="font-size:.9rem">%s</p></div>'
        % (T.TOKENS[k], U.esc(label), T.TOKENS[k])
        for k, label in [("accent", "Teal"), ("accent-bright", "Teal bright"), ("ink", "Ink"),
                         ("grey-50", "Surface"), ("white", "White")])
    type_rows = "".join(
        '<div style="border-top:1px solid var(--g100);padding:22px 0">'
        '<p class="card__meta">%s</p><p class="%s" style="margin-top:8px">%s</p></div>'
        % (U.esc(name), cls, U.esc(sample))
        for name, cls, sample in [
            ("Hero", "hero-title", "Your product, on the shelves that matter."),
            ("Heading 1", "h1", "Two channels, one network."),
            ("Heading 2", "h2", "What we do for a brand."),
            ("Lede", "lede", "GDH buys your product, stocks it and sells it on."),
        ])
    buttons = U.btn_row(U.btn("Primary", "#"), U.btn("Ghost", "#", "ghost"))
    body = (U.pagehead([("Home", "index.html"), ("Style guide", "style-guide.html")],
                       "Style guide", "The GDH visual system.",
                       "Colour, type and the components this site is built from.")
            + U.section(U.head_block("Colour", "Palette.")
                        + '<div class="grid grid--4">%s</div>' % swatches)
            + U.section(U.head_block("Type", "Roboto, five weights.") + type_rows,
                        variant="grey")
            + U.section(U.head_block("Components", "Buttons and links.")
                        + buttons + '<p style="margin-top:28px">%s</p>'
                        % U.link_arrow("Arrow link", "#"))
            + U.section(U.head_block("Logo", "On light and on dark.")
                        + '<div class="grid grid--2">'
                        '<div style="padding:44px;background:var(--g50)">'
                        '<img src="%s" alt="The GDH logo on a light background" style="height:64px;width:auto"></div>'
                        '<div style="padding:44px;background:var(--ink)">'
                        '<img src="%s" alt="The GDH logo on a dark background" style="height:64px;width:auto"></div>'
                        '</div>' % (LOGO_DARK, LOGO_LIGHT), variant="grey"))
    return shell("style-guide.html", "Style guide | GDH",
                 "The GDH visual system: the colour palette, the Roboto type scale, the "
                 "button and link components, and how the logo is used on light and dark "
                 "backgrounds.", body, "")


# ------------------------------------------------------------- build it all
def build_all(out, pages_data):
    """Scrie toate paginile in `out`. `pages_data` e lista din pages_data_gdh."""
    import inner_gdh as I
    written = {}

    def put(name, markup):
        with open(os.path.join(out, name), "w", encoding="utf-8") as fh:
            fh.write(markup)
        written[name] = len(markup)

    put("index.html", home())

    # --- sector si serviciu
    for entry in pages_data:
        current = "distribution" if entry["slug"].startswith(("distribution", "service-")) \
            else "sectors"
        put(entry["slug"] + ".html", data_page(entry, current))

    # --- programele de client
    case_cards = [U.card(t, lead, fn, meta=sector)
                  for fn, (t, sector, lead, _i) in I.CASES.items()]
    put("brands.html", listing(
        "brands.html", "Brands", "Brands we distribute.",
        "How food, household, health and dental brands reached chain listings and practice "
        "shelves through GDH.", case_cards, "brands", "Programmes we run."))
    for fn, (title, sector, lead, items) in I.CASES.items():
        put(fn, article(fn, sector, title, lead, items,
                        ("All brands", "brands.html"),
                        ("Brands", "brands.html"), "brands"))

    # --- articole
    post_cards = [U.card(title, paras[0][:132].rsplit(" ", 1)[0] + "…", fn,
                         meta="%s · %s" % (cat, date))
                  for fn, (cat, date, title, paras) in I.POSTS.items()]
    put("insights.html", listing(
        "insights.html", "Insights", "From the commercial desk.",
        "Practical guidance on chain listings, on-shelf availability, sell-out data and the "
        "dental channel.", post_cards, "insights", "Latest thinking."))
    for fn, (cat, date, title, paras) in I.POSTS.items():
        put(fn, article(fn, "%s · %s" % (cat, date), title, paras[0],
                        [("", p) for p in paras[1:]],
                        ("More insights", "insights.html"),
                        ("Insights", "insights.html"), "insights"))

    # --- pagini scrise de mana
    put("about-us.html", simple_page(
        "about-us.html", C.ABOUT, "about",
        extra=U.section(U.head_block("The network", "In short.") + U.stats(C.STATS),
                        variant="grey")))
    put("partner-with-us.html", simple_page("partner-with-us.html", C.PARTNER))
    put("careers.html", simple_page("careers.html", C.CAREERS))
    put("locations.html", simple_page("locations.html", C.LOCATIONS))
    put("licenses.html", simple_page("licenses.html", C.LICENCES))
    put("changelog.html", simple_page("changelog.html", C.CHANGELOG))
    put("404.html", simple_page("404.html", C.NOT_FOUND, noindex=True))
    put("contact.html", contact_page())
    put("style-guide.html", style_guide())
    return written


def deploy_files(out, pages):
    """robots, sitemap, antete si redirectari pentru Cloudflare Pages."""
    urls = sorted(p for p in pages if p.endswith(".html") and p != "404.html")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = C.SITE_URL + ("/" if u == "index.html" else "/" + u[:-5])
        sm.append("  <url><loc>%s</loc></url>" % loc)
    sm.append("</urlset>")
    open(os.path.join(out, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")

    open(os.path.join(out, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % C.SITE_URL)

    rows = [(was, now) for was, now in C.redirects() if now in pages]
    open(os.path.join(out, "_redirects"), "w", encoding="utf-8").write(
        "".join("/%s  /%s  301\n" % (was[:-5], now[:-5]) for was, now in rows))

    open(os.path.join(out, "_headers"), "w", encoding="utf-8").write(
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
        "\n/css/*\n  Cache-Control: public, max-age=31536000, immutable\n"
        "\n/js/*\n  Cache-Control: public, max-age=31536000, immutable\n")
