# -*- coding: utf-8 -*-
"""Etapa 3: paginile interioare (about, quote, servicii, studii de caz, articole)."""
import os, re, html

# ---------------------------------------------------------------- continut
def P(*paras):
    return list(paras)


PAGES = {
    "about-us.html": dict(
        mark=True,
        title="About GDH",
        kicker="/About",
        lead="A distribution company built around one promise: your product reaches the shelf, on time, "
             "in the right quantity, in the right condition.",
        body=P(
            ("Who we are",
             "GDH — Global Distribution Holdings — stores, picks, packs and delivers physical products for "
             "brands that sell through retail, pharmacy, HoReCa and online channels. We run our own "
             "warehouses, our own delivery fleet and our own field teams, which means a single organisation "
             "is accountable from goods-in to shelf."),
            ("How we work",
             "Every client starts with a coverage plan: which SKUs are stored where, how much stock cover we "
             "hold, which routes serve which delivery points, and what happens when demand spikes. The plan "
             "is reviewed monthly against fill rate, delivery accuracy and cost per drop — three numbers we "
             "report on for every account."),
            ("The network",
             "38 regional hubs, ambient and temperature-controlled storage, and daily routes into major "
             "cities with two-to-three weekly service for smaller towns. Capacity is shared across clients, "
             "so a seasonal peak for one brand does not require a new warehouse for another."),
            ("Why brands move to us",
             "Most of our clients arrive after managing a warehouse operator, a carrier and a merchandising "
             "agency separately — three contracts, three reports, and nobody responsible for the gap between "
             "them. We remove the gaps by owning the whole flow."),
        ),
        stats=[("38", "regional hubs"), ("4.200+", "delivery points weekly"),
               ("98,6%", "on-time delivery"), ("24h", "standard order cut-off")],
    ),
    "get-a-quote.html": dict(
        title="Get a distribution quote",
        kicker="/Quote",
        lead="Send us your product list and your delivery footprint. You get storage, handling and per-drop "
             "pricing back — usually within two working days.",
        body=P(
            ("What to send us",
             "Your SKU list with dimensions and weights, storage conditions (ambient, chilled, frozen), "
             "average and peak monthly volumes, the delivery points you need covered, and your order "
             "cut-off times. If you do not have all of it, send what you have and we will fill the gaps in "
             "a short call."),
            ("What you get back",
             "A written plan with storage cost per pallet, handling cost per order line, delivery cost per "
             "drop by region, and the service levels we commit to. No setup fee, no minimum contract length "
             "in the first quarter."),
            ("Next step",
             "Write to office@gdh-group.com or call +40 21 300 40 50 and ask for the distribution "
             "desk. If it is easier, use the contact form and we will come back to you."),
        ),
        cta=("Open the contact form", "contact.html"),
    ),
    "style-guide.html": dict(
        logo_boards=True,
        title="Brand & style guide",
        kicker="/Style guide",
        lead="The visual system behind the GDH identity: colour, type and the rules we apply across every "
             "surface, from the warehouse signage to this website.",
        body=P(
            ("Colour",
             "GDH Red (#E01021) is the primary colour and carries the logo, primary actions and highlights. "
             "Ink (#111111) carries typography and the diagonal cut inside the wordmark. White is the "
             "resting surface. No other accent colour is used in brand communication."),
            ("Typography",
             "Inter Tight in five weights — 300, 400, 500, 600 and 700. Headlines run at weight 600 to 700 "
             "with tight tracking; body copy runs at 400. The font is hosted on our own servers, never "
             "loaded from a third party."),
            ("The logo",
             "Heavy geometric letterforms cut by two diagonals, over the descriptor GLOBAL DISTRIBUTION "
             "HOLDINGS. The cuts and the descriptor are black on light backgrounds and white on dark ones — "
             "both versions are shown above. The letter G on its own is the mark we use for icons. Never "
             "re-colour the red, stretch the artwork or add effects to it."),
            ("Spacing",
             "Clear space around the logo equals the height of the letter G. Minimum reproduction width is "
             "96 px on screen and 28 mm in print."),
        ),
        swatches=[("#E01021", "GDH Red"), ("#111111", "Ink"), ("#F5F5F5", "Surface"), ("#FFFFFF", "White")],
    ),
    "licenses.html": dict(
        title="Licences & credits",
        kicker="/Licences",
        lead="What this site is built from, and under which terms.",
        body=P(
            ("Content",
             "All copy, product descriptions, service definitions and client programme summaries on this "
             "site belong to GDH — Global Distribution Holdings, © 2026. All rights reserved."),
            ("Typeface",
             "Inter Tight by Rasmus Andersson, released under the SIL Open Font License 1.1. The font files "
             "are served from this domain; no font CDN is contacted when you load a page."),
            ("Code",
             "The site is plain HTML, CSS and JavaScript with no third-party trackers. Two libraries are "
             "bundled and served from this domain: Lenis, an MIT-licensed smooth-scroll helper, and GSAP "
             "with its ScrollTrigger and SplitText plugins, used under the GSAP standard licence."),
            ("Photography",
             "Photography and illustration are licensed for use by GDH in its own commercial "
             "communications and may not be extracted from this site for other purposes."),
        ),
    ),
    "changelog.html": dict(
        title="Network changelog",
        kicker="/Changelog",
        lead="What changed in the GDH distribution network — new hubs, new routes, new services.",
        body=P(
            ("August 2026 — Cold chain at hub D2",
             "Chilled storage extended by 1.400 pallet positions at the București D2 hub, with dedicated "
             "chilled loading bays and temperature logging on every dispatched load."),
            ("June 2026 — Two new regional hubs",
             "Hubs opened in Cluj and Constanța, bringing daily route coverage to two further regions and "
             "cutting average delivery lead time in the north-west by one working day."),
            ("March 2026 — Unit picking for D2C",
             "Unit-level picking and branded packing launched for direct-to-consumer and marketplace "
             "orders, with next-day parcel dispatch on orders placed before the 15:00 cut-off."),
            ("January 2026 — Retail execution teams",
             "Field teams introduced for shelf placement, planogram checks and promotional set-up in the "
             "stores already served by our delivery routes."),
        ),
    ),
    "404.html": dict(
        mark=True,
        title="Page not found",
        kicker="/404",
        lead="This page is not on our route. It may have been moved, renamed, or it never existed.",
        body=P(
            ("Try one of these",
             "Head back to the home page, look through our distribution services, or open the contact form "
             "and tell us what you were looking for."),
        ),
        cta=("Back to the home page", "index.html"),
        noindex=True,
    ),
}

SERVICES = {
    "service-one-of-the-best-accountable-team.html": (
        "One Accountable Distribution Team",
        "One team owning storage, fulfilment and delivery — with a single point of contact for your brand.",
        [("What it covers",
          "A named account manager, a warehouse team that knows your SKUs, and a dispatch desk that "
          "handles exceptions before you hear about them. You escalate once, not to three suppliers."),
         ("How it works",
          "We agree service levels for order accuracy, dispatch time and delivery windows, then review "
          "them monthly against the numbers. Anything below target comes with a corrective plan, not an "
          "explanation."),
         ("Who it suits",
          "Brands running national distribution who are tired of coordinating a warehouse operator, a "
          "carrier and a field agency that each blame the other.")]),
    "service-clear-shipment-visibility.html": (
        "Clear Stock Visibility",
        "See stock on hand, stock in transit and stock at store level, with reorder points you control.",
        [("What it covers",
          "Live stock levels per warehouse and per SKU, orders in picking, loads dispatched, and proof of "
          "delivery per store — all in one view, exported however your systems need it."),
         ("Batch and expiry",
          "Every movement carries batch, lot and expiry data, so recalls take minutes to scope and "
          "short-dated stock is rotated before it becomes a write-off."),
         ("Reordering",
          "You set the stock cover you want to hold per SKU. We flag anything drifting below it, with "
          "enough lead time to react.")]),
    "service-flexible-transport-options.html": (
        "Flexible Delivery Options",
        "Pallet, case or unit delivery, on fixed routes or on demand, with the frequency each channel needs.",
        [("Channels",
          "Supermarket chains on scheduled slot deliveries, independent stores and pharmacies on fixed "
          "weekly routes, HoReCa on early-morning drops, and direct-to-consumer parcels through our "
          "fulfilment desk."),
         ("Formats",
          "Full pallets, mixed pallets, shelf-ready cases or single units — picked to whatever format the "
          "receiving location actually wants to handle."),
         ("Peaks",
          "Seasonal peaks are covered from shared capacity across the network, so you do not pay for "
          "vehicles and pallet positions you only need eight weeks a year.")]),
    "service-scalable-capacity-with-shipment.html": (
        "Capacity That Scales With Demand",
        "Cover a launch, a seasonal peak or continuous nationwide replenishment on the same network.",
        [("Launches",
          "New product launches get dedicated put-away and a listing-by-listing rollout plan, so stock "
          "lands in stores in the week the campaign starts, not the week after."),
         ("Peaks",
          "Storage and route capacity flex up for Christmas, Easter and back-to-school without a new "
          "contract, using capacity shared across the client base."),
         ("Steady state",
          "Between peaks you pay for the pallet positions and drops you actually use, reviewed monthly.")]),
    "service-dispute-resolution-litigation.html": (
        "Returns & Reverse Logistics",
        "Structured handling of returns, recalls, damaged goods and expired stock — with the paperwork done.",
        [("Returns",
          "Store returns are collected on the same routes that deliver, triaged at the hub, and either "
          "returned to sellable stock or written off with photographic evidence."),
         ("Recalls",
          "Because every movement carries batch and lot data, a recall is scoped in minutes and executed "
          "on the next route cycle, with a full audit trail per delivery point."),
         ("Credit notes",
          "Returned quantities reconcile against the original delivery, so your finance team gets clean "
          "credit-note data instead of a monthly dispute.")]),
}

CASES = {
    "case-study-supply-chain-optimization.html": (
        "Grocery Retail Replenishment", "Grocery Retail",
        "Daily replenishment, shelf-ready packing and route delivery for a fast-growing grocery brand.",
        [("The situation",
          "The brand had listings in three national chains and stock sitting in two rented warehouses with "
          "no shared view. Store-level availability was around 88% and nobody could say why."),
         ("What we changed",
          "Stock consolidated into two GDH hubs, shelf-ready packing introduced at the pick face, and "
          "deliveries moved onto daily fixed routes aligned with each chain's receiving slots."),
         ("The result",
          "On-shelf availability moved from 88% to 97,4% within two quarters, and cost per drop fell 14% "
          "because half-empty vehicles disappeared from the plan.")]),
    "case-study-supply-chain-optimization-jz7lc.html": (
        "Pharmacy Distribution", "Pharmacy",
        "Temperature-controlled storage and batch-tracked delivery to a national pharmacy network.",
        [("The situation",
          "A para-pharmacy supplier needed chilled storage, batch traceability and delivery into more than "
          "900 pharmacies, several of which accept goods only in a two-hour morning window."),
         ("What we changed",
          "Chilled pallet positions at two hubs, temperature logging on every dispatched load, and "
          "early-morning routes built around each pharmacy's receiving window."),
         ("The result",
          "Zero temperature excursions across the first year, and recall scoping reduced from two days of "
          "phone calls to a single batch query.")]),
    "case-study-transportation-efficiency.html": (
        "Route Delivery Efficiency", "Route Delivery",
        "Rebuilding a national route plan around real drop density instead of historical habit.",
        [("The situation",
          "Routes had grown by accretion over six years. Vehicles were running at 61% fill and three "
          "regions were served by two overlapping routes each."),
         ("What we changed",
          "Every delivery point was re-clustered by drop size and receiving window, then routes were "
          "rebuilt from scratch and re-timed against actual unloading data."),
         ("The result",
          "Vehicle fill rose to 84%, two vehicles came off the plan entirely, and average delivery lead "
          "time dropped by half a day.")]),
    "case-study-transportation-freight.html": (
        "Industrial Supply Distribution", "Industrial Supply",
        "Storage and scheduled delivery of consumables and spare parts to production and service networks.",
        [("The situation",
          "A supplier of industrial consumables held stock at each of its five service branches, which "
          "meant five sets of slow-moving inventory and no visibility of total cover."),
         ("What we changed",
          "Stock centralised into one GDH hub with next-day delivery to all five branches and direct "
          "delivery to end sites for the twenty fastest-moving lines."),
         ("The result",
          "Total inventory fell 31% with no drop in service, and branch staff stopped spending mornings "
          "counting stock.")]),
    "case-study-warehousing-distribution.html": (
        "Warehousing & Distribution", "Warehousing",
        "Consolidating three rented warehouses into one managed distribution operation.",
        [("The situation",
          "Three warehouses, three operators, three stock files. Month-end reconciliation took four days "
          "and never fully agreed."),
         ("What we changed",
          "Full stock migration into two GDH hubs over six weekends, with one stock file, one goods-in "
          "process and one set of KPIs."),
         ("The result",
          "Reconciliation is now a report, not a project, and storage cost per pallet fell 19%.")]),
    "case-study-e-commerce-logistics.html": (
        "D2C & Marketplace Fulfilment", "D2C & Marketplace",
        "Unit picking, branded packing and next-day parcel dispatch for online and marketplace orders.",
        [("The situation",
          "The brand ran its own web store from an office storeroom. At 400 orders a day the storeroom "
          "stopped working and dispatch slipped to three days."),
         ("What we changed",
          "Unit-level picking at a GDH hub, branded packing materials held on site, and a 15:00 cut-off "
          "for next-day parcel dispatch, with marketplace orders pulled in through the same queue."),
         ("The result",
          "Dispatch back to next-day at four times the volume, and packing errors down to 0,3%.")]),
    "case-study-e-commerce-logistics-excellence.html": (
        "Peak Season Fulfilment", "D2C & Marketplace",
        "Absorbing a 6x November peak without adding a single square metre of dedicated space.",
        [("The situation",
          "November volumes ran six times the annual average. Renting seasonal space and hiring seasonal "
          "pickers cost more than the peak earned."),
         ("What we changed",
          "Peak capacity drawn from shared pallet positions and a shared pick team across the client base, "
          "with a pre-agreed ramp plan starting in September."),
         ("The result",
          "Peak absorbed with no dedicated space, and cost per order in November came in below the "
          "previous year's off-peak figure.")]),
    "case-study-international-logistics.html": (
        "Multi-Country Distribution", "Cross-border",
        "Serving three neighbouring markets from one hub, without three separate operations.",
        [("The situation",
          "The brand had opened in two neighbouring markets and was about to sign a separate warehouse "
          "and carrier in each."),
         ("What we changed",
          "One hub serving all three markets with country-specific labelling done at the pick face, and "
          "weekly line-haul into local delivery partners."),
         ("The result",
          "Two contracts avoided, stock cover reduced by holding one pool instead of three, and new-market "
          "launch time cut from months to weeks.")]),
}

POSTS = {
    "post-warehouse-inventory-solutions.html": (
        "Warehouse & Inventory", "June 10, 2026",
        "Stock cover is a decision, not a number you inherit",
        [("Most distributors hold the stock cover they happened to end up with. It came from an old "
          "spreadsheet, a bad month three years ago, or a supplier's minimum order quantity — not from a "
          "decision anyone made deliberately."),
         ("Cover should be set per SKU, from three inputs: how fast the line moves, how variable that "
          "movement is, and how long replenishment actually takes including the bad weeks. Lines that move "
          "steadily need surprisingly little. Lines that spike need more than the average suggests."),
         ("The practical test is simple. If you cannot say, per SKU, how many days of cover you intend to "
          "hold and why, then your working capital is being decided by accident.")]),
    "post-freight-transportation.html": (
        "Route Delivery", "October 9, 2026",
        "Cost per drop tells you more than cost per kilometre",
        [("Kilometre-based costing makes long routes look expensive and dense urban routes look cheap. In "
          "distribution the opposite is often true: the expensive part is the stop, not the distance."),
         ("A delivery point that takes forty minutes to unload, needs a two-hour window and accepts three "
          "cases costs more than a rural drop forty kilometres further out that takes six minutes and "
          "accepts a pallet."),
         ("Price the stop. Then decide which delivery points deserve daily service, which move to a weekly "
          "route, and which should be consolidated into a bigger, less frequent drop.")]),
    "post-logistics-technology.html": (
        "Distribution Technology", "October 8, 2026",
        "You do not need a new system. You need one stock file.",
        [("Most distribution problems that get blamed on software are actually reconciliation problems. "
          "Two warehouses, two stock files, and a nightly export that nobody fully trusts."),
         ("Before evaluating a new platform, find out how many places your stock quantity is stored in and "
          "which one wins in a disagreement. If the answer is 'it depends', no platform will fix it."),
         ("One authoritative stock file, one goods-in process and one definition of 'available' will do "
          "more for fill rate than any dashboard.")]),
    "post-industry-news-trends.html": (
        "Retail News & Trends", "October 7, 2026",
        "Retailers are shifting risk onto suppliers — quietly",
        [("Shorter order lead times, tighter receiving windows and penalties for partial deliveries have "
          "all become normal. None of them appear as a price change, but all of them move cost and risk "
          "onto the supplier."),
         ("The distributors handling this well are the ones who priced it: they know what a two-hour "
          "receiving window costs them, and they negotiate frequency and drop size accordingly."),
         ("The ones handling it badly are absorbing it silently and wondering why margin is drifting.")]),
    "post-expert-tips-guides.html": (
        "Practical Guides", "March 11, 2026",
        "A checklist for moving to a distribution partner",
        [("Migrating stock is the easy part. What breaks a transition is everything around it: master "
          "data, order cut-offs, and who tells the stores."),
         ("Before the first pallet moves, agree the SKU master with dimensions and weights, the storage "
          "conditions per line, the order cut-off, the delivery calendar per channel, and the exact "
          "escalation path for a missed drop."),
         ("Migrate the slowest-moving lines first. If something goes wrong, it goes wrong on stock nobody "
          "is waiting for.")]),
    "post-supply-chain-management.html": (
        "Supply Chain Management", "April 22, 2026",
        "Fill rate is the only KPI your customer feels",
        [("Warehouse productivity, vehicle fill and cost per pallet all matter internally. The customer "
          "experiences exactly one number: did the ordered quantity arrive, complete, when it was "
          "promised."),
         ("Measure fill rate at line level, not order level, and measure it against what was ordered, not "
          "against what you confirmed. Confirming a reduced quantity and then delivering it in full is "
          "not a 100% fill rate."),
         ("Once it is measured honestly, the causes sort themselves into three buckets: no stock, wrong "
          "stock, or late vehicle. Each has a different fix.")]),
    "post-technology-digital-transformation.html": (
        "Technology & Automation", "October 4, 2026",
        "Automate the pick face before you automate the report",
        [("Automation projects in distribution tend to start with reporting because reporting is visible "
          "to management. The returns are almost always larger at the pick face."),
         ("Scanning at pick, batch capture at put-away and a screen at goods-in remove the errors that "
          "reporting can only describe after the fact."),
         ("Fix the data where it is created. Every layer above it gets cheaper and more trustworthy.")]),
    "post-e-commerce-logistics.html": (
        "D2C & Marketplace", "October 3, 2026",
        "Unit picking is a different business from pallet picking",
        [("Brands that move into direct-to-consumer often assume their existing warehouse can absorb it. "
          "It usually cannot, because unit picking has a completely different cost structure."),
         ("A pallet operation optimises for weight and volume. A unit operation optimises for touches per "
          "order and packing accuracy — different layout, different staffing, different packaging stock."),
         ("Run them as two operations sharing one stock pool, or accept that one of the two will be run "
          "badly.")]),
}


def build(out, nav, footer, css_head):
    import pages_gdh as PG

    def shell(fn, title, desc, body_html, noindex=False, og_type="website"):
        return (
            "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta content=\"width=device-width, initial-scale=1\" name=\"viewport\">"
            "<title>%s</title><meta content=\"%s\" name=\"description\">"
            "%s%s%s</head><body>"
            "<a class=\"gdh-skip\" href=\"#gdh-main\">Skip to content</a>"
            "<div class=\"page-wrapper\">%s<main id=\"gdh-main\" tabindex=\"-1\">%s</main>%s</div>"
            "%s</body></html>"
            % (esc(title), esc(desc),
               '<meta name="robots" content="noindex">' if noindex else "",
               css_head, PG.head_common(fn, title, desc, og_type),
               '<div class="gdh-innernav">%s</div>' % nav, body_html, footer,
               PG.SCRIPTS))

    def esc(t):
        return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def hero(kicker, title, lead, mark=False):
        badge = ('<img src="img/gdh-logo.png" alt="GDH — Global Distribution Holdings" '
                 'class="gdh-logo gdh-hero-mark" width="180" height="75" decoding="async">'
                 '<div class="space-1-normal"></div>') if mark else ""
        return ('<section class="section inner-hero"><div class="space-5-small"></div>'
                '<div class="container g-container">%s'
                '<div class="font-1-extra-small worm-gray">%s</div>'
                '<div class="space-1-normal"></div><h1 class="section-heading">%s</h1>'
                '<div class="space-1-normal"></div>'
                '<p class="papragraph-regular is-black" style="max-width:56ch">%s</p></div>'
                '<div class="space-3-normal"></div></section>'
                % (badge, esc(kicker), esc(title), esc(lead)))

    def logo_showcase():
        """Ghidul de brand arată efectiv ambele variante ale siglei."""
        return ('<section class="section"><div class="container g-container">'
                '<div class="gdh-logo-boards">'
                '<div class="gdh-logo-board is-light">'
                '<img src="img/gdh-logo.png" alt="Sigla GDH pe fundal deschis" '
                'class="gdh-logo" width="300" height="126" decoding="async">'
                '<div class="font-1-extra-small worm-gray">Pe fundal deschis</div></div>'
                '<div class="gdh-logo-board is-dark">'
                '<img src="img/gdh-logo-light.png" alt="Sigla GDH pe fundal închis" '
                'class="gdh-logo" width="300" height="126" decoding="async">'
                '<div class="font-1-extra-small">On dark backgrounds</div></div>'
                '<div class="gdh-logo-board is-mark">'
                '<img src="img/gdh-mark.png" alt="Marca GDH" class="gdh-logo" '
                'width="110" height="107" decoding="async">'
                '<div class="font-1-extra-small worm-gray">The mark, for icons</div></div>'
                '</div></div><div class="space-3-normal"></div></section>')

    def blocks(items):
        out_html = ['<section class="section"><div class="container g-container">'
                    '<div class="inner-prose" style="max-width:72ch;display:grid;gap:34px">']
        for h, p in items:
            out_html.append('<div><h2 class="font-1-normal" style="margin:0 0 10px">%s</h2>'
                            '<p class="papragraph-regular is-black" style="margin:0">%s</p></div>'
                            % (esc(h), esc(p)))
        out_html.append('</div></div><div class="space-5-small"></div></section>')
        return "".join(out_html)

    written = []

    # ---- pagini simple
    for fn, cfg in PAGES.items():
        body = hero(cfg["kicker"], cfg["title"], cfg["lead"], mark=cfg.get("mark", False))
        if cfg.get("logo_boards"):
            body += logo_showcase()
        if cfg.get("stats"):
            cards = "".join(
                '<div class="gdh-stat"><div class="gdh-stat-value">%s</div>'
                '<div class="font-1-extra-small worm-gray gdh-stat-label">%s</div></div>'
                % (esc(a), esc(b))
                for a, b in cfg["stats"])
            body += ('<section class="section"><div class="container g-container">'
                     '<div style="display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(190px,1fr))">'
                     '%s</div></div><div class="space-3-normal"></div></section>' % cards)
        if cfg.get("swatches"):
            sw = "".join(
                '<div><div style="height:96px;border-radius:14px;border:1px solid rgba(0,0,0,.1);'
                'background:%s"></div><div class="font-1-extra-small worm-gray" style="margin-top:10px">'
                '%s — %s</div></div>' % (a, esc(b), a) for a, b in cfg["swatches"])
            body += ('<section class="section"><div class="container g-container">'
                     '<div style="display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(180px,1fr))">'
                     '%s</div></div><div class="space-3-normal"></div></section>' % sw)
        body += blocks(cfg["body"])
        if cfg.get("cta"):
            label, href = cfg["cta"]
            body += ('<section class="section"><div class="container g-container">'
                     '<a href="%s" class="primary-button g-inline-block"><div class="button-text-pill">'
                     '<div class="button-text">%s</div><div class="button-text">%s</div></div></a></div>'
                     '<div class="space-5-small"></div></section>' % (href, esc(label), esc(label)))
        page_title = cfg["title"] if "GDH" in cfg["title"] else "%s | GDH" % cfg["title"]
        html_out = shell(fn, page_title, cfg["lead"], body, cfg.get("noindex", False))
        open(os.path.join(out, fn), "w", encoding="utf-8").write(html_out)
        written.append(fn)

    # ---- pagini de serviciu
    for fn, (title, lead, items) in SERVICES.items():
        body = hero("/Services", title, lead) + blocks(items)
        body += ('<section class="section"><div class="container g-container">'
                 '<a href="contact.html" class="primary-button g-inline-block"><div class="button-text-pill">'
                 '<div class="button-text">Request Quote</div><div class="button-text">Request Quote</div>'
                 '</div></a></div><div class="space-5-small"></div></section>')
        open(os.path.join(out, fn), "w", encoding="utf-8").write(
            shell(fn, "%s | GDH" % title, lead, body))
        written.append(fn)

    # ---- studii de caz
    for fn, (title, sector, lead, items) in CASES.items():
        body = hero("/Clients — %s" % sector, title, lead) + blocks(items)
        body += ('<section class="section"><div class="container g-container">'
                 '<a href="case-study.html" class="primary-button g-inline-block">'
                 '<div class="button-text-pill"><div class="button-text">All Client Programmes</div>'
                 '<div class="button-text">All Client Programmes</div></div></a></div>'
                 '<div class="space-5-small"></div></section>')
        open(os.path.join(out, fn), "w", encoding="utf-8").write(
            shell(fn, "%s | GDH" % title, lead, body, og_type="article"))
        written.append(fn)

    # ---- articole
    for fn, (cat, date, title, paras) in POSTS.items():
        items = [("", p) for p in paras]
        body = hero("/Insights — %s · %s" % (cat, date), title, paras[0])
        inner = "".join('<p class="papragraph-regular is-black">%s</p>' % esc(p) for p in paras[1:])
        body += ('<section class="section"><div class="container g-container">'
                 '<div style="max-width:70ch;display:grid;gap:20px">%s</div></div>'
                 '<div class="space-5-small"></div></section>' % inner)
        body += ('<section class="section"><div class="container g-container">'
                 '<a href="blog.html" class="primary-button g-inline-block"><div class="button-text-pill">'
                 '<div class="button-text">More Insights</div><div class="button-text">More Insights</div>'
                 '</div></a></div><div class="space-5-small"></div></section>')
        open(os.path.join(out, fn), "w", encoding="utf-8").write(
            shell(fn, "%s | GDH" % title, paras[0][:180], body, og_type="article"))
        written.append(fn)

    return written
