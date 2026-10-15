# -*- coding: utf-8 -*-
"""Asambleaza paginile GDH din componente si continut.

Fiecare pagina trece prin `shell()`, care pune antetul, navigatia, subsolul si
metadatele. Continutul vine din content_gdh.py (scris de mana), din
pages_data_gdh.py (paginile de sector si serviciu) si din inner_gdh.py
(programele de client si articolele).
"""
import json
import os
import re

import content_gdh as C
import ui_gdh as U

LOGO_DARK = "img/gdh-logo.png"        # pe fundal deschis
LOGO_LIGHT = "img/gdh-logo-light.png"  # pe fundal inchis
STACKED_DARK = "img/gdh-logo-stacked.png"         # sigla verticala, pe deschis
STACKED_LIGHT = "img/gdh-logo-stacked-light.png"  # sigla verticala, pe inchis

# Fotografia din bannerul fiecarei pagini. Paginile de sector si de serviciu
# au fiecare fotografia lor; paginile de text pot repeta una din alta sectiune.
# O pagina care nu apare aici se randeaza curat, fara fotografie: raftul de
# drogherie si cabinetul stomatologic inca nu au fotografii potrivite.
IMAGES = {
    "sectors.html": "img/warehouse-wide.webp",
    "sector-retail.html": "img/packing.webp",
    "sector-grocery.html": "img/stock-check.webp",
    "sector-convenience.html": "img/sortation.webp",
    "sector-private-label.html": "img/planning.webp",
    "distribution.html": "img/operations-floor.webp",
    "service-chain-listings.html": "img/team.webp",
    "service-stock-and-delivery.html": "img/warehouse-racking.webp",
    "service-shelf-execution.html": "img/fulfilment.webp",
    "service-sell-out-visibility.html": "img/planning-desk.webp",
    "service-returns.html": "img/loading-dock.webp",
    "about-us.html": "img/gdh-warehouse-front.webp",
    "careers.html": "img/pallet-jack.webp",
    "locations.html": "img/gdh-warehouse-aerial.webp",
    "contact.html": "img/gdh-warehouse-front.webp",
    "partner-with-us.html": "img/planning.webp",
}

# Toate fotografiile din care se aleg perechile de la finalul paginilor.
LIBRARY = ["img/automation.webp", "img/fulfilment.webp", "img/loading-dock.webp",
           "img/operations-floor.webp", "img/packing.webp", "img/pallet-jack.webp",
           "img/planning.webp", "img/planning-desk.webp", "img/sortation.webp",
           "img/stock-check.webp", "img/team.webp", "img/warehouse-racking.webp",
           "img/warehouse-wide.webp"]


# Fotografiile cladirilor GDH arata ceva anume, deci au descriere; restul sunt
# ilustrative si raman cu alt="" (cititoarele de ecran le sar).
ALT = {
    "img/gdh-warehouse-front.webp": "The GDH warehouse, with the GDH — Global Distribution "
                                    "Holdings sign on its facade",
    "img/gdh-warehouse-aerial.webp": "Aerial view of the GDH warehouse at dusk, with the GDH "
                                     "logo on the wall and loading bays alongside",
}


def alt(src):
    return ALT.get(src, "")


def img(slot):
    return IMAGES.get(slot)


# --------------------------------------------------------------------- shell
def head(page, title, desc, noindex=False, og_type="website", og_image=None,
         og_size=(1200, 630), extra=""):
    url = C.SITE_URL + ("/" if page == "index.html" else "/" + page[:-len(".html")])
    og = C.SITE_URL + "/" + (og_image or "img/og-image.jpg")
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
        '<meta property="og:image:width" content="%d">'
        '<meta property="og:image:height" content="%d">'
        '<meta name="twitter:card" content="summary_large_image">'
        '<meta name="twitter:title" content="%s">'
        '<meta name="twitter:description" content="%s">'
        '<meta name="twitter:image" content="%s">'
        '<link rel="alternate" type="application/rss+xml" title="GDH news" href="%s/news/feed.xml">'
        '%s'
        % (e(title), e(desc),
           '<meta name="robots" content="noindex">' if noindex else "",
           e(url), e(og_type), e(C.SITE_NAME), e(url), e(title), e(desc), e(og),
           og_size[0], og_size[1], e(title), e(desc), e(og), e(C.SITE_URL), extra))


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


def rootify(markup):
    """Legaturile relative devin absolute fata de radacina site-ului.

    Paginile din subfoldere (news/...) si pagina 404 (servita la orice adresa,
    oricat de adanca) n-ar mai gasi css/site.css sau img/... relativ la ele."""
    return re.sub(r'(\s(?:href|src|poster)=")(?!https?:|/|#|mailto:|tel:|data:)',
                  r"\1/", markup)


def shell(page, title, desc, body, current="", noindex=False, jsonld="", og_type="website",
          over=False, og_image=None, og_size=(1200, 630), extra_head=""):
    """`over`: pagina incepe cu bannerul video, antetul porneste alb."""
    # titlul si descrierea scrise de mana au intaietate: ele apar cand linkul
    # e trimis mai departe (vezi seo_gdh.py)
    import seo_gdh
    if seo_gdh.get(page):
        title, desc = seo_gdh.get(page)
    contact = (C.EMAIL, C.PHONE, C.ADDRESS)
    markup = (
        '<!DOCTYPE html><html lang="en"><head>%s'
        '<link rel="stylesheet" href="css/site.css">%s</head><body>'
        '<a class="gdh-skip" href="#main">Skip to content</a>'
        '%s%s'
        '<main id="main" tabindex="-1">%s</main>'
        '%s<script src="js/site.js" defer></script></body></html>'
        % (head(page, title, desc, noindex, og_type, og_image, og_size, extra_head), jsonld,
           U.chrome(C.TOPBAR, C.NAV, LOGO_DARK, current, over=over),
           U.drawer(C.NAV, COMPANY, contact, LOGO_DARK),
           body,
           U.footer(C.FOOTER_NAV, STACKED_LIGHT, C.LEGAL, contact)))
    if "/" in page or page == "404.html":
        markup = rootify(markup)
    return markup


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


def write_card():
    """Partea de jos a cardului lipit, pe paginile de text: adresa de scris."""
    return ('<div><p class="dcard__label" style="color:var(--text)">Write to us</p>'
            '<a class="dcard__mail" href="mailto:%s">%s</a></div>' % (U.esc(C.EMAIL), U.esc(C.EMAIL)))


def simple_page(page, data, current="", trail=None, noindex=False, extra="", lead="",
                buttons=()):
    """Pagina de text, pe structura paginii de detaliu: cuprinsul lipit in
    stanga, randurile titlu / text in dreapta. `lead` intra imediat sub banner
    (formularul de pe Contact sales), `extra` dupa text."""
    trail = trail or [("Home", "index.html"), (data["kicker"], page)]
    secs = [(h, b) for h, b in data["sections"]]
    index = [(h, "#" + U.slug(h)) for h, _b in secs if h]
    card = U.card_tags("On this page", index) + write_card()
    body = (U.pagehead(trail, data["kicker"], data["title"], data["lede"], buttons,
                       image=img(page), figure="©26", alt=alt(img(page)))
            + lead
            + U.section(U.detail(card, U.drows(secs)))
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
         image="img/planning-desk.webp",
         text="We prepare the submission, take the meeting with the chain buyers we already "
              "supply, and buy the opening order ourselves.",
         tags=["Submission", "Buyer meeting", "Opening order"]),
    dict(title="Stock & delivery", href="service-stock-and-delivery.html",
         image="img/loading-dock.webp",
         text="One delivery into our bay. From there the stock is ours: we store it and "
              "deliver it to every depot and store, every week.",
         tags=["Goods-in", "Storage", "Weekly delivery"]),
    dict(title="Shelf execution", href="service-shelf-execution.html",
         image="img/fulfilment.webp",
         text="Field teams correct facings, rebuild displays and photograph every store "
              "call, so the planogram holds after launch week.",
         tags=["Facings", "Displays", "Store photos"]),
    dict(title="Sell-out visibility", href="service-sell-out-visibility.html",
         image="img/stock-check.webp",
         text="Weekly rate of sale per chain and SKU, with weeks of cover and batch "
              "records — what sold, where, and how fast.",
         tags=["Rate of sale", "Weeks of cover", "Batch records"]),
    dict(title="Returns & recalls", href="service-returns.html",
         image="img/pallet-jack.webp",
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
        ("Based in Timișoara, Romania", "Europe/Bucharest"))

    about = U.section(
        U.lead_say(h["lede"], "About GDH")
        + '<div class="lead-say" style="margin-top:44px"><div></div><div>%s</div></div>'
        % U.btn("Learn about us", "about-us.html")
        + U.wide_image("img/gdh-warehouse-aerial.webp", alt("img/gdh-warehouse-aerial.webp")))

    # banda care curge, apoi „de unde incep” si cele doua povesti, pe gri
    feats = "".join(
        U.feature(f["title"], f["kicker"], f["text"], f["href"], f["image"], tag="0%d" % i)
        for i, f in enumerate(h["features"], 1))
    start = ('<section class="section section--grey" style="padding-top:clamp(60px,7vw,100px)">'
             '%s<div class="wrap" style="margin-top:clamp(50px,6vw,90px)">%s%s'
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

    latest = NEWS["posts"][:3]
    news = U.section(
        U.head_block("News", "Latest from GDH.",
                     "Announcements from the network, posted as they happen.",
                     U.link_arrow("All news", "news.html"))
        + '<div class="grid grid--3">%s</div>' % "".join(news_card(p) for p in latest),
        variant="grey") if latest else ""

    body = (hero + about + start + services + how + sectors + stats
            + news + insights + contact_section()
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


# a patra fisa de proces, aceeasi peste tot: e regula de baza a afacerii
NO_INVOICE = dict(title="Nothing to pay",
                  text="No listing fee, no storage charge, no delivery cost. We buy the stock "
                       "and earn from the distribution margin — your brand is never invoiced.")


def position(slug_):
    """Locul paginii in grupul ei din meniu, ca „03~09”, pentru cifra din banner."""
    for group in C.NAV:
        hrefs = [h for _l, h, _d in group.get("items") or []]
        if slug_ + ".html" in hrefs:
            return "%02d~%02d" % (hrefs.index(slug_ + ".html") + 1, len(hrefs))
    return "©26"


_PAIRS = {}


def closing_pair(page, shot, order):
    """Cele doua fotografii de la finalul unei pagini de detaliu.

    Se aleg o data pentru toate paginile, in ordinea meniului: niciodata
    fotografia din bannerul paginii, mereu cele mai putin folosite pana atunci
    pe tot site-ul (bannere, prima pagina, perechile deja date), si nicio
    pereche nu se repeta. Asa fiecare fotografie apare de un numar apropiat de
    ori, in loc ca aceleasi cinci sa se invarta peste tot.
    """
    if not _PAIRS:
        uses = {p: 0 for p in LIBRARY}
        for used in list(IMAGES.values()) + [x["image"] for x in SERVICES] \
                + [f["image"] for f in C.HOME["features"]]:
            if used in uses:
                uses[used] += 1
        seen = set()
        for slug_ in order:
            banner = IMAGES.get(slug_ + ".html")
            if not banner:
                continue
            ranked = sorted((p for p in LIBRARY if p != banner),
                            key=lambda p: (uses[p], LIBRARY.index(p)))
            pair = None
            for i, first in enumerate(ranked):
                for second in ranked[i + 1:]:
                    if frozenset((first, second)) not in seen:
                        pair = (first, second)
                        break
                if pair:
                    break
            seen.add(frozenset(pair))
            for x in pair:
                uses[x] += 1
            _PAIRS[slug_ + ".html"] = list(pair)
    return _PAIRS.get(page, [])


def data_page(entry, current):
    """O pagina de sector sau de serviciu, pe structura paginii de detaliu din
    referinta: banner cu cifra, card lipit cu etichete si contorul de €0,
    randuri titlu / text, fise de proces numerotate, doua imagini la final."""
    page = entry["slug"] + ".html"
    trail = [("Home", "index.html"), (entry["kicker"], page)]
    secs = [(x["heading"], x["body"]) for x in entry["sections"]]
    shot = img(page)

    head = U.pagehead(trail, entry["kicker"], entry["title"], entry["lede"],
                      [U.btn("Partner with us", "partner-with-us.html"),
                       U.btn("Contact sales", "contact-sales.html", "ghost")],
                      image=shot, figure=position(entry["slug"]))

    bullets = list(entry.get("bullets") or [])
    card = (U.card_tags("What you get", [b["title"] for b in bullets])
            + U.count_figure(0, 100, "Billed to the brands we carry", prefix="€"))
    main = U.drows(secs[:2])
    if bullets:
        # regula „nu platiti nimic” intra doar daca pagina nu o spune deja
        said = any(w in (b["title"] + " " + b["text"]).lower()
                   for b in bullets for w in ("invoice", "fee", "pay", "cost", "charge"))
        main += U.pcards(bullets if said else bullets + [NO_INVOICE])
    main += U.drows(secs[2:])
    # paginile fara fotografie (raft, stomatologie) raman fara, ca si pana acum
    if shot:
        import pages_data_gdh as PD
        main += U.duo(closing_pair(page, shot, [e["slug"] for e in PD.PAGES]))

    body = head + U.section(U.detail(card, main))
    body += faq_section(entry.get("faq", []))

    near = siblings(entry["slug"])
    if near:
        body += U.section(U.head_block("Explore", "Next door.") + U.related(near),
                          variant="grey")

    body += cta_section("Send us your range.",
                        "We will tell you honestly where it fits and how fast we can start.")
    return shell(page, page_title(entry["title"]),
                 meta_desc(entry["lede"], secs), body, current)


# ----------------------------------------------------------- listing pages
def listing(page, kicker, title, lede, cards, current, section_title="All of them."):
    body = (U.pagehead([("Home", "index.html"), (kicker, page)], kicker, title, lede,
                       image=img(page), figure="(%02d)" % len(cards))
            + U.section(U.head_block("", section_title)
                        + '<div class="grid grid--3">%s</div>' % "".join(cards))
            + cta_section("Send us your range.",
                          "Tell us what you make and which shelves it belongs on."))
    return shell(page, page_title(title), meta_desc(lede), body, current)


def article(page, kicker, title, lede, blocks, back, trail_parent, current):
    """Articol: banner, apoi fisa lipita (categorie, data, timp de citire) langa text."""
    parts = [p.strip() for p in kicker.split("·")]
    words = sum(len(b.split()) for _h, b in blocks) + len(lede.split())
    info = U.card_info([("Category", parts[0]),
                        ("Published", parts[1] if len(parts) > 1 else ""),
                        ("Reading time", "%d min" % max(1, round(words / 200)))])
    card = ('<div><p class="dcard__label">[ article ]</p><div style="margin-top:18px">%s</div></div>'
            '<div>%s</div>' % (info, U.btn(back[0], back[1], "primary")))
    day = parts[1].split()[-1][-2:] if len(parts) > 1 else "26"
    body = (U.pagehead([("Home", "index.html"), trail_parent, (clip(title), page)],
                       parts[0], title, lede, image=img(page), figure="©" + day)
            + U.section(U.detail(card, U.prose_blocks(blocks)))
            + cta_section("Send us your range.",
                          "Tell us what you make and which shelves it belongs on."))
    return shell(page, page_title(title), meta_desc(lede, [("", b) for _h, b in blocks]),
                 body, current, og_type="article")


# ------------------------------------------------------------------ stiri
NEWS_ABOUT = [
    ("What we publish here",
     "GDH’s own announcements, written by us and dated: changes to the network, new "
     "channels and capability, partnerships, and notes on the retail and dental categories "
     "we distribute. We post as things happen — most working days there is something new. "
     "Longer analysis goes under Insights."),
    ("Follow the news",
     "Every item is also published in our RSS feed at gdh-group.com/news/feed.xml, which any "
     "feed reader can follow. There is no sign-up, no newsletter and no tracking: the site "
     "sets no cookies and runs no analytics."),
]


def news_url(post):
    return "news/%s.html" % post["slug"]


def news_card(post):
    import news_gdh as N
    return U.card(post["title"], post["summary"], news_url(post),
                  meta="%s · %s" % (post["category"], N.human_date(post["date"])),
                  image=post.get("img"), cta="Read the news")


def news_lead(post):
    """Prima stire de pe pagina de stiri, mare: imagine in stanga, text in dreapta."""
    import news_gdh as N
    media = ('<img src="%s" alt="%s" loading="eager" decoding="async">'
             % (U.esc(post["img"]), U.esc(post.get("image_alt", ""))) if post.get("img")
             else '<div class="news-lead__poster" aria-hidden="true"></div>')
    return ('<a class="news-lead" href="%s"><div class="news-lead__media">%s'
            '<span class="card__tag">Latest</span></div>'
            '<div class="news-lead__body"><p class="card__meta"><span class="chip">%s</span>'
            '<span>%s</span></p><h2 class="news-lead__title">%s</h2>'
            '<p class="muted">%s</p><span class="link-arrow">Read the news%s</span></div></a>'
            % (U.esc(news_url(post)), media, U.esc(post["category"]),
               U.esc(N.human_date(post["date"])), U.esc(post["title"]),
               U.esc(post["summary"]), U.HOOK))


def pager(page_no, pages_total):
    if pages_total <= 1:
        return ""
    def href(n):
        return "news.html" if n == 1 else "news/page/%d.html" % n
    items = []
    if page_no > 1:
        items.append('<a class="pager__step" href="%s" rel="prev">Newer</a>' % href(page_no - 1))
    for n in range(1, pages_total + 1):
        items.append('<span class="pager__n is-current" aria-current="page">%02d</span>' % n
                     if n == page_no else '<a class="pager__n" href="%s">%02d</a>' % (href(n), n))
    if page_no < pages_total:
        items.append('<a class="pager__step" href="%s" rel="next">Older</a>' % href(page_no + 1))
    return '<nav class="pager" aria-label="News pages">%s</nav>' % "".join(items)


def news_index(posts, page_no, pages_total):
    """O pagina din lista de stiri (12 pe pagina). Prima are stirea cea mai noua mare."""
    import news_gdh as N
    import legal_data_gdh
    data = [e for e in legal_data_gdh.PAGES if e["slug"] == "news"][0]
    keep = dict(data["sections"])
    about = NEWS_ABOUT + [(h, keep[h]) for h in
                          ("Press enquiries", "What we will and will not comment on",
                           "Using our material") if h in keep]
    page = "news.html" if page_no == 1 else "news/page/%d.html" % page_no
    chunk = posts[(page_no - 1) * N.PER_PAGE: page_no * N.PER_PAGE]
    trail = [("Home", "index.html"), ("News", "news.html")]
    if page_no > 1:
        trail.append(("Page %d" % page_no, page))

    if not posts:
        listing = ('<div class="card card--text" style="min-height:0"><p class="h3">The first news '
                   'item is on its way.</p><p class="muted">Check back soon, or follow the RSS '
                   'feed.</p></div>')
    elif page_no == 1:
        listing = news_lead(chunk[0]) + (
            '<div class="grid grid--3" style="margin-top:clamp(50px,6vw,90px)">%s</div>'
            % "".join(news_card(p) for p in chunk[1:]) if len(chunk) > 1 else "")
    else:
        listing = '<div class="grid grid--3">%s</div>' % "".join(news_card(p) for p in chunk)

    body = (U.pagehead(trail, "News", "News from GDH.",
                       "Announcements from the GDH network: new channels and capability, "
                       "partnerships and notes on the retail and dental categories we "
                       "distribute — dated, and written by us.",
                       figure="(%02d)" % len(posts))
            + U.section(listing + pager(page_no, pages_total), tight=True))
    if page_no == 1:
        index = [(h, "#" + U.slug(h)) for h, _b in about]
        card = (U.card_tags("About this page", index)
                + '<div><p class="dcard__label" style="color:var(--text)">Press</p>'
                  '<a class="dcard__mail" href="mailto:%s?subject=Press">%s</a></div>'
                  % (U.esc(C.EMAIL), U.esc(C.EMAIL)))
        body += U.section(U.head_block("About", "How we publish.") + U.detail(card, U.drows(about)),
                          variant="grey")
    body += cta_section("Send us your range.",
                        "Tell us what you make and which shelves it belongs on.")

    if page_no == 1:
        title, desc = None, None          # din seo_gdh.py
    else:
        title = "News from GDH — page %d" % page_no
        desc = ("Older announcements from GDH, page %d: network changes, new channels, "
                "partnerships and notes on the retail and dental categories." % page_no)
    jsonld = json_ld({
        "@context": "https://schema.org", "@type": "CollectionPage",
        "name": "News from GDH", "url": canonical(page),
        "hasPart": [{"@type": "NewsArticle", "headline": p["title"],
                     "url": canonical(news_url(p)), "datePublished": N.iso(p["date"])}
                    for p in chunk]})
    return shell(page, title or "", desc or "", body, current="news", jsonld=jsonld)


def canonical(page):
    return C.SITE_URL + ("/" if page == "index.html" else "/" + page[:-len(".html")])


def json_ld(data):
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))


def share_links(url, title):
    from urllib.parse import quote
    u, t = quote(url, safe=""), quote(title, safe="")
    links = [("LinkedIn", "https://www.linkedin.com/sharing/share-offsite/?url=%s" % u),
             ("X", "https://twitter.com/intent/tweet?url=%s&text=%s" % (u, t)),
             ("Facebook", "https://www.facebook.com/sharer/sharer.php?u=%s" % u),
             ("WhatsApp", "https://wa.me/?text=%s%%20%s" % (t, u)),
             ("Email", "mailto:?subject=%s&body=%s" % (t, u))]
    return ('<div><p class="dcard__label">[ share ]</p><div class="dcard__tags">%s</div></div>'
            % "".join('<a href="%s" target="_blank" rel="noopener">%s</a>'
                      % (U.esc(h), U.esc(n)) for n, h in links))


def news_article(post, posts):
    import news_gdh as N
    page = news_url(post)
    url = canonical(page)
    i = posts.index(post)
    newer = posts[i - 1] if i > 0 else None
    older = posts[i + 1] if i + 1 < len(posts) else None
    more = [p for p in posts if p is not post][:3]

    rows = [("Category", post["category"]), ("Published", N.human_date(post["date"]))]
    if post.get("updated") and post["updated"] != post["date"]:
        rows.append(("Updated", N.human_date(post["updated"])))
    rows.append(("Reading time", "%d min" % post["minutes"]))
    card = ('<div><p class="dcard__label">[ news ]</p><div style="margin-top:18px">%s</div></div>'
            '%s<div>%s</div>' % (U.card_info(rows), share_links(url, post["title"]),
                                 U.btn("All news", "news.html")))

    steps = []
    if older:
        steps.append('<a class="newsnav__item" href="%s" rel="prev"><span class="mono">Previous</span>'
                     '<span>%s</span></a>' % (U.esc(news_url(older)), U.esc(older["title"])))
    if newer:
        steps.append('<a class="newsnav__item newsnav__item--next" href="%s" rel="next">'
                     '<span class="mono">Next</span><span>%s</span></a>'
                     % (U.esc(news_url(newer)), U.esc(newer["title"])))
    main = ('<div class="article news-body">%s</div>%s'
            % (N.markdown(post["body"]),
               ('<nav class="newsnav" aria-label="More news">%s</nav>' % "".join(steps)) if steps else ""))

    body = (U.pagehead([("Home", "index.html"), ("News", "news.html"), (clip(post["title"]), page)],
                       post["category"], post["title"], post["summary"],
                       image=post.get("img"), alt=post.get("image_alt", ""),
                       figure="%02d.%02d" % (post["date"].day, post["date"].month))
            + U.section(U.detail(card, main)))
    if more:
        body += U.section(U.head_block("More news", "Also from GDH.",
                                       align_cta=U.link_arrow("All news", "news.html"))
                          + '<div class="grid grid--3">%s</div>' % "".join(news_card(p) for p in more),
                          variant="grey")
    body += cta_section("Send us your range.",
                        "Tell us what you make and which shelves it belongs on.")

    # „ | GDH” doar daca incape in 60 de caractere si titlul nu numeste deja GDH
    title = post["title"]
    if "GDH" not in title and len(title) <= 54:
        title += " | GDH"
    modified = post.get("updated") or post["date"]
    image = C.SITE_URL + "/" + (post.get("og") or "img/og-image.jpg")
    article = {
        "@context": "https://schema.org", "@type": "NewsArticle",
        "headline": post["title"][:110], "description": post["summary"],
        "datePublished": N.iso(post["date"]), "dateModified": N.iso(modified),
        "articleSection": post["category"], "wordCount": post["words"],
        "image": [image], "url": url, "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "author": {"@type": "Organization", "name": C.SITE_NAME, "url": C.SITE_URL + "/"},
        "publisher": {"@type": "Organization", "name": C.SITE_NAME,
                      "logo": {"@type": "ImageObject", "url": C.SITE_URL + "/img/icon-512.png"}},
        "inLanguage": "en"}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": C.SITE_URL + "/"},
        {"@type": "ListItem", "position": 2, "name": "News", "item": canonical("news.html")},
        {"@type": "ListItem", "position": 3, "name": post["title"], "item": url}]}
    extra = ('<meta property="article:published_time" content="%s">'
             '<meta property="article:modified_time" content="%s">'
             '<meta property="article:section" content="%s">'
             % (N.iso(post["date"]), N.iso(modified), U.esc(post["category"])))
    return shell(page, title, post["summary"], body, current="news",
                 jsonld=json_ld(article) + json_ld(crumbs), og_type="article",
                 og_image=post.get("og"), extra_head=extra)


def build_news(out, src, written_put):
    """Paginile de stiri, fotografiile lor si cartonasele de share."""
    import news_gdh as N
    posts, scheduled = N.load(src)
    N.build_images(posts, src, os.path.join(out, "img"))
    # cartonasul de share al stirii: JPEG 1200x630 decupat din fotografie
    from PIL import Image
    for p in posts:
        if not p.get("img"):
            continue
        im = Image.open(os.path.join(out, p["img"])).convert("RGB")
        tw, th = 1200, 630
        sc = max(tw / im.width, th / im.height)
        im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
        l, t = (im.width - tw) // 2, (im.height - th) // 2
        name = "news-%s-share.jpg" % p["slug"]
        im.crop((l, t, l + tw, t + th)).save(os.path.join(out, "img", name), "JPEG",
                                             quality=86, optimize=True)
        p["og"] = "img/" + name

    total = max(1, -(-len(posts) // N.PER_PAGE))
    for n in range(1, total + 1):
        written_put("news.html" if n == 1 else "news/page/%d.html" % n, news_index(posts, n, total))
    for p in posts:
        written_put(news_url(p), news_article(p, posts))
    return posts, scheduled


# ------------------------------------------------------------- formulare
def _person_fields():
    return ('<div class="grid grid--2">'
            '<label class="field"><span>Name</span><input name="Name" autocomplete="name" required></label>'
            '<label class="field"><span>Company</span><input name="Company" autocomplete="organization" required></label>'
            '<label class="field"><span>Email</span><input name="Email" type="email" autocomplete="email" required></label>'
            '<label class="field"><span>Phone</span><input name="Phone" type="tel" autocomplete="tel"></label>'
            '</div>')


def sales_form_section():
    """Formularul de pe Contact sales: cere exact ce cere pagina — gama,
    capacitatea lunara, canalul — si spune ce urmeaza."""
    form = (
        '<form data-gdh-form="1" data-subject="Sales enquiry — new range" '
        'method="post" action="contact-sales.html">'
        + _person_fields() +
        '<div class="grid grid--2">'
        '<label class="field"><span>Channel</span><select name="Channel">'
        '<option>Retail chains</option><option>Dental practices &amp; laboratories</option>'
        '<option>Both</option><option>Not sure yet</option></select></label>'
        '<label class="field"><span>Monthly capacity</span>'
        '<input name="Monthly capacity" placeholder="e.g. 4,000 cases"></label>'
        '</div>'
        '<label class="field"><span>Your range</span>'
        '<textarea name="Range" required placeholder="Product list with pack sizes, shelf life, '
        'and any listings or certifications you already hold. Send what you have — gaps are '
        'fine."></textarea></label>'
        + U.submit("Send your range") +
        '</form>')
    aside = (
        '<div>%s<h2 class="h1" style="font-size:var(--t-h3)">Start with one message.</h2>'
        '<p class="muted" style="margin-top:20px;font-size:var(--t-large);max-width:40ch">'
        'Tell us what you make and what you can supply each month. A first reply usually '
        'arrives within two working days, from a person, not an autoresponder.</p>'
        '<p style="margin-top:20px;font-weight:600">It costs you nothing, at any stage.</p>'
        '<div style="display:flex;flex-direction:column;align-items:flex-start;gap:18px;margin-top:36px">'
        '<a class="link-arrow" href="mailto:%s">%s%s</a>'
        '<a class="link-arrow" href="tel:%s">%s%s</a></div></div>'
        % (U.eyebrow("Send your range"), U.esc(C.EMAIL), U.esc(C.EMAIL), U.HOOK,
           U.esc(C.PHONE.replace(" ", "")), U.esc(C.PHONE), U.HOOK))
    return ('<section class="section section--grey" id="sales-form"><div class="wrap">'
            '<div class="split" style="align-items:start">%s'
            '<div class="form-card">%s</div></div></div></section>' % (aside, form))


# ------------------------------------------------------------- contact page
def contact_page():
    c = C.CONTACT
    form = (
        '<form data-gdh-form="1" data-subject="Distribution enquiry" '
        'method="post" action="contact.html">'
        + _person_fields() +
        '<label class="field"><span>What do you make?</span>'
        '<textarea name="Message" required placeholder="Your range, your monthly capacity, '
        'and the chains or practices you want to reach."></textarea></label>'
        + U.submit("Send message") +
        '</form>')
    aside = (
        '<div>%s<h2 class="h1" style="font-size:var(--t-h3)">Timiș, Romania.</h2>'
        '<p class="muted" style="margin-top:20px;font-size:var(--t-large)">%s</p>'
        '<div style="display:flex;flex-direction:column;align-items:flex-start;gap:18px;margin-top:36px">'
        '<a class="link-arrow" href="mailto:%s">%s%s</a>'
        '<a class="link-arrow" href="tel:%s">%s%s</a></div></div>'
        % (U.eyebrow("Where we are"), "<br>".join(U.esc(a) for a in C.ADDRESS),
           U.esc(C.EMAIL), U.esc(C.EMAIL), U.HOOK,
           U.esc(C.PHONE.replace(" ", "")), U.esc(C.PHONE), U.HOOK))
    body = (U.pagehead([("Home", "index.html"), ("Contact", "contact.html")],
                       c["kicker"], c["title"], c["lede"], image=img("contact.html"),
                       alt=alt(img("contact.html")))
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
        '<div style="border-top:1px solid var(--line);padding:28px 0;display:flex;'
        'flex-wrap:wrap;gap:12px 20px">'
        '<p class="mono" style="font-size:12px;color:var(--text);flex:0 0 160px">%s</p>'
        '<p class="%s" style="flex:1 1 260px;min-width:0">%s</p></div>'
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
                        '<div style="padding:clamp(24px,4vw,54px);background:#fff;border-radius:8px;display:grid;place-items:center">'
                        '<img src="%s" alt="The stacked GDH logo on a light background" style="width:min(230px,100%%);height:auto"></div>'
                        '<div style="padding:clamp(24px,4vw,54px);background:#000;border-radius:8px;display:grid;place-items:center">'
                        '<img src="%s" alt="The stacked GDH logo on a dark background" style="width:min(230px,100%%);height:auto"></div>'
                        '</div>' % (LOGO_DARK, LOGO_LIGHT, STACKED_DARK, STACKED_LIGHT),
                        variant="grey"))
    return shell("style-guide.html", "Style guide | GDH",
                 "The GDH visual system: the black-and-white palette and banner gradient, the "
                 "Inter Tight and IBM Plex Mono type scale, the button and link components, "
                 "and the logo on light and dark backgrounds.", body, "")


# ------------------------------------------------------------- build it all
NEWS = {"posts": [], "scheduled": 0}


def build_all(out, pages_data, src="."):
    """Scrie toate paginile in `out`. `pages_data` e lista din pages_data_gdh."""
    import inner_gdh as I
    import news_gdh as N
    written = {}
    # stirile se citesc primele: prima pagina le arata pe cele mai noi
    NEWS["posts"], NEWS["scheduled"] = N.load(src)

    def put(name, markup):
        path = os.path.join(out, name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(markup)
        written[name] = len(markup)

    posts, scheduled = build_news(out, src, put)
    NEWS["posts"], NEWS["scheduled"] = posts, scheduled
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
            if entry["slug"] == "news":
                continue          # news.html e acum lista de stiri (build_news)
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
            sales = entry["slug"] == "contact-sales"
            put(name, simple_page(name, dict(
                kicker=entry["kicker"], title=entry["title"], lede=entry["lede"],
                sections=entry["sections"]), extra=note,
                lead=sales_form_section() if sales else "",
                buttons=[U.btn("Send your range", "#sales-form")] if sales else ()))
    except ImportError:
        pass

    put("contact.html", contact_page())
    put("style-guide.html", style_guide())
    return written


def deploy_files(out, pages):
    """robots, sitemap-uri, fluxul RSS, antete si redirectari pentru Cloudflare Pages."""
    import news_gdh as N
    from xml.sax.saxutils import escape as x
    posts = NEWS["posts"]
    dated = {news_url(p): (p.get("updated") or p["date"]) for p in posts}
    if posts:
        dated["news.html"] = max(dated.values())
    urls = sorted(p for p in pages if p.endswith(".html") and p != "404.html")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        last = ("<lastmod>%s</lastmod>" % dated[u].isoformat()) if u in dated else ""
        sm.append("  <url><loc>%s</loc>%s</url>" % (x(canonical(u)), last))
    sm.append("</urlset>")
    open(os.path.join(out, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")

    # Google News: doar stirile din ultimele doua zile, cum cere specificatia
    today = N.now().date()
    recent = [p for p in posts if (today - p["date"]).days <= 2]
    ns = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
          'xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">']
    for p in recent:
        ns.append("  <url><loc>%s</loc><news:news><news:publication><news:name>GDH</news:name>"
                  "<news:language>en</news:language></news:publication>"
                  "<news:publication_date>%s</news:publication_date><news:title>%s</news:title>"
                  "</news:news></url>" % (x(canonical(news_url(p))), N.iso(p["date"]), x(p["title"])))
    ns.append("</urlset>")
    open(os.path.join(out, "news-sitemap.xml"), "w", encoding="utf-8").write("\n".join(ns) + "\n")

    # fluxul RSS, ultimele 30 de stiri
    os.makedirs(os.path.join(out, "news"), exist_ok=True)
    items = []
    for p in posts[:30]:
        link = canonical(news_url(p))
        items.append("<item><title>%s</title><link>%s</link><guid isPermaLink=\"true\">%s</guid>"
                     "<pubDate>%s</pubDate><category>%s</category><description>%s</description></item>"
                     % (x(p["title"]), x(link), x(link), N.rfc822(p["date"]), x(p["category"]),
                        x(p["summary"])))
    feed = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>'
            '<title>GDH news</title><link>%s</link>'
            '<atom:link href="%s/news/feed.xml" rel="self" type="application/rss+xml"/>'
            '<description>Announcements from GDH — Global Distribution Holdings.</description>'
            '<language>en</language>%s%s</channel></rss>\n'
            % (x(canonical("news.html")), x(C.SITE_URL),
               ("<lastBuildDate>%s</lastBuildDate>" % N.rfc822(posts[0]["date"])) if posts else "",
               "".join(items)))
    open(os.path.join(out, "news", "feed.xml"), "w", encoding="utf-8").write(feed)

    open(os.path.join(out, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\nSitemap: %s/news-sitemap.xml\n"
        % (C.SITE_URL, C.SITE_URL))

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
