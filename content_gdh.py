# -*- coding: utf-8 -*-
"""Arhitectura site-ului GDH si textele scrise de mana.

Paginile de sector si de serviciu isi iau continutul din `pages_data_gdh.py`.
Aici stau navigatia, subsolul si paginile pe care le scriem direct: prima
pagina, despre noi, contact, parteneriat si paginile utilitare.
"""

SITE_NAME = "GDH — Global Distribution Holdings"
SITE_URL = "https://gdh-group.com"
EMAIL = "office@gdh-group.com"
PHONE = "+40 21 300 40 50"
ADDRESS = ["Str. Depozitelor 24", "Hala D2, Sector 2", "București, România"]

# --------------------------------------------------------------- navigatie
NAV = [
    dict(key="sectors", id="sectors", title="Sectors", href="sectors.html", columns=[
        dict(title="Retail", links=[
            ("Retail overview", "sector-retail.html"),
            ("Grocery", "sector-grocery.html"),
            ("Health & Beauty", "sector-health-beauty.html"),
            ("Convenience", "sector-convenience.html"),
            ("Private Label", "sector-private-label.html"),
        ]),
        dict(title="Dental", links=[
            ("Dental overview", "sector-dental.html"),
            ("Practices & Clinics", "sector-dental-practices.html"),
            ("Laboratories", "sector-dental-laboratories.html"),
        ]),
        dict(title="Proof", links=[
            ("Brands we distribute", "brands.html"),
            ("Insights", "insights.html"),
        ]),
        dict(title="Start here", links=[
            ("Partner with us", "partner-with-us.html"),
            ("Contact sales", "contact.html"),
        ]),
    ]),
    dict(key="distribution", id="distribution", title="Distribution",
         href="distribution.html", columns=[
        dict(title="What we do", links=[
            ("Distribution overview", "distribution.html"),
            ("Chain listings", "service-chain-listings.html"),
            ("Stock & delivery", "service-stock-and-delivery.html"),
        ]),
        dict(title="In store", links=[
            ("Shelf execution", "service-shelf-execution.html"),
            ("Returns & recalls", "service-returns.html"),
        ]),
        dict(title="Data", links=[
            ("Sell-out visibility", "service-sell-out-visibility.html"),
        ]),
        dict(title="Start here", links=[
            ("Partner with us", "partner-with-us.html"),
            ("Contact sales", "contact.html"),
        ]),
    ]),
    dict(key="brands", title="Brands", href="brands.html"),
    dict(key="insights", title="Insights", href="insights.html"),
    dict(key="about", title="About us", href="about-us.html"),
]

TOPBAR = [
    ("Contact", "contact.html"),
    ("Careers", "careers.html"),
    ("Locations", "locations.html"),
    ("Partner with us", "partner-with-us.html"),
]

FOOTER_NAV = [
    dict(title="Sectors", links=[
        ("Retail", "sector-retail.html"),
        ("Grocery", "sector-grocery.html"),
        ("Health & Beauty", "sector-health-beauty.html"),
        ("Convenience", "sector-convenience.html"),
        ("Private Label", "sector-private-label.html"),
        ("Dental", "sector-dental.html"),
    ]),
    dict(title="Distribution", links=[
        ("Chain listings", "service-chain-listings.html"),
        ("Stock & delivery", "service-stock-and-delivery.html"),
        ("Shelf execution", "service-shelf-execution.html"),
        ("Sell-out visibility", "service-sell-out-visibility.html"),
        ("Returns & recalls", "service-returns.html"),
    ]),
    dict(title="Company", links=[
        ("About us", "about-us.html"),
        ("Brands we distribute", "brands.html"),
        ("Insights", "insights.html"),
        ("Careers", "careers.html"),
        ("Locations", "locations.html"),
        ("Contact", "contact.html"),
    ]),
]

LEGAL = [
    ("Licences & credits", "licenses.html"),
    ("Style guide", "style-guide.html"),
    ("Changelog", "changelog.html"),
]

# --------------------------------------------------------------- prima pagina
HOME = dict(
    kicker="Welcome to GDH",
    title="Your product, on the shelves that matter.",
    lede="GDH buys your product, stocks it and sells it into the country’s largest store "
         "chains and dental practices. **One partner for the whole route to market — and "
         "it costs your brand nothing.**",
    topics_title="What do you need?",
    topics=[
        ("Get listed in a national chain", "service-chain-listings.html"),
        ("Reach dental practices", "sector-dental.html"),
        ("Hold the shelf I already have", "service-shelf-execution.html"),
        ("See what is actually selling", "service-sell-out-visibility.html"),
        ("Cover convenience and proximity", "sector-convenience.html"),
        ("Produce a chain’s own brand", "sector-private-label.html"),
    ],
    features=[
        dict(kicker="First-time distribution",
             title="You make it. We get it on shelf.",
             text="Most brands we carry arrive after years of pitching chain buyers on their "
                  "own. We already supply those buyers every week, so your range enters a "
                  "conversation that is already happening.",
             href="service-chain-listings.html",
             image="img/automation.webp"),
        dict(kicker="The dental channel",
             title="Dentistry does not buy like retail.",
             text="Small, frequent, clinically specific orders, decided by the practitioner. "
                  "We are in those practices every week, which is a far shorter road than "
                  "building a dental sales force from scratch.",
             href="sector-dental.html",
             image="img/stock-check.webp"),
    ],
    sectors_title="Two channels, one network.",
    sectors_lede="Retail and dental share our warehouses and our delivery routes. Each has "
                 "its own commercial team, because the two buy nothing alike.",
    services_title="What we do for a brand.",
    services_lede="From the first buyer meeting to the shelf and back again. Take one piece "
                  "or the whole route to market.",
    stats_title="The network, in short.",
    stats_note="Figures describe the GDH network and are reviewed each quarter.",
    cta_title="Send us your range.",
    cta_text="Tell us what you make, which chains you want to reach and what you can supply "
             "each month. We will tell you honestly where it fits.",
)

# --------------------------------------------------------------- pagini scrise
ABOUT = dict(
    kicker="About us",
    title="A distributor, not a logistics supplier.",
    lede="We buy the product, we own the stock, and we are accountable for how it sells.",
    sections=[
        ("Who we are",
         "GDH — Global Distribution Holdings — buys products from factories and brands, holds "
         "them in our own warehouses, and sells and delivers them into the country’s largest "
         "store chains, independent retailers, pharmacies and dental practices. We are not a "
         "freight company and not a logistics supplier for hire. We take ownership of the "
         "product, and of how it performs on the shelf."),
        ("What we distribute",
         "Two ranges. Retail: food and beverage, household and personal care, and health and "
         "beauty lines sold through the big chains. Dental: materials, consumables and "
         "equipment for practices, clinics and laboratories. The two channels share our "
         "warehouses and our delivery network, but each has its own commercial team."),
        ("What it costs the brands we carry",
         "Nothing. We do not invoice the factories and brands whose products we distribute — "
         "no listing fee, no storage charge, no delivery cost. We buy the stock and we earn "
         "from distributing it. That means we only make money when your product actually "
         "sells, which is the incentive you want your distributor to have."),
        ("Why brands come to us",
         "Because the hard part is not moving a pallet. It is getting a buyer at a national "
         "chain to take your call, agree a listing, and then keep the shelf full once they "
         "do. We already supply those buyers, and we are already in those practices."),
    ],
)

PARTNER = dict(
    kicker="Partner with us",
    title="Send us your range.",
    lede="Tell us what you make and where it belongs. We come back with the chains we can "
         "reach, the volume we can move and how quickly we can start.",
    sections=[
        ("What to send us",
         "Your product list with pack sizes, barcodes and shelf life, your production capacity "
         "per month, any listings or exclusivity you already hold, and the certifications your "
         "category requires. If you do not have all of it, send what you have and we will fill "
         "the gaps in a short call."),
        ("What you get back",
         "An honest read on where your range fits: which chains and channels we believe will "
         "take it, what volume that means per month, what pack format each buyer will expect, "
         "and when we could realistically put it in front of them. If we do not think it will "
         "sell, we will say so — we are the ones buying the stock."),
        ("What it costs you",
         "Nothing, at this stage or any other. We are a distributor, not a service provider. "
         "We buy your product and earn from selling it on. You will never receive an invoice "
         "from GDH."),
    ],
)

CAREERS = dict(
    kicker="Careers",
    title="Work where the shelf is the scoreboard.",
    lede="Warehouse, delivery, field merchandising and commercial roles across the network.",
    sections=[
        ("How we work",
         "Our teams are measured on things they can see: orders picked correctly, deliveries "
         "made in the window, shelves that are full when the shopper arrives. There is very "
         "little abstraction in this business, which is what most people like about it."),
        ("Where the roles are",
         "Warehouse and goods-in at our hubs, drivers on regional routes, field merchandisers "
         "in the stores we serve, and commercial roles working directly with chain buyers and "
         "dental practices."),
        ("How to apply",
         "Write to %s with the role you are interested in and a short note about what you have "
         "done. We read everything that arrives and reply either way." % EMAIL),
    ],
)

LOCATIONS = dict(
    kicker="Locations",
    title="Where we operate.",
    lede="Head office and the hub network that serves the retail and dental channels.",
    sections=[
        ("Head office",
         "%s, %s, %s. The commercial desks for both the retail and dental channels sit here, "
         "alongside goods-in and the main ambient and chilled storage."
         % (ADDRESS[0], ADDRESS[1], ADDRESS[2])),
        ("The hub network",
         "Regional hubs carry stock closer to the stores and practices they serve, so "
         "replenishment does not depend on a single building. Major cities sit on daily "
         "routes; smaller towns and rural delivery points are served on a fixed weekly cycle."),
        ("Visiting us",
         "If you are considering working with us, come and see the operation before you "
         "decide. Write to %s and we will arrange it." % EMAIL),
    ],
)

LICENCES = dict(
    kicker="Licences",
    title="Licences & credits.",
    lede="What this site is built from, and under which terms.",
    sections=[
        ("Content",
         "All copy, product descriptions, service definitions and client programme summaries "
         "on this site belong to GDH — Global Distribution Holdings, © 2026. All rights "
         "reserved."),
        ("Typeface",
         "Roboto by Christian Robertson, released under the Apache License 2.0. The font files "
         "are served from this domain; no font CDN is contacted when you load a page."),
        ("Code",
         "The site is plain HTML, CSS and JavaScript with no third-party trackers, no "
         "analytics and no external requests of any kind. There are no bundled libraries — "
         "the interactions are written from scratch."),
        ("Photography",
         "Photography and illustration are licensed for use by GDH in its own commercial "
         "communications and may not be extracted from this site for other purposes."),
        ("Brands and trademarks",
         "Product and chain names referenced on this site remain the property of their owners. "
         "Mentioning a retailer or a brand here does not imply their endorsement of GDH."),
    ],
)

CHANGELOG = dict(
    kicker="Changelog",
    title="What changed in the network.",
    lede="New channels, new coverage, new capability.",
    sections=[
        ("August 2026 — Cold chain extended",
         "Chilled storage extended at the București D2 hub, opening the chilled and "
         "short-shelf-life categories to the brands we carry."),
        ("June 2026 — Two new regional hubs",
         "Hubs opened in Cluj and Constanța, bringing daily store coverage to two further "
         "regions and shortening replenishment lead time in the north-west."),
        ("March 2026 — Dental equipment added",
         "The dental range extended beyond materials and consumables to small equipment, with "
         "installation and warranty handled through the practices we already supply."),
        ("January 2026 — Field merchandising teams",
         "Field teams introduced for shelf placement, planogram checks and promotional set-up "
         "in the stores already on our delivery routes."),
    ],
)

NOT_FOUND = dict(
    kicker="404",
    title="This page is not on our route.",
    lede="It may have been moved, renamed, or it never existed.",
    sections=[
        ("Try one of these",
         "Head back to the home page, look through what we do for brands, or open the contact "
         "form and tell us what you were looking for."),
    ],
)

# Cifrele retelei. Sunt valori de lucru: inlocuieste-le cu cele reale inainte de
# publicare, din acest singur loc.
STATS = [
    ("Two", "channels: retail and dental"),
    ("Daily", "routes into major cities"),
    ("Weekly", "calls on the practices we serve"),
    ("Zero", "invoices sent to our brands"),
]

CONTACT = dict(
    kicker="Contact",
    title="Talk to the commercial desk.",
    lede="Tell us what you make and where it belongs. We read everything that arrives and "
         "reply either way.",
    name="Commercial desk",
    role="Retail & dental channels",
    blurb="For brands: listings, volumes and how quickly we could start. For stores and "
          "practices: ordering, deliveries and returns.",
)


# Adresele vechi raman valide. Cheia e adresa de dinainte, valoarea e pagina de
# acum; de aici se scrie dist/_redirects (301).
RENAMED = {
    # rescrierea din octombrie: sectiuni intregi si-au schimbat numele
    "service.html": "distribution.html",
    "case-study.html": "brands.html",
    "blog.html": "insights.html",
    "service-dental-distribution.html": "sector-dental.html",
    "service-retail-chain-listings.html": "service-chain-listings.html",
}


def redirects():
    """Perechi (adresa veche, adresa noua), inclusiv cele din era Webflow."""
    pairs = dict(RENAMED)
    try:
        import inner_gdh
        for was, now in inner_gdh.RENAME.items():
            # lantuim: slug Webflow -> numele de dupa -> pagina de acum
            pairs[was] = pairs.get(now, now)
    except Exception:
        pass
    return sorted(pairs.items())
