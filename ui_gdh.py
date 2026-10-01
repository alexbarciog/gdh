# -*- coding: utf-8 -*-
"""Componentele din care se asambleaza paginile GDH.

Fiecare functie intoarce markup, niciuna nu scrie pe disc. Clasele sunt cele
definite in theme_gdh.py — daca adaugi una noua aici, adaug-o si acolo.
"""
import html as _html

ARROW = ('<svg viewBox="0 0 16 16" fill="none" aria-hidden="true">'
         '<path d="M1 8h13M9 3l5 5-5 5" stroke="currentColor" stroke-width="2" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def esc(t):
    return _html.escape(str(t), quote=True)


def rich(t):
    """Text de continut cu **ingrosare** — singurul marcaj permis in copy."""
    out, bold = [], False
    for chunk in esc(t).split("**"):
        out.append(("<strong>%s</strong>" % chunk) if bold and chunk else chunk)
        bold = not bold
    return "".join(out)


# ---------------------------------------------------------------- atoms
def eyebrow(text, muted=False):
    if not text:
        return ""
    cls = "eyebrow eyebrow--muted" if muted else "eyebrow"
    return '<p class="%s">%s</p>' % (cls, esc(text))


def btn(label, href, kind="primary"):
    """Buton drept, cu eticheta cu majuscule. Fara sageata: in limbajul-sursa
    butoanele sunt curate, iar sageata e rezervata link-urilor de tip text."""
    return '<a class="btn btn--%s" href="%s">%s</a>' % (kind, esc(href), esc(label))


def link_arrow(label, href):
    return '<a class="link-arrow" href="%s">%s%s</a>' % (esc(href), esc(label), ARROW)


def btn_row(*buttons):
    items = [b for b in buttons if b]
    return ('<div class="btn-row">%s</div>' % "".join(items)) if items else ""


# ---------------------------------------------------------------- chrome
def topbar(links):
    items = "".join('<a href="%s">%s</a>' % (esc(h), esc(t)) for t, h in links)
    return ('<div class="hairline"></div>'
            '<div class="topbar"><div class="wrap">%s</div></div>' % items)


def chrome(links, nav, logo_src, current=""):
    """Banda de gradient, bara utilitara si antetul, intr-o singura piesa fixa.

    Daca bara utilitara ramane in curgerea normala a paginii, ea pleaca la
    derulare si antetul se lipeste singur de marginea de sus — exact saritura
    care arata gresit. Asa se misca toate trei la fel: adica deloc.
    """
    return ('<div class="chrome" id="gdh-chrome">%s%s</div>'
            % (topbar(links), header(nav, logo_src, current)))


CLOSE_ICON = ('<svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" fill="none" '
              'stroke="currentColor" stroke-width="2" stroke-linecap="round">'
              '<path d="M4 4l12 12M16 4L4 16"/></svg>')


def _mega(group):
    """Panoul mare al unei sectiuni din meniu.

    Ocupa latimea paginii, are fundalul de gradient, un titlu, intrarile cu o
    descriere sub fiecare, un buton de inchidere si un indemn incadrat jos.
    """
    items = "".join(
        '<li><a class="mega__item" href="%s">'
        '<span class="mega__label"><span class="mega__chev" aria-hidden="true">&rsaquo;</span>%s</span>'
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
    """Bara principala: sigla, navigatie cu mega-meniu, actiune, buton de telefon."""
    links = []
    for group in nav:
        here = group.get("key") == current
        cls = "nav__link" + (" is-current" if here else "")
        # aria-current, nu doar o clasa de CSS: altfel pagina curenta nu e
        # anuntata de cititoarele de ecran
        mark = ' aria-current="page"' if here else ""
        if group.get("items"):
            links.append('<a class="%s" href="%s"%s data-mega="mega-%s" '
                         'aria-expanded="false">%s</a>%s'
                         % (cls, esc(group["href"]), mark, group["id"],
                            esc(group["title"]), _mega(group)))
        else:
            links.append('<a class="%s" href="%s"%s>%s</a>'
                         % (cls, esc(group["href"]), mark, esc(group["title"])))
    return (
        '<header class="header" id="gdh-header">'
        '<div class="wrap">'
        '<a class="brand" href="index.html" aria-label="GDH — Global Distribution Holdings, home">'
        '<img class="brand__ink" src="%s" alt="GDH — Global Distribution Holdings" '
        'width="96" height="40" decoding="async">'
        '<img class="brand__light" src="img/gdh-logo-light.png" alt="" aria-hidden="true" '
        'width="96" height="40" decoding="async">'
        '</a>'
        '<nav class="nav" aria-label="Main">%s</nav>'
        '<a class="btn btn--primary nav__cta" href="contact.html">Contact sales</a>'
        '<button class="burger" type="button" aria-expanded="false" '
        'aria-controls="gdh-drawer" aria-label="Menu"><span></span></button>'
        '</div></header>' % (esc(logo_src), "".join(links)))


def drawer(nav):
    groups = []
    for group in nav:
        if group.get("items"):
            pid = "drawer-%s" % group["id"]
            links = "".join('<li><a href="%s">%s</a></li>' % (esc(href), esc(label))
                            for label, href, _desc in group["items"])
            groups.append(
                '<div class="drawer__group">'
                '<button class="drawer__top" type="button" aria-expanded="false" '
                'aria-controls="%s">%s'
                '<span class="topics__arrow" aria-hidden="true">+</span></button>'
                '<div class="drawer__panel" id="%s"><ul>%s</ul></div></div>'
                % (pid, esc(group["title"]), pid, links))
        else:
            groups.append('<div class="drawer__group">'
                          '<a class="drawer__top" href="%s">%s</a></div>'
                          % (esc(group["href"]), esc(group["title"])))
    return ('<div class="drawer" id="gdh-drawer"><div class="wrap">%s'
            '<div style="margin-top:32px">%s</div></div></div>'
            % ("".join(groups), btn("Contact sales", "contact.html")))


def footer(nav, logo_src, legal):
    cols = []
    for col in nav:
        li = "".join('<li><a href="%s">%s</a></li>' % (esc(h), esc(t)) for t, h in col["links"])
        cols.append('<div><h3>%s</h3><ul>%s</ul></div>' % (esc(col["title"]), li))
    legal_links = "".join('<li><a href="%s">%s</a></li>' % (esc(h), esc(t)) for t, h in legal)
    return (
        '<footer class="footer"><div class="wrap">'
        '<div class="footer__main">'
        '<div><a href="index.html" aria-label="GDH, home">'
        '<img src="%s" alt="GDH — Global Distribution Holdings" width="120" height="50" '
        'decoding="async" style="height:48px"></a>'
        '<p class="muted" style="margin-top:20px;max-width:34ch">GDH buys, stocks and '
        'distributes retail and dental products into the country’s largest store '
        'chains and dental practices — at no cost to the brands we carry.</p></div>'
        '%s</div>'
        '<div class="footer__legal"><p>© 2026 GDH — Global Distribution Holdings. '
        'All rights reserved.</p><ul>%s</ul></div>'
        '</div></footer>' % (esc(logo_src), "".join(cols), legal_links))


# ---------------------------------------------------------------- blocks
def hero(kicker, title, lede, buttons, image=None):
    media = ('<div class="hero__media"><img src="%s" alt="" loading="eager" '
             'fetchpriority="high" decoding="async"></div>' % esc(image)) if image else ""
    return ('<section class="hero">%s<div class="wrap"><div class="hero__inner">'
            '%s<h1 class="hero-title">%s</h1><p class="lede">%s</p>%s'
            '</div></div></section>'
            % (media, eyebrow(kicker), rich(title), rich(lede), btn_row(*buttons)))


def crumbs(trail):
    items = []
    for i, (label, href) in enumerate(trail):
        last = i == len(trail) - 1
        items.append('<li><span aria-current="page">%s</span></li>' % esc(label) if last
                     else '<li><a href="%s">%s</a></li>' % (esc(href), esc(label)))
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>%s</ol></nav>' % "".join(items)


def pagehead(trail, kicker, title, lede, buttons=(), image=None):
    media = ('<div class="pagehead__media"><img src="%s" alt="" loading="eager" '
             'decoding="async"></div>' % esc(image)) if image else ""
    body = ('<div>%s%s<h1 class="h1">%s</h1><p class="lede">%s</p>%s</div>'
            % (crumbs(trail), eyebrow(kicker), rich(title), rich(lede), btn_row(*buttons)))
    grid = body + media if media else body
    cls = "pagehead__grid" if media else "pagehead__grid pagehead__grid--solo"
    style = "" if media else ' style="grid-template-columns:1fr;max-width:56rem"'
    return ('<section class="pagehead"><div class="wrap"><div class="%s"%s>%s</div>'
            '</div></section>' % (cls, style, grid))


def section(inner, variant="", tight=False, reveal=True):
    cls = "section"
    if tight:
        cls += " section--tight"
    if variant:
        cls += " section--%s" % variant
    attr = ' data-reveal' if reveal else ""
    return '<section class="%s"%s><div class="wrap">%s</div></section>' % (cls, attr, inner)


def head_block(kicker, title, lede="", align_cta=None):
    parts = [eyebrow(kicker), '<h2 class="h1">%s</h2>' % rich(title)]
    if lede:
        parts.append('<p class="lede" style="margin-top:16px">%s</p>' % rich(lede))
    if align_cta:
        parts.append('<div style="margin-top:24px">%s</div>' % align_cta)
    return '<div style="max-width:56rem;margin-bottom:48px">%s</div>' % "".join(parts)


def card(title, text, href, meta="", image=None, cta="Read more"):
    media = ('<div class="card__media"><img src="%s" alt="" loading="lazy" '
             'decoding="async"></div>' % esc(image)) if image else ""
    return ('<a class="card" href="%s">%s<div class="card__body">'
            '%s<h3 class="h3">%s</h3><p class="muted">%s</p>'
            '<div class="card__foot"><span class="link-arrow">%s%s</span></div>'
            '</div></a>'
            % (esc(href), media,
               ('<p class="card__meta">%s</p>' % esc(meta)) if meta else "",
               esc(title), esc(text), esc(cta), ARROW))


def tile(title, text, href):
    return ('<a class="tile" href="%s"><h3 class="h3">%s</h3>'
            '<p class="muted" style="margin-top:10px">%s</p></a>'
            % (esc(href), esc(title), esc(text)))


def topics(items):
    links = "".join('<a href="%s">%s<span class="topics__arrow" aria-hidden="true">%s</span></a>'
                    % (esc(h), esc(t), "&rarr;") for t, h in items)
    return '<div class="topics">%s</div>' % links


def stats(pairs):
    cells = "".join('<div class="stat"><div class="stat__value">%s</div>'
                    '<div class="stat__label">%s</div></div>' % (esc(v), esc(l))
                    for v, l in pairs)
    return '<div class="grid grid--4">%s</div>' % cells


def split(title, paras, image=None, kicker="", cta=None, reverse=False):
    body = [eyebrow(kicker), '<h2 class="h1">%s</h2>' % rich(title),
            '<div class="prose" style="margin-top:20px">%s</div>'
            % "".join('<p class="muted">%s</p>' % rich(p) for p in paras)]
    if cta:
        body.append('<div style="margin-top:28px">%s</div>' % cta)
    media = ('<div class="split__media"><img src="%s" alt="" loading="lazy" '
             'decoding="async"></div>' % esc(image)) if image else ""
    cls = "split split--reverse" if reverse else "split"
    return '<div class="%s">%s<div>%s</div></div>' % (cls, media, "".join(body))


def prose_blocks(items):
    out = []
    for heading, body in items:
        out.append('<div>%s<p class="muted">%s</p></div>'
                   % (('<h2 class="h2" style="margin-bottom:10px">%s</h2>' % esc(heading))
                      if heading else "", rich(body)))
    return ('<div class="prose" style="display:grid;gap:34px;max-width:72ch">%s</div>'
            % "".join(out))


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
            '<div><p class="card__meta">%s</p><p class="h2" style="margin-top:6px">%s</p></div>'
            '<div><p class="muted">%s</p>'
            '<p style="margin-top:10px"><a href="mailto:%s">%s</a> &middot; '
            '<a href="tel:%s">%s</a></p></div>'
            '<div>%s</div></div>'
            % (esc(role), esc(name), esc(text), esc(email), esc(email),
               esc(phone.replace(" ", "")), esc(phone),
               btn("Write a message", "contact.html")))


def cta_band(title, text, primary, secondary=None):
    return ('<div class="split" style="align-items:center">'
            '<div><h2 class="h1">%s</h2><p class="lede" style="margin-top:16px">%s</p></div>'
            '<div>%s</div></div>'
            % (rich(title), rich(text), btn_row(primary, secondary)))
