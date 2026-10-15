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
    "insights.html": "img/planning.webp",
    "about-us.html": "img/team.webp",
    "careers.html": "img/team.webp",
    "locations.html": "img/warehouse-wide.webp",
    "partner-with-us.html": "img/planning.webp",
}


def img(slot):
    return IMAGES.get(slot)


# --------------------------------------------------------------------- shell
def head(page, title, desc, noindex=False, og_type="website"):
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
        '<meta name="theme-color" content="#000000">'
        '<meta name="color-scheme" content="light">'
        '<meta property="og:type" content="%s">'
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
           e(url), e(og_type), e(C.SITE_NAME), e(url), e(title), e(desc), e(og),
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
                    "streetAddress": "%s, %s" % (C.ADDRESS[0], C.ADDRESS[1]),
                    "postalCode": "307200",
                    "addressLocality": "Ghiroda",
                    "addressRegion": "Timiș",
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


def newest_first(posts):
    """Articolele, de la cel mai nou. Dictionarul nu era in ordinea datelor."""
    months = ("January February March April May June July August September "
              "October November December").split()

    def key(item):
        date = item[1][1]
        parts = date.replace(",", "").split()
        try:
            return (int(parts[2]), months.index(parts[1]) + 1, int(parts[0]))
        except (IndexError, ValueError):
            return (0, 0, 0)

    return sorted(posts.items(), key=key, reverse=True)


def page_title(headline):
    """Titlul din tab. Sufixul de brand intra doar daca nu impinge peste 62 de
    caractere — altfel Google il taie oricum si pierdem finalul titlului."""
    headline = headline.rstrip(".")
    suffixed = "%s | GDH" % headline
    return suffixed if len(suffixed) <= 62 else headline


def meta_desc(lede, sections=(), floor=70):
    """Descrierea de cautare. Daca lede-ul e prea scurt, imprumutam din prima
    sectiune pana trecem de pragul util."""
    # ** e marcaj de ingrosare pentru pagina, nu text: nu are ce cauta in
    # description, og:description sau twitter:description
    text = lede.replace("**", "").strip()
    for item in sections:
        if len(text) >= floor:
            break
        body = item[1] if isinstance(item, (tuple, list)) else item.get("body", "")
        text = (text + " " + body.replace("**", "").strip()).strip()
    if len(text) > 180:
        text = text[:177].rsplit(" ", 1)[0] + "…"
    return text


# linkurile de companie din meniul complet
COMPANY = [
    ("About us", "about-us.html"),
    ("Insights", "insights.html"),
    ("Careers", "careers.html"),
    ("News", "news.html"),
    ("Locations", "locations.html"),
    ("Partner with us", "partner-with-us.html"),
    ("Contact", "contact.html"),
]


def shell(page, title, desc, body, current="", noindex=False, jsonld="", og_type="website",
          over=False):
    """`over`: pagina incepe cu bannerul video, antetul porneste alb."""
    contact = (C.EMAIL, C.PHONE, C.ADDRESS)
    return (
        '<!DOCTYPE html><html lang="en"><head>%s'
        '<link rel="stylesheet" href="css/site.css">%s</head><body>'
        '<a class="gdh-skip" href="#main">Skip to content</a>'
        '%s%s'
        '<main id="main" tabindex="-1">%s</main>'
        '%s<script src="js/site.js" defer></script></body></html>'
        % (head(page, title, desc, noindex, og_type), jsonld,
           U.chrome(C.TOPBAR, C.NAV, LOGO_DARK, current, over=over),
           U.drawer(C.NAV, COMPANY, contact, LOGO_DARK),
           body,
           U.footer(C.FOOTER_NAV, LOGO_LIGHT, C.LEGAL, contact)))


# ----------------------------------------------------------------- fragments
def contact_section():
    c = C.CONTACT
    return U.section(
        U.head_block("Contact", "Get in touch with the commercial desk.",
                     "We read everything that arrives and reply either way.")
        + U.contact_band(c["name"], c["role"], c["blurb"], C.EMAIL, C.PHONE),
        variant="grey")


def cta_section(title, text):
    return U.cta_band(title, text,
                      U.btn("Partner with us", "partner-with-us.html"),
                      U.btn("Contact sales", "contact-sales.html", "on-dark"))


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
# Serviciile din vitrina de pe prima pagina. Etichetele sunt luate din ce
# promite pagina fiecarui serviciu, nu inventate.
SERVICES = [
    dict(title="Chain listings", href="service-chain-listings.html",
         image="img/planning.webp",
         text="We prepare the submission, take the meeting with the chain buyers we already "
              "supply, and buy the opening order ourselves.",
         tags=["Submission", "Buyer meeting", "Opening order"]),
    dict(title="Stock & delivery", href="service-stock-and-delivery.html",
         image="img/warehouse-racking.webp",
         text="One delivery into our bay. From there the stock is ours: we store it and "
              "deliver it to every depot and store, every week.",
         tags=["Goods-in", "Storage", "Weekly delivery"]),
    dict(title="Shelf execution", href="service-shelf-execution.html",
         image="img/team.webp",
         text="Field teams correct facings, rebuild displays and photograph every store "
              "call, so the planogram holds after launch week.",
         tags=["Facings", "Displays", "Store photos"]),
    dict(title="Sell-out visibility", href="service-sell-out-visibility.html",
         image="img/stock-check.webp",
         text="Weekly rate of sale per chain and SKU, with weeks of cover and batch "
              "records — what sold, where, and how fast.",
         tags=["Rate of sale", "Weeks of cover", "Batch records"]),
    dict(title="Returns & recalls", href="service-returns.html",
         image="img/packing.webp",
         text="Collected on the delivery round, graded at our hub, and every recall traced "
              "back by batch.",
         tags=["Collection", "Grading", "Recall tracing"]),
]


def home():
    h = C.HOME
    hero = U.home_hero(
        ["Your product,", "on the shelves", "that matter."],
        "We buy, stock and sell your range into the country’s largest store chains and "
        "dental practices.",
        [U.btn("Partner with us", "partner-with-us.html"),
         U.btn("What we do", "distribution.html", "on-dark")],
        [(s["title"], s["href"]) for s in SERVICES[:4]],
        ("img/gdh-mark.png", "Retail & dental", "Two channels, one network"),
        ("Based in Ghiroda, Romania", "Europe/Bucharest"))

    about = U.section(
        U.lead_say(h["lede"], "About GDH")
        + '<div class="lead-say" style="margin-top:44px"><div></div><div>%s</div></div>'
        % U.btn("Learn about us", "about-us.html"))

    # banda care curge, apoi „de unde incep” si cele doua povesti, pe gri
    feats = "".join(
        U.feature(f["title"], f["kicker"], f["text"], f["href"], f["image"], tag="0%d" % i)
        for i, f in enumerate(h["features"], 1))
    start = ('<section class="section section--grey" style="padding-top:clamp(60px,7vw,100px)">'
             '%s<div class="wrap" data-reveal style="margin-top:clamp(50px,6vw,90px)">%s%s'
             '<div class="features" style="margin-top:clamp(70px,8vw,120px)">%s</div>'
             '</div></section>'
             % (U.marquee(["Retail", "~", "Dental", "~", "Distribution", "~"]),
                U.head_block("Start here", h["topics_title"],
                             "Six ways brands usually begin. Pick the one closest to yours."),
                U.topics(h["topics"]), feats))

    services = U.section(
        U.head_block("Distribution", h["services_title"], h["services_lede"],
                     U.link_arrow("See everything we do", "distribution.html"))
        + U.services_showcase(SERVICES), variant="ink", cls="is-dark")

    how = U.section(
        U.head_block("How it works", "From your range to a full shelf.", center=True)
        + U.process(
            [("Send us your range",
              "Product list, pack sizes, capacity. Send what you have; we fill the gaps."),
             ("We meet the buyer",
              "We prepare the submission and take it to buyers we already supply."),
             ("We buy the stock",
              "We buy the opening order, hold it and deliver to every depot and store."),
             ("On shelf, reported",
              "Field teams hold the planogram; you see sell-out every week.")],
            "Need a route to market?", "It costs your brand nothing.",
            U.btn("Send us your range", "partner-with-us.html")))

    sectors = U.section(
        U.head_block("Sectors", h["sectors_title"], h["sectors_lede"],
                     U.link_arrow("All sectors", "sectors.html"))
        + '<div class="grid grid--4">%s</div>' % "".join([
            U.tile("Grocery", "Food and beverage into national grocery chains.",
                   "sector-grocery.html", "/01"),
            U.tile("Health & Beauty", "Personal care into drugstore chains and pharmacies.",
                   "sector-health-beauty.html", "/02"),
            U.tile("Convenience", "Small-format stores no single brand can serve alone.",
                   "sector-convenience.html", "/03"),
            U.tile("Dental", "Materials and consumables into practices and laboratories.",
                   "sector-dental.html", "/04"),
        ]), variant="grey")

    stats = U.section(U.giant("The network", "in short") + U.stats(C.STATS),
                      variant="ink", cls="is-dark")

    import inner_gdh as I

    posts = newest_first(I.POSTS)[:3]
    insights = U.section(
        U.head_block("Insights", "From the commercial desk.",
                     align_cta=U.link_arrow("All insights", "insights.html"))
        + '<div class="grid grid--3">%s</div>' % "".join(
            U.card(title, paras[0][:132].rsplit(" ", 1)[0] + "…", fn, meta="%s · %s" % (cat, date))
            for fn, (cat, date, title, paras) in posts))

    body = (hero + about + start + services + how + sectors + stats
            + insights + contact_section()
            + cta_section(h["cta_title"], h["cta_text"]))
    return shell("index.html",
                 "GDH — Global Distribution Holdings | Retail & Dental Distribution",
                 "GDH buys, stocks and distributes retail and dental products into the "
                 "country's largest store chains and dental practices — at no cost to the "
                 "brands we carry.",
                 body, current="", jsonld=org_jsonld(), over=True)


# ------------------------------------------------- sector / service pages
def siblings(slug, limit=3):
    """Pagini vecine din aceeasi sectiune de meniu, pentru blocul de la final."""
    for group in C.NAV:
        items = group.get("items") or []
        hrefs = [h for _l, h, _d in items]
        if slug + ".html" not in hrefs:
            continue
        others = [(l, h, d) for l, h, d in items if h != slug + ".html"]
        if not others:
            return []
        # pornim din dreptul paginii curente, ca fiecare pagina sa arate alti vecini
        start = hrefs.index(slug + ".html")
        rotated = others[start % len(others):] + others[:start % len(others)]
        return rotated[:limit]
    return []


def data_page(entry, current):
    """O pagina de sector sau de serviciu.

    Continutul are aceeasi forma peste tot — sectiuni, fise, intrebari — deci
    daca il randam mereu la fel ies pagini identice. Alegem unul din trei
    ritmuri, dupa pozitia paginii, ca doua pagini vecine sa nu arate la fel.
    """
    page = entry["slug"] + ".html"
    trail = [("Home", "index.html"), (entry["kicker"], page)]
    secs = [(x["heading"], x["body"]) for x in entry["sections"]]
    shot = img(page)
    rhythm = entry.get("rhythm", 0)

    body = U.pagehead(trail, entry["kicker"], entry["title"], entry["lede"],
                      [U.btn("Partner with us", "partner-with-us.html"),
                       U.btn("Contact sales", "contact-sales.html", "on-dark")],
                      image=shot)

    def spread(items, reverse=False):
        """Text langa fotografie; fara fotografie, proza pe doua coloane."""
        if shot and items:
            h, b = items[0]
            return U.split(h, [b], image=shot, reverse=reverse)
        return U.two_col(items)

    if rhythm == 0:
        body += U.section(U.lead_say(secs[0][1], secs[0][0]))
        body += U.section(spread(secs[1:2]), variant="grey")
        if len(secs) > 2:
            body += U.statement(entry["kicker"], secs[2][1])
        if len(secs) > 3:
            body += U.section(U.two_col(secs[3:]))
    elif rhythm == 1:
        body += U.section(U.steps(secs[:3]))
        if len(secs) > 3:
            body += U.statement(entry["kicker"], secs[3][1])
        if len(secs) > 4:
            body += U.section(spread(secs[4:5], reverse=True), variant="grey")
    else:
        body += U.section(U.lead_say(secs[0][1], secs[0][0]))
        body += U.section(U.two_col(secs[1:3]), variant="grey")
        if len(secs) > 3:
            body += U.section(U.prose_blocks(secs[3:4]), variant="ink", cls="is-dark")
        if len(secs) > 4:
            body += U.section(spread(secs[4:5]))

    if entry.get("bullets"):
        body += U.section(U.head_block("", "In practice.") + U.facts(entry["bullets"]),
                          variant="" if rhythm == 1 else "grey")
    body += faq_section(entry.get("faq", []))

    near = siblings(entry["slug"])
    if near:
        body += U.section(U.head_block("", "Next door.") + U.related(near), tight=True)

    body += cta_section("Send us your range.",
                        "We will tell you honestly where it fits and how fast we can start.")
    return shell(page, page_title(entry["title"]),
                 meta_desc(entry["lede"], secs), body, current)


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
                 body, current, og_type="article")


# ------------------------------------------------------------- contact page
def contact_page():
    c = C.CONTACT
    form = (
        '<form data-gdh-form="1" data-subject="Distribution enquiry" '
        'method="post" action="contact.html">'
        '<div class="grid grid--2">'
        '<label class="field"><span>Name</span><input name="Name" required></label>'
        '<label class="field"><span>Company</span><input name="Company" required></label>'
        '<label class="field"><span>Email</span><input name="Email" type="email" required></label>'
        '<label class="field"><span>Phone</span><input name="Phone"></label>'
        '</div>'
        '<label class="field"><span>What do you make?</span>'
        '<textarea name="Message" required placeholder="Your range, your monthly capacity, '
        'and the chains or practices you want to reach."></textarea></label>'
        + U.submit("Send message") +
        '</form>')
    aside = (
        '<div>%s<h2 class="h1" style="font-size:var(--t-h3)">Ghiroda, Timiș.</h2>'
        '<p class="muted" style="margin-top:20px;font-size:var(--t-large)">%s</p>'
        '<div style="display:flex;flex-direction:column;align-items:flex-start;gap:18px;margin-top:36px">'
        '<a class="link-arrow" href="mailto:%s">%s%s</a>'
        '<a class="link-arrow" href="tel:%s">%s%s</a></div></div>'
        % (U.eyebrow("Where we are"), "<br>".join(U.esc(a) for a in C.ADDRESS),
           U.esc(C.EMAIL), U.esc(C.EMAIL), U.HOOK,
           U.esc(C.PHONE.replace(" ", "")), U.esc(C.PHONE), U.HOOK))
    body = (U.pagehead([("Home", "index.html"), ("Contact", "contact.html")],
                       c["kicker"], c["title"], c["lede"])
            + U.section('<div class="split" style="align-items:start">%s<div>%s</div></div>'
                        % (aside, form)))
    return shell("contact.html", "Contact | GDH", c["lede"], body, "")


# ----------------------------------------------------------- style guide
def style_guide():
    import theme_gdh as T
    swatches = "".join(
        '<div><div style="height:140px;border-radius:8px;background:%s;'
        'border:1px solid var(--line)"></div>'
        '<p class="card__meta" style="margin-top:14px"><span class="chip">%s</span>'
        '<span>%s</span></p></div>'
        % (T.TOKENS[k], U.esc(label), T.TOKENS[k])
        for k, label in [("black", "Black"), ("dark-two", "Dark"), ("text", "Text"),
                         ("light-3", "Light 3"), ("light-2", "Surface"), ("white", "White")])
    swatches += ('<div><div style="height:140px;border-radius:8px;'
                 'background:#000 url(%s) center/cover"></div>'
                 '<p class="card__meta" style="margin-top:14px"><span class="chip">Gradient</span>'
                 '<span>banner video</span></p></div>' % U.POSTER)
    type_rows = "".join(
        '<div style="border-top:1px solid var(--line);padding:28px 0;display:grid;'
        'grid-template-columns:minmax(120px,1fr) 4fr;gap:20px">'
        '<p class="mono" style="font-size:12px;color:var(--text)">%s</p><p class="%s">%s</p></div>'
        % (U.esc(name), cls, U.esc(sample))
        for name, cls, sample in [
            ("Display / 90", "hero-title", "Your product, on the shelves that matter."),
            ("Heading / 70", "h1", "Two channels, one network."),
            ("Heading / 28", "h2", "What we do for a brand."),
            ("Body / 16", "lede", "GDH buys your product, stocks it and sells it on."),
            ("Label / mono 14", "mono", "Retail ~ Dental ~ Distribution"),
        ])
    buttons = U.btn_row(U.btn("Primary", "#"), U.btn("Ghost", "#", "ghost"))
    body = (U.pagehead([("Home", "index.html"), ("Style guide", "style-guide.html")],
                       "Style guide", "The GDH visual system.",
                       "Colour, type and the components this site is built from.")
            + U.section(U.head_block("Colour", "Palette.",
                                     "Black, white and three greys. Colour comes from one "
                                     "place: the moving gradient, which rhymes with the logo.")
                        + '<div class="grid grid--4">%s</div>' % swatches)
            + U.section(U.head_block("Type", "Inter Tight and IBM Plex Mono.") + type_rows,
                        variant="grey")
            + U.section(U.head_block("Components", "Buttons and links.")
                        + buttons + '<p style="margin-top:36px">%s</p>'
                        % U.link_arrow("Arrow link", "#"))
            + U.section(U.head_block("Logo", "On light and on dark.")
                        + '<div class="grid grid--2">'
                        '<div style="padding:54px;background:#fff;border-radius:8px">'
                        '<img src="%s" alt="The GDH logo on a light background" style="height:64px;width:auto"></div>'
                        '<div style="padding:54px;background:#000;border-radius:8px">'
                        '<img src="%s" alt="The GDH logo on a dark background" style="height:64px;width:auto"></div>'
                        '</div>' % (LOGO_DARK, LOGO_LIGHT), variant="grey"))
    return shell("style-guide.html", "Style guide | GDH",
                 "The GDH visual system: the black-and-white palette and banner gradient, the "
                 "Inter Tight and IBM Plex Mono type scale, the button and link components, "
                 "and the logo on light and dark backgrounds.", body, "")


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

    # --- articole
    post_cards = [U.card(title, paras[0][:132].rsplit(" ", 1)[0] + "…", fn,
                         meta="%s · %s" % (cat, date))
                  for fn, (cat, date, title, paras) in newest_first(I.POSTS)]
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
    # paginile juridice, de presa si de contact comercial
    try:
        import legal_data_gdh
        for entry in legal_data_gdh.PAGES:
            name = entry["slug"] + ".html"
            note = ""
            if entry.get("needsReview"):
                note = U.section(
                    '<div class="tile" style="border-left-color:var(--accent)">'
                    '<p class="card__meta">Before publication</p>'
                    '<p class="muted" style="margin-top:8px">This page is a working draft. '
                    'The details shown in square brackets must be completed from the '
                    'company’s own registration documents, and the text should be reviewed '
                    'by a qualified adviser before it is relied upon.</p></div>',
                    tight=True, reveal=False)
            put(name, simple_page(name, dict(
                kicker=entry["kicker"], title=entry["title"], lede=entry["lede"],
                sections=entry["sections"]), extra=note))
    except ImportError:
        pass

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
