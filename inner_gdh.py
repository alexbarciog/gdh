# -*- coding: utf-8 -*-
"""Etapa 3: paginile interioare (about, quote, servicii, studii de caz, articole)."""
import os, re, html


# Adresele mostenite din sablon vorbeau despre transport si oferte de pret.
# Harta ramane aici ca sa rescriem link-urile din snapshot si sa scoatem
# redirectari 301 pentru adresele vechi.
RENAME = {
    "service-one-of-the-best-accountable-team.html":   "service-retail-chain-listings.html",
    "service-clear-shipment-visibility.html":          "service-sell-out-visibility.html",
    "service-flexible-transport-options.html":         "service-stock-and-delivery.html",
    "service-scalable-capacity-with-shipment.html":    "service-dental-distribution.html",
    "service-dispute-resolution-litigation.html":      "service-shelf-execution.html",
    "case-study-supply-chain-optimization.html":       "case-national-grocery-listing.html",
    "case-study-transportation-efficiency.html":       "case-drugstore-chain-rollout.html",
    "case-study-supply-chain-optimization-jz7lc.html": "case-dental-consumables-rollout.html",
    "case-study-transportation-freight.html":          "case-dental-equipment-distribution.html",
    "case-study-warehousing-distribution.html":        "case-convenience-chains.html",
    "case-study-e-commerce-logistics.html":            "case-private-label.html",
    "case-study-e-commerce-logistics-excellence.html": "case-seasonal-promotion.html",
    "case-study-international-logistics.html":         "case-market-entry.html",
    "post-warehouse-inventory-solutions.html":         "post-what-a-chain-buyer-decides.html",
    "post-freight-transportation.html":                "post-listings-and-facings.html",
    "post-logistics-technology.html":                  "post-sell-out-not-sell-in.html",
    "post-industry-news-trends.html":                  "post-retailers-shifting-risk.html",
    "post-expert-tips-guides.html":                    "post-before-you-approach-a-chain.html",
    "post-supply-chain-management.html":               "post-on-shelf-availability.html",
    "post-technology-digital-transformation.html":     "post-the-dental-channel.html",
    "post-e-commerce-logistics.html":                  "post-private-label.html",
    "get-a-quote.html":                                "partner-with-us.html",
}

# ---------------------------------------------------------------- continut
def P(*paras):
    return list(paras)


PAGES = {
    "about-us.html": dict(
        mark=True,
        title="About GDH",
        kicker="/About",
        lead="A distributor of retail and dental products, built around one promise: your product "
             "reaches the shelf it belongs on, and it costs you nothing to put it there.",
        body=P(
            ("Who we are",
             "GDH — Global Distribution Holdings — is a distributor. We buy products from factories and "
             "brands, hold them in our own warehouses, and sell and deliver them into the country's "
             "largest store chains, independent retailers, pharmacies and dental practices. We are not a "
             "freight company and not a logistics supplier: we take ownership of the product and we take "
             "ownership of how it sells."),
            ("What we distribute",
             "Two ranges. Retail: food and beverage, household and personal care, and health and beauty "
             "lines sold through the big chains. Dental: materials, consumables and equipment for "
             "practices, clinics and laboratories. The two channels share our warehouses and our "
             "delivery network, but each has its own commercial team."),
            ("What it costs the brands we carry",
             "Nothing. We do not invoice the factories and brands whose products we distribute — no "
             "listing fee, no storage charge, no delivery cost. We buy the stock and we earn from "
             "distributing it. That means we only make money when your product actually sells, which is "
             "the incentive you want your distributor to have."),
            ("Why brands come to us",
             "Because the hard part is not moving a pallet, it is getting a buyer at a national chain to "
             "take your call, agree a listing, and then keep the shelf full once they do. We already "
             "supply those buyers every week. Your range goes into a conversation that is already "
             "happening."),
        ),
        stats=[("11", "retail chains under contract"), ("1.900+", "stores supplied directly"),
               ("380+", "dental practices and labs"), ("0", "invoices sent to our brands")],
    ),
    "partner-with-us.html": dict(
        title="Partner with GDH",
        kicker="/Partner with us",
        lead="Send us your range and your production capacity. We come back with the chains we can "
             "reach, the volumes we can move and how quickly we can start — usually within two "
             "working days.",
        body=P(
            ("What to send us",
             "Your product list with pack sizes, barcodes and shelf life, your production capacity per "
             "month, any listings or exclusivity you already hold, and the certifications your category "
             "requires. If you do not have all of it, send what you have and we will fill the gaps in a "
             "short call."),
            ("What you get back",
             "An honest read on where your range fits: which chains and which channels we believe will "
             "take it, what volume that means per month, what pack format each buyer will expect, and "
             "when we could realistically put it in front of them."),
            ("What it costs you",
             "Nothing, at this stage or any other. We are a distributor, not a service provider — we buy "
             "your product and earn from selling it on. You will never receive an invoice from GDH."),
            ("Next step",
             "Write to office@gdh-group.com or call +40 21 300 40 50 and ask for the commercial desk. "
             "If it is easier, use the contact form and we will come back to you."),
        ),
        cta=("Open the contact form", "contact.html"),
    ),
    "style-guide.html": dict(
        logo_boards=True,
        title="Brand & style guide",
        kicker="/Style guide",
        lead="The visual system behind the GDH identity: colour, type and the rules we apply across "
             "every surface, from warehouse signage to this website.",
        body=P(
            ("Colour",
             "GDH Orange (#FE3F03) is the primary colour and carries the logo, primary actions and "
             "highlights. Ink (#111111) carries typography and the diagonal cut inside the wordmark. "
             "White is the resting surface. No other accent colour is used in brand communication."),
            ("Typography",
             "Inter Tight in five weights — 300, 400, 500, 600 and 700. Headlines run at weight 600 to "
             "700 with tight tracking; body copy runs at 400. The font is hosted on our own servers, "
             "never loaded from a third party."),
            ("The logo",
             "Heavy geometric letterforms cut by two diagonals, over the descriptor GLOBAL DISTRIBUTION "
             "HOLDINGS. The cuts and the descriptor are black on light backgrounds and white on dark "
             "ones — both versions are shown above. The letter G on its own is the mark we use for "
             "icons. Never re-colour the red, stretch the artwork or add effects to it."),
            ("Spacing",
             "Clear space around the logo equals the height of the letter G. Minimum reproduction width "
             "is 96 px on screen and 28 mm in print."),
        ),
        swatches=[("#FE3F03", "GDH Orange"), ("#111111", "Ink"), ("#F5F5F5", "Surface"), ("#FFFFFF", "White")],
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
             "Inter Tight by Rasmus Andersson, released under the SIL Open Font License 1.1. The font "
             "files are served from this domain; no font CDN is contacted when you load a page."),
            ("Code",
             "The site is plain HTML, CSS and JavaScript with no third-party trackers. Two libraries are "
             "bundled and served from this domain: Lenis, an MIT-licensed smooth-scroll helper, and GSAP "
             "with its ScrollTrigger and SplitText plugins, used under the GSAP standard licence."),
            ("Photography",
             "Photography and illustration are licensed for use by GDH in its own commercial "
             "communications and may not be extracted from this site for other purposes."),
            ("Brands and trademarks",
             "Product and chain names referenced on this site remain the property of their owners. "
             "Mentioning a retailer or a brand here does not imply their endorsement of GDH."),
        ),
    ),
    "changelog.html": dict(
        title="Network changelog",
        kicker="/Changelog",
        lead="What changed in the GDH distribution network — new chains, new channels, new coverage.",
        body=P(
            ("August 2026 — Cold chain at hub D2",
             "Chilled storage extended by 1.400 pallet positions at the București D2 hub, opening the "
             "chilled and short-shelf-life categories to the brands we carry."),
            ("June 2026 — Two new regional hubs",
             "Hubs opened in Cluj and Constanța, bringing daily store coverage to two further regions "
             "and cutting replenishment lead time in the north-west by one working day."),
            ("March 2026 — Dental equipment added",
             "The dental range extended beyond materials and consumables to small equipment, with "
             "installation and warranty handling arranged through the practices we already supply."),
            ("January 2026 — Field merchandising teams",
             "Field teams introduced for shelf placement, planogram checks and promotional set-up in "
             "the stores already on our delivery routes."),
        ),
    ),
    "404.html": dict(
        mark=True,
        title="Page not found",
        kicker="/404",
        lead="This page is not on our route. It may have been moved, renamed, or it never existed.",
        body=P(
            ("Try one of these",
             "Head back to the home page, look through what we do for brands, or open the contact form "
             "and tell us what you were looking for."),
        ),
        cta=("Back to the home page", "index.html"),
        noindex=True,
    ),
}

SERVICES = {
    "service-retail-chain-listings.html": (
        "Retail Chain Listings",
        "We already supply the buyers. We take your range to them, negotiate the listing and own the "
        "launch.",
        [("What it covers",
          "Category review preparation, the buyer meeting itself, pricing and promotional terms, "
          "barcode and master-data setup with the chain, and the first order. You are not sold a "
          "service here — we buy your product and carry it in."),
         ("How it works",
          "We only take a range to a buyer when we believe it will sell, because we are the ones "
          "buying the stock. That means an honest conversation up front about pack format, price "
          "point and which chains are realistic, before anyone's time is spent."),
         ("Who it suits",
          "Producers with capacity and a product that works, who have no route into the big chains — "
          "and brands already listed in one chain who want the other ten.")]),
    "service-sell-out-visibility.html": (
        "Sell-Out Visibility",
        "See what sold, in which chain and at what rate, with stock cover per SKU and proof of "
        "delivery per store.",
        [("What it covers",
          "Sell-out per chain and per SKU, stock on hand in our warehouses, orders in picking, loads "
          "dispatched and proof of delivery per store — in one view, exported however your systems "
          "need it."),
         ("Batch and expiry",
          "Every movement carries batch, lot and expiry data, so a recall takes minutes to scope and "
          "short-dated stock is rotated before it becomes a write-off."),
         ("Forecasting",
          "The same data goes back to your production planning. If a line is moving faster than the "
          "plan, you hear it from us while there is still time to make more.")]),
    "service-stock-and-delivery.html": (
        "Nationwide Stock & Delivery",
        "We buy and hold the stock, then supply every chain depot, store and practice from our own "
        "warehouses and routes.",
        [("Channels",
          "Chain distribution centres on scheduled slot deliveries, independent stores and pharmacies "
          "on fixed weekly routes, dental practices and laboratories on their own cycle, and "
          "cash-and-carry depots on call-off."),
         ("Formats",
          "Full pallets, mixed pallets, shelf-ready cases or single units — picked to whatever format "
          "the receiving location actually wants to handle."),
         ("Peaks",
          "Seasonal peaks are absorbed from shared capacity across our whole portfolio, so a six-week "
          "Christmas push does not need a warehouse of its own.")]),
    "service-dental-distribution.html": (
        "Dental Distribution",
        "Materials, consumables and equipment into dental practices, clinics, laboratories and dental "
        "depots nationwide.",
        [("The channel",
          "Dentistry does not buy like retail. Orders are small, frequent and clinically specific, the "
          "buyer is usually the practitioner or the practice manager, and the decision turns on "
          "clinical confidence rather than shelf price."),
         ("What we carry",
          "Restorative and impression materials, disposables and infection control, prosthetics and "
          "laboratory supplies, and small equipment with installation and warranty handled through the "
          "practices we already serve."),
         ("Why it works",
          "We are already in those practices every week delivering consumables. Adding a new line to "
          "an existing, trusted delivery relationship is a far shorter road than building one from "
          "scratch.")]),
    "service-shelf-execution.html": (
        "Shelf Execution & Merchandising",
        "Field teams that place the product, hold the planogram, build the promotion and report back "
        "what they actually see in store.",
        [("In store",
          "Our people are in the stores we deliver to. They place stock on shelf, correct facings, "
          "rebuild displays that have been picked apart, and set up promotional space on the day it "
          "goes live — not three days later."),
         ("What you get back",
          "Photographs, planogram compliance and competitor activity from the stores we visit, so you "
          "can see the shelf without flying someone around the country to look at it."),
         ("Returns and recalls",
          "Store returns come back on the same routes that deliver, are triaged at the hub, and are "
          "either returned to sellable stock or written off with evidence. Because every movement "
          "carries batch data, a recall is scoped in minutes.")]),
}

CASES = {
    "case-national-grocery-listing.html": (
        "National Grocery Listing", "Grocery Retail",
        "Taking a regional food producer from three counties to national listings in two grocery chains.",
        [("The situation",
          "A good product with real regional loyalty, sold through independents in three counties. The "
          "producer had approached two national chains directly over four years and never got past a "
          "first meeting."),
         ("What we did",
          "We reworked the pack format and case configuration to what those two buyers actually expect, "
          "took the range into an existing category review, and bought the opening order ourselves."),
         ("The result",
          "Listed in both chains within one season, national distribution across 680 stores, and a "
          "producer whose only operational change was making more.")]),
    "case-drugstore-chain-rollout.html": (
        "Drugstore Chain Rollout", "Health & Beauty",
        "Placing a personal care range into a national drugstore chain and holding the shelf afterwards.",
        [("The situation",
          "The brand had won a listing on its own but was losing facings at every category review. "
          "Nobody was visiting stores, so nobody could say why sell-out was below forecast."),
         ("What we did",
          "We took over distribution and put the range on our field merchandising round: facings "
          "corrected weekly, displays rebuilt, promotional space set up on day one of each campaign."),
         ("The result",
          "Sell-out per store rose by just under a third over two quarters, and the range gained a "
          "facing at the following review instead of losing one.")]),
    "case-dental-consumables-rollout.html": (
        "Dental Consumables Rollout", "Dental",
        "Putting a consumables range into dental practices and laboratories across the country.",
        [("The situation",
          "A manufacturer of infection-control disposables with a strong product, no field force, and "
          "no realistic way to reach several thousand individual practices one at a time."),
         ("What we did",
          "The range went onto our existing dental delivery cycle, introduced by the people who already "
          "call on those practices every week, with samples carried on the same vans."),
         ("The result",
          "Stocked in more than 380 practices and laboratories inside a year, at a fraction of what "
          "building a dental sales force would have cost.")]),
    "case-dental-equipment-distribution.html": (
        "Dental Equipment Distribution", "Dental",
        "Adding small equipment to a consumables relationship that was already running weekly.",
        [("The situation",
          "An equipment maker selling through occasional trade fairs and a distributor who treated "
          "equipment as an afterthought. Installation and warranty were nobody's clear responsibility."),
         ("What we did",
          "Equipment added to the practices we already supply, with installation scheduled against our "
          "delivery calendar and warranty claims handled by our own desk rather than bounced back to "
          "the manufacturer."),
         ("The result",
          "Units placed through practices that already trusted the delivery relationship, and warranty "
          "response measured in days instead of weeks.")]),
    "case-convenience-chains.html": (
        "Convenience & Proximity Chains", "Convenience",
        "Reaching 1.100 small-format stores that no single brand can economically serve alone.",
        [("The situation",
          "A snack brand listed nationally in the large-format chains and completely absent from "
          "convenience, where the category over-indexes. Serving those stores alone was not worth it "
          "for one brand's volume."),
         ("What we did",
          "The range joined a mixed route already delivering other categories into those stores, so the "
          "cost of the drop was shared across everything on the van."),
         ("The result",
          "1.100 convenience stores added as a channel, with a cost per drop no single-brand operation "
          "could have reached.")]),
    "case-private-label.html": (
        "Private Label for a Chain", "Private Label",
        "Matching a chain's own-brand brief to a producer who could actually deliver it.",
        [("The situation",
          "A chain wanted an own-brand line in a category we already supply, and needed a producer who "
          "could meet the specification, the volume and the audit — reliably, from the first order."),
         ("What we did",
          "We brought in a producer from our existing portfolio, managed specification and packaging "
          "against the chain's brief, and took commercial responsibility for supply."),
         ("The result",
          "A private-label line in national distribution, a producer with volume it could plan around, "
          "and a chain with one accountable counterpart instead of three.")]),
    "case-seasonal-promotion.html": (
        "Seasonal Promotion Execution", "Grocery Retail",
        "Building and executing a nationwide promotional push across 1.400 stores in six weeks.",
        [("The situation",
          "A promotion agreed centrally with the chain, six weeks to execute it, and a brand with no "
          "way to confirm whether the display was actually built in any given store."),
         ("What we did",
          "Promotional stock pre-positioned at our hubs before week one, display units delivered on "
          "the same vans, and our field teams building and photographing every site on the day."),
         ("The result",
          "Displays live in 1.400 stores inside the first three days of the promotion, with "
          "photographic proof per store and no out-of-stocks during the campaign.")]),
    "case-market-entry.html": (
        "Market Entry for an Imported Brand", "Market Entry",
        "Bringing an established foreign brand into the market without it opening an office here.",
        [("The situation",
          "A brand with a strong position in its home market, no local entity, no local listings and "
          "no idea which of the chains here would be the right first door."),
         ("What we did",
          "We handled labelling and local compliance, chose two chains for the entry rather than "
          "chasing all of them, bought the opening stock and ran the launch from our own warehouses."),
         ("The result",
          "A market entry that cost the brand no local infrastructure, with the third and fourth chain "
          "added once the first two had proven the sell-out.")]),
}

POSTS = {
    "post-what-a-chain-buyer-decides.html": (
        "Retail Strategy", "June 10, 2026",
        "What a chain buyer is actually deciding",
        [("Brands prepare for a buyer meeting by talking about their product. Buyers are not deciding "
          "whether your product is good. They are deciding what comes off the shelf to make room for "
          "it, and whether the category earns more afterwards."),
         ("That reframes everything you bring to the meeting. Not 'our product is better', but 'here is "
          "the shopper your category is currently losing, here is what this line adds per metre of "
          "shelf, and here is why it does not simply cannibalise what you already stock'."),
         ("It also explains why a distributor who already sits in that category review gets a different "
          "hearing. The buyer is not evaluating a stranger's claim — they are evaluating a proposal "
          "from someone whose other lines they can already measure.")]),
    "post-listings-and-facings.html": (
        "Shelf Execution", "October 9, 2026",
        "A listing is permission. A facing is the actual business.",
        [("Winning a listing feels like the finish line, and for a lot of brands it is where the work "
          "stops. The product is in the system, the first order ships, and everyone moves on."),
         ("Then the shelf does what shelves do. A neighbouring brand's rep tidies their block outwards. "
          "A promotion rebuilds the bay and your facing does not come back. A store runs a gap for three "
          "weeks and the replenishment system quietly learns that the line does not sell."),
         ("None of that appears in your sell-in numbers until the category review, when it appears all "
          "at once. Somebody has to be in the store. Either you pay a field force to do it, or you work "
          "with a distributor whose people are already walking that aisle for other reasons.")]),
    "post-sell-out-not-sell-in.html": (
        "Data & Insight", "October 8, 2026",
        "Sell-in is not sell-out, and only one of them matters",
        [("Most producers manage their business on sell-in: what left the warehouse, what was invoiced, "
          "what the distributor ordered. It is the easiest number to get and the least informative one "
          "you can run on."),
         ("Sell-in is a measure of how much stock you pushed into the channel. It can rise for months "
          "while the shelf is not moving at all, and the correction, when it comes, arrives as a "
          "cancelled order and a warehouse full of short-dated product."),
         ("Sell-out — units actually scanned at the till, by store and by week — tells you whether the "
          "pack size works, whether the price point works, whether the promotion did anything, and "
          "which stores should never have been listed. Ask for it before you sign with anyone.")]),
    "post-retailers-shifting-risk.html": (
        "Retail News & Trends", "October 7, 2026",
        "Retailers are shifting risk onto suppliers — quietly",
        [("Shorter order lead times, tighter receiving windows and penalties for partial deliveries have "
          "all become normal. None of them appear as a price change, but every one of them moves cost "
          "and risk onto the supplier."),
         ("The suppliers handling this well are the ones who priced it: they know what a two-hour "
          "receiving window costs them, and they negotiate frequency and drop size accordingly."),
         ("The ones handling it badly are absorbing it silently and wondering why margin is drifting.")]),
    "post-before-you-approach-a-chain.html": (
        "Practical Guides", "March 11, 2026",
        "A checklist before you approach a national chain",
        [("Most first meetings with a chain buyer fail on preparation, not on product. The questions are "
          "predictable, and not having the answers ends the conversation politely and permanently."),
         ("Before the meeting, know: your true cost per unit at the volume being discussed, your "
          "capacity if they take all their stores rather than a region, your shelf life and how it "
          "survives their distribution, your barcodes and master data, the certifications your category "
          "requires, and what happens to your other customers if this listing lands."),
         ("If you cannot answer the capacity question with a number, do not take the meeting yet. The "
          "worst outcome in this business is not being turned down — it is winning a listing you cannot "
          "supply.")]),
    "post-on-shelf-availability.html": (
        "Availability", "April 22, 2026",
        "On-shelf availability is the only number the shopper feels",
        [("Warehouse productivity, vehicle fill and cost per pallet all matter internally. The shopper "
          "experiences exactly one thing: whether the product was there when they reached for it."),
         ("Measure availability in the store, not in your warehouse. Stock sitting in a chain's "
          "distribution centre while the shelf is empty counts as a stock-out to everyone who matters, "
          "and it is one of the most common failures in the whole chain."),
         ("Once it is measured honestly, the causes sort into three buckets: we did not make it, it did "
          "not get delivered, or it got delivered and never made it onto the shelf. The third is far "
          "more common than most brands believe.")]),
    "post-the-dental-channel.html": (
        "Dental Channel", "October 4, 2026",
        "The dental channel does not behave like retail",
        [("Brands that succeed in retail often assume dentistry is the same game at a smaller scale. It "
          "is not. The order is small, frequent and clinically specific, and the person deciding is the "
          "person who will use the product on a patient that afternoon."),
         ("There is no shelf to win and no planogram to negotiate. There is a practitioner who has used "
          "the same material for eleven years and will not change for a price difference. Trust is "
          "built by the person who turns up every week, not by a campaign."),
         ("Which is why distribution matters more here than almost anywhere. A new line introduced by "
          "someone the practice already relies on gets tried. The same line in a mailshot does not.")]),
    "post-private-label.html": (
        "Private Label", "October 3, 2026",
        "Private label is not your enemy. It is often your best customer.",
        [("Producers treat a chain's own-brand range as the competition, and in shelf terms it is. But "
          "somebody manufactures it, and that somebody gets volume they can plan a year around."),
         ("Private label buys differently from branded listings: the specification is fixed, the volume "
          "is large and steady, the marketing cost is zero, and the relationship survives category "
          "reviews that would remove a small brand."),
         ("The right answer for most producers with spare capacity is both — a branded line to build "
          "equity and margin, and a private-label line underneath it to fill the factory. They are not "
          "in conflict as long as the specifications are genuinely different.")]),
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
                '<img src="img/gdh-logo.png" alt="The GDH logo on a light background" '
                'class="gdh-logo" width="300" height="126" decoding="async">'
                '<div class="font-1-extra-small worm-gray">On light backgrounds</div></div>'
                '<div class="gdh-logo-board is-dark">'
                '<img src="img/gdh-logo-light.png" alt="The GDH logo on a dark background" '
                'class="gdh-logo" width="300" height="126" decoding="async">'
                '<div class="font-1-extra-small">On dark backgrounds</div></div>'
                '<div class="gdh-logo-board is-mark">'
                '<img src="img/gdh-mark.png" alt="The GDH mark" class="gdh-logo" '
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
                 '<div class="button-text">Work With Us</div><div class="button-text">Work With Us</div>'
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
