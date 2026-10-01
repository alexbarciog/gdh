# -*- coding: utf-8 -*-
"""Textele GDH (generat din copy_gdh.py) — vezi build_gdh.py."""

BRAND = 'GDH'
BRAND_FULL = 'Global Distribution Holdings'
SITE_NAME = 'GDH — Global Distribution Holdings'

# Adresa publică. Un singur loc de schimbat dacă se mută domeniul: de aici se
# construiesc og:url, canonical și adresa absolută a imaginii de partajare
# (WhatsApp/Discord nu acceptă cale relativă la og:image).
SITE_URL = 'https://gdh-group.com'

OG_ALT = ('GDH — Global Distribution Holdings: retail and dental product '
          'distribution into the country\u2019s largest store chains')

TITLES = {
    'index.html': (
        'GDH — Global Distribution Holdings | Retail & Dental Product Distribution',
        'GDH is a distributor of retail and dental products. We buy, stock and place your '
        'products in the country’s largest store chains and dental practices — at no cost to '
        'your brand.'),
    'service.html': (
        'What We Do for Brands | GDH',
        'Chain listings, stock and nationwide delivery, dental distribution and in-store '
        'execution — everything needed to take a product from the factory gate to the shelf.'),
    'case-study.html': (
        'Brands We Distribute | GDH',
        'How food, household, health and dental brands reached national chain listings and '
        'practice shelves through GDH.'),
    'blog.html': (
        'Retail & Dental Distribution Insights | GDH',
        'Practical guidance on chain listings, on-shelf availability, sell-out data and the '
        'dental channel, from the GDH commercial team.'),
    'contact.html': (
        'Partner with GDH | Retail & Dental Distribution',
        'Tell us what you make and which shelves it belongs on. We will come back with the '
        'chains we can reach, the volumes we can move and how fast we can start.'),
}

# noduri de text potrivite exact (dupa strip)
EXACT = [
    ('Frevanta – Webflow HTML Website Template',
     'GDH — Global Distribution Holdings'),
    ('Freight & Logistics Insights Frevanta',
     'Retail & Dental Distribution Insights'),
    ('Why choose Frevanta',
     'Why brands choose GDH'),
    ('1. What services does Frevanta provide?',
     '1. What does GDH distribute?'),
    ('3. Does Frevanta handle international shipments?',
     '3. Which retailers and practices do you supply?'),
    ('4. Can I use only one Frevanta service?',
     '4. What does it cost our brand to work with GDH?'),
    ('“Before Frevanta, we spent hours contacting separate carriers and warehouses for shipment '
     'updates. Now we have one team, one plan, and a much clearer view of every order in '
     'motion.”',
     '“Before GDH we were pitching chain buyers on our own and getting nowhere. GDH already had '
     'the listings and the relationships, so our range was on shelf in one season instead of '
     'three.”'),
    ('“Working with Frevanta completely transformed the way we manage shipments. Everything is '
     'organized in one place, saving our team valuable time while giving us complete confidence '
     'in every delivery.”',
     '“GDH changed how our products reach the market. They buy the stock, handle every chain and '
     'keep the shelves full — our team stopped managing distribution and went back to making '
     'product.”'),
    ('“Frevanta helped us replace manual coordination with a seamless workflow. Our team '
     'communicates better, responds faster, and keeps every shipment on schedule.”',
     '“We have never seen an invoice from GDH. They take the product, sell it into the chains '
     'and look after it in store. Our only job is to keep producing to the forecast they give '
     'us.”'),
    ('“Tracking shipments across different providers was frustrating and time-consuming. Now '
     'everything is organized in one system, helping us save time while improving delivery '
     'accuracy every day.”',
     '“Getting a dental range into practices used to take us years of cold calls. GDH already '
     'delivers to those clinics every week, so our consumables were on their shelves within '
     'months.”'),
    ('Frevanta provides global freight forwarding and logistics across air, ocean, road and '
     'rail, with warehousing, customs clearance and last-mile delivery.',
     'GDH is a distributor of retail and dental products. We buy, stock and place products from '
     'factories and brands into the country’s largest store chains, pharmacies and dental '
     'practices.'),
    ('Frevanta coordinates air, ocean, road, and rail freight with warehousing, customs '
     'clearance, and last-mile delivery — giving your business one team, one plan, and clear '
     'visibility from pickup to destination.',
     'GDH buys your product, stocks it and sells it into the country’s largest store chains and '
     'dental practices — one partner for the whole route to market, at no cost to your brand.'),
    ('© 2026 Frevanta. All Rights Reserved.',
     '© 2026 GDH — Global Distribution Holdings. All rights reserved.'),
    ('Service',
     'What We Do'),
    ('Project',
     'Brands'),
    ('Blog',
     'Insights'),
    ('Start Project',
     'Work With Us'),
    ('Book a Call',
     'Talk to Us'),
    ('View Service',
     'What We Do'),
    ('Explore Air Freight',
     'Explore Retail Distribution'),
    ('Track a Shipment',
     'Submit Your Product'),
    ('View All Project',
     'All Brands We Carry'),
    ('See More Blogs',
     'More Insights'),
    ('View Project',
     'Read the Story'),
    ('Get a Quote',
     'Partner With Us'),
    ('3.5+million satisfied customers',
     '4.200+ stores and practices served weekly'),
    ('Global freight forwarding blind.',
     'Your product, in the country’s biggest chains.'),
    ('Freight changes hands',
     'Your product changes hands'),
    ('A shipment may pass through multiple carriers, terminals, customs authorities, and '
     'distribution centers before it reaches its final destination. Every handoff creates '
     'another opportunity for delays, missing information, and unexpected costs.',
     'Between your production line and the shopper, a product passes through a buyer’s listing, '
     'a warehouse, a delivery van and a shelf. Every handover is another chance for an empty '
     'shelf, a lost facing or a delisting nobody saw coming.'),
    ('Freight changes hands. Responsibility should not.',
     'Your product changes hands. Responsibility should not.'),
    ('coordinate capacity',
     'win shelf space'),
    ('communicate matters',
     'communicate clearly'),
    ('moving parts',
     'moving parts'),
    ('Total Global Users',
     'Units sold through last year'),
    ('Worldwide Customer',
     'Nationwide chain coverage'),
    ('68+ Country observation',
     '1.900+ stores supplied directly'),
    ('No hidden fees or suppries',
     'No fees charged to the brand'),
    ('Customized design plans',
     'A plan per brand and per chain'),
    ('One logistics for every of the journey.',
     'One partner for the whole route to market.'),
    ('From urgent air cargo to long-term warehousing and final-mile delivery, our services can '
     'work independently or as one connected supply-chain solution.',
     'From the first buyer meeting to shelf replenishment and in-store promotions, our work can '
     'cover a single chain or your entire route to market.'),
    ('Air Freight',
     'Retail Chain Distribution'),
    ('Flexible airport-to-airport and door-to-door solutions for urgent, high-value, and '
     'time-sensitive shipments.',
     'We hold the listings and supply the country’s largest supermarket, drugstore, convenience '
     'and cash-and-carry chains out of our own stock.'),
    ('Ocean Freight',
     'Dental Distribution'),
    ('Reliable FCL, LCL, consolidation, and port-to-door shipping for global import and export '
     'operations.',
     'Materials, consumables and equipment delivered to dental practices, clinics, laboratories '
     'and dental depots across the country.'),
    ('Road Freight & Trucking',
     'Stock, Storage & Delivery'),
    ('Regional and cross-border FTL, LTL, and dedicated trucking services built around your '
     'schedule.',
     'We buy your product, hold it in our own warehouses and keep every chain depot and store '
     'supplied from it, on our own routes.'),
    ('Warehousing & Distribution',
     'Shelf Execution & Merchandising'),
    ('Secure storage, inventory coordination, cross-docking, order preparation, and regional '
     'distribution.',
     'Our field teams place the product, keep planograms correct, build promotions and report '
     'back what they actually see in store.'),
    ('Tell us what you are moving, where it needs to go, and when it needs to arrive.',
     'Tell us what you make, which chains you want to reach and what volume you can supply.'),
    ('Coordinate',
     'List'),
    ('We compare transport modes, carrier points to create a practical shipping plan.',
     'We take your range to the buyers we already supply, negotiate the listing and agree the '
     'launch.'),
    ('Moving',
     'Supply'),
    ('From pickup and export documentation to customs & and keep your team informed.',
     'We buy your stock, hold it in our warehouses, and keep every depot and store supplied from it.'),
    ('Delivery',
     'Sell'),
    ('Monitor',
     'Grow'),
    ('Follow your shipment in real time with status updates and delivery notifications.',
     'You see what sold, where and how fast — and we use it to win more facings, more stores and '
     'more chains.'),
    ('Know where your freight stands—and what happens next',
     'Know what is selling — and what moves next'),
    ('Real-time milestone updates',
     'Sell-out data per chain'),
    ('Estimated arrival visibility',
     'Stock cover per SKU'),
    ('Document status',
     'Batch, lot and expiry status'),
    ('Proof of delivery',
     'Proof of delivery per store'),
    ('Dedicated support contact',
     'A named commercial contact'),
    ('Access shipment milestones, estimated arrival information, documents, and status updates '
     'in one clear view. When plans change, your team receives the information needed to respond '
     'quickly.',
     'See what each chain ordered, what reached the shelf and what sold through, in one view. '
     'When a line moves faster than planned, your production team hears it from us early.'),
    ('One Accountable Team',
     'One Accountable Partner'),
    ('Instead of managing disconnected providers, you receive one primary team responsible for '
     'coordinating the complete shipment journey.',
     'Instead of a broker, a warehouse and a merchandising agency, one company owns your product '
     'from our goods-in door to the shelf edge.'),
    ('Proactive Communication',
     'Proactive Communication'),
    ('We communicate key milestones, risks, and required decisions before they become urgent '
     'operational problems.',
     'We flag slow sell-out, thin stock cover and listing risk early — while there is still time '
     'to act.'),
    ('Solutions Built Around Your Cargo',
     'Built Around Your Product'),
    ('Route, service level, transport mode, and handling requirements are selected around your '
     'priorities—not a fixed package.',
     'Pack format, order cut-off, delivery frequency and shelf plan are set around your product '
     'and the chains it sells in — not a fixed package.'),
    ('Scalable Capacity]',
     'Capacity That Scales'),
    ('Support a one-time shipment, seasonal demand, or an ongoing international supply chain '
     'through the same operational network.',
     'A single-chain pilot, a seasonal push or year-round national supply, all on the same network.'),
    ('Logistics shaped your industry operates.',
     'Built around how your category actually sells.'),
    ('One of the  Best Accountable Team',
     'Retail Chain Listings'),
    ('Representing clients in disputes with a focus on strategy, evidence, and outcome.',
     'We already supply the buyers. We take your range to them, negotiate the listing and own '
     'the launch.'),
    ('Clear Shipment Visibility',
     'Sell-Out Visibility'),
    ('Select air, ocean, road, rail, or multimodal transportation, capacity, and delivery '
     'priorities.',
     'See what sold, in which chain and at what rate, with stock cover per SKU and proof of '
     'delivery per store.'),
    ('Flexible Transport Options',
     'Nationwide Stock & Delivery'),
    ('Receive milestone updates, document status, estimated arrival information, communication.',
     'We buy and hold the stock, then supply every chain depot, store and practice from our own '
     'warehouses and routes.'),
    ('Scalable Capacity with shipment',
     'Dental Distribution'),
    ('Support one-time shipments, seasonal demand, or an ongoing international supply chain.',
     'Materials, consumables and equipment into practices, clinics, laboratories and dental depots.'),
    ('Better coordination creates measurable results.',
     'Better distribution creates measurable results.'),
    ('Supply Chain Optimization',
     'National Grocery Listing'),
    ('Inventory, fulfillment, distribution, and final-mile coordination for growing retail '
     'operations.',
     'Taking a regional food brand from three counties to national listings in two grocery chains.'),
    ('Transportation Efficiency',
     'Dental Consumables Rollout'),
    ('Time-sensitive inbound freight and parts distribution that help production and service '
     'networks stay moving.',
     'Putting a consumables range into dental practices and laboratories across the country.'),
    ('Coordinated transportation and storage solutions for sensitive, high-volume, and '
     'time-critical goods',
     'Distribution for brands that need shelf space, not another logistics supplier'),
    ('E-Commerce Logistics Excellence',
     'Seasonal Promotion Execution'),
    ('Inbound materials, project cargo, and outbound distribution designed around production '
     'schedules.',
     'Building and executing a nationwide promotional push across 1.400 stores in six weeks.'),
    ('What our customer saying about us?',
     'What our brands say about us'),
    ('Director of Operations, RetailPeak',
     'Commercial Director, RetailPeak'),
    ('Operations Director',
     'Founder & Owner'),
    ('Supply Chain Manager',
     'Export Manager'),
    ('Flexible Pricing plan',
     'How a GDH partnership works'),
    ('Freight Transportation',
     'Market Entry'),
    ('Essential brand identity design (logo, color, typography).',
     'Your range taken to buyers at two national chains.'),
    ('Basic UI/UX design for landing page or app prototype.',
     'Stock bought by GDH — never invoiced to you.'),
    ('Simple creative consultation (up to 2 sessions).',
     'Warehousing and delivery to every depot we supply.'),
    ('Fast turnaround time for quick launch.',
     'Monthly sell-out reporting per chain and per SKU.'),
    ('Easy revision process (up to 2 revisions).',
     'A named commercial contact for your account.'),
    ('Full brand identity system (logo, colors, typography, visual elements).',
     'Listings across our full retail chain network.'),
    ('UI/UX design for website or app (multi-page design).',
     'Dental channel added: practices, clinics and laboratories.'),
    ('Creative campaign concept & social media kit.',
     'Field merchandising in every store we deliver to.'),
    ('Strategic creative consultation (up to 4 sessions).',
     'Promotional calendar planned and executed per chain.'),
    ('More flexibility on revisions (up to 4 revisions).',
     'Planogram and facings negotiated at category review.'),
    ('Project timeline tailored to your business goals.',
     'Weekly sell-out data and forecasts back to your production.'),
    ('Customs & Final Delivery',
     'Full Category Partnership'),
    ('Comprehensive brand identity & guidelines (logo, visual system, brand assets).',
     'Everything in National Retail, across every channel we serve.'),
    ('Advanced UI/UX design for multi-platform products.',
     'Category planning with the chain buyer, season by season.'),
    ('Full creative campaign development (social, digital ads, and offline-ready).',
     'New product development briefed from real shelf data.'),
    ('Dedicated project manager & priority support.',
     'Dedicated account team and priority shelf escalation.'),
    ('Unlimited creative consultation during project.',
     'Packaging and pack-format advice for each chain.'),
    ('Unlimited revisions during project timeline.',
     'Returns, recalls and short-dated stock handled end to end.'),
    ('Deep market & competitor analysis included.',
     'Competitor and category tracking in every store we serve.'),
    ('We understand that building a company — and finding the right partner — raises a lot of '
     'questions.',
     'Handing your product to a distributor raises a lot of questions. Here are the ones brands '
     'ask most.'),
    ('Yes, our AI systems are designed to integrate seamlessly with popular business tools, '
     'CRMs, communication platforms, and workflow management systems.',
     'Retail and dental products. On the retail side: food and beverage, household and personal '
     'care, and health and beauty lines sold through the large store chains. On the dental side: '
     'materials, consumables and equipment for practices, clinics and laboratories.'),
    ('2. How quickly will I receive a quote?',
     '2. How do we start working with you?'),
    ('5. What information is needed for a freight quote?',
     '5. What do you need from us to get started?'),
    ('Our Blog & insights',
     'Insights from retail and dental distribution'),
    ('Warehouse & Inventory Solutions',
     'Retail Strategy'),
    ('Freight & Transportation',
     'Shelf Execution'),
    ('Logistics Technology',
     'Data & Insight'),
    ('Industry News & Trends',
     'Retail News & Trends'),
    ('Expert Tips & Guides',
     'Practical Guides'),
    ('Supply Chain Management',
     'Availability'),
    ('Technology & Digital Transformation',
     'Dental Channel'),
    ('Receive practical logistics guidance and company updates in your inbox.',
     'Practical distribution guidance and GDH updates, straight to your inbox.'),
    ('Receive practical logistics guidance',
     'Practical distribution guidance'),
    ('and company updates in your inbox.',
     'and GDH updates in your inbox.'),
    ('Our Service',
     'Company'),
    ('Case Study',
     'Clients'),
    ('350 7 Avenue SW, ',
     'Calea Lugojului nr 148, '),
    ('Calgary, AB T2P ',
     'CTPark, '),
    ('3N9, Canada',
     '307200 Ghiroda, România'),
    ('+0076 20 7946 0857',
     '+40 21 300 40 50'),
    ('partners@mastercare.com',
     'office@gdh-group.com'),
    ('Freight Forwarding &amp; Logistics Services',
     'What We Do for Brands'),
    ('Freight Forwarding & Logistics Services',
     'What We Do for Brands'),
    ('Explore air, ocean, road, rail, 3PL, and last-mile delivery services designed to keep '
     'global supply chains moving.',
     'How GDH takes a product from the factory gate to the shelf: chain listings, stock and '
     'delivery, dental distribution and in-store execution.'),
    ('A highly accountable team',
     'One accountable partner'),
    ('Alternative dispute resolution',
     'Planogram and facings checks'),
    ('Teams in this process.',
     'One team across the whole flow.'),
    ('Full shipment visibility throughout',
     'Full sell-out visibility throughout'),
    ('Clear and transparent shipment',
     'Clear, honest sell-out data'),
    ('End-to-end flexible transport',
     'End-to-end national coverage'),
    ('Altern solutions for every Transfarant',
     'A route to market for every channel'),
    ('Seamless flexible transport',
     'Seamless nationwide delivery'),
    ('Flexible and scalable capacity',
     'Flexible and scalable capacity'),
    ('Pre-litigation advisory and case assessment',
     'Shelf audits and promotional set-up'),
    ('Dispute Resolution &amp; Litigation',
     'Shelf Execution &amp; Merchandising'),
    ('Dispute Resolution & Litigation',
     'Shelf Execution & Merchandising'),
    ('Professional legal support.',
     'Professional in-store execution.'),
    ('Strategic dispute resolution and litigation',
     'Planned, reported shelf execution'),
    ('Effective solutions for dispute resolution',
     'Effective execution in every store we serve'),
    ('Freight &amp; Supply Chain Case Studies',
     'Brands We Distribute'),
    ('Freight & Supply Chain Case Studies',
     'Brands We Distribute'),
    ('Request a Freight &amp; Logistics Quote',
     'Partner with GDH'),
    ('Request a Freight & Logistics Quote',
     'Partner with GDH'),
    ('/Case Study',
     '/Brands'),
    ('/Blog',
     '/Insights'),
    ('Brand Identity',
     'Grocery Retail'),
    ('UI Design',
     'Dental'),
    ('Transportation &amp; Freight',
     'Health &amp; Beauty'),
    ('Transportation & Freight',
     'Health & Beauty'),
    ('E-Commerce Logistics',
     'Convenience'),
    ('International Logistics',
     'Market Entry'),
    ('$1,300',
     'No fee'),
    ('$3,800',
     'No fee'),
    ('$8,190',
     'No fee'),
    ('Get started',
     'Talk to us'),
    ('Popular',
     'Most chosen'),
    ('Clear shipment visibility',
     'Clear sell-out visibility'),
]

# inlocuiri de subsir, aplicate doar in noduri de text si atribute alese
SUBSTR = [
    ('“Before Frevanta', '“Before GDH'),
    ('“Working with', '“Working with'),
    ('“Frevanta', '“GDH'),
    ('Frevanta', 'GDH'),
    ('tel:+00762079460857', 'tel:+40213004050'),
    ('mailto:partners@mastercare.com', 'mailto:office@gdh-group.com'),
]
