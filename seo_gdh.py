# -*- coding: utf-8 -*-
"""Titlul si descrierea fiecarei pagini, scrise de mana.

Sunt textele care apar cand cineva trimite linkul (WhatsApp, LinkedIn,
Facebook, Slack) si in rezultatele Google: <title>, meta description,
og:title/og:description si twitter:title/twitter:description vin toate de aici.

Reguli, verificate la fiecare build de `check()`:
  - fiecare pagina are o intrare, si niciun titlu sau descriere nu se repeta;
  - titlul are cel mult 60 de caractere si contine „GDH”;
  - descrierea are intre 110 si 160 de caractere si e o fraza intreaga,
    fara „…” — previzualizarile taie dupa ~160 de caractere.
"""

SEO = {
    "index.html": (
        "GDH | Retail and Dental Distribution in Romania",
        "GDH buys, stocks and distributes retail and dental products into Romania's largest "
        "store chains and dental practices, at no cost to the brands we carry."),

    # ---------------------------------------------------------- sectoare
    "sectors.html": (
        "Sectors: retail and dental distribution | GDH",
        "Two channels, one network: GDH supplies retail chains and dental practices from the "
        "same warehouses and lorries, with a separate commercial team for each."),
    "sector-retail.html": (
        "Retail distribution into national chains | GDH",
        "GDH buys retail stock outright and sells it into supermarket, drugstore, convenience "
        "and cash-and-carry chains. The listings and buyer calls already exist."),
    "sector-grocery.html": (
        "Food and drink into grocery chains | GDH",
        "GDH buys your food and drink lines, holds them in its own warehouses and replenishes "
        "the national grocery chains every week. You never see an invoice from us."),
    "sector-health-beauty.html": (
        "Health and beauty into drugstores | GDH",
        "GDH places beauty and personal care lines into the drugstore chains and pharmacies it "
        "calls on every week, and holds the facings once won, at no cost to you."),
    "sector-convenience.html": (
        "Convenience store distribution | GDH",
        "No single brand can afford to call on thousands of small convenience stores. GDH "
        "already does, every week, so your line rides a route that is already paid for."),
    "sector-private-label.html": (
        "Private label for retail chains | GDH",
        "Chains ask GDH for own-brand lines. We match the brief to a producer, agree the "
        "specification and buy the run ourselves, so we carry the accountability."),
    "sector-dental.html": (
        "Dental distribution: practices and labs | GDH",
        "Dentistry buys in small, repeat orders, on clinical trust. GDH buys your range, holds "
        "it and puts it in front of practices, clinics and laboratories weekly."),
    "sector-dental-practices.html": (
        "Distribution to dental practices and clinics | GDH",
        "Practices order small, often and to a clinical spec. GDH stocks your range, calls on "
        "practices weekly and delivers to the surgery door, free to your brand."),
    "sector-dental-laboratories.html": (
        "Distribution to dental laboratories | GDH",
        "Labs buy on lead time and traceability. GDH stocks your materials, alloys and "
        "consumables and delivers them to the bench with lot records, free to you."),

    # ---------------------------------------------------------- servicii
    "distribution.html": (
        "Distribution from factory to shelf | GDH",
        "GDH buys your stock and sells it into chains, pharmacies and dental practices: "
        "listings, storage, delivery, shelf work and sell-out data, free to you."),
    "service-chain-listings.html": (
        "Chain listings: get your range listed | GDH",
        "GDH prepares the submission, takes the buyer meeting, agrees terms and buys the "
        "opening order itself, so your range reaches the shelf at no cost to you."),
    "service-stock-and-delivery.html": (
        "Stock and delivery across Romania | GDH",
        "Your product arrives once, at our goods-in bay. From then it is GDH stock, in our "
        "warehouses and on our routes to depots, stores, pharmacies and clinics."),
    "service-shelf-execution.html": (
        "Shelf execution and merchandising | GDH",
        "GDH field teams walk the stores we sell into, put your stock where the planogram says, "
        "rebuild displays and photograph every call for you. It costs you nothing."),
    "service-sell-out-visibility.html": (
        "Sell-out data, store by store | GDH",
        "See what shoppers and practices actually bought: GDH reports sell-out per chain and per "
        "SKU every week, with stock cover, proof of delivery and batch records."),
    "service-returns.html": (
        "Returns and recalls handled for you | GDH",
        "GDH collects returns on the same van that delivers, grades them at our hub and traces "
        "recalls by batch, so you get one clean credit line instead of a dispute."),

    # ---------------------------------------------------------- articole
    "insights.html": (
        "Insights from the GDH commercial desk",
        "Practical articles from GDH on chain listings, shelf facings, on-shelf availability, "
        "sell-out data, private label and the dental channel."),
    "post-what-a-chain-buyer-decides.html": (
        "What a chain buyer is actually deciding | GDH",
        "Buyers are not judging whether your product is good. They decide what comes off the "
        "shelf to make room for it, and whether the category earns more afterwards."),
    "post-listings-and-facings.html": (
        "A listing is permission, a facing is business | GDH",
        "Winning a chain listing is where many brands stop working. Then facings shrink, gaps "
        "run for weeks and the system learns your line does not sell. Here is why."),
    "post-sell-out-not-sell-in.html": (
        "Sell-in is not sell-out | GDH Insights",
        "Sell-in shows how much stock you pushed into the channel. Sell-out, scanned at the till "
        "by store and week, shows whether your pack, price and promotion work."),
    "post-retailers-shifting-risk.html": (
        "Retailers are quietly shifting risk to suppliers | GDH",
        "Shorter lead times, tight receiving windows and penalties for partial deliveries all "
        "move cost onto suppliers. The ones who cope well have priced it in."),
    "post-before-you-approach-a-chain.html": (
        "Checklist before you approach a national chain | GDH",
        "First meetings with a chain buyer fail on preparation, not product. Know your unit "
        "cost, full-chain capacity, shelf life, barcodes and certifications first."),
    "post-on-shelf-availability.html": (
        "On-shelf availability is what shoppers feel | GDH",
        "Shoppers only experience one number: whether the product was there. Measure "
        "availability in the store, not the warehouse, and fix the cause behind each gap."),
    "post-the-dental-channel.html": (
        "The dental channel is not like retail | GDH",
        "Dental orders are small, frequent and clinically specific, and the buyer is the "
        "practitioner. Trust comes from whoever turns up every week, not from a campaign."),
    "post-private-label.html": (
        "Private label can be your best customer | GDH",
        "A chain's own-brand range is shelf competition, but someone makes it. For producers "
        "with spare capacity, private label brings steady, plannable volume."),

    # ---------------------------------------------------------- compania
    "about-us.html": (
        "About GDH: a distributor, not a logistics firm",
        "GDH buys products from brands, owns the stock in its own warehouses and sells it into "
        "retail chains and dental practices. Our brands are never invoiced."),
    "partner-with-us.html": (
        "Partner with GDH: send us your range",
        "Tell GDH what you make and where it belongs. We reply with the chains we can reach, "
        "the volume we can move and how fast we can start, at no cost to you."),
    "careers.html": (
        "Careers at GDH: warehouse, delivery and sales",
        "Warehouse, delivery, field merchandising and commercial roles at GDH, where the work "
        "is measured on full shelves and on-time deliveries. Write to us to apply."),
    "locations.html": (
        "Locations: head office and hubs | GDH",
        "GDH's head office and main warehouse are at CTPark, Ghiroda, Timiș, with regional hubs "
        "that keep stock close to the stores and dental practices we serve."),
    "news.html": (
        "Retail, FMCG and dental industry news | GDH",
        "Daily retail, FMCG and dental industry news for brands selling in Romania, "
        "summarised by the GDH commercial desk with every source linked."),
    "changelog.html": (
        "Changelog: what is new in the GDH network",
        "What changed at GDH: extended chilled storage in Ghiroda, new hubs in Cluj and "
        "Constanța, small dental equipment and field merchandising teams."),
    "contact.html": (
        "Contact GDH: commercial desk in Timiș, Romania",
        "Write to the GDH commercial desk about listings, volumes, ordering, deliveries or "
        "returns. Office at CTPark, Ghiroda, Timiș. We reply to every message."),
    "contact-sales.html": (
        "Contact sales: send GDH your product range",
        "Brand owners, manufacturers and importers: send GDH your range and monthly capacity. A"
        " first reply usually comes within two working days, free of charge."),

    # ---------------------------------------------------------- juridic si utilitar
    "privacy.html": (
        "Privacy notice | GDH",
        "gdh-group.com sets no cookies, runs no analytics and contacts no other server. The only "
        "personal data GDH holds is what you choose to send us by email."),
    "cookies.html": (
        "Cookies: this website uses none | GDH",
        "gdh-group.com sets no cookies and loads no analytics, tracking pixels or external "
        "requests. There is nothing to accept and nothing to switch off."),
    "terms.html": (
        "General terms of supply | GDH",
        "The general terms on which GDH buys stock from the brands it carries and sells and "
        "delivers it to retailers, dental practices and laboratories."),
    "imprint.html": (
        "Legal notice: who runs gdh-group.com | GDH",
        "The company that operates gdh-group.com, how to reach it, and who is accountable for "
        "what appears on these pages. GDH, CTPark, Ghiroda, Timiș, Romania."),
    "whistleblowing.html": (
        "Whistleblowing: raise a concern | GDH",
        "If something at GDH looks unlawful or seriously wrong, tell us. What can be reported, "
        "how to report it in confidence, and what happens after you do."),
    "licenses.html": (
        "Licences and credits | GDH",
        "What gdh-group.com is built from: GDH's own copy, licensed photography, Inter Tight "
        "and IBM Plex Mono under the Open Font License, and plain HTML and CSS."),
    "style-guide.html": (
        "Style guide: the GDH visual system",
        "The colour, type and components behind gdh-group.com: black-and-white palette, banner "
        "gradient, Inter Tight and IBM Plex Mono, buttons and the GDH logo."),
    "404.html": (
        "Page not found | GDH",
        "This page is not on our route. It may have been moved or renamed. Head back to the GDH"
        " home page, or tell us what you were looking for."),
}

TITLE_MAX = 60
DESC_MIN, DESC_MAX = 110, 160


def get(page):
    return SEO.get(page)


def check(pages):
    """Opreste build-ul daca o pagina scrisa nu are titlu si descriere proprii,
    daca doua pagini le impart, sau daca un text iese din limite."""
    problems = []
    for page in pages:
        if page not in SEO:
            problems.append("%s: lipseste din seo_gdh.SEO" % page)
    titles, descs = {}, {}
    for page, (title, desc) in SEO.items():
        if page not in pages:
            problems.append("%s: intrare pentru o pagina care nu exista" % page)
        if len(title) > TITLE_MAX:
            problems.append("%s: titlu de %d caractere (max %d)" % (page, len(title), TITLE_MAX))
        if "GDH" not in title:
            problems.append("%s: titlul nu contine GDH" % page)
        if not DESC_MIN <= len(desc) <= DESC_MAX:
            problems.append("%s: descriere de %d caractere (%d-%d)"
                            % (page, len(desc), DESC_MIN, DESC_MAX))
        if "…" in desc or desc.endswith(","):
            problems.append("%s: descrierea pare taiata" % page)
        if title in titles:
            problems.append("%s: acelasi titlu ca %s" % (page, titles[title]))
        if desc in descs:
            problems.append("%s: aceeasi descriere ca %s" % (page, descs[desc]))
        titles[title], descs[desc] = page, page
    if problems:
        raise SystemExit("SEO:\n  " + "\n  ".join(problems))
