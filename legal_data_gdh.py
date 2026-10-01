# -*- coding: utf-8 -*-
"""Paginile juridice, de presa si de contact comercial.

Structura: slug, kicker, title, lede, sections[(heading, body)], needsReview.
Parantezele drepte sunt intentionate: sunt datele de registru pe care
trebuie sa le completeze firma. Nu inventam numere de inregistrare.
"""

PAGES = [   {   'slug': 'contact-sales',
        'kicker': 'Contact sales',
        'title': 'Talk to the people who would buy your stock.',
        'lede': 'If you make or import a product and want it on Romanian shelves, this is the '
                'desk to write to. One email with your range and your monthly capacity starts '
                'it, and **the answer costs you nothing**.',
        'sections': [   (   'Who should get in touch',
                            'This page is for the people who make or import a product and want '
                            'it distributed: brand owners, manufacturers, importers and anyone '
                            'holding the rights to a range in this market. Retail or dental, one '
                            'line or two hundred, already listed somewhere or never on a shelf — '
                            'the conversation starts the same way. If you are a store, a chain '
                            'depot, a practice, a clinic or a laboratory that already buys from '
                            'us, use the main contact page instead. Orders, deliveries, invoices '
                            'and returns are handled there, and sending them to this desk only '
                            'slows them down.'),
                        (   'What to send us',
                            'Put as much of this in the first email as you can. Your product '
                            'list with pack sizes and barcodes. Shelf life for each line, and '
                            'any storage condition tighter than ambient. How many units a month '
                            'you can produce or import today, and how quickly you could raise '
                            'that. Any listing, distribution agreement or exclusivity you '
                            'already hold, including ones that have lapsed. And the '
                            'certifications your category requires — food, cosmetic, medical '
                            'device, dental. Prices help, though a wholesale price band is '
                            'enough to begin with. A spreadsheet or a PDF is fine. There is no '
                            'portal to fill in.'),
                        (   'Send it even if there are gaps',
                            'Very few first emails arrive complete, and we would rather read an '
                            'incomplete one this week than a perfect one next quarter. Send what '
                            'exists and mark what does not. Barcodes not yet assigned, shelf '
                            'life still being tested, capacity that depends on an order being '
                            'firm — all of that is normal, and all of it is either something we '
                            'can work around or something we can tell you how to close. The gaps '
                            'usually take one short call to fill.'),
                        (   'What you get back',
                            'A written read on where your range fits, from the commercial lead '
                            'for your channel. It names the chains and channels we believe will '
                            'take it, the monthly volume that implies, the pack format each '
                            'buyer will expect, what has to change before a buyer sees it, and '
                            'the earliest range review or practice cycle we could realistically '
                            'aim at. If we think a line will not sell, we say so and explain '
                            'why. That is not bluntness for its own sake — we are the ones '
                            'buying the stock, so an optimistic answer costs us more than it '
                            'costs you.'),
                        (   'How quickly we come back',
                            'A first reply usually arrives within two working days, and it comes '
                            'from a person rather than an autoresponder. The fuller read takes '
                            'longer, because it means checking your category against shelves we '
                            'already serve: expect it inside a fortnight for a straightforward '
                            'range, and longer where the category carries regulatory work or '
                            "where samples need assessing. If a chain's range review calendar "
                            'makes a date urgent, say so in the first email and we will work '
                            'backwards from it.'),
                        (   'What it costs you',
                            '**Nothing, at any stage.** There is no charge for the read, no '
                            'listing fee, no storage charge, no delivery cost and no marketing '
                            'contribution. GDH is a distributor, not a service provider: we buy '
                            'your stock at a wholesale price and earn from selling it on into '
                            'the chains and practices we serve. Your brand will never receive an '
                            'invoice from us. The practical consequence is that we only earn '
                            'once your product actually sells, which is the incentive you want '
                            'on the other side of the table.'),
                        (   'What the first meeting looks like',
                            'About an hour. On our side, the commercial lead for your channel, '
                            'plus someone from the supply team if your range has handling or '
                            'shelf-life conditions. No pitch deck. We go through your product '
                            'list line by line, ask what you can produce and what you have '
                            'already promised elsewhere, and tell you which doors we think are '
                            "open. Bring samples if you have them; a buyer's reaction to a pack "
                            'is hard to predict from a photograph. It can happen at our Ghiroda '
                            'hub, at your factory, or on a call — and if you come to us, you are '
                            'welcome to walk the warehouse while you are here.'),
                        (   'How to reach the commercial desk',
                            'Write to office@gdh-group.com with your brand name in the subject '
                            'line, or call +40 21 300 40 50 and ask for the commercial desk. '
                            'Post reaches us at Calea Lugojului nr 148, CTPark, 307200 Ghiroda. '
                            'The contact form on this site simply opens a message in your own '
                            'email client with the fields filled in — nothing is sent to a '
                            'server here and nothing is stored — so if you want to attach a '
                            'product list, it is quicker to email us directly.')],
        'needsReview': False},
    {   'slug': 'news',
        'kicker': 'News',
        'title': 'News from the distribution network.',
        'lede': 'This is where GDH publishes its own announcements: changes to the network, new '
                'channels and capability, and notes on the categories we distribute. Press '
                'enquiries are handled from here too.',
        'sections': [   (   'What we publish here',
                            'This page carries GDH’s own announcements, written by us and '
                            'published when there is something concrete to report. Three kinds '
                            'of item appear: changes to the network, new channels and new '
                            'capability, and notes on the categories we distribute. We do not '
                            'run a news desk and we do not publish to a schedule. If a month '
                            'passes with nothing here, it is because nothing changed that a '
                            'brand, a buyer or a dental practice would need to know about. '
                            'Everything on this page is dated.'),
                        (   'Network changes',
                            'Anything that alters where our stock sits or how it moves: a hub '
                            'opening or closing, storage extended into a new temperature range, '
                            'a delivery route moving from weekly to daily, or a change in the '
                            'regions a hub serves. These items matter to the brands we carry, '
                            'because they change which stores and practices a product can reach '
                            'and how fast the shelf can be refilled. The same record appears in '
                            'shorter, list form on the changelog.'),
                        (   'New channels and capability',
                            'When we open a channel we did not previously serve, or add '
                            'something we could not previously do, we announce it here. That '
                            'covers new retail formats, extensions to the dental range, '
                            'additional field and merchandising work in stores already on our '
                            'routes, and changes to how we report sell-out data back to brands. '
                            'Each note says plainly what is now possible and who it is relevant '
                            'to. We do not announce capability we are still building.'),
                        (   'Category notes',
                            'Short pieces on what we see in the ranges we distribute: pack '
                            'formats buyers are asking for, categories moving between shelves, '
                            'and regulatory or labelling changes that affect what can be listed. '
                            'These are observations from our own order book and our own '
                            'conversations with chain buyers, clinics and laboratories. They are '
                            'not market research and they are not forecasts. Where a subject '
                            'deserves more than a few paragraphs, it goes under Insights '
                            'instead.'),
                        (   'Press enquiries',
                            'Write to office@gdh-group.com with “Press” in the subject line, or '
                            'call +40 21 300 40 50 during office hours. Tell us your outlet, '
                            'what you are working on and your deadline. Press enquiries are '
                            'handled by one person alongside their other work, so we cannot '
                            'promise a same-day answer — but you will get a reply, including '
                            'when the reply is that we cannot help. Post reaches us at Calea '
                            'Lugojului nr 148, CTPark, 307200 Ghiroda. Press contact: [Name and '
                            'title of press contact].'),
                        (   'What we will and will not comment on',
                            'We will talk about our own operation: what we distribute, how the '
                            'network is laid out, and how we work with the brands we carry and '
                            'the chains and practices we supply. We will not discuss any '
                            'customer’s or supplier’s commercial terms, volumes or pricing, and '
                            'we will not confirm or deny a commercial relationship the other '
                            'party has not made public itself. We do not comment on other '
                            'companies, on pending legal matters, or on anything covered by a '
                            'confidentiality agreement.'),
                        (   'Using our material',
                            'Quote anything on this site with attribution to GDH. Logos and '
                            'photography are licensed for our own commercial communications and '
                            'are not cleared for republication — ask us and we will send what we '
                            'can, with the credit line it requires. If you need a statement '
                            'attributed to a named person, request it rather than assembling one '
                            'from this site: we will not put words to anyone’s name without '
                            'their sight of them. Nothing published here is written by an agency '
                            'on our behalf.'),
                        (   'No sign-up, no tracking',
                            'There is no subscription form on this page and no newsletter to '
                            'join. The site sets no cookies, runs no analytics and makes no '
                            'external requests. Our hosting provider keeps short technical '
                            'server logs, as any host must. The contact form opens your own '
                            'email client and sends nothing until you press send; the email '
                            'address and telephone number on the contact page reach the same '
                            'team directly. To follow what we publish, bookmark this page and '
                            'the changelog, and check them when it suits you.')],
        'needsReview': False},
    {   'slug': 'privacy',
        'kicker': 'Privacy',
        'title': 'Your data, and how little of it we hold',
        'lede': 'This website sets no cookies, runs no analytics and makes no requests to any '
                'other server. **The only personal data we hold is what you choose to send us in '
                'an email.** This notice explains what happens to it.',
        'sections': [   (   'The short version',
                            'This site is a set of static pages. It sets no cookies. It runs no '
                            'analytics, no tracking pixels and no third-party embeds. Every '
                            'font, image, stylesheet and script is served from this domain, so '
                            'loading a page sends no request to any other company; only our '
                            'hosting provider sees that the page was served. There is no login, '
                            'no account and no database. The only personal data we ever hold is '
                            'what you decide to put in an email to us. Everything below is '
                            'detail on that one point.'),
                        (   'Who is responsible for your data',
                            'The controller is [Registered company name], trading as GDH — '
                            'Global Distribution Holdings, with its registered office at Calea '
                            'Lugojului nr 148, CTPark, 307200 Ghiroda, Romania. Registered in '
                            'Romania under [company registration number]; VAT number [VAT '
                            'number]. For anything in this notice, write to office@gdh-group.com '
                            'or ring +40 21 300 40 50 and ask for [name or role of the data '
                            'protection contact]. Where you see square brackets, the detail '
                            'still has to be filled in. We would rather leave a visible gap than '
                            'print a number we have not checked.'),
                        (   'What the website collects: nothing',
                            'No cookies are set by these pages, so there is no cookie banner to '
                            'click. We do not count visits, record sessions, fingerprint devices '
                            'or run tests on visitors. Nothing on these pages reports back to '
                            'us. The one thing outside the pages themselves is the server that '
                            'delivers them: our hosting provider, [name of hosting provider], '
                            'may keep short technical logs such as IP addresses and request '
                            'times in order to serve the site and block attacks. We do not use '
                            'those logs for marketing and do not link them to anything else.'),
                        (   'What happens when you use the contact form',
                            'The form asks for your name, company, email, phone and a message. '
                            'It does not send anything anywhere by itself. When you press send, '
                            'the page opens your own email program with those details already '
                            'written into a message addressed to office@gdh-group.com. Nothing '
                            'leaves your device until you send that message yourself, and if you '
                            'close the draft we never see it. There is no server-side form '
                            'handler, no form service and no database behind the form. What '
                            'reaches us is an ordinary email in an ordinary mailbox.'),
                        (   'Why we are allowed to hold it',
                            'We hold your email because you wrote to us and want an answer. For '
                            'a business enquiry the lawful basis is our legitimate interest in '
                            'replying and in keeping a record of what was discussed (Article '
                            '6(1)(f) GDPR). Where the exchange is a step towards a supply '
                            'agreement, the basis is a contract or the steps taken before one '
                            '(Article 6(1)(b)). We do not add enquirers to a mailing list, we '
                            'send no marketing without your consent, and we carry out no '
                            'profiling and no automated decision-making.'),
                        (   'How long we keep enquiry correspondence',
                            'Enquiry email is deleted [retention period, for example 24 months] '
                            'after the last message in the exchange. If the enquiry becomes a '
                            'trading relationship, the correspondence joins the customer or '
                            'supplier file and is kept for as long as that relationship lasts, '
                            'plus the period Romanian accounting and tax law requires for '
                            'commercial records: [statutory retention period]. Nothing is kept '
                            'just in case. If you ask us to delete your enquiry sooner and we '
                            'have no legal reason to keep it, we will.'),
                        (   'Who else sees your enquiry',
                            'Your message is read by the people at GDH who need to answer it — '
                            'usually one commercial lead in the retail or dental team. We do not '
                            'sell personal data, and we do not pass it to the brands or chains '
                            'we work with unless you have asked us to make an introduction. '
                            'Technically, our email is handled by [name of email and IT '
                            'provider], acting as a processor under a written agreement. If that '
                            'provider stores or supports mail outside the European Economic '
                            'Area, the transfer relies on [transfer mechanism, for example '
                            'standard contractual clauses].'),
                        (   'Your rights, and how to complain',
                            'Under the GDPR you may ask for a copy of the personal data we hold '
                            'about you, have it corrected or erased, restrict or object to how '
                            'we use it, or receive it in a portable form. Where we rely on '
                            'consent, you can withdraw it at any time. Write to '
                            'office@gdh-group.com and we will reply within one month. If you are '
                            'not satisfied, you may complain to the Romanian supervisory '
                            'authority, ANSPDCP (Autoritatea Națională de Supraveghere a '
                            'Prelucrării Datelor cu Caracter Personal), at dataprotection.ro. '
                            'This notice was last reviewed [date]. It describes what we do; it '
                            'is not legal advice.')],
        'needsReview': True},
    {   'slug': 'imprint',
        'kicker': 'Legal notice',
        'title': 'Who is responsible for this website.',
        'lede': 'The company that operates gdh-group.com, how to reach it, and who is '
                'accountable for what appears on these pages.',
        'sections': [   (   'Site operator',
                            'This website, gdh-group.com, is operated by GDH — Global '
                            'Distribution Holdings, a company registered in Romania and trading '
                            'as a distributor of retail and dental products. Registered office: '
                            'Calea Lugojului nr 148, CTPark, 307200 Ghiroda, Romania. Legal '
                            'form: [Legal form of the company]. Full registered name as entered '
                            'in the trade register: [Full registered company name]. Where these '
                            'pages use the short name GDH, they mean that company and no other.'),
                        (   'How to reach us',
                            'Email: office@gdh-group.com. Telephone: +40 21 300 40 50. Post: '
                            'Calea Lugojului nr 148, CTPark, 307200 Ghiroda, Romania. Email and '
                            'telephone are the fastest routes, and both reach the same team. The '
                            'contact form on this site is not a form in the usual sense — it '
                            'opens a message in your own email program, already addressed to us, '
                            'which you then send yourself. Nothing you type into it reaches us '
                            'until you press send in your own email client.'),
                        (   'Registration and tax details',
                            'The identifiers below belong in this notice and must be filled in '
                            "from the company's own registration documents before this page goes "
                            'live. Trade register number (Registrul Comerțului): [Trade register '
                            'number]. Unique registration code: [Unique registration code]. VAT '
                            'identification number: [VAT identification number]. Subscribed and '
                            'paid-up share capital: [Share capital]. Office of registration: '
                            '[Registry office where the company is entered]. Until those '
                            'brackets are replaced with the real values, nothing in this section '
                            'should be treated as confirmed.'),
                        (   'Who may represent the company',
                            'The person or persons authorised to act for the company and to '
                            'enter into agreements on its behalf: [Name of managing director or '
                            'administrator], and [Name of any further authorised representative '
                            '— remove if there is only one]. Correspondence that needs to reach '
                            'a legal representative should go by post to the registered office '
                            'above, marked for their attention, rather than to the general email '
                            'address. We do not publish direct personal contact details for '
                            'individuals on this site.'),
                        (   'Responsibility for content',
                            'Responsible for the content of this website: [Name of the person '
                            'responsible for content], at the registered office above. We write '
                            'and check these pages ourselves and we try to keep them accurate. '
                            'Even so, ranges, coverage and commercial terms change, and a page '
                            'can be out of date by the time you read it. Nothing here is a '
                            'binding offer. What we agree with a brand or a customer is set out '
                            'in the contract we sign, not on a web page. If something looks '
                            'wrong, tell us and we will correct it.'),
                        (   'What this site does not do',
                            'This is a static website. It sets no cookies, runs no analytics, '
                            'loads no trackers and embeds nothing from third parties. Text, '
                            'images, fonts, stylesheets and scripts are all served from this '
                            'domain, so opening a page here makes no request to any other '
                            'company. There is no server-side form handling and no database '
                            'behind these pages. The only way to send us anything is the email '
                            'link described above, which uses your own email program. That is '
                            'why you will not see a cookie banner on this site.')],
        'needsReview': True},
    {   'slug': 'terms',
        'kicker': 'Terms',
        'title': 'General terms of supply.',
        'lede': 'The general terms on which GDH buys stock from the brands it carries, and sells '
                'and delivers it on to retailers, practices and laboratories. The commercial '
                'detail sits in each individual agreement.',
        'sections': [   (   'Scope',
                            'These terms describe the general basis on which GDH — Global '
                            'Distribution Holdings buys stock from the brands it carries, and '
                            'sells and delivers that stock to retailers, dental practices, '
                            'clinics and laboratories. They are published so both sides can see '
                            'the shape of the relationship before anything is signed. They are '
                            'not a contract on their own, and they are not legal advice. Prices, '
                            'volumes, lead times, payment periods, rebates and exclusivity are '
                            'agreed in writing in each individual supply or purchase agreement, '
                            'and where that agreement says something different, it prevails. '
                            'These terms have not been reviewed by a lawyer. Treat them as a '
                            'plain description of how we work, not as a guarantee of '
                            'compliance.'),
                        (   'How orders and purchase are agreed',
                            'Nothing is binding until it is confirmed in writing. For stock we '
                            'buy, we issue a purchase order setting out product, quantity, '
                            'price, delivery location and the requested delivery date. That '
                            'order becomes binding when the supplier confirms it, or when goods '
                            'are dispatched against it. For stock we sell, the order a chain, '
                            'store or practice places with our commercial desk is an offer to '
                            'buy, and our written confirmation accepts it. We may decline an '
                            'order, or confirm part of it, where stock is short or an account '
                            'sits outside its agreed credit terms. Quotations are indicative and '
                            'open only for the period stated on them.'),
                        (   'The stock we buy is ours',
                            'GDH is a distributor. We are not an agent, a courier or a '
                            'third-party logistics provider. We buy stock, we pay for it, and '
                            'from that point it is ours: it sits in our warehouses, on our '
                            'books, and it is sold on in our own name and at our own risk. We do '
                            'not invoice the brands we carry for listings, shelf space, delivery '
                            'or field work, and we do not hold their stock on consignment unless '
                            'an individual agreement says so in writing. Our margin is the '
                            'difference between what we pay and what we sell for.'),
                        (   'Delivery, acceptance, title and risk',
                            'We deliver to the address and within the window set out in the '
                            'confirmed order. Each delivery travels with a delivery note listing '
                            'what is in it. Signing that note confirms the units and packages '
                            'received, not the condition of goods inside sealed packaging. '
                            'Shortages, visible damage and wrong items should be noted on the '
                            'delivery note at the time, or reported to us within [Acceptance '
                            'period, in working days]. Hidden defects should be reported as soon '
                            'as they are found. Risk in the goods passes to the buyer on '
                            'delivery. Title passes on payment in full, unless the individual '
                            'agreement sets a different point. Until then the buyer keeps the '
                            'goods identifiable and insured.'),
                        (   'Returns and recalls',
                            'Returns are agreed before goods travel back. We take back goods '
                            'delivered in error, damaged in our care, or short-dated beyond the '
                            'limit in the individual agreement. Saleable stock returned for any '
                            'other reason is accepted at our discretion and may carry a handling '
                            'charge. Goods must come back in their original packaging, quoting '
                            'the return reference we issue. Recalls take priority over '
                            'everything else. We hold batch and delivery records for the stock '
                            'we distribute, so affected units can be traced to the stores and '
                            'practices that received them, and we act on a brand’s written '
                            'recall or withdrawal instruction without waiting for commercial '
                            'questions to be settled.'),
                        (   'Payment',
                            'Invoices are issued on or after delivery and are payable within the '
                            'period set in the individual agreement — commonly [Agreed payment '
                            'period, in days] days from the invoice date. Payment is by bank '
                            'transfer to the account printed on the invoice. We never ask for '
                            'payment to a different account by email, and any message that does '
                            'should be checked with us by telephone before anything is paid. '
                            'Overdue amounts carry statutory late-payment interest under '
                            'Romanian law. We may hold further deliveries, or ask for payment in '
                            'advance, while an account is overdue. Disputed items should be '
                            'raised within [Invoice dispute period, in days] days; the '
                            'undisputed balance stays payable.'),
                        (   'Liability and force majeure',
                            'We answer for what we control: the stock we own, the deliveries we '
                            'make and the records we keep. Our liability for any claim is '
                            'limited to the value of the goods concerned, or to the cap written '
                            'into the individual agreement. We do not accept liability for lost '
                            'profit, lost sales, the loss of a listing, or other indirect or '
                            'consequential loss. Nothing here limits liability that cannot be '
                            'limited by law, including death or personal injury caused by '
                            'negligence, fraud, and the rights consumer protection law gives an '
                            'end buyer. Neither side is in breach for delay caused by events '
                            'outside its reasonable control — flood, fire, strike, failure of '
                            'utilities, a public authority’s decision. Obligations resume when '
                            'the event ends.'),
                        (   'Governing law, and who we are',
                            'These terms and each individual agreement are governed by Romanian '
                            'law. Both sides will try to settle a dispute by talking first. '
                            'Failing that, it goes to the competent court in [Judicial district '
                            'of the competent court], Romania. If one clause turns out to be '
                            'unenforceable, the rest stands. Our details: GDH — Global '
                            'Distribution Holdings, Calea Lugojului nr 148, CTPark, 307200 '
                            'Ghiroda, Romania. Company registration number [Company registration '
                            'number]. VAT number [VAT number]. Represented by [Name of managing '
                            'director]. For a question about these terms, or a copy of the '
                            'current supply agreement, write to office@gdh-group.com or call +40 '
                            '21 300 40 50.')],
        'needsReview': True},
    {   'slug': 'cookies',
        'kicker': 'Cookies',
        'title': 'This site does not use cookies.',
        'lede': 'No cookies, no analytics, no tracking pixels, no external requests. There is '
                'nothing here to accept and nothing to switch off. This page explains what that '
                'means for you.',
        'sections': [   (   'The short version',
                            'This site sets no cookies. Not analytics cookies, not preference '
                            'cookies, not advertising cookies, not even "strictly necessary" '
                            "ones. Nothing is written to your browser's cookie store when you "
                            'open a page here, and nothing is read from it. The site is a set of '
                            'static files. The pages, the stylesheet, the scripts, the typeface '
                            'and the images are all served from this domain, and no other server '
                            'is contacted while you read. There is also no local storage or '
                            'session storage in use, so nothing is kept on your device between '
                            'visits.'),
                        (   'What we do not use',
                            'There is no analytics on this site, hosted or third-party. There '
                            'are no tracking pixels, no advertising tags and no conversion '
                            'tracking. There are no embedded maps, videos, chat widgets, social '
                            'buttons, comment systems or font services. Each of those would '
                            "quietly contact another company's servers as the page loads and "
                            'hand that company your IP address, whether or not you clicked '
                            'anything. We have left all of them out. We cannot build a profile '
                            'of you because we are not collecting the parts you would need to '
                            'build one.'),
                        (   'What your browser still does on its own',
                            'Your browser keeps its own copy of files it has already downloaded, '
                            'so a second visit loads faster. That cache sits on your device '
                            "under your browser's control. We cannot read it and cannot tell "
                            'whether it exists. Your browser also keeps its own history and may '
                            'remember where you had scrolled to. None of that is a cookie, and '
                            'none of it is sent to us. If you clear your browsing data, nothing '
                            'of ours is lost; the files are simply downloaded again next time.'),
                        (   'Why there is no consent banner',
                            'Consent banners exist because sites place things on your device '
                            'that are not needed to show you the page. This site does not, so '
                            'there is nothing to ask you about and nothing to opt out of. You '
                            'will not be interrupted by a cookie dialogue, and you will not be '
                            'nudged into accepting anything. You do not have to take our word '
                            "for it either: open your browser's developer tools, look at the "
                            'storage and network panels, and reload the page. You should see no '
                            'cookies and no requests leaving this domain.'),
                        (   'Requests still reach a server',
                            'Showing you a web page means your browser has to ask a server for '
                            'files, so the request itself is visible to whoever runs that '
                            'server. This site is hosted by [Name of hosting provider], which '
                            'may keep standard technical logs of requests — typically the IP '
                            "address, the time, the file requested and the browser's user-agent "
                            'string — for security and to keep the service running. Those logs '
                            'are a by-product of serving the site. We do not use them to follow '
                            'individuals between visits and we do not combine them with anything '
                            'else. Retention: [Server log retention period].'),
                        (   'The contact form',
                            'The contact form has no server behind it. When you submit it, the '
                            'site opens a new message in your own email program with the details '
                            'already filled in, and you decide whether to send it. Nothing is '
                            'stored on this site, no database records your draft, and no cookie '
                            'remembers what you typed. If you close the page instead of sending, '
                            'nothing has left your device. What happens to an email you do '
                            'choose to send to us is covered by our [Privacy notice].'),
                        (   'If this ever stops being true',
                            'If we ever add something that stores or reads data on your device — '
                            'a measurement tool, an embedded video, a live chat, a payment step '
                            '— we will update this page before it goes live. We will say what it '
                            'is, what it stores, how long it lasts and who else can see it, and '
                            'we will ask for your consent before anything beyond the strictly '
                            'necessary is set. We would rather lose the measurement than quietly '
                            'start tracking people who came here on the understanding that we do '
                            'not.'),
                        (   'Questions',
                            'This page describes how the site actually works as at [Date of last '
                            'review]. It is a description of our practice, not legal advice. If '
                            'you have a question about it, or you think the site is doing '
                            'something this page does not describe, we would genuinely like to '
                            'know. Write to office@gdh-group.com or call +40 21 300 40 50. Our '
                            'registered address is Calea Lugojului nr 148, CTPark, 307200 '
                            'Ghiroda, Romania.')],
        'needsReview': True},
    {   'slug': 'whistleblowing',
        'kicker': 'Whistleblowing',
        'title': 'Raise a concern, in confidence.',
        'lede': 'If something in the way GDH works looks unlawful or seriously wrong, tell us. '
                'This page explains what can be reported, how to report it confidentially, and '
                'what happens after you do.',
        'sections': [   (   'What you can report',
                            'Use this channel for anything you believe is unlawful or seriously '
                            'wrong in how GDH operates. That includes fraud, theft or false '
                            'accounting; bribery, kickbacks or improper payments to win a '
                            'listing; product safety problems, including tampering, counterfeit '
                            'stock or a break in the cold chain; health and safety risks in a '
                            'warehouse or on a delivery route; harm to the environment; breaches '
                            'of competition, data protection or employment law; and any attempt '
                            'to cover one of these up. You do not need proof before you speak to '
                            'us. A reasonable belief that something is wrong is enough.'),
                        (   'Who can report',
                            'Anyone who sees it. Our own staff, including temporary and agency '
                            'workers and people who have since left; job applicants; the brands '
                            'whose products we distribute; the chains, stores, practices, '
                            'clinics and laboratories we supply; hauliers, contractors and other '
                            'suppliers; and anyone else who deals with us. You do not have to '
                            'work for GDH, and you do not have to be the person affected. If you '
                            'learned of the problem through your work with us, this channel is '
                            'open to you.'),
                        (   'How to report',
                            'There are two routes, and both go to the people who handle reports '
                            'rather than to a line manager. By email, to [dedicated '
                            'whistleblowing email address], which is read only by [role or name '
                            'of the person responsible for receiving reports]. By post, in a '
                            'sealed envelope marked "Whistleblowing — confidential", to GDH, '
                            'Calea Lugojului nr 148, CTPark, 307200 Ghiroda. Tell us what '
                            'happened, where and when, who was involved, and attach anything '
                            'that helps. If you would rather explain it in person, say so and we '
                            'will arrange a meeting.'),
                        (   'Confidentiality and anonymity',
                            'Your identity is treated as confidential. It is shared only with '
                            'the people needed to look into the report, and only passed further '
                            'where the law requires it. We will tell you before that happens, '
                            'unless telling you would prejudice the investigation. You may also '
                            'report anonymously: send a letter without a name and we will still '
                            'assess it. Bear in mind that an email carries the address it was '
                            'sent from, so post is the safer route if you want to stay '
                            'anonymous. This site has no online reporting form, no analytics and '
                            'no trackers.'),
                        (   'No retaliation',
                            'Nobody may be penalised for a report made in good faith. For our '
                            'own people that means no dismissal, demotion, transfer, pay cut, '
                            'disciplinary action, withheld training or hostile treatment. For a '
                            'brand, store, practice or supplier it means no cancelled order, '
                            'suspended listing, terminated contract or quiet blacklisting. The '
                            'same protection covers anyone who helps with a report and anyone '
                            'connected to the person who made it, such as a colleague or a '
                            'relative. Retaliation is itself a disciplinary matter here, and a '
                            'threat of it is treated the same way.'),
                        (   'What happens after a report',
                            'We acknowledge your report within seven days of receiving it, '
                            'unless you reported anonymously and left no way to reply. [Role of '
                            'the person responsible for receiving reports] then assesses it and '
                            'decides whether an investigation is needed, which may involve '
                            'interviews and checks of documents and records. Anyone named is '
                            'given a fair chance to respond. You will hear the outcome, and what '
                            'we are doing about it, within three months of the acknowledgement. '
                            'If the matter is still open at that point we will say so and give '
                            'you a new date.'),
                        (   'Reporting to an authority instead',
                            'You are not obliged to come to us first, and nothing here requires '
                            'you to exhaust our channel before going elsewhere. You may report '
                            'directly to the competent national authority, [name of the '
                            'competent national authority in Romania], and, where EU funds or EU '
                            'law are involved, to the relevant European institution. Doing so '
                            'costs you none of the protection described on this page. Where '
                            'there is a serious and immediate danger to the public, you may also '
                            'make the matter public. A lawyer or a trade union can advise you; '
                            'this page is not legal advice.'),
                        (   'What this channel is not for',
                            'Routine business matters reach a solution faster through the team '
                            'that can actually fix them. Order queries, delivery problems, '
                            'invoices, returns and product complaints go to the commercial desk '
                            'at office@gdh-group.com or +40 21 300 40 50. Requests about your '
                            'own personal data belong with our privacy contact. Anything of that '
                            'kind sent to the whistleblowing channel will simply be passed on, '
                            'which costs you time.')],
        'needsReview': True}]
