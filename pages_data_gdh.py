# -*- coding: utf-8 -*-
"""Continutul paginilor de sector si de serviciu.

Structura: slug, kicker, title, lede, sections[heading/body],
bullets[title/text], faq[q/a]. Randarea e in site_gdh.data_page().
"""

PAGES = [   {   'slug': 'sectors',
        'kicker': 'Sectors',
        'title': 'Retail and dental — the shelves we already supply',
        'lede': 'GDH distributes into two channels: retail and dental. The same warehouses and '
                'the same lorries serve both, but each channel has **its own commercial team** — '
                'a chain category buyer and a practice principal do not respond to the same '
                'conversation.',
        'sections': [   {   'heading': 'One network, two commercial teams',
                            'body': 'GDH runs a single warehouse estate and a single route plan. '
                                    'Stock for a shampoo range and stock for a composite filling '
                                    'material sit in the same buildings and travel on the same '
                                    'vehicles, which is what makes it viable for us to carry '
                                    'smaller ranges at all. Commercially the two channels are '
                                    'kept apart. Retail has account managers who sit in front of '
                                    'chain category buyers and work to their range review '
                                    'calendar. Dental has representatives who call on practices, '
                                    'clinics and laboratories. Neither team is asked to sell '
                                    'outside what it knows.'},
                        {   'heading': 'Grocery and convenience',
                            'body': 'The large grocery chains, and the convenience and forecourt '
                                    'networks behind them. We hold listings across ambient food, '
                                    'drinks, household and pet lines, and we deliver either into '
                                    "a chain's own depots or store by store, depending on how "
                                    'that retailer wants to be served. For a brand on its own '
                                    'this is the hardest door in the market: range reviews run '
                                    'on a fixed calendar, and a buyer wants to see that somebody '
                                    'can keep the shelf full between them. We are in those '
                                    'stores every week already.'},
                        {   'heading': 'Health, beauty and pharmacy',
                            'body': 'Personal care, cosmetics, supplements and over-the-counter '
                                    'lines, sold into drugstore chains, beauty retailers and '
                                    'independent pharmacies. The pharmacy side is a long tail — '
                                    'hundreds of individual counters rather than a handful of '
                                    'depots — so it is served from the same vans that cover our '
                                    'dental round. Health and beauty also carries more rules '
                                    'than grocery: claims, labelling, batch traceability, '
                                    'recall. Our team reads a product dossier before the first '
                                    'order is placed, not after a buyer has sent it back.'},
                        {   'heading': 'Private label and own-brand programmes',
                            'body': 'Chains that want a product made to their own specification, '
                                    'and manufacturers that would rather make it than build a '
                                    'brand. We sit in the middle. We know which categories a '
                                    'retailer is short in, what price architecture the shelf '
                                    'needs, and which factories can hold that specification at '
                                    "volume. The name on the pack stays the retailer's. "
                                    'Responsibility for stock, delivery and shelf condition is '
                                    'ours. For a manufacturer it is the quickest route to '
                                    'committed volume without spending anything on marketing.'},
                        {   'heading': 'Dental: practices, clinics, laboratories and depots',
                            'body': 'Materials, consumables, small instruments and equipment. '
                                    'Four kinds of customer, each ordering differently: '
                                    'single-surgery practices buying little and often, group '
                                    'clinics working from agreed lists, laboratories that need '
                                    'specific alloys and ceramics by batch, and dental depots '
                                    'that resell. This channel runs on trust in the person who '
                                    'walks through the door, so our representatives carry '
                                    'product knowledge rather than a price sheet. Items with '
                                    'shelf-life or temperature conditions are held in the same '
                                    'warehouses, in dedicated monitored areas.'}],
        'bullets': [   {   'title': 'Shared network',
                           'text': 'One warehouse estate, one route plan. Retail and dental '
                                   'stock move together — which is exactly what makes it worth '
                                   'our while to carry a small range.'},
                       {   'title': 'Separate commercial teams',
                           'text': 'Selling to a chain category buyer and selling to a practice '
                                   'principal are different jobs. Each channel has its own '
                                   'account managers and its own call list.'},
                       {   'title': 'Nothing billed either way',
                           'text': 'Whichever sector your product sells into, your brand never '
                                   'sees an invoice from us. We buy the stock and earn from '
                                   'distribution margin.'}],
        'faq': [   {   'q': 'We only sell into one sector. Does that matter?',
                       'a': 'No. Most of the brands we carry sit in a single channel, and '
                            'nothing about how we work changes because of it. A dental '
                            'consumables maker deals with the dental team and never hears from '
                            'retail. What a single range still gets is the whole warehouse and '
                            'delivery network behind it, because the cost of running that '
                            'network is already spread across everything in it.'},
                   {   'q': 'Can a product cross from dental into retail?',
                       'a': 'Occasionally. Oral care is the obvious bridge: a line that starts '
                            'in practices can earn a place on a drugstore shelf once there is '
                            'evidence it sells. We do not force it. Retail wants different pack '
                            'sizes, different margins and packaging built for a scanner, and a '
                            'product that works in a surgery is not automatically ready for '
                            'that. If the move looks worth making, we will say so and tell you '
                            'what has to change.'},
                   {   'q': 'Who at GDH would we actually deal with?',
                       'a': 'One commercial lead in the channel your product belongs in, from '
                            'the first meeting onwards. They set the forecast you produce to, '
                            'take the range through buyer meetings or practice visits, and '
                            'remain your contact once it is selling. The warehouse and transport '
                            'side sits behind them. You are welcome to come and see it, but you '
                            'should not have to manage two relationships to sell one product.'}]},
    {   'slug': 'sector-retail',
        'kicker': 'Retail',
        'title': 'Your range on the shelves of the chains that matter',
        'lede': 'GDH buys retail stock outright and sells it into supermarket, drugstore, '
                'convenience and cash-and-carry chains across the country. The listings and the '
                'weekly buyer calls already exist — **your brand joins them**.',
        'sections': [   {   'heading': 'The chains we sell into',
                            'body': 'Four kinds of retail buyer sit behind almost every grocery '
                                    'and personal care purchase in the country: the national '
                                    'supermarket groups, the drugstore and pharmacy chains, the '
                                    'convenience and forecourt networks, and the cash-and-carry '
                                    'and wholesale houses that supply independents. GDH holds '
                                    'accounts and trading terms with all four. Each buys '
                                    'differently — a supermarket wants a range plan and a '
                                    'promotional calendar, a convenience chain wants a short, '
                                    'fast-selling selection in small case sizes. We match your '
                                    'product to the formats where it will actually sell, rather '
                                    'than pushing it everywhere at once.'},
                        {   'heading': 'Getting listed',
                            'body': 'Chains review categories on a calendar, not on request. We '
                                    'know when each window opens and what each buyer expects to '
                                    'see in it: a clean range proposal, case configuration, '
                                    'shelf price, margin, and a reason the category grows rather '
                                    'than simply shifts. We build that case, present it as part '
                                    'of our own portfolio, and negotiate the terms. Because the '
                                    'buyer already trades with us, the conversation starts at '
                                    'the product rather than at credit checks and supplier '
                                    'onboarding. Where a buyer wants proof first, we place the '
                                    'range in a store group as a trial.'},
                        {   'heading': 'Bought, stocked, delivered',
                            'body': 'We buy your production outright and bring it into our own '
                                    "warehouses. From there it is picked to each chain's order — "
                                    "pallets to a retailer's distribution centre, mixed cases to "
                                    'individual stores, small drops to convenience sites — on '
                                    'the delivery windows each account has agreed with us. The '
                                    'stock holding is ours, so an order is filled from goods '
                                    'already in the country rather than from a production run. '
                                    'You produce to a forecast we give you and invoice us. '
                                    'Everything after your loading bay is our responsibility.'},
                        {   'heading': 'Keeping it on shelf',
                            'body': 'A listing is only worth what the shelf actually holds. Our '
                                    'field team calls on stores to check the product is sited '
                                    'where the plan says, that facings have not been quietly '
                                    'reduced, and that gaps are filled before a buyer sees an '
                                    "availability problem. We read each chain's sell-out data "
                                    'weekly, reorder against it, and flag lines that are slowing '
                                    'while there is still time to fix the price, the pack or the '
                                    'position. Promotions are planned with the buyer and stocked '
                                    'in advance, so an offer never runs out mid-week.'},
                        {   'heading': 'What we need from you',
                            'body': 'Samples, specifications, barcodes, shelf-ready packaging or '
                                    'the willingness to change it, and a production capacity you '
                                    'can commit to. Then an honest answer on lead times, because '
                                    'a chain penalises a supplier who misses a delivery window '
                                    'and we are that supplier. In return you get the listings, '
                                    'the stock risk, the deliveries and the store work, and no '
                                    'invoice from us for any of it. GDH earns a distribution '
                                    'margin on goods it has bought. If the product does not '
                                    'sell, that is our loss before it is yours.'}],
        'bullets': [   {   'title': 'We buy, you invoice us',
                           'text': 'Stock is purchased outright and paid on agreed terms. The '
                                   'money risk of a slow line sits with GDH, not with your '
                                   'brand.'},
                       {   'title': 'Listings already open',
                           'text': 'Trading terms, buyer contacts and category review dates '
                                   'exist across supermarket, drugstore, convenience and '
                                   'cash-and-carry chains. Your range joins an existing '
                                   'account.'},
                       {   'title': 'Nothing to pay',
                           'text': 'No listing fee, no storage charge, no delivery cost, no '
                                   'quote. GDH is paid by the distribution margin on the goods '
                                   'it owns.'}],
        'faq': [   {   'q': 'What does it cost us to be distributed by GDH?',
                       'a': 'Nothing. We do not invoice brands. There is no listing fee, no '
                            'storage charge, no delivery cost and no quotation to sign. We buy '
                            'your stock at an agreed price and earn our money on the margin '
                            'between that price and what we sell it for into the chains. The '
                            'commercial consequence is simple: we only take on a range we '
                            'believe we can sell through.'},
                   {   'q': 'How long before our product is actually on shelf?',
                       'a': "It depends on the chain's category review calendar more than on us. "
                            'Some formats — convenience, cash-and-carry, independents supplied '
                            'through wholesale — can take new stock within weeks. The large '
                            'supermarket groups work to fixed review windows, so the honest '
                            'answer is the next window that fits your category. We will tell you '
                            'which windows are coming, what each buyer needs to see, and where a '
                            'store trial can start earlier.'},
                   {   'q': 'Do you already distribute something that competes with us?',
                       'a': 'Often, yes — we carry broad ranges, and a buyer expects that from a '
                            'distributor. What we will not do is hold two lines we cannot both '
                            'sell. Before we take a range on we say plainly where it sits '
                            'against what we already supply, which chains it suits, and whether '
                            'it needs a different pack or price to earn its own space rather '
                            "than take someone else's."}]},
    {   'slug': 'sector-grocery',
        'kicker': 'Grocery',
        'title': 'Your food and drink range, on national grocery shelves',
        'lede': 'We buy your food and drink lines outright, hold them in our own warehouses and '
                'replenish the national grocery chains week after week. **You never see an '
                'invoice from us.**',
        'sections': [   {   'heading': 'We already hold the grocery listings',
                            'body': 'Getting a food or drink line into a national chain is '
                                    'mostly a question of access. The buyers deal with a handful '
                                    'of distributors they already trade with, on a range review '
                                    'calendar set months ahead. We are in those meetings. Our '
                                    'depot codes are live and our delivery rounds already stop '
                                    'at every regional distribution centre each week. A brand '
                                    'coming through us joins a conversation that is already '
                                    'happening, rather than starting one from the outside and '
                                    'waiting for a reply.'},
                        {   'heading': 'Pack formats that work on a grocery shelf',
                            'body': 'Most ranges that fail a buyer meeting fail on the pack, not '
                                    'the product. A case too deep for a convenience store, an '
                                    'outer that leaves a gap in the bay, a tray that cannot be '
                                    'merchandised in one movement — any of it can cost you the '
                                    'listing. We go through case count, outer dimensions, pallet '
                                    'layer, barcode hierarchy and the shelf-ready option before '
                                    'anything is presented. Where a change is needed you hear it '
                                    'early, while the tooling decision is still open.'},
                        {   'heading': 'Shelf life managed on the way in',
                            'body': 'Food and drink is bought against its date code. We take '
                                    'stock in with the remaining life the chains require at '
                                    'depot intake, rotate strictly on date in our own warehouses '
                                    'and pick oldest first on every order. Cover is set by life: '
                                    'long ambient lines carry weeks of stock, short-life lines '
                                    'are bought in smaller and more frequent lots. If a batch '
                                    'does start to run short of life, we move it through our '
                                    'independent and convenience accounts instead of letting it '
                                    'reach write-off.'},
                        {   'heading': 'A replenishment rhythm, not a series of orders',
                            'body': 'Grocery runs to a weekly beat. Orders drop, depot slots are '
                                    'booked, vehicles are loaded, shelves are filled again — the '
                                    'same cycle, every week, in every region. We hold the stock '
                                    'that absorbs that beat, so your factory is not reacting to '
                                    'it. You produce against a forecast we give you ahead of '
                                    'time and we carry the buffer between your production runs '
                                    "and the chain's order pattern. When sell-out moves, we tell "
                                    'you what we are seeing and adjust what we buy.'},
                        {   'heading': 'Promotional volume, built before it is needed',
                            'body': 'A feature week or a multibuy can lift volume several times '
                                    'over for a short period, and the damage is done when the '
                                    'stock is not there. Promotions are agreed with the buyer '
                                    'well in advance, so we build the cover into our purchase '
                                    'plan ahead of the date, flag the production you need in '
                                    'time and hold it until the chain calls it off. When the '
                                    'promotion ends we wind the order pattern back down, rather '
                                    'than leaving a factory running at promotional rate.'}],
        'bullets': [   {   'title': 'We buy the stock',
                           'text': 'Title passes to us at the warehouse door. We carry the '
                                   'working capital, the holding risk and the date risk on every '
                                   'case we take in.'},
                       {   'title': 'Ambient and chilled',
                           'text': 'Both temperature regimes run through the same warehouses and '
                                   'the same weekly rounds, from long-life store cupboard lines '
                                   'to short-dated chilled.'},
                       {   'title': 'Nothing to pay',
                           'text': 'No listing fee, no storage charge, no delivery cost, no '
                                   'quote. We earn from distribution margin, so no invoice ever '
                                   'comes from us to you.'}],
        'faq': [   {   'q': 'What does it cost our brand to work with GDH?',
                       'a': 'Nothing. We buy your stock at an agreed price and earn our margin '
                            'when we sell it on. There is no listing fee, no storage charge, no '
                            'delivery cost and no quote to review. Once the trade price and the '
                            'terms are agreed, every cost of warehousing, selling and delivering '
                            'the range sits with us, not with you.'},
                   {   'q': 'Do you take chilled and short shelf life lines?',
                       'a': 'Yes. We run ambient and chilled stock through the same warehouses '
                            'and the same weekly delivery rounds. Short-life lines simply need '
                            'tighter ordering, so we buy in smaller, more frequent lots and hold '
                            'less cover. Tell us the total life of the product and the minimum '
                            'life the chains must receive at intake, and we will build the order '
                            'pattern around it.'},
                   {   'q': 'Do we need to change our pack format first?',
                       'a': 'Usually not much. Bring us what you make and we will tell you where '
                            'it will struggle: an outer that does not fill a shelf, a case count '
                            'too deep for a small store, a tray that will not merchandise '
                            'cleanly. Plenty of lines go on exactly as they are. Others need a '
                            'different case quantity or a shelf-ready outer before a buyer will '
                            'take them.'}]},
    {   'slug': 'sector-health-beauty',
        'kicker': 'Health & Beauty',
        'title': 'Beauty and personal care onto drugstore and pharmacy shelves',
        'lede': 'Personal care and beauty lines live or die on shelf space. We buy your stock, '
                'place it into the drugstore chains and pharmacies we already call on every '
                'week, and hold the facings once they are won — **at no cost to your brand**.',
        'sections': [   {   'heading': 'The shelves we already serve',
                            'body': 'The buyers in this category are the drugstore chains, the '
                                    'pharmacy groups and the independent pharmacies that order '
                                    'week by week. We are already in front of them. Our '
                                    'representatives walk those aisles on a fixed call cycle, so '
                                    'a new personal care line is presented by someone the buyer '
                                    'and the counter staff already know. For your brand that '
                                    'removes the hardest part: getting a hearing in the first '
                                    'place. We buy the stock from you, hold it in our own '
                                    'warehouses, and sell and deliver it into those accounts '
                                    'ourselves.'},
                        {   'heading': 'Facings, and holding on to them',
                            'body': 'Winning a facing is one job. Keeping it is another. A line '
                                    'that runs empty for a fortnight loses space at the next '
                                    'reset, and that space is hard to win back. We forecast from '
                                    'actual sell-out, hold buffer stock in depth and replenish '
                                    "on each chain's order rhythm rather than waiting for a gap "
                                    'to be reported to us. Where a retailer allows it, we add '
                                    'secondary siting — counter units, dump bins, end panels — '
                                    'so the range is seen twice in the store rather than once.'},
                        {   'heading': 'Category reviews',
                            'body': 'Drugstore and pharmacy categories are reviewed to a '
                                    'calendar, and the submission window is short. We know when '
                                    'each account reviews skincare, haircare, oral care and '
                                    'cosmetics, and we prepare the submission: range proposal, '
                                    'case and margin data, barcodes and dimensions, artwork and '
                                    'sample units. You supply the product and the specification; '
                                    'we build the argument in the format that buyer expects. If '
                                    'a review moves a line down the planogram or out of it, you '
                                    'hear it from us straight away, along with the reason the '
                                    'buyer actually gave.'},
                        {   'heading': 'Planogram discipline',
                            'body': 'A planogram agreed at head office means nothing if the '
                                    'store does not build it. Our field team checks the '
                                    'implementation: correct block, correct order, correct '
                                    'number of facings, shelf-edge labels present, price marking '
                                    'right, no competitor product sitting in your space. Gaps '
                                    'are filled from stock on the van or flagged for the next '
                                    'delivery. Store-level notes and photographs come back to '
                                    'us, and we pass on what affects your lines — including the '
                                    'stores where the range is quietly being squeezed, so it can '
                                    'be raised before the next review.'},
                        {   'heading': 'Seasonal gifting',
                            'body': 'Gift sets are produced months ahead and sell in weeks. We '
                                    'commit to gifting ranges early, take the stock into our '
                                    "warehouses before the peak and deliver to each chain's own "
                                    'on-shelf date, with pre-pack display units built to the '
                                    "retailer's footprint. We plan the end of the season too: "
                                    'clearance routes for residual stock, so your brand is not '
                                    "holding cartons of last December's sets in January and the "
                                    'next listing is not prejudiced by a messy run-out.'}],
        'bullets': [   {   'title': 'Nothing to invoice',
                           'text': 'We buy your stock and earn from distribution margin. No '
                                   'listing fee, no storage charge, no delivery cost. Your brand '
                                   'never receives an invoice from us.'},
                       {   'title': 'Facings defended',
                           'text': 'Space won at head office is checked store by store — block, '
                                   'order, facings, shelf-edge labels — and gaps are filled '
                                   'before weak sales show up in the category review.'},
                       {   'title': 'Batch and date control',
                           'text': 'Cosmetics and personal care rotate on date. We pick by '
                                   'batch, run stock first in, first out, and can trace a batch '
                                   'back out of the trade if it has to be withdrawn.'}],
        'faq': [   {   'q': 'What does it cost our brand to be distributed by GDH?',
                       'a': 'Nothing. We buy your stock outright and earn from the margin '
                            'between what we pay you and what we sell it for. There is no '
                            'listing fee, no storage charge and no delivery cost. Your brand '
                            'invoices us for the goods we order, and you will never receive an '
                            'invoice from us for distribution, warehousing or in-store work.'},
                   {   'q': 'Can you reach independent pharmacies as well as the drugstore '
                            'chains?',
                       'a': 'Yes. The chains take the volume, but independents matter for a '
                            'pharmacy-positioned line and they buy small quantities across a '
                            'wide range. We already deliver to them, so adding your products is '
                            'a matter of loading the range into an existing call, not building a '
                            'new route. You get both channels from one trading relationship.'},
                   {   'q': 'How far ahead do you need a seasonal gifting range?',
                       'a': 'Earlier than most brands expect. Chain buyers commit to gifting '
                            'well before the season, and the pre-pack unit, artwork and case '
                            'configuration have to exist at the point of submission. Bring us '
                            'the concept and costings in good time for that review window, and '
                            'be straight with us about production lead times so we do not sell '
                            'volume you cannot make.'}]},
    {   'slug': 'sector-convenience',
        'kicker': 'Convenience',
        'title': 'Convenience: thousands of small doors, one shared route',
        'lede': 'Convenience stores sell in ones and twos, order in handfuls and hold shelves '
                'barely a metre wide. No single brand can afford to call on them. We already do '
                '— every week, with a full basket, so **your line rides a route that is already '
                'paid for**.',
        'sections': [   {   'heading': 'The maths of a single-brand call',
                            'body': 'A convenience store holds what it can sell in a few days. '
                                    'It orders two cases, sometimes one. Send your own van to '
                                    "that door and the fuel, the driver's hour, the paperwork "
                                    'and the return trip all sit on top of two cases of product. '
                                    'Repeat that across thousands of small shops on back '
                                    'streets, forecourts and transport hubs and the route costs '
                                    'more than the margin it earns. That is why most brands stop '
                                    'at the big chains and leave the small-format trade to '
                                    'chance.'},
                        {   'heading': 'A shared route makes it viable',
                            'body': 'Our van does not call on that shop for your brand. It calls '
                                    'with a full basket — ambient grocery, household lines, '
                                    'confectionery, health and personal care, oral care — built '
                                    'from every brand we carry. The cost of the drop is divided '
                                    'across the whole order, so a two-case line pays its way. '
                                    'You get the same door, the same frequency and the same '
                                    'driver as brands many times your size, because none of you '
                                    'is funding the journey alone.'},
                        {   'heading': 'Built for a one-facing shelf',
                            'body': 'Small-format space is measured in facings, not metres. We '
                                    'tell you which of your packs can earn one: the single-serve '
                                    'or small count rather than the family size, the price point '
                                    'a shopper decides on at the till, and an outer case a shop '
                                    'with no stockroom can actually take in. Where the channel '
                                    'expects a price-marked pack, we say so before you print. '
                                    'Lines that cannot hold a facing come off the route rather '
                                    'than sitting in a back room going out of date.'},
                        {   'heading': 'Symbol groups, forecourts and independents',
                            'body': 'Small-format trade is not one customer. Symbol groups and '
                                    'buying groups list centrally, then each store orders for '
                                    'itself. Forecourt operators buy to a range set at head '
                                    'office. Independents and neighbourhood shops decide at the '
                                    'counter, or collect from a depot when it suits them. We '
                                    'hold the central listings and we call on the stores, so a '
                                    'decision taken at head office turns into stock on the shelf '
                                    '— and the shopkeeper nobody ever contacted is still offered '
                                    'the line.'},
                        {   'heading': 'We own the stock and the risk',
                            'body': 'We buy your product outright and carry it on our books. '
                                    'That means we also carry the credit risk across thousands '
                                    'of small accounts, chase the payments and absorb the slow '
                                    'payers. You invoice us, once, against the order we place. '
                                    'Date control sits with us too: we rotate what is on the '
                                    'shelf, pull short-dated stock off the route and settle '
                                    'returns with the store. The awkward parts of selling in '
                                    'small quantities stay our problem, not yours.'}],
        'bullets': [   {   'title': 'Shared drop cost',
                           'text': 'The call is funded by a full mixed basket, not by your two '
                                   'cases. Small volumes reach the door at the same cost per '
                                   'drop as large ones.'},
                       {   'title': 'Cases broken down',
                           'text': 'We split full outers into what a small shop can sell before '
                                   'it dates, and consolidate the remainder across the rest of '
                                   'the route.'},
                       {   'title': 'Weekly call cycle',
                           'text': 'Fixed routes, fixed days. Our people are in these stores '
                                   'every week to take the order, check the facing and put the '
                                   'stock out.'}],
        'faq': [   {   'q': 'We have only two lines. Is that enough for the convenience channel?',
                       'a': 'Yes. A short range is only uneconomic when it has to fund its own '
                            'route. On ours it travels with everything else on the van, so the '
                            'cost per door is the same for two lines as for two hundred. What '
                            'matters is whether each line can hold a facing and turn over in a '
                            'few days. If it can, it belongs on the route.'},
                   {   'q': 'What does it cost us to put product on your convenience route?',
                       'a': 'Nothing. We buy your stock, hold it in our own warehouses and sell '
                            'it on. There is no listing fee, no storage charge and no delivery '
                            'cost. We earn from the margin between what we pay you and what we '
                            'sell at, so we only make money once the product leaves the shelf. '
                            'Your side of it is production and supply.'},
                   {   'q': 'Will our packaging need to change for small stores?',
                       'a': 'Sometimes the outer case does. A shop with no stockroom cannot take '
                            'a twenty-four count of a large format, and a case that will not fit '
                            'under the counter gets refused. We will tell you what the shelf '
                            'takes before you commit to a print run — pack size, outer count, '
                            'whether the channel expects a price-marked pack — and you decide. '
                            'Nothing is mandatory.'}]},
    {   'slug': 'sector-private-label',
        'kicker': 'Private label',
        'title': "Private label: from a chain's brief to a filled shelf",
        'lede': 'Chains ask us for own-brand lines they can build a range around. We match the '
                'brief to a producer, agree the specification, and buy the run ourselves — so '
                '**the accountability sits with us**.',
        'sections': [   {   'heading': 'How an own-brand line starts',
                            'body': 'A category manager has a gap on the shelf: a price point '
                                    'below the branded lines, a pack size nobody else offers, or '
                                    'a claim the chain wants to own. That becomes a brief. We '
                                    'see those briefs because we are in front of the same buyers '
                                    'every week with the brands we already carry. The first job '
                                    'is translating the brief into something a factory can work '
                                    'from — annual volume, pack format, shelf life, '
                                    'declarations, and the date the first delivery has to land.'},
                        {   'heading': 'Matching the brief to a producer',
                            'body': 'GDH does not own factories. What we hold is a working '
                                    'picture of who can actually make the thing: line speed, '
                                    'certifications, minimum runs, and whether a producer '
                                    'genuinely wants own-brand volume rather than treating it as '
                                    'filler. We shortlist on that first and on cost second. '
                                    "Samples go to the chain's technical team, a trial run "
                                    'follows, and the producer is held to a written '
                                    'specification rather than to a conversation. If a '
                                    'shortlisted factory cannot meet the volume cleanly, we say '
                                    'so before anyone commits artwork or a launch date.'},
                        {   'heading': 'Specification, artwork and packaging',
                            'body': 'Private label lives or dies on detail. Ingredient or '
                                    'material specification, declarations and warnings, '
                                    'barcodes, case configuration, batch and date coding, and '
                                    "artwork built to the chain's own brand guidelines. We keep "
                                    'the approved specification and the signed-off print files, '
                                    'so the second run matches the first and a change of '
                                    'producer does not quietly change the product. Where '
                                    'labelling rules differ between markets, the pack is drawn '
                                    'up to the strictest version rather than reworked after the '
                                    'first order.'},
                        {   'heading': 'One supplier, one accountability line',
                            'body': 'The chain raises a single purchase order, to us. We buy the '
                                    'production run, hold it in our own warehouses and deliver '
                                    "into depots and stores against the chain's orders. If a run "
                                    'slips, a batch falls outside specification or a store runs '
                                    "short, that is ours to fix — we do not pass a factory's "
                                    'problem along to a buyer. Carrying the stock is what makes '
                                    'that promise real: the inventory sits on our books, so the '
                                    'risk of a long run or a slow start is ours.'},
                        {   'heading': 'Repeat runs, reviews and dental own-brand',
                            'body': 'Once a line is listed, sell-out data from the chain turns '
                                    'into call-offs for the producer, so the factory builds to a '
                                    'forecast instead of guessing at a reorder. At range review '
                                    'we come back with what the numbers support: hold the line, '
                                    'change the pack, move the price point, or stop. The dental '
                                    'channel works the same way. Practice groups and '
                                    'laboratories want consumables under their own name, and the '
                                    'brief, the specification and the accountability follow the '
                                    'same route.'}],
        'bullets': [   {   'title': 'Briefs we see early',
                           'text': 'We call on the same category buyers every week. Own-brand '
                                   'briefs reach us while the volume, pack format and launch '
                                   'date are still being decided.'},
                       {   'title': 'Producers chosen on capacity',
                           'text': 'Shortlists built on line speed, certification and real '
                                   'appetite for own-brand runs, then on cost. We say so when a '
                                   'factory cannot hold the specification.'},
                       {   'title': 'The stock risk is ours',
                           'text': 'We buy the production run and hold it in our own warehouses. '
                                   'The chain raises one purchase order, to us, and short stores '
                                   'are ours to sort out.'}],
        'faq': [   {   'q': 'We manufacture for other brands. How do we get in front of these '
                            'briefs?',
                       'a': 'Tell us what your lines run, at what volume, to which '
                            'certifications, and where you have spare capacity. When a brief '
                            'fits, we put you on the shortlist and bring the specification to '
                            'you. We buy the run ourselves, so you are selling to one customer '
                            "working to one forecast, rather than chasing a chain's procurement "
                            'team on your own.'},
                   {   'q': 'Who owns the brand, the specification and the artwork?',
                       'a': 'The chain owns the brand and the artwork. The specification is '
                            "agreed between the chain's technical team, the producer and us, and "
                            'we hold the approved master and the signed-off print files. A '
                            'repeat run is then made to the same document as the first one, and '
                            'a change of producer has to meet the existing specification rather '
                            'than set a new one.'},
                   {   'q': 'What does private label cost our side?',
                       'a': 'Nothing. We do not charge producers or brands for listings, storage '
                            'or delivery, and we do not issue quotes. We buy the production run '
                            'and earn from the distribution margin on what we sell into the '
                            'chains. Your only cost is making the product to specification and '
                            'to the call-offs we give you.'}]},
    {   'slug': 'sector-dental',
        'kicker': 'Dental',
        'title': 'Dental products, into the practices that use them',
        'lede': 'Dentistry does not buy like retail. It buys in small, repeat quantities, on '
                'clinical trust, one surgery at a time. We buy your range, hold it, and put it '
                'in front of **practices, clinics and laboratories** every week.',
        'sections': [   {   'heading': 'How dentistry buys',
                            'body': 'Retail buying is centralised. One buyer in one office '
                                    'decides for hundreds of stores, and a listing moves volume '
                                    'the day it goes live. Dentistry is the opposite. The '
                                    'decision sits with the principal dentist, the practice '
                                    'manager or the lead technician, and it is made one surgery '
                                    'at a time. Orders are small, frequent and topped up as the '
                                    'diary fills. What moves a decision is handling the '
                                    'material, trusting the result and knowing the box will '
                                    "arrive before Monday's list — not a promotion."},
                        {   'heading': 'What we carry',
                            'body': 'Three groups of product, each with its own handling. '
                                    'Restorative and laboratory materials: composites, cements, '
                                    'impression and model materials, endodontic consumables. '
                                    'Everyday consumables: gloves, barriers, suction, burs, '
                                    'sterilisation pouches and surgery disposables. Equipment: '
                                    'handpieces, curing lights, scalers and the small capital '
                                    'items a practice replaces over time. Materials carry lot '
                                    'numbers and expiry dates, some need controlled temperature, '
                                    'and a few are ordered only when a case is booked. We stock '
                                    'to that reality rather than to one convenient pallet '
                                    'profile.'},
                        {   'heading': 'Where the product goes',
                            'body': 'Four kinds of customer, and they order differently. '
                                    'Independent practices buy little and often, usually by '
                                    'phone or standing order. Multi-site dental groups '
                                    'centralise part of their buying and leave the rest to each '
                                    'surgery. Laboratories order by technique and by case: '
                                    'larger quantities of fewer lines. Depots and resellers buy '
                                    'to stock and expect full cases and clean paperwork. We hold '
                                    'one inventory and serve all four from it, so a brand does '
                                    'not need a separate plan for each route.'},
                        {   'heading': 'Lots, expiry and withdrawal',
                            'body': 'Dental stock is dated stock. Every inbound delivery is '
                                    'booked in by lot and expiry, picked first-expiry-first-out, '
                                    'and traceable to the practice that received it. Short-dated '
                                    'lines are flagged while there is still time to move them, '
                                    'not written off at the end of the year. If a lot has to be '
                                    'withdrawn, we can name every customer holding it and '
                                    'collect it. The same records answer the questions a quality '
                                    'audit asks — the part a brand usually cannot see from the '
                                    'factory gate.'},
                        {   'heading': 'How a range gets adopted',
                            'body': 'A dentist adopts a material when someone puts it in their '
                                    'hand. Our people are in practices, clinics and laboratories '
                                    'every week, so a new range travels with an order that was '
                                    'already going there: a trial box, a chairside '
                                    'demonstration, a technique sheet, a session with the nurse '
                                    'who sets the tray. Then we tell you what we heard — which '
                                    'lines reorder, which ones sit, and what practices asked for '
                                    'that you do not yet make. That is worth more than a '
                                    'forecast built in an office.'}],
        'bullets': [   {   'title': 'In the surgery every week',
                           'text': 'Our representatives already call on practices, clinics and '
                                   'laboratories. A new range goes out with an order that was '
                                   'heading there anyway.'},
                       {   'title': 'Lot and expiry control',
                           'text': 'Every line booked in by lot and expiry, picked '
                                   'first-expiry-first-out, and traceable to the practice '
                                   'holding it — including when a lot has to come back.'},
                       {   'title': 'Nothing to invoice',
                           'text': 'No listing fee, no storage charge, no delivery cost. We buy '
                                   'your stock and earn from distribution margin. Adding a '
                                   'dental range costs your brand nothing.'}],
        'faq': [   {   'q': "Why can't we treat dental like another retail category?",
                       'a': 'Because there is no central listing to win. A retail chain decides '
                            'once for every store; dentistry decides surgery by surgery, and the '
                            'person deciding is usually the clinician who will use the material. '
                            'That means many small accounts, frequent small orders, and adoption '
                            'built on handling the product rather than on a promotional '
                            'calendar. The work sits in the calling and the restocking, which is '
                            'the part we already do.'},
                   {   'q': 'Do you handle equipment as well as consumables?',
                       'a': 'Yes, but differently. Consumables move on standing orders, where '
                            'availability decides everything. Equipment moves on demonstration, '
                            'a longer decision and a delivery arranged around the practice '
                            'diary. We stock the small capital items a surgery replaces over '
                            'time, and we work through depots and resellers where a larger '
                            'installation is better served by their own engineers than by ours.'},
                   {   'q': 'What does it cost us to put a dental range with GDH?',
                       'a': 'Nothing. We buy the stock from you, hold it in our own warehouses '
                            'and sell it on to practices, clinics, laboratories and depots. '
                            'There is no listing fee, no storage charge and no delivery cost, '
                            'and you will never receive an invoice from us. We earn from the '
                            'margin between what we pay you and what the channel pays us, which '
                            'only works if your range keeps reordering.'}]},
    {   'slug': 'sector-dental-practices',
        'kicker': 'Practices & clinics',
        'title': 'Getting your range into dental practices and clinics',
        'lede': 'Practices order small, order often, and order to a clinical specification. We '
                'hold your range in stock, call on practices, clinics and laboratories every '
                'week, and deliver to the surgery door. It costs your brand **nothing**.',
        'sections': [   {   'heading': 'How a practice actually orders',
                            'body': 'A dental practice does not order like a store. It orders a '
                                    'box of gloves, two packs of composite in one shade, a '
                                    'handful of burs — and then it orders again next week. The '
                                    'order is usually placed between patients, for something '
                                    "needed before the next day's list. We hold your range "
                                    'broken down to that scale, so a surgery can buy the '
                                    'quantity it will use rather than a carton it has nowhere to '
                                    'put.'},
                        {   'heading': 'The practitioner is the decision maker',
                            'body': 'There is no category buyer in a practice. The person who '
                                    'chooses the material is normally the person using it: the '
                                    'principal, an associate, or the practice manager acting on '
                                    'what the clinicians asked for. That decision is clinical '
                                    'before it is commercial — handling, setting time, shade, '
                                    'fit with the kit already in the surgery. Our people talk to '
                                    'that person directly, in the practice, and put your product '
                                    'in front of them with the detail a clinician asks for.'},
                        {   'heading': 'Trust is built by the weekly delivery',
                            'body': 'In this channel, trust comes from turning up. We run fixed '
                                    'weekly routes, so practices, clinics and laboratories see '
                                    'the same faces on the same day and learn that what they '
                                    'order arrives. That reliability is what makes a '
                                    'practitioner willing to move a consumable across to a new '
                                    'brand: they know they will not be left mid-week without it. '
                                    'It also earns your range a regular slot in a conversation '
                                    'that would otherwise never take place.'},
                        {   'heading': 'What we carry and how we hold it',
                            'body': 'Materials, consumables and small equipment: restoratives '
                                    'and cements, impression and endodontic lines, instruments, '
                                    'gloves and surgery disposables. We buy the stock from you, '
                                    'pay for it, and hold it in our own warehouse. From there we '
                                    'pick by the single pack, record batch numbers and expiry '
                                    'dates, move short-dated stock first, and keep every lot '
                                    'traceable from our racking to the practice that signed for '
                                    'it.'},
                        {   'heading': 'What it costs your brand',
                            'body': 'Nothing. We are not a service you hire. We buy your stock, '
                                    'take ownership of it, and earn from the margin when we sell '
                                    'it on to practices. There is no listing fee, no storage '
                                    'charge, no delivery cost and nothing to approve. You are '
                                    'paid for the goods you sell us. We carry the warehouse, the '
                                    'vans, the sales calls and the credit risk across several '
                                    'thousand practices.'}],
        'bullets': [   {   'title': 'Picked by the pack',
                           'text': 'We break your case packs down to surgery quantities, so a '
                                   'practice can order the two boxes it will use instead of a '
                                   'carton it has nowhere to store.'},
                       {   'title': 'Same route, same week',
                           'text': 'Fixed weekly calls on practices, clinics and laboratories. '
                                   'Your range gets asked after, restocked and replaced before a '
                                   'surgery runs out of it.'},
                       {   'title': 'Batch and expiry controlled',
                           'text': 'Every lot is recorded from our racking to the practice that '
                                   'received it, so short-dated stock moves first and anything '
                                   'recalled can be traced.'}],
        'faq': [   {   'q': 'Who do you actually deliver to?',
                       'a': 'Independent practices and group practices, specialist and private '
                            'clinics, dental laboratories, and the dental depots that supply '
                            'smaller surgeries. They already sit on our delivery routes, and '
                            'that is the point: we are calling on them weekly for other lines, '
                            'so adding your range means adding product to a van and a '
                            'conversation that already exist.'},
                   {   'q': 'Our products need explaining chairside. Can your team do that?',
                       'a': 'Yes. We brief our people on your range before it goes on the van, '
                            'carry your technique guides and sample kits, and arrange chairside '
                            'demonstrations with your own clinical trainer where that is what '
                            'wins the practice. We will not pretend to be your clinical '
                            'educator, but we will get your trainer in front of the right '
                            'practitioners and follow up for the order.'},
                   {   'q': 'What does this cost us?',
                       'a': 'Nothing. There is no fee of any kind. We buy stock from you on '
                            'trade terms, hold it at our own expense, and make our money on the '
                            'distribution margin. No charge for warehouse space, no charge per '
                            'delivery, no charge for the calls into practices, and nothing for '
                            'you to sign off. If a line sells slowly, that stock sits on our '
                            'books, not yours.'}]},
    {   'slug': 'sector-dental-laboratories',
        'kicker': 'Laboratories',
        'title': 'Dental laboratories: your materials on the bench',
        'lede': 'Laboratories buy on lead time and traceability, not on brochures. We hold your '
                'materials, alloys and consumables in our own stock and deliver them to the '
                'benches that use them — **at no cost to your brand**.',
        'sections': [   {   'heading': 'What a laboratory actually orders',
                            'body': "A laboratory's order list is long and oddly shaped. "
                                    'Zirconia discs and blocks in several shades, PMMA and wax '
                                    'for try-ins, investment and model stone by the sack, '
                                    'separating agents, polishing wheels, burs, articulators, '
                                    'and alloys by the gram. Most of it is repeat consumption in '
                                    'small quantities, ordered when a case is already on the '
                                    'bench. That profile is why laboratories buy badly from a '
                                    'distant supplier: the value per line is small and the '
                                    'urgency is high. We carry the whole range, so a lab fills '
                                    'its list in one order.'},
                        {   'heading': 'Lead time is the whole argument',
                            'body': 'A laboratory works to a fitting date it did not choose. If '
                                    'a disc in the right shade is not on the shelf, the case '
                                    'slips and the dentist hears about it. We size stock cover '
                                    'per line against what the laboratories we serve actually '
                                    'consume, not against a forecast. Orders placed before the '
                                    'daily cut-off leave on our own rounds. Where a line is '
                                    'slow-moving but critical — an uncommon shade, a specific '
                                    'alloy weight — we still hold a floor quantity, because that '
                                    'is the order that decides whether a lab keeps buying your '
                                    'brand.'},
                        {   'heading': 'Alloys and the high-value lines',
                            'body': 'Alloys are ordered by weight, kept under control and '
                                    'counted carefully. We hold precious and non-precious alloys '
                                    'in secured stock, book them in by weight and lot, and send '
                                    'the certificate with the delivery. Part-ingots and small '
                                    'weights are handled rather than refused, because that is '
                                    'how laboratories actually work. The same discipline applies '
                                    'to CAD/CAM blanks: they arrive in sealed packs with shade '
                                    'and batch printed on them, and they reach the bench with '
                                    'that marking intact. Nothing is decanted, relabelled or '
                                    'broken out of its validated pack.'},
                        {   'heading': 'Batch traceability, kept rather than promised',
                            'body': 'A laboratory has to be able to say which lot of which '
                                    'material went into a device it made, and to keep that '
                                    'record for years. If our paperwork is vague, the lab has to '
                                    'write to you instead. So we record lot numbers at goods-in, '
                                    'pick first-expiry-first, and print lot and expiry on the '
                                    'delivery note that stays with the order. If a line has to '
                                    'be pulled, we can list every laboratory and depot that '
                                    'received that batch and recover it, without waiting on an '
                                    'audit.'},
                        {   'heading': 'What we need from your side',
                            'body': 'Supply we can plan against, and documents that travel with '
                                    'the goods: safety data sheets, declarations of conformity, '
                                    'instructions for use in the language the laboratory works '
                                    'in, and shelf life and storage conditions per line. Tell us '
                                    'the pack formats you can produce and we will tell you which '
                                    'ones move on a bench. From there the stock is ours. We buy '
                                    'it, hold it, sell it and look after it in the laboratory, '
                                    'and you never see an invoice from us for listing, storage '
                                    'or delivery.'}],
        'bullets': [   {   'title': 'Held, not ordered in',
                           'text': 'Your discs, alloys and consumables sit in our warehouse, '
                                   'bought and paid for. A laboratory ordering today is served '
                                   'from stock, not from your next production run.'},
                       {   'title': 'Lot numbers end to end',
                           'text': 'Every delivery note carries lot and expiry. From goods-in to '
                                   'bench we can say which batch went where, and pull a line '
                                   'back the same week if you ask us to.'},
                       {   'title': 'Nothing billed to your brand',
                           'text': 'No listing fee, no storage charge, no delivery cost and '
                                   'nothing to sign up for. We buy the stock from you and earn '
                                   'from distribution margin.'}],
        'faq': [   {   'q': 'Do you supply laboratories directly, or through dental depots?',
                       'a': 'Both. We deliver to laboratories on our own rounds, in the week '
                            'they order, and we also supply the dental depots that resell to '
                            'smaller benches. Which route a laboratory prefers is its choice, '
                            'not ours. Your line sits in the same stock either way, and both '
                            'routes report back to us with the same lot records, so traceability '
                            'does not change with the channel.'},
                   {   'q': 'Our materials have a shelf life. How is that handled?',
                       'a': 'We hold each line in the conditions it specifies and pick '
                            'first-expiry-first, so the oldest usable batch leaves first. Stock '
                            'cover is set against real consumption, which keeps the holding '
                            'small enough that material does not age on our shelves. If a batch '
                            'does become short-dated, we tell you and agree what happens to it. '
                            'We do not quietly push it into laboratories.'},
                   {   'q': 'What does it cost us to have you stock our range?',
                       'a': 'Nothing. We buy your product outright and take ownership of the '
                            'stock, so there is no listing fee, no storage charge and nothing '
                            'billed for delivery into laboratories. We earn from the margin '
                            'between what we pay you and what the laboratory pays us. That means '
                            'we only make money when the material is actually used and '
                            'reordered, which is the outcome you want too.'}]},
    {   'slug': 'distribution',
        'kicker': 'Distribution',
        'title': 'Distribution that takes your product from factory to shelf',
        'lede': "We buy your stock, hold it in our own warehouses and sell it into the country's "
                'largest chains, independent retailers, pharmacies and dental practices. **You '
                'never see an invoice from us.** We earn from the distribution margin.',
        'sections': [   {   'heading': 'The listings are already in place',
                            'body': 'Listings come first. GDH holds supplier accounts with the '
                                    'grocery, pharmacy and specialist chains, and our commercial '
                                    'team sits in front of those category buyers on a regular '
                                    'cycle. Your range is presented inside an account that '
                                    'already exists, with trading terms, barcodes and product '
                                    'data handled the way each buyer expects. We build the case '
                                    'ourselves: the gap your product fills in the category, the '
                                    'shelf it belongs on, the volume we are prepared to commit '
                                    "to. You do not chase meetings or learn a new buyer's "
                                    'paperwork.'},
                        {   'heading': 'We buy the stock and carry it',
                            'body': 'Your product leaves the factory against a purchase order '
                                    'from GDH, and from that moment the stock is ours. We pay '
                                    'for it, hold it in our warehouses and carry the working '
                                    'capital, the forecast risk and the stockholding. You '
                                    'produce to an agreed volume and invoice us on normal terms. '
                                    'There is no consignment arrangement to administer and no '
                                    'storage bill coming back to you. Our buying team '
                                    'replenishes against real demand, so what you receive is a '
                                    'production plan you can resource.'},
                        {   'heading': 'Nationwide delivery on a fixed rhythm',
                            'body': 'From our warehouses we deliver to every store, pharmacy, '
                                    'practice and depot on the account. Some chains take full '
                                    'pallets into their own distribution centres; others are '
                                    'served store by store on a weekly round. Dental practices, '
                                    'clinics and laboratories are called on directly, in the '
                                    'same vehicles that already cover that area. Because we '
                                    'control both the stock and the rounds, an empty shelf can '
                                    'be filled on the next run instead of waiting for a separate '
                                    'supplier to be scheduled in.'},
                        {   'heading': 'Shelf execution, store by store',
                            'body': 'A listing is not the same as being on sale. Our field team '
                                    'works the stores: facings checked and counted, stock '
                                    'brought out of the back room, planograms respected, '
                                    'short-dated units pulled, agreed displays built and sited '
                                    'where they were promised. Where a chain permits it, we '
                                    "place the store's order ourselves. When a store quietly "
                                    'stops ordering, we see it and go in. This is the part most '
                                    'brands cannot do at national scale, and it decides whether '
                                    'a product sells or drifts towards delisting.'},
                        {   'heading': 'Sell-out reporting and returns',
                            'body': 'You see what actually left the shelf. We report sell-out by '
                                    'chain, by region and by line, next to our own stock '
                                    'position and the orders we have placed with you. That gives '
                                    'you something firm to produce against, and early warning on '
                                    'lines that need a price, a pack or a promotion rather than '
                                    'more volume. Returns, damages and short-dated stock are '
                                    'handled by us under the terms of each account and credited '
                                    'through our books, so your brand stays out of store-level '
                                    'disputes.'}],
        'bullets': [   {   'title': 'We buy, you invoice us',
                           'text': 'Your product moves against a GDH purchase order. We pay for '
                                   'it, hold it and carry the risk. You produce to the forecast '
                                   'and invoice us on normal terms.'},
                       {   'title': 'One partner, every channel',
                           'text': 'Grocery and pharmacy chains, independent retailers, dental '
                                   'practices, clinics and laboratories — reached through '
                                   'accounts and delivery rounds that already exist.'},
                       {   'title': 'Nothing for you to pay',
                           'text': 'No listing fee, no storage charge, no delivery cost, nothing '
                                   'to approve before we start. GDH earns from the distribution '
                                   'margin and nowhere else.'}],
        'faq': [   {   'q': 'What does it cost our brand to work with GDH?',
                       'a': 'Nothing. We do not invoice the brands we carry. There is no listing '
                            'fee, no storage charge, no delivery cost and no charge for the work '
                            'our field team does in store. We buy your product at an agreed '
                            'price and make our money on the margin between what we pay you and '
                            'what we sell it for. Our interest and yours are identical: more '
                            'units off the shelf.'},
                   {   'q': 'Do we still have to pitch the chains ourselves?',
                       'a': 'No. We present your range to the buyers we already see, inside '
                            'supplier accounts we already hold. You give us the product facts, '
                            'the samples and the data; we build the commercial case and '
                            'negotiate the listing. You are welcome in the room when a buyer '
                            'wants to hear from the maker, but the account, the terms and the '
                            'follow-up stay with us.'},
                   {   'q': 'What happens to stock that does not sell?',
                       'a': 'We own it, so it is our problem first. Slow lines appear in the '
                            'sell-out report long before they become dead stock, and we act on '
                            'them: a promotion, a narrower store list, a pack change, or a frank '
                            'price conversation with you. Returns, damages and short-dated units '
                            "are handled by us under each account's terms. You are never asked "
                            'to buy stock back unless that was agreed in advance.'}]},
    {   'slug': 'service-chain-listings',
        'kicker': 'Chain listings',
        'title': 'Getting your range listed in the major chains',
        'lede': 'Chains open their categories on a fixed calendar. We prepare the submission, '
                'take the buyer meeting, agree the terms and **buy the opening order ourselves** '
                '— so your range reaches the shelf without your brand paying for any of it.',
        'sections': [   {   'heading': 'The review calendar sets the clock',
                            'body': 'Chains do not add lines whenever they feel like it. Each '
                                    'category is reviewed on a set date, the planogram is '
                                    'redrawn, and what is agreed in that meeting holds the shelf '
                                    'until the next review. So we work backwards from those '
                                    'dates. We know which categories open when, because we are '
                                    'in front of those buyers every week, and that tells us '
                                    'months ahead whether your range goes into the coming review '
                                    'or the one after it, and what has to be finished before '
                                    'then.'},
                        {   'heading': 'Building the category case',
                            'body': 'A buyer is not buying your product. They are buying a '
                                    'change to their category, and the submission has to answer '
                                    'it in those terms: which shelf the line sits on, which '
                                    'existing line it stands beside, what it brings that the '
                                    'range does not already have, what it is likely to replace. '
                                    'We write that case with you, using what we see across the '
                                    'chains week to week — which sizes move, which price points '
                                    'sit empty, which formats shoppers reach for first. Samples, '
                                    'pack shots and costings go in with it.'},
                        {   'heading': 'In the buyer meeting',
                            'body': 'Our commercial team takes the meeting. We are already an '
                                    'approved supplier with a trading agreement in place, so the '
                                    'conversation starts at the range rather than at supplier '
                                    'onboarding. The buyer asks what buyers always ask: can you '
                                    'supply it every week, what happens when it goes on '
                                    'promotion, who fixes it when a store runs out. We answer '
                                    'that from our own warehouse and our own delivery rounds. '
                                    'You come in where the product itself needs explaining — '
                                    'formulation, factory, capacity, what is coming next.'},
                        {   'heading': 'Pricing and promotional terms',
                            'body': 'Three numbers get agreed. What the chain pays us, what the '
                                    'product sits at on shelf, and what it drops to on '
                                    'promotion. We build those back from your factory cost and '
                                    'the margin the category expects, and we tell you plainly '
                                    'when a cost price will not clear the hurdle. The '
                                    'promotional calendar is settled in the same conversation: '
                                    'how many weeks, at what depth, in which trading periods. '
                                    'You see the terms before we commit to them, and you are '
                                    'invoiced for none of it. We earn on the stock we buy.'},
                        {   'heading': 'Barcodes, master data and the opening order',
                            'body': 'Then the unglamorous part, which is where most listings '
                                    'stall. Every line needs a barcode at unit and case level, a '
                                    'case configuration, true weights and dimensions, pallet '
                                    'patterns, ingredient and allergen text, shelf-life rules '
                                    "and photography at the resolution the retailer's systems "
                                    "will accept. We set all of it up in each chain's supplier "
                                    'portal and keep it correct as packs change. Once the data '
                                    'clears, the chain raises its first order on GDH and we buy '
                                    'the opening stock from you outright. Your side of it is one '
                                    'delivery into our warehouse.'}],
        'bullets': [   {   'title': 'Already an approved supplier',
                           'text': 'Trading agreements, supplier codes and portal access are in '
                                   'place before your range is ever discussed, so the only open '
                                   'question in the meeting is the product.'},
                       {   'title': 'No invoice, ever',
                           'text': 'We do not charge for submission work, buyer meetings or '
                                   'master data setup. GDH earns from the margin on the stock it '
                                   'buys from you.'},
                       {   'title': 'We buy the opening order',
                           'text': 'The first order is placed on GDH, not on you. We take the '
                                   'stock position and carry the risk; you produce to the '
                                   'forecast we give you.'}],
        'faq': [   {   'q': 'How long does getting listed take?',
                       'a': "That is set by the chain's review calendar, not by us. Each "
                            'category reopens on a fixed date, and a range either makes that '
                            'review or waits for the next one. Once we have agreed which '
                            'categories you belong in, we can tell you the dates we are aiming '
                            'at and exactly what has to be finished — samples, costings, '
                            'barcodes, images, data — before each one closes.'},
                   {   'q': 'What does the listing work cost our brand?',
                       'a': 'Nothing. There is no listing fee, no submission fee, no charge for '
                            'the data and portal work, and no charge for the meetings. GDH buys '
                            'your stock and sells it on into the chains, and our income is the '
                            'margin between those two prices. If a range does not get listed, '
                            'you have paid nothing for the attempt.'},
                   {   'q': 'What if a buyer turns the range down?',
                       'a': 'It happens, and the reason is usually worth having. Buyers decline '
                            'because the category has no space, the price architecture does not '
                            'work, or the pack is wrong for their shelf. We bring that back to '
                            'you in plain terms, change what can be changed, and then either '
                            'resubmit at the next review or go at the same category through '
                            'another chain, independent retailers or pharmacy, where the gap may '
                            'be real.'}]},
    {   'slug': 'service-stock-and-delivery',
        'kicker': 'Stock & delivery',
        'title': 'We buy the stock and run every route to the shelf',
        'lede': 'Your product arrives once, at our goods-in bay. After that it is **our stock**, '
                'in our warehouses, on our routes — into chain depots, store back doors, '
                'pharmacies and dental practices, week after week.',
        'sections': [   {   'heading': 'One delivery in, the whole country out',
                            'body': 'You make one delivery, into our goods-in bay. We raise the '
                                    'purchase order, take the stock onto our books and pay for '
                                    'it. From that point the product is ours. We hold it, we '
                                    'insure it, we carry the cost of it sitting on a rack, and '
                                    'we decide how to spread it across the chains and practices '
                                    'we supply. You do not book depot windows, chase labelling '
                                    'standards or pay for storage. Nothing described on this '
                                    'page is invoiced back to you. We earn on the margin between '
                                    'what we buy at and what we sell at.'},
                        {   'heading': 'Stored the way the line needs',
                            'body': 'Lines are stored to suit the product, not the building. '
                                    'Ambient racking for dry grocery, household and personal '
                                    'care. Chilled and temperature-controlled rooms for the '
                                    'lines that require them. Lockable, controlled areas for '
                                    'dental materials and anything with a restricted shelf life. '
                                    'Every pallet carries its batch or lot number and its expiry '
                                    'date, and we pick first-expiry-first so the oldest stock '
                                    'leaves first. Returns, damages and short-dated units are '
                                    'held apart from sellable stock until they are cleared, '
                                    'credited or destroyed.'},
                        {   'heading': 'Picked in the format the receiver wants',
                            'body': 'Different receivers want the product in different shapes, '
                                    'and we build to each one. Full pallets for the chain depots '
                                    'that accept nothing else. Layer and case picks for smaller '
                                    'depots and cash-and-carry. Mixed pallets built store by '
                                    'store where a chain cross-docks. Shelf-ready trays and '
                                    'display units where the buyer has agreed one. Single boxes '
                                    'for independent shops, pharmacies and dental practices, '
                                    'which rarely order a full case of anything. Pack format is '
                                    'agreed with you before the first order, because it decides '
                                    'how cleanly the product lands on the shelf.'},
                        {   'heading': 'Our own routes, on a fixed rhythm',
                            'body': 'We run our own routes to a weekly pattern, so every account '
                                    'knows which day it sees us. Chain depots are delivered into '
                                    'their booked windows, with the paperwork and labelling each '
                                    'one insists on. Independent stores, pharmacies and dental '
                                    'practices sit on a called route: the same driver, the same '
                                    'day, a top-up on every visit. Frequency is set per account '
                                    'rather than per brand. A fast line in a convenience chain '
                                    'may go twice a week, while a dental consumable may go '
                                    'monthly.'},
                        {   'heading': 'Peaks are built before they arrive',
                            'body': 'A peak is a stock problem before it is a delivery problem. '
                                    'Christmas, promotional weeks, back-to-school and the '
                                    'ordering spike before practice holidays all need product '
                                    'made early and held. We agree the volume with you months '
                                    'out, buy it ahead and warehouse it so the chains can draw '
                                    'it down in one hit. Promotional pallets and display units '
                                    'are made up in advance and staged, routes are doubled for '
                                    'the week, and extra pick and driver shifts are added. If a '
                                    'peak outruns the plan, you hear it from us while there is '
                                    'still production time.'}],
        'bullets': [   {   'title': 'The stock is ours',
                           'text': 'We buy it, pay for it and carry it. No listing fee, no '
                                   'storage charge, no delivery cost — nothing here comes back '
                                   'to you as an invoice.'},
                       {   'title': 'Stored as the line needs',
                           'text': 'Ambient, chilled and controlled storage. Batch and expiry on '
                                   'every pallet, first-expiry-first picking, and short-dated '
                                   'units held apart from sellable stock.'},
                       {   'title': 'Picked for each receiver',
                           'text': 'Full pallets, layer and case picks, mixed store pallets, '
                                   'shelf-ready units and single boxes — out on our own weekly '
                                   'routes to depots, shops and practices.'}],
        'faq': [   {   'q': 'Who owns the stock once it is in your warehouse?',
                       'a': 'We do. We buy the product from you on a purchase order, and it '
                            'comes onto our books when we accept it at goods-in. The working '
                            'capital, the insurance, the slow-moving risk and the storage cost '
                            'are ours from that moment. You are paid for what we buy, on agreed '
                            'terms, and you are never invoiced for holding or moving it '
                            'afterwards.'},
                   {   'q': 'Can you handle chilled lines and dental materials properly?',
                       'a': 'Yes. We hold ambient, chilled and temperature-controlled space, '
                            'plus lockable controlled areas for dental materials and anything '
                            'with a short or restricted shelf life. Batch or lot and expiry are '
                            'recorded on receipt and travel with the pallet, picking is '
                            'first-expiry-first, and we can give you the batch history of any '
                            'unit we have delivered.'},
                   {   'q': 'Do we have to deliver to every chain depot ourselves?',
                       'a': 'No. You make one delivery, into our goods-in bay, in the pack '
                            'format we agreed. We break it down and build pallets, cases or '
                            "single boxes to each receiver's rules, then run it out on our own "
                            'routes to depots, stores, pharmacies and practices. Depot booking '
                            'windows, labelling standards and delivery paperwork are our job, '
                            'not yours.'}]},
    {   'slug': 'service-shelf-execution',
        'kicker': 'Shelf execution',
        'title': 'Your product, put on the shelf properly',
        'lede': 'Delivery is only half the job. Our field teams walk the stores we sell into, '
                'put your stock where it belongs, rebuild what the week has pulled apart, and '
                'photograph the result for you. **It costs you nothing.**',
        'sections': [   {   'heading': 'A listing is not a shelf',
                            'body': 'A listing is permission to be on a shelf. It is not a '
                                    'guarantee that your product is on one. Stock sits in back '
                                    'rooms. Facings get taken by whoever restocked last. A '
                                    'two-for-one goes live on Monday and the bay is still set '
                                    'for last month. We buy your stock and we own it until the '
                                    'till rings, so none of that is academic to us. Our field '
                                    'teams call on the stores, pharmacies and practices we sell '
                                    'into, and they fix what they find.'},
                        {   'heading': 'What a call looks like',
                            'body': 'The team member arrives with your planogram, the '
                                    'promotional plan and a scanner. They check the bay against '
                                    'the plan, count what is on display, and bring the rest of '
                                    'your stock out of the back room and onto the shelf. Facings '
                                    'are corrected and blocked by brand rather than scattered. '
                                    'Dates are rotated so older stock sells first. Gaps are '
                                    'ordered there and then. In dental practices there is no '
                                    'bay, but there is a stockroom and a surgery cupboard, and '
                                    'the same call applies to both.'},
                        {   'heading': 'Planogram compliance, in practice',
                            'body': 'Chains agree a planogram centrally and then a hundred '
                                    'stores interpret it. We work to the version the buyer '
                                    'signed, and where a store has drifted we put it back. If '
                                    'the store has a reason for the change, a smaller bay or a '
                                    'fixture replaced, we record it and tell you, because a plan '
                                    'nobody can physically build is worth knowing about. '
                                    'Compliance is only useful if it is reported honestly, so we '
                                    'report both: what we corrected, and what we could not.'},
                        {   'heading': 'Displays and promotions, set on the day',
                            'body': 'Secondary displays do the work a shelf cannot. We assemble '
                                    'units, site them where the store has agreed, and fill them. '
                                    'Where a display has been collapsed, raided for stock or '
                                    'pushed into a corner, we rebuild it. Promotions are set on '
                                    'the morning they start: shelf-edge labels on, price right, '
                                    'stock out, the old mechanic removed. Seasonal builds come '
                                    'down when the season does, so your brand is not left '
                                    'sitting behind an out-of-date header.'},
                        {   'heading': 'Photographs back to you',
                            'body': 'Every call ends with pictures: the bay before, the bay '
                                    'after, the display, the promotional set-up. They are dated '
                                    'and tied to the store. You see your product the way a '
                                    'shopper saw it that morning, in shops you will never stand '
                                    'in. Alongside the photographs you get the plain facts, what '
                                    'was on display, what was in the back room, what had run out '
                                    'and what we ordered. Enough to decide what to change next, '
                                    'and nothing dressed up.'}],
        'bullets': [   {   'title': 'In store, in person',
                           'text': 'Field teams call on the chains, independents, pharmacies and '
                                   'dental practices we already sell into, so your lines are '
                                   'seen by someone whose job is to fix them.'},
                       {   'title': 'Built back to plan',
                           'text': 'Facings corrected, back-room stock brought forward, displays '
                                   'rebuilt and promotions set on the morning they go live '
                                   'rather than the week after.'},
                       {   'title': 'Photographed, not claimed',
                           'text': 'Dated before-and-after pictures by store, with what was on '
                                   'display, what sat in the back room and what we re-ordered on '
                                   'the spot.'}],
        'faq': [   {   'q': 'What does the field work cost us?',
                       'a': 'Nothing. We never invoice the brands we carry. We have bought your '
                            'stock, it is ours until it sells through, and getting it onto the '
                            'shelf is how we earn. There is no field-visit charge, no display '
                            'fee and no reporting package to buy. If a store call improves your '
                            'sell-through, that is the whole point of it.'},
                   {   'q': 'How often will our lines be called on?',
                       'a': 'It depends on the account and how fast the line moves. '
                            'High-turnover lines in large chains are called on frequently; '
                            'slower lines and smaller independents less so, on a cycle agreed '
                            'with you. Promotional weeks and new listings always get a visit at '
                            'launch. We will tell you the cycle for your lines before we agree '
                            'it, rather than leave you guessing.'},
                   {   'q': 'Can we brief the team on how we want the product merchandised?',
                       'a': 'Yes, and we would rather you did. Send us the planogram, the block '
                            'order, the display drawings and the rules you care about: eye-level '
                            'position, facings by variant, which lines sit together. We brief '
                            'the field teams from that. Where a store will not allow something, '
                            'we tell you what we did instead. What we will not do is promise a '
                            'build the fixture cannot take.'}]},
    {   'slug': 'service-sell-out-visibility',
        'kicker': 'Sell-out visibility',
        'title': 'See what actually sold, store by store',
        'lede': 'Sell-in tells you what we bought. Sell-out tells you what shoppers and '
                'practices actually took off the shelf. You get **both**, per chain and per SKU, '
                'with stock cover, proof of delivery and batch data behind every line.',
        'sections': [   {   'heading': 'What you actually see',
                            'body': 'Sell-out per chain and per SKU, by week. Rate of sale for '
                                    'every line in every chain we supply. Stock on hand in our '
                                    'warehouses, orders in picking, deliveries booked for the '
                                    'week, and proof of delivery per store. It sits in one view, '
                                    'and it leaves in whatever form your systems want — a '
                                    'scheduled export mapped to your own SKU codes, or a login '
                                    'for your commercial team. You do not have to ask us for a '
                                    'spreadsheet at month end.'},
                        {   'heading': 'Stock cover, not just stock',
                            'body': 'A number on hand tells you little. What you need is weeks '
                                    'of cover: how long the stock in our warehouses lasts at the '
                                    'rate the chain is currently selling, and the same read on '
                                    "what sits in the chain's own depots. Lines running thin get "
                                    'flagged while there is still time to produce more. Lines '
                                    'building up get flagged too, before they age into a '
                                    'mark-down. The flag comes with the figure it is based on, '
                                    'so you can argue with it.'},
                        {   'heading': 'Proof of delivery, store by store',
                            'body': 'Every drop is signed for at the receiving location — chain '
                                    'distribution centre, store, pharmacy or dental practice — '
                                    'and that record is attached to the line it belongs to. If a '
                                    'chain says a delivery never arrived, or a store insists it '
                                    'was short, the answer is a document rather than an '
                                    'argument. The same record is what lets us settle deductions '
                                    'and claims with the buyer directly, so your commercial team '
                                    'is not pulled into paperwork it never created.'},
                        {   'heading': 'Batch and expiry on every movement',
                            'body': 'Batch, lot and expiry travel with the goods from the moment '
                                    'we receive them to the moment they are signed for in store. '
                                    'Scoping a recall is then a question, not a project: we can '
                                    'say which batch went to which locations, in what quantity, '
                                    'and on what date. Short-dated stock surfaces the same way. '
                                    'It gets rotated forward, pushed into a promotion or moved '
                                    'to a faster channel while it still has value, rather than '
                                    'being discovered as a write-off.'},
                        {   'heading': 'Back into your production plan',
                            'body': 'The same data goes to whoever builds your production plan. '
                                    'We tell you what is selling, where, and at what rate, and '
                                    'what we expect to buy from you over the coming weeks, so '
                                    'your factory is planning against real demand instead of '
                                    "last year's guess. If a line is moving faster than anyone "
                                    'expected, you hear it from us while there is still time to '
                                    'make more. If it is moving slowly, you hear that too, with '
                                    'the stores and chains it is happening in.'}],
        'bullets': [   {   'title': 'Per chain, per SKU',
                           'text': 'Weekly rate of sale for every line in every chain we supply, '
                                   'not a national average that hides which account is working.'},
                       {   'title': 'Cover you can act on',
                           'text': 'Weeks of cover per SKU across our warehouses and the chain '
                                   'depots, with thin lines and slow lines both flagged early.'},
                       {   'title': 'Traceable to the store',
                           'text': 'Batch, lot and expiry on every movement, plus a signed proof '
                                   'of delivery for each location we drop at.'}],
        'faq': [   {   'q': 'Where does the sell-out data come from?',
                       'a': "Three places. The chains' own till and depot reporting, where our "
                            'supply agreement gives us access to it. Our own records of what we '
                            'picked, delivered and had signed for. And what our field people see '
                            'in the stores they visit each week. We clean it, map it to your SKU '
                            'codes and tell you plainly where a chain reports monthly rather '
                            'than weekly.'},
                   {   'q': 'What does the reporting cost us?',
                       'a': 'Nothing. We do not invoice the brands we carry — there is no '
                            'listing fee, no storage charge and no delivery cost coming back to '
                            'you. We buy your stock and we earn from distributing it, so '
                            'reporting is not a service we sell you. It is how we run our own '
                            'business, and you see the same numbers we do.'},
                   {   'q': 'Can it feed our own systems?',
                       'a': 'Yes. Scheduled file exports mapped to your article numbers, a '
                            'direct feed into your planning system, or a login for people who '
                            'just want to look. Tell us the field names you use and we match '
                            'them, rather than handing you a report in our format and leaving '
                            'the mapping to you. Most brands take a weekly export and a monthly '
                            'review on top of it.'}]},
    {   'slug': 'service-returns',
        'kicker': 'Returns & recalls',
        'title': 'Returns and recalls, handled on the way back',
        'lede': 'Every store we deliver to is a store we collect from. Returns ride back on the '
                'same van, get triaged at our hub, and reach you as **one clean credit line** — '
                'not an argument three months later.',
        'sections': [   {   'heading': 'Collected on the round that delivers',
                            'body': 'The van that drops stock at a store also picks up what is '
                                    'coming back. The collection sits on the same run as the '
                                    'delivery, so a store manager hands over damaged units, '
                                    'short-dated lines or a discontinued facing in one movement '
                                    'at the back door. Nothing waits for a separate booking, and '
                                    'nothing sits in a stockroom for weeks turning into a '
                                    'dispute. Returns reach our hub the same day the van closes '
                                    'its round.'},
                        {   'heading': 'Triaged at the hub, line by line',
                            'body': 'Everything that comes back is booked in against the store, '
                                    'the date and a reason code before any decision is taken. '
                                    'Returns are then graded by hand into three outcomes: '
                                    'sellable stock that goes straight back into the pick face, '
                                    'units that need a new outer or a fresh label and are '
                                    'repacked on site, and stock that cannot be sold again. Each '
                                    'outcome is recorded against the original batch, so the '
                                    'decision can be traced long after the pallet has gone.'},
                        {   'heading': 'Write-offs backed by evidence',
                            'body': 'Stock is only written off once there is something to look '
                                    'at. Damaged and expired units are photographed, counted and '
                                    'logged against the store that returned them, with the '
                                    'reason stated plainly — crushed outer, seal failure, '
                                    'expired date code, label damage. You see the same record we '
                                    'do. That keeps write-offs out of the realm of trust, and it '
                                    'shows quickly whether a problem is one store, one delivery '
                                    'round, or something in the packaging itself.'},
                        {   'heading': 'Recalls scoped by batch, not by guesswork',
                            'body': 'Batch and lot numbers are captured when your stock arrives '
                                    'at our warehouse and carried through every pick and every '
                                    'drop. If you need to pull a batch, we can say which stores '
                                    'and practices took it, how many units each one received, '
                                    'and what is still in our own racking. Affected stock is '
                                    'blocked in the system before the first phone call is made, '
                                    'then collected on the normal rounds. Clean batches stay on '
                                    'sale, which keeps the recall narrow.'},
                        {   'heading': 'Credit notes that reconcile first time',
                            'body': 'Every return leaves the hub as structured data: store, '
                                    'date, product code, batch, quantity, reason and outcome. '
                                    'The same record feeds the credit note we raise for the '
                                    'retailer and the report that comes to you, so both sides '
                                    'work from one set of figures. Your finance team is not '
                                    'matching photographs to spreadsheets, and nobody is chasing '
                                    'a deduction nobody recognises. Returns stop being a monthly '
                                    'surprise and become a line you can plan around.'}],
        'bullets': [   {   'title': 'Collected on the round',
                           'text': 'The van that delivers your stock takes the returns back the '
                                   'same day. No separate booking, no third party, nothing left '
                                   'in a stockroom to turn into a dispute.'},
                       {   'title': 'Batch-level recall',
                           'text': 'Lot numbers are captured at goods-in and follow every pick '
                                   'and every drop, so a recall names the exact stores, the '
                                   'exact units, and nothing beyond them.'},
                       {   'title': 'Evidence, then write-off',
                           'text': 'Damage and date expiry are photographed, counted and coded '
                                   'against the store that sent them back before anything is '
                                   'written out of our stock position.'}],
        'faq': [   {   'q': 'What does returns handling cost our brand?',
                       'a': 'Nothing. We buy your stock, so returns from the stores are ours to '
                            'manage, not a service we bill you for. There is no collection '
                            'charge, no handling fee and no storage charge on returned units. '
                            'Our margin comes from distribution, which is exactly why we would '
                            'rather get a sound unit back on the shelf than handle it twice.'},
                   {   'q': 'How quickly can you act on a recall?',
                       'a': 'As soon as you give us the batch, we block it. Stock in our racking '
                            'is frozen in the system straight away, and we can list every store '
                            'and practice that received units from that batch and how many each '
                            'one took. Collections are then added to rounds already going to '
                            'those sites, so nothing waits for a special run. You get a '
                            'reconciled count of what came back and what could not be found.'},
                   {   'q': 'Do returned units go back on sale?',
                       'a': 'Where they safely can, yes. A unit with a scuffed outer and a sound '
                            'product inside is repacked and returned to the pick face; a unit '
                            'with a damaged primary pack, a broken seal or an expired date code '
                            'is not. Dental consumables are judged more strictly, because '
                            'practices will not accept anything with a questionable seal. We '
                            'report the split between resold and written off by product and by '
                            'reason, not as one figure.'}]}]
