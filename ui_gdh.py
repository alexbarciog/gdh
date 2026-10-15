# -*- coding: utf-8 -*-
"""Componentele din care se asambleaza paginile GDH.

Fiecare functie intoarce markup, niciuna nu scrie pe disc. Clasele sunt cele
definite in theme_gdh.py — daca adaugi una noua aici, adaug-o si acolo.
"""
import html as _html

# sageata dreapta, pentru legaturi
ARROW = ('<svg viewBox="0 0 16 16" fill="none" aria-hidden="true">'
         '<path d="M1 8h13M9 3l5 5-5 5" stroke="currentColor" stroke-width="1.5" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')
# sageata cu carlig — cea din butoanele referintei
HOOK = ('<svg viewBox="0 0 18 18" fill="none" aria-hidden="true">'
        '<path d="M3 3.5v5.25A2.75 2.75 0 0 0 5.75 11.5H15M11.5 8l3.5 3.5-3.5 3.5" '
        'stroke="currentColor" stroke-width="1.5" stroke-linecap="round" '
        'stroke-linejoin="round"/></svg>')
# sageata in diagonala, pentru listele numerotate
DIAG = ('<svg viewBox="0 0 12 12" fill="none" aria-hidden="true">'
        '<path d="M2 10L10 2M4 2h6v6" stroke="currentColor" stroke-width="1.3" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>')
PLUS = ('<svg viewBox="0 0 13 13" fill="none" aria-hidden="true">'
        '<path d="M6.5 0v13M0 6.5h13" stroke="currentColor" stroke-width="1"/></svg>')
CLOSE_ICON = ('<svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" fill="none" '
              'stroke="currentColor" stroke-width="2" stroke-linecap="round">'
              '<path d="M4 4l12 12M16 4L4 16"/></svg>')

VIDEO = "img/banner.mp4"
POSTER = "img/banner-poster.webp"


def esc(t):
    return _html.escape(str(t), quote=True)


def rich(t):
    """Text de continut cu **ingrosare** — singurul marcaj permis in copy."""
    out, bold = [], False
    for chunk in esc(t).split("**"):
        out.append(("<strong>%s</strong>" % chunk) if bold and chunk else chunk)
        bold = not bold
    return "".join(out)


def video(cls="", lazy=False):
    """Degradeul in miscare din banner. Fara sunet, in bucla, cu afisul ca
    rezerva; cele `lazy` pornesc doar cand ajung pe ecran (vezi site.js)."""
    return ('<video class="%s" muted loop playsinline %s poster="%s" aria-hidden="true" '
            'tabindex="-1"%s><source src="%s" type="video/mp4"></video>'
            % (cls, "" if lazy else "autoplay", POSTER,
               ' preload="none" data-lazy-video' if lazy else ' preload="auto"', VIDEO))


# ---------------------------------------------------------------- atoms
def eyebrow(text, muted=False):
    if not text:
        return ""
    cls = "eyebrow eyebrow--muted" if muted else "eyebrow"
    return '<p class="%s">%s</p>' % (cls, esc(text))


def _roll(label):
    """Eticheta pusa de doua ori: la hover coloana urca si apare copia."""
    return ('<span class="btn__clip"><span class="btn__track"><span>%s</span>'
            '<span aria-hidden="true">%s</span></span></span>' % (esc(label), esc(label)))


def btn(label, href, kind="primary", icon=True, extra=""):
    """Pastila cu eticheta care se rostogoleste si sageata cu carlig."""
    ico = ('<span class="btn__icon" aria-hidden="true">%s%s</span>' % (HOOK, HOOK)) if icon else ""
    return ('<a class="btn btn--%s%s" href="%s">%s%s</a>'
            % (kind, (" " + extra) if extra else "", esc(href), _roll(label), ico))


def submit(label):
    return ('<button class="btn btn--primary" type="submit">%s'
            '<span class="btn__icon" aria-hidden="true">%s%s</span></button>'
            % (_roll(label), HOOK, HOOK))


def link_arrow(label, href):
    return '<a class="link-arrow" href="%s">%s%s</a>' % (esc(href), esc(label), HOOK)


def btn_row(*buttons):
    items = [b for b in buttons if b]
    return ('<div class="btn-row">%s</div>' % "".join(items)) if items else ""


def rise(lines, tag="h1", cls="hero-title"):
    """Titlu mare care urca rand cu rand din spatele unei masti."""
    if isinstance(lines, str):
        lines = [lines]
    inner = "".join('<span class="rise"><span>%s</span></span>' % rich(l) for l in lines)
    return '<%s class="%s" data-rise>%s</%s>' % (tag, cls, inner, tag)


# ---------------------------------------------------------------- chrome
def chrome(links, nav, logo_src, current="", over=False):
    """Antetul fix. `over` = pagina incepe cu bannerul video, deci antetul
    porneste alb pe transparent si trece pe alb mat dupa derulare."""
    return ('<div class="chrome%s" id="gdh-chrome">%s</div>'
            % (" chrome--over" if over else "", header(nav, logo_src, current)))


def _mega(group):
    """Panoul unei sectiuni din meniu: titlu, intrari numerotate, indemn jos."""
    items = "".join(
        '<li><a class="mega__item" href="%s">'
        '<span class="mega__label">%s</span>'
        '%s</a></li>'
        % (esc(href), esc(label),
           ('<span class="mega__desc">%s</span>' % esc(desc)) if desc else "")
        for label, href, desc in group["items"])

    cta = ""
    if group.get("cta"):
        c_label, c_text, c_href = group["cta"]
        cta = ('<a class="mega__cta" href="%s"><span class="mega__cta-title">%s%s</span>'
               '<span class="mega__cta-text">%s</span></a>'
               % (esc(c_href), esc(c_label), ARROW, esc(c_text)))

    return (
        '<div class="mega" id="mega-%s"><div class="wrap">'
        '<div class="mega__top"><div>%s<h2 class="mega__title">%s</h2></div>'
        '<button class="mega__close" type="button">Close%s</button></div>'
        '<ul class="mega__grid">%s</ul>%s'
        '</div></div>'
        % (group["id"],
           '<p class="mega__eyebrow">%s</p>' % esc(group.get("eyebrow", group["title"])),
           esc(group.get("heading", group["title"])),
           CLOSE_ICON, items, cta))


def header(nav, logo_src, current=""):
    """Sigla, navigatia numerotata cu mega-meniu, actiunea si butonul Menu."""
    links = []
    entries = list(nav) + [dict(key="contact", title="Contact", href="contact.html")]
    for n, group in enumerate(entries, 1):
        here = group.get("key") == current
        cls = "nav__link" + (" is-current" if here else "")
        # aria-current, nu doar o clasa de CSS: altfel pagina curenta nu e
        # anuntata de cititoarele de ecran
        mark = ' aria-current="page"' if here else ""
        label = '%s<sup aria-hidden="true">(%d)</sup>' % (_roll(group["title"]), n)
        if group.get("items"):
            links.append('<a class="%s" href="%s"%s data-mega="mega-%s" '
                         'aria-expanded="false">%s</a>%s'
                         % (cls, esc(group["href"]), mark, group["id"], label, _mega(group)))
        else:
            links.append('<a class="%s" href="%s"%s>%s</a>'
                         % (cls, esc(group["href"]), mark, label))
    return (
        '<header class="header" id="gdh-header">'
        '<div class="wrap">'
        '<a class="brand" href="index.html" aria-label="GDH — Global Distribution Holdings, home">'
        '<img class="brand__ink" src="%s" alt="GDH — Global Distribution Holdings" '
        'width="175" height="38" decoding="async">'
        '<img class="brand__light" src="img/gdh-logo-light.png" alt="" aria-hidden="true" '
        'width="175" height="38" decoding="async">'
        '</a>'
        '<nav class="nav" aria-label="Main">%s</nav>'
        '<div class="header__actions">%s'
        '<button class="burger" type="button" aria-expanded="false" '
        'aria-controls="gdh-drawer"><span class="burger__lines" aria-hidden="true">'
        '<i></i><i></i></span>Menu</button></div>'
        '</div></header>'
        % (esc(logo_src), "".join(links),
           btn("Contact sales", "contact-sales.html", "primary", icon=False,
               extra="btn--sm nav__cta")))


def drawer(nav, company, contact, logo_src):
    """Meniul complet, deschis din butonul „Menu”: coloane si un bloc de contact."""
    cols = []
    for group in nav:
        if not group.get("items"):
            continue
        links = "".join('<li><a href="%s">%s</a></li>' % (esc(href), esc(label))
                        for label, href, _desc in group["items"])
        cols.append('<div><p class="drawer__title">%s</p><ul class="drawer__list">%s</ul></div>'
                    % (esc(group["title"]), links))
    links = "".join('<li><a href="%s">%s</a></li>' % (esc(h), esc(t)) for t, h in company)
    cols.append('<div><p class="drawer__title">Company</p><ul class="drawer__list">%s</ul></div>'
                % links)
    email, phone, address = contact
    aside = ('<div class="drawer__aside"><p class="drawer__title" style="margin:0">Get in touch</p>'
             '<a href="mailto:%s">%s</a><a href="tel:%s">%s</a><p>%s</p>%s</div>'
             % (esc(email), esc(email), esc(phone.replace(" ", "")), esc(phone),
                "<br>".join(esc(a) for a in address),
                btn("Partner with us", "partner-with-us.html")))
    return ('<div class="drawer" id="gdh-drawer" role="dialog" aria-modal="true" '
            'aria-label="Menu"><div class="drawer__panel">'
            '<div class="drawer__head"><a href="index.html" aria-label="GDH, home">'
            '<img src="%s" alt="GDH — Global Distribution Holdings" width="156" height="34"></a>'
            '<button class="mega__close drawer__close" type="button">Close%s</button></div>'
            '<div class="drawer__cols">%s%s</div></div></div>'
            % (esc(logo_src), CLOSE_ICON, "".join(cols), aside))


def footer(nav, logo_src, legal, contact=None):
    cols = []
    for col in nav:
        li = "".join('<li><a href="%s">%s</a></li>' % (esc(h), esc(t)) for t, h in col["links"])
        cols.append('<div><h3>%s</h3><ul>%s</ul></div>' % (esc(col["title"]), li))
    if contact:
        email, phone, address = contact
        cols.append('<div><h3>Get in touch</h3><ul>'
                    '<li><a href="mailto:%s">%s</a></li><li><a href="tel:%s">%s</a></li>'
                    '<li style="color:var(--w-60);line-height:1.5">%s</li></ul></div>'
                    % (esc(email), esc(email), esc(phone.replace(" ", "")), esc(phone),
                       "<br>".join(esc(a) for a in address)))
    legal_links = "".join('<li><a href="%s">%s</a></li>' % (esc(h), esc(t)) for t, h in legal)
    return (
        '<footer class="footer"><div class="wrap">'
        '<div class="footer__main">'
        '<div class="footer__info"><a href="index.html" aria-label="GDH, home">'
        '<img src="%s" alt="GDH — Global Distribution Holdings" width="141" height="110" '
        'decoding="async"></a>'
        '<p>GDH buys, stocks and distributes retail and dental products into the country’s '
        'largest store chains and dental practices — at no cost to the brands we carry.</p></div>'
        '<div class="footer__menus">%s</div></div>'
        '<div class="footer__legal"><p>© 2026 GDH — Global Distribution Holdings. '
        'All rights reserved.</p><ul>%s</ul></div>'
        '</div></footer>' % (esc(logo_src), "".join(cols), legal_links))


# ---------------------------------------------------------------- blocks
def home_hero(title_lines, lede, buttons, services, badge, where):
    """Bannerul primei pagini: video pe tot ecranul, titlu urias, lista de
    servicii in dreapta, banda de informatii jos si axa verticala cu cruce."""
    items = "".join(
        '<li><a href="%s"><span class="n">/%03d</span><span class="rule"></span>'
        '<span class="t">%s</span>%s</a></li>' % (esc(href), i, esc(label), DIAG)
        for i, (label, href) in enumerate(services, 1))
    logo, b_title, b_sub = badge
    w_label, w_tz = where
    return (
        '<section class="hero is-dark" aria-label="Introduction">'
        '<div class="hero__media">%s</div>'
        '<div class="hero__axis" aria-hidden="true">%s</div>'
        '<div class="wrap hero__inner">'
        '<div class="hero__top">'
        '<div class="hero__copy">%s%s</div>'
        '<div class="hero__side">'
        '<div><p class="hero__list-title">What we do</p><ul class="hero__list">%s</ul></div>'
        '<p class="lede">%s</p></div></div>'
        '<div class="hero__info">'
        '<div class="hero__badge"><img src="%s" alt="" width="61" height="48">'
        '<div><strong>%s</strong><span>%s</span></div></div>'
        '<div class="hero__where"><span>%s</span>'
        '<span><time data-clock data-tz="%s">&nbsp;</time></span></div>'
        '</div></div></section>'
        % (video("hero__video"), PLUS, rise(title_lines), btn_row(*buttons), items,
           rich(lede), esc(logo), esc(b_title), esc(b_sub), esc(w_label), esc(w_tz)))


def crumbs(trail):
    items = []
    for i, (label, href) in enumerate(trail):
        last = i == len(trail) - 1
        items.append('<li><span aria-current="page">%s</span></li>' % esc(label) if last
                     else '<li><a href="%s">%s</a></li>' % (esc(href), esc(label)))
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>%s</ol></nav>' % "".join(items)


def pagehead(trail, kicker, title, lede, buttons=(), image=None, figure="©26", alt=""):
    """Bannerul paginilor interioare, ca pagina de detaliu din referinta:
    titlul mare si descrierea in stanga, o cifra uriasa in dreapta, apoi
    fotografia lata, care se deschide la derulare."""
    media = ('<div class="pagehead__media"><img src="%s" alt="%s" loading="eager" '
             'decoding="async"></div>' % (esc(image), esc(alt))) if image else ""
    fig = ('<p class="pagehead__fig" aria-hidden="true">%s</p>' % esc(figure)) if figure else ""
    return ('<section class="pagehead"><div class="wrap">%s%s'
            '<div class="pagehead__grid">'
            '<div class="pagehead__title">%s<p class="lede pagehead__lede">%s</p>%s</div>%s'
            '</div>%s</div></section>'
            % (crumbs(trail), eyebrow(kicker), rise(title, "h1", "h1"),
               rich(lede), btn_row(*buttons), fig, media))


def wide_image(src, alt):
    """Fotografie lata, rotunjita, care se deschide la derulare (ca in banner)."""
    return ('<div class="pagehead__media wide-media"><img src="%s" alt="%s" loading="lazy" '
            'decoding="async"></div>' % (esc(src), esc(alt)))


def slug(text):
    import re
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60]


# ---------------------------------------------------------------- detail page
def detail(card, main):
    """Corpul paginii de detaliu: cardul gri lipit in stanga, continutul in dreapta."""
    return ('<div class="detail"><aside class="dcard">%s</aside>'
            '<div class="detail__main">%s</div></div>' % (card, main))


def card_tags(label, tags):
    """Partea de sus a cardului: eticheta intre paranteze drepte si etichetele.
    `tags` sunt texte simple sau perechi (text, legatura)."""
    out = []
    for t in tags:
        if isinstance(t, (tuple, list)):
            out.append('<a href="%s"># %s</a>' % (esc(t[1]), esc(t[0])))
        else:
            out.append("<span># %s</span>" % esc(t))
    return ('<div><p class="dcard__label">[ %s ]</p><div class="dcard__tags">%s</div></div>'
            % (esc(label), "".join(out)))


def card_info(rows):
    """Randuri eticheta / valoare, pentru articole."""
    return '<dl class="dinfo">%s</dl>' % "".join(
        '<div><dt>%s</dt><dd>%s</dd></div>' % (esc(k), esc(v)) for k, v in rows)


def count_figure(to, frm, label, prefix="", suffix=""):
    """Cifra mare care numara pana la valoarea ei cand ajunge pe ecran.
    In HTML sta valoarea finala, deci fara JavaScript se vede corect."""
    return ('<div class="dcount"><p class="count" data-count-to="%s" data-count-from="%s" '
            'data-prefix="%s" data-suffix="%s">%s%s%s</p><p class="dcard__label">%s</p></div>'
            % (to, frm, esc(prefix), esc(suffix), esc(prefix), to, esc(suffix), esc(label)))


def drows(items):
    """Randurile de continut: titlul in stanga, textul in dreapta, cu ancora."""
    return '<div class="drows">%s</div>' % "".join(
        '<div id="%s"><h2 class="h2">%s</h2><p class="muted">%s</p></div>'
        % (slug(h), esc(h), rich(b)) for h, b in items)


def pcards(items):
    """Fisele de proces numerotate, cu bara neagra langa titlu."""
    return '<div class="pcards">%s</div>' % "".join(
        '<div class="pcard"><div class="pcard__top"><h3>%s</h3><span class="pcard__n">/%03d</span>'
        '</div><p>%s</p></div>' % (esc(it["title"]), i, esc(it["text"]))
        for i, it in enumerate(items, 1))


def duo(images):
    """Doua imagini alaturate, la finalul continutului."""
    return '<div class="duo">%s</div>' % "".join(
        '<div class="duo__img"><img src="%s" alt="" loading="lazy" decoding="async"></div>'
        % esc(i) for i in images)


def section(inner, variant="", tight=False, reveal=False, cls=""):
    # intrarile se fac pe componente (site.js), nu pe sectiunea intreaga
    classes = "section"
    if tight:
        classes += " section--tight"
    if variant:
        classes += " section--%s" % variant
    if cls:
        classes += " " + cls
    attr = ' data-reveal' if reveal else ""
    return '<section class="%s"%s><div class="wrap">%s</div></section>' % (classes, attr, inner)


def head_block(kicker, title, lede="", align_cta=None, center=False):
    """Capul de sectiune: eticheta si titlul in stanga, descrierea si legatura
    in dreapta — „section-title-wrapper” din referinta."""
    side = ""
    if lede or align_cta:
        side = '<div class="shead__side">%s%s</div>' % (
            ('<p class="lede">%s</p>' % rich(lede)) if lede else "", align_cta or "")
    return ('<div class="shead%s"><div class="shead__title">%s<h2 class="h1">%s</h2></div>%s</div>'
            % (" shead--center" if center else "", eyebrow(kicker), rich(title), side))


def card(title, text, href, meta="", image=None, cta="Read more"):
    """Card de articol. Cu imagine: imaginea rotunjita si eticheta peste ea;
    fara: un bloc gri, cu titlul sus si legatura jos."""
    chips = ""
    if meta:
        parts = [p.strip() for p in meta.split("·")]
        chips = '<p class="card__meta"><span class="chip">%s</span>%s</p>' % (
            esc(parts[0]), "".join("<span>%s</span>" % esc(p) for p in parts[1:]))
    foot = '<div class="card__foot"><span class="link-arrow">%s%s</span></div>' % (esc(cta), HOOK)
    if image:
        return ('<a class="card" href="%s"><div class="card__media"><img src="%s" alt="" '
                'loading="lazy" decoding="async"></div><div class="card__body">'
                '%s<h3 class="h3">%s</h3><p class="muted">%s</p></div></a>'
                % (esc(href), esc(image), chips, esc(title), esc(text)))
    return ('<a class="card card--text" href="%s"><div class="card__body">'
            '%s<h3 class="h3">%s</h3><p class="muted">%s</p>%s</div></a>'
            % (esc(href), chips, esc(title), esc(text), foot))


def tile(title, text, href, num=""):
    return ('<a class="tile" href="%s"><div class="tile__top"><span class="tile__num">%s</span>%s</div>'
            '<div><h3 class="h3">%s</h3><p class="muted" style="margin-top:12px">%s</p></div></a>'
            % (esc(href), esc(num), DIAG, esc(title), esc(text)))


def topics(items):
    links = "".join('<a href="%s">%s<span class="topics__arrow" aria-hidden="true">%s</span></a>'
                    % (esc(h), esc(t), ARROW) for t, h in items)
    return '<div class="topics">%s</div>' % links


def stats(pairs):
    cells = "".join('<div class="stat"><div class="stat__top"><span class="stat__num">/%02d</span>'
                    '<span class="stat__value">%s</span></div>'
                    '<div class="stat__label">%s</div></div>' % (i, esc(v), esc(l))
                    for i, (v, l) in enumerate(pairs, 1))
    return '<div class="stats">%s</div>' % cells


def giant(*lines):
    """Titlul urias pe negru."""
    return '<h2 class="giant">%s</h2>' % "".join("<span>%s</span>" % esc(l) for l in lines)


def marquee(words):
    """Banda care curge. Textul e pus de doua ori, ca bucla sa nu aiba cusatura."""
    run = "".join("<span>%s</span>" % esc(w) for w in words)
    return ('<div class="marquee" aria-hidden="true"><div class="marquee__track">%s%s</div></div>'
            % (run, run))


def split(title, paras, image=None, kicker="", cta=None, reverse=False):
    body = [eyebrow(kicker), '<h2 class="h1">%s</h2>' % rich(title),
            '<div class="prose" style="margin-top:24px">%s</div>'
            % "".join('<p class="muted">%s</p>' % rich(p) for p in paras)]
    if cta:
        body.append('<div style="margin-top:32px">%s</div>' % cta)
    media = ('<div class="split__media"><img src="%s" alt="" loading="lazy" '
             'decoding="async"></div>' % esc(image)) if image else ""
    cls = "split split--reverse" if reverse else "split"
    return '<div class="%s">%s<div>%s</div></div>' % (cls, media, "".join(body))


def feature(title, where, text, href, image, tag=""):
    """Card de „proiect” din referinta: imagine, nume si eticheta, text sub."""
    return ('<a class="feature" href="%s"><div class="feature__media">%s'
            '<img src="%s" alt="" loading="lazy" decoding="async"></div>'
            '<div class="feature__row"><span class="feature__name">%s</span>'
            '<span class="feature__where">%s</span></div><p class="muted">%s</p></a>'
            % (esc(href), ('<span class="card__tag">%s</span>' % esc(tag)) if tag else "",
               esc(image), esc(title), esc(where), esc(text)))


def services_showcase(items):
    """Serviciile pe negru: imaginea serviciului activ in stanga, lista in
    dreapta; cel activ se deschide intr-un card alb cu etichete."""
    aside_imgs = "".join('<img src="%s" alt="" loading="lazy" decoding="async"%s data-svc-img="%d">'
                         % (esc(it["image"]), ' class="is-on"' if i == 0 else "", i)
                         for i, it in enumerate(items))
    rows = []
    for i, it in enumerate(items):
        tags = "".join("<span># %s</span>" % esc(t) for t in it["tags"])
        rows.append(
            '<div class="svc__item%s" data-svc="%d">'
            '<h3><button class="svc__head" type="button" aria-expanded="%s" '
            'aria-controls="svc-%d">%s</button></h3>'
            '<div class="svc__body" id="svc-%d"><div><div class="svc__inner">'
            '<p>%s</p><div class="svc__tags">%s</div>'
            '<a class="svc__more" href="%s">Discover now%s</a></div></div></div></div>'
            % (" is-active" if i == 0 else "", i, "true" if i == 0 else "false", i,
               esc(it["title"]), i, esc(it["text"]), tags, esc(it["href"]), ARROW))
    return ('<div class="svc" data-svc-root><div class="svc__aside">'
            '<p class="svc__label" data-svc-label>01 %s</p>'
            '<div class="svc__media">%s</div></div>'
            '<div class="svc__list">%s</div></div>'
            % (esc(items[0]["title"]), aside_imgs, "".join(rows)))


def process(steps, core_title, core_sub, core_btn):
    """Cei patru pasi, in romburi, in jurul crucii."""
    cells = "".join(
        '<div class="process__step"><div class="diamond"><span><b>%02d.</b><i>%s</i></span></div>'
        '<p>%s</p></div>' % (i, esc(t), esc(d)) for i, (t, d) in enumerate(steps, 1))
    return ('<div class="process">%s<div class="process__core"><p>%s<span>%s</span></p>%s</div></div>'
            % (cells, esc(core_title), esc(core_sub), core_btn))


def prose_blocks(items):
    """Cu titluri: randuri, titlul in stanga si textul in dreapta.
    Fara titluri (articolele): o singura coloana de citit."""
    if not any(h for h, _b in items):
        return '<div class="article">%s</div>' % "".join(
            '<p>%s</p>' % rich(b) for _h, b in items)
    out = []
    for heading, body in items:
        out.append('<div><h2 class="h2">%s</h2><p class="muted">%s</p></div>'
                   % (esc(heading), rich(body)))
    return '<div class="rows">%s</div>' % "".join(out)


def accordion(items):
    out = []
    for i, (q, a) in enumerate(items):
        out.append('<div class="acc__item"><h3><button class="acc__top" type="button" '
                   'aria-expanded="false" aria-controls="acc-%d">%s'
                   '<span class="acc__sign" aria-hidden="true"></span></button></h3>'
                   '<div class="acc__panel" id="acc-%d"><p>%s</p></div></div>'
                   % (i, esc(q), i, esc(a)))
    return '<div class="acc">%s</div>' % "".join(out)


def contact_band(name, role, text, email, phone):
    return ('<div class="contact-card">'
            '<div><p class="card__meta"><span class="chip">%s</span></p>'
            '<p class="h2" style="margin-top:18px">%s</p></div>'
            '<div><p class="muted">%s</p>'
            '<p style="margin-top:12px;font-weight:500"><a href="mailto:%s">%s</a> &middot; '
            '<a href="tel:%s">%s</a></p></div>'
            '<div>%s</div></div>'
            % (esc(role), esc(name), esc(text), esc(email), esc(email),
               esc(phone.replace(" ", "")), esc(phone),
               btn("Write a message", "contact.html")))


def cta_band(title, text, primary, secondary=None, kicker="Ready to start"):
    """Blocul de final: degradeul in miscare intr-o cutie rotunjita."""
    return ('<section class="cta is-dark"><div class="cta__box">%s'
            '<div class="cta__inner"><div class="cta__copy">%s'
            '<h2 class="cta__title">%s</h2><p class="cta__text">%s</p>%s</div>'
            '<span class="cta__year">©2026</span></div></div></section>'
            % (video(lazy=True), eyebrow(kicker), rich(title), rich(text),
               btn_row(primary, secondary)))


# ---------------------------------------------------------------- treatments
def lead_say(text, label="Overview"):
    """Prima sectiune, ca declaratie: text mare, cuvintele se aprind la derulare."""
    return ('<div class="lead-say"><div class="lead-say__label">%s</div>'
            '<p class="words" data-words>%s</p></div>' % (eyebrow(label), rich(text)))


def steps(items):
    """Sectiuni numerotate, cu linii intre ele."""
    rows = []
    for i, (heading, body) in enumerate(items, 1):
        rows.append('<div class="step"><div class="step__num">%02d.</div>'
                    '<h3>%s</h3><p class="muted">%s</p></div>'
                    % (i, esc(heading), rich(body)))
    return '<div class="steps">%s</div>' % "".join(rows)


def statement(kicker, text):
    """O singura fraza, mare, pe degradeul din banner."""
    return ('<section class="statement is-dark"><div class="wrap">'
            '<div class="statement__box">%s<p class="statement__text">%s</p></div></div></section>'
            % (eyebrow(kicker), rich(text)))


def two_col(items):
    """Proza pe doua coloane, pentru blocurile dense."""
    body = "".join('<div><h2 class="h2">%s</h2>'
                   '<p class="muted">%s</p></div>' % (esc(h), rich(b))
                   for h, b in items)
    return '<div class="prose prose--two">%s</div>' % body


def facts(items):
    """Fisele scurte, incadrate, numerotate."""
    return '<div class="facts">%s</div>' % "".join(
        '<div class="fact"><h3>%s</h3><p class="muted">%s</p></div>'
        % (esc(it["title"]), esc(it["text"])) for it in items)


def related(items):
    """Trei pagini vecine, ca sa nu se termine fiecare pagina in acelasi zid."""
    return '<div class="related">%s</div>' % "".join(
        '<a href="%s"><span class="related__label">%s</span>'
        '<span class="related__desc">%s</span>'
        '<span class="related__go">Explore%s</span></a>'
        % (esc(href), esc(label), esc(desc), HOOK)
        for label, href, desc in items)
