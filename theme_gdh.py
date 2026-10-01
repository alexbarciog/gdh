# -*- coding: utf-8 -*-
"""Sistemul vizual GDH, scris de la zero.

Limbajul e cel al unui site de logistica de contract: alb si negru, un singur
accent, butoane drepte cu eticheta cu majuscule, titluri foarte mari si un
container de 1200 px. Accentul e portocaliul GDH (#fe3f03), nu culoarea altcuiva,
iar textele si imaginile sunt ale noastre.

Nu mai pornim de la foaia de stil a sablonului Webflow: aceea descria alt fel de
pagina (butoane pastila, alt ritm, alta tipografie) si ar fi trebuit combatuta
la fiecare regula.
"""

TOKENS = {
    # culori
    "ink": "#0b0b0b",
    "ink-soft": "#1b1b1b",
    "band": "#12161f",          # banda inchisa din spatele antetelor interioare
    # Paleta ceruta de client: turcoazul din limbajul vizual al partenerului.
    # #00767a e tonul de actiune (5.42:1 cu alb, trece AA peste tot), #33c1bd e
    # tonul luminos, folosit doar peste fundaluri inchise (8.91:1 pe tus).
    "accent": "#00767a",
    "accent-dark": "#006165",
    "accent-bright": "#33c1bd",
    "accent-sky": "#48bbe5",
    "accent-tint": "#e9f6f6",
    "grey-900": "#2e2e2e",
    "grey-700": "#5c5c5c",
    "grey-500": "#8a8a8a",
    "grey-400": "#a1a1a1",
    "grey-200": "#dddddd",
    "grey-100": "#e8e8e8",
    "grey-50": "#f7f7f7",
    "white": "#ffffff",
    # tipografie
    "font": "'GDH Roboto', system-ui, -apple-system, 'Segoe UI', Arial, sans-serif",
    # ritm
    "container": "1200px",
    "gutter": "24px",
}


def css():
    """Foaia de stil completa a site-ului."""
    t = TOKENS
    return f"""
/* ============================================================ tokens */
:root{{
  --ink:{t['ink']};
  --ink-soft:{t['ink-soft']};
  --band:{t['band']};
  --accent:{t['accent']};
  --accent-dark:{t['accent-dark']};
  --accent-bright:{t['accent-bright']};
  --accent-sky:{t['accent-sky']};
  --accent-tint:{t['accent-tint']};
  --g900:{t['grey-900']};
  --g700:{t['grey-700']};
  --g500:{t['grey-500']};
  --g400:{t['grey-400']};
  --g200:{t['grey-200']};
  --g100:{t['grey-100']};
  --g50:{t['grey-50']};
  --white:{t['white']};
  --font:{t['font']};
  --container:{t['container']};
  --gutter:{t['gutter']};

  /* scara tipografica: titlul urca pana la 78px, ca in referinta */
  --t-hero:clamp(2.5rem,5.6vw,4.9rem);
  --t-h1:clamp(2.1rem,4.2vw,3.5rem);
  --t-h2:clamp(1.5rem,2.3vw,1.72rem);
  --t-h3:1.22rem;
  --t-body:1.125rem;
  --t-small:0.95rem;
  --t-eyebrow:0.8rem;

  /* ritm vertical */
  --s-1:8px; --s-2:16px; --s-3:24px; --s-4:32px;
  --s-5:48px; --s-6:64px; --s-7:88px; --s-8:120px;
}}

/* ============================================================ reset */
*,*::before,*::after{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%;scroll-behavior:smooth}}
body{{margin:0;background:var(--white);color:var(--ink);
  font-family:var(--font);font-size:var(--t-body);line-height:1.6;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}}
img,svg,video{{max-width:100%;height:auto;display:block}}
a{{color:inherit;text-decoration:none}}
button{{font:inherit;color:inherit}}
h1,h2,h3,h4,p,figure,blockquote,ul,ol{{margin:0}}
ul,ol{{padding:0;list-style:none}}
::selection{{background:var(--accent);color:#fff}}

:focus-visible{{outline:3px solid var(--accent);outline-offset:3px}}
.gdh-skip{{position:absolute;left:-9999px;top:0;z-index:300;background:var(--accent);
  color:#fff;padding:14px 22px;font-weight:700;letter-spacing:.04em;text-transform:uppercase}}
.gdh-skip:focus{{left:0}}

/* ============================================================ layout */
.wrap{{width:100%;max-width:var(--container);margin-inline:auto;
  padding-inline:var(--gutter)}}
.section{{padding-block:var(--s-7)}}
.section--tight{{padding-block:var(--s-6)}}
.section--grey{{background:var(--g50)}}
.section--ink{{background:var(--ink);color:#fff}}
.grid{{display:grid;gap:var(--s-4)}}
.grid--2{{grid-template-columns:repeat(2,1fr)}}
.grid--3{{grid-template-columns:repeat(3,1fr)}}
.grid--4{{grid-template-columns:repeat(4,1fr)}}
@media (max-width:980px){{
  .grid--3,.grid--4{{grid-template-columns:repeat(2,1fr)}}
}}
@media (max-width:640px){{
  .grid--2,.grid--3,.grid--4{{grid-template-columns:1fr}}
  .section{{padding-block:var(--s-6)}}
}}

/* ============================================================ type */
.eyebrow{{font-size:var(--t-eyebrow);font-weight:700;letter-spacing:.14em;
  text-transform:uppercase;color:var(--accent);margin-bottom:var(--s-2)}}
.eyebrow--muted{{color:var(--g400)}}
.hero-title{{font-size:var(--t-hero);font-weight:600;line-height:1.08;
  letter-spacing:-.02em}}
.h1{{font-size:var(--t-h1);font-weight:600;line-height:1.14;letter-spacing:-.015em}}
.h2{{font-size:var(--t-h2);font-weight:700;line-height:1.3}}
.h3{{font-size:var(--t-h3);font-weight:700;line-height:1.35}}
.lede{{font-size:1.22rem;line-height:1.55;color:var(--g700);max-width:62ch}}
.lede strong{{color:var(--ink);font-weight:700}}
/* pe benzile inchise, accentuarea trebuie sa fie alba: var(--ink) o facea
   aproape invizibila peste fundalul inchis */
.hero strong,.pagehead strong,.section--ink strong{{color:#fff}}
/* accentul de actiune e prea inchis peste tus: pe benzile inchise folosim
   tonul luminos, care are 8.9:1 pe fundalul nostru */
.hero .eyebrow,.pagehead .eyebrow,.section--ink .eyebrow{{color:var(--accent-bright)}}
.section--ink .link-arrow,.hero .link-arrow{{border-bottom-color:var(--accent-bright)}}
.footer h3{{color:#fff}}
.prose{{max-width:68ch}}
.prose p + p{{margin-top:var(--s-3)}}
.muted{{color:var(--g700)}}
.section--ink .muted,.section--ink .lede{{color:rgba(255,255,255,.72)}}

/* ============================================================ buttons */
.btn{{display:inline-flex;align-items:center;gap:12px;border:2px solid transparent;
  padding:15px 30px;font-size:.88rem;font-weight:700;letter-spacing:.08em;
  text-transform:uppercase;cursor:pointer;white-space:nowrap;
  transition:background .2s,color .2s,border-color .2s}}
/* sageata e un SVG fara dimensiuni proprii: fara asta se intinde cat tot butonul */
.btn svg{{width:15px;height:15px;flex:none}}
.btn--primary{{background:var(--accent);color:#fff;border-color:var(--accent)}}
.btn--primary:hover{{background:var(--accent-dark);border-color:var(--accent-dark)}}
.btn--ghost{{background:transparent;color:var(--ink);border-color:var(--ink)}}
.btn--ghost:hover{{background:var(--ink);color:#fff}}
.btn--on-dark{{background:transparent;color:#fff;border-color:rgba(255,255,255,.55)}}
.btn--on-dark:hover{{background:#fff;color:var(--ink);border-color:#fff}}
.btn-row{{display:flex;flex-wrap:wrap;gap:var(--s-2);margin-top:var(--s-4)}}
.link-arrow{{display:inline-flex;align-items:center;gap:10px;font-weight:700;
  font-size:.9rem;letter-spacing:.04em;border-bottom:2px solid var(--accent);
  padding-bottom:3px;transition:gap .2s}}
.link-arrow:hover{{gap:16px}}
.link-arrow svg{{width:16px;height:16px;flex:none}}

/* ============================================================ topbar */
.topbar{{background:var(--ink);color:rgba(255,255,255,.75);font-size:.82rem}}
.topbar .wrap{{display:flex;justify-content:flex-end;align-items:center;
  gap:var(--s-3);min-height:38px}}
.topbar a:hover{{color:#fff}}
@media (max-width:860px){{.topbar{{display:none}}}}

/* amprenta de culoare din capul paginii */
.hairline{{height:4px;background:linear-gradient(90deg,
  var(--accent-bright) 0%,var(--accent) 30%,var(--accent-sky) 58%,
  var(--accent-dark) 80%,var(--ink) 100%)}}

/* ============================================================ header */
.header{{position:sticky;top:0;z-index:120;background:#fff;
  border-bottom:1px solid var(--g100)}}
.header .wrap{{display:flex;align-items:center;justify-content:space-between;
  gap:var(--s-4);min-height:76px}}
.brand img{{height:40px;width:auto}}
.nav{{display:flex;align-items:center;gap:var(--s-4)}}
.nav__link{{font-size:.84rem;font-weight:700;letter-spacing:.1em;
  text-transform:uppercase;padding:28px 0;position:relative;white-space:nowrap}}
.nav__link[aria-expanded="true"],.nav__link:hover{{color:var(--accent)}}
.nav__link.is-current::after{{content:"";position:absolute;left:0;right:0;bottom:22px;
  height:3px;background:var(--accent)}}
.nav__cta{{margin-left:var(--s-2)}}
@media (max-width:1080px){{.nav,.nav__cta{{display:none}}}}

/* mega-meniu */
.mega{{position:absolute;left:0;right:0;top:100%;background:#fff;
  border-top:1px solid var(--g100);box-shadow:0 24px 48px rgba(0,0,0,.09);
  display:none}}
.mega.is-open{{display:block}}
.mega__inner{{display:grid;grid-template-columns:repeat(4,1fr);gap:var(--s-5);
  padding-block:var(--s-5)}}
.mega__col h3{{font-size:.78rem;font-weight:700;letter-spacing:.12em;
  text-transform:uppercase;color:var(--g400);margin-bottom:var(--s-2)}}
.mega__col li + li{{margin-top:10px}}
.mega__col a{{font-size:1rem;font-weight:500}}
.mega__col a:hover{{color:var(--accent)}}

/* meniul de telefon */
.burger{{display:none;width:48px;height:48px;align-items:center;justify-content:center;
  background:none;border:0;cursor:pointer}}
.burger span{{display:block;width:26px;height:2px;background:var(--ink);position:relative}}
.burger span::before,.burger span::after{{content:"";position:absolute;left:0;
  width:26px;height:2px;background:var(--ink);transition:transform .25s,top .25s}}
.burger span::before{{top:-8px}} .burger span::after{{top:8px}}
.burger[aria-expanded="true"] span{{background:transparent}}
.burger[aria-expanded="true"] span::before{{top:0;transform:rotate(45deg)}}
.burger[aria-expanded="true"] span::after{{top:0;transform:rotate(-45deg)}}
@media (max-width:1080px){{.burger{{display:flex}}}}

.drawer{{position:fixed;inset:76px 0 0;background:#fff;z-index:110;
  overflow-y:auto;padding:var(--s-4) 0 var(--s-7);display:none}}
.drawer.is-open{{display:block}}
.drawer__group + .drawer__group{{border-top:1px solid var(--g100)}}
.drawer__top{{display:flex;justify-content:space-between;align-items:center;
  width:100%;padding:18px 0;background:none;border:0;cursor:pointer;
  font-size:1rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase}}
.drawer__panel{{display:none;padding-bottom:var(--s-3)}}
.drawer__panel.is-open{{display:block}}
.drawer__panel li + li{{margin-top:12px}}
.drawer__panel a{{color:var(--g700)}}
html.nav-open{{overflow:hidden}}

/* ============================================================ hero */
.hero{{position:relative;background:var(--band);color:#fff;overflow:hidden}}
.hero__media{{position:absolute;inset:0}}
.hero__media img{{width:100%;height:100%;object-fit:cover;opacity:.45}}
.hero__media::after{{content:"";position:absolute;inset:0;
  background:linear-gradient(90deg,rgba(11,11,11,.92) 0%,rgba(11,11,11,.72) 48%,rgba(11,11,11,.35) 100%)}}
.hero__inner{{position:relative;padding-block:clamp(72px,11vw,150px);max-width:52rem}}
.hero .lede{{color:rgba(255,255,255,.8);margin-top:var(--s-3)}}
.hero .eyebrow{{color:#fff;opacity:.72}}

/* antetul paginilor interioare: text la stanga, imagine la dreapta */
.pagehead{{background:var(--band);color:#fff}}
/* .lede e gri inchis implicit: peste banda inchisa a antetului nu se citea */
.pagehead .lede{{color:rgba(255,255,255,.8)}}
.pagehead .muted{{color:rgba(255,255,255,.72)}}
.pagehead__grid{{display:grid;grid-template-columns:1fr 1fr;gap:var(--s-6);
  align-items:center;padding-block:var(--s-7)}}
.pagehead__media img{{width:100%;aspect-ratio:4/3;object-fit:cover}}
@media (max-width:860px){{
  .pagehead__grid{{grid-template-columns:1fr;gap:var(--s-4)}}
}}

/* ============================================================ breadcrumb */
.crumbs{{font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;
  color:rgba(255,255,255,.6);margin-bottom:var(--s-3)}}
.crumbs ol{{display:flex;flex-wrap:wrap;gap:8px}}
.crumbs li + li::before{{content:"/";margin-right:8px;color:rgba(255,255,255,.35)}}
.crumbs a:hover{{color:#fff}}
.crumbs [aria-current]{{color:#fff}}

/* ============================================================ cards */
.card{{display:flex;flex-direction:column;background:#fff;height:100%;
  border:1px solid var(--g100);transition:border-color .2s,transform .2s}}
a.card:hover{{border-color:var(--accent);transform:translateY(-3px)}}
.card__media{{aspect-ratio:3/2;overflow:hidden;background:var(--g100)}}
.card__media img{{width:100%;height:100%;object-fit:cover;transition:transform .5s}}
a.card:hover .card__media img{{transform:scale(1.04)}}
.card__body{{padding:var(--s-3);display:flex;flex-direction:column;gap:10px;flex:1}}
.card__meta{{font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--g400);font-weight:700}}
.card__foot{{margin-top:auto;padding-top:var(--s-2)}}

/* fise de subiect, fara imagine */
.tile{{display:block;padding:var(--s-4);background:var(--g50);height:100%;
  border-left:4px solid transparent;transition:border-color .2s,background .2s}}
a.tile:hover{{border-left-color:var(--accent);background:#fff;
  box-shadow:0 14px 34px rgba(0,0,0,.07)}}

/* lista de subiecte din pagina principala */
.topics{{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--g100)}}
.topics a{{background:#fff;padding:var(--s-3) var(--s-4);display:flex;
  align-items:center;justify-content:space-between;gap:var(--s-2);
  font-weight:500;transition:background .2s,color .2s}}
.topics a:hover{{background:var(--ink);color:#fff}}
.topics a:hover .topics__arrow{{color:var(--accent)}}
.topics__arrow{{color:var(--accent);font-weight:700}}
@media (max-width:860px){{.topics{{grid-template-columns:1fr}}}}

/* ============================================================ figures */
.stat{{border-top:3px solid var(--accent);padding-top:var(--s-2)}}
.stat__value{{font-size:clamp(2.2rem,3.6vw,3rem);font-weight:700;line-height:1;
  letter-spacing:-.02em}}
.stat__label{{color:var(--g700);font-size:var(--t-small);margin-top:8px}}

/* ============================================================ split */
.split{{display:grid;grid-template-columns:1fr 1fr;gap:var(--s-6);align-items:center}}
.split--reverse .split__media{{order:2}}
.split__media img{{width:100%;aspect-ratio:4/3;object-fit:cover}}
@media (max-width:860px){{
  .split{{grid-template-columns:1fr;gap:var(--s-4)}}
  .split--reverse .split__media{{order:0}}
}}

/* ============================================================ accordion */
.acc__item{{border-bottom:1px solid var(--g200)}}
.acc__top{{display:flex;justify-content:space-between;align-items:center;gap:var(--s-3);
  width:100%;padding:var(--s-3) 0;background:none;border:0;cursor:pointer;
  text-align:left;font-size:1.1rem;font-weight:700}}
.acc__top:hover{{color:var(--accent)}}
.acc__sign{{flex:none;width:22px;height:22px;position:relative}}
.acc__sign::before,.acc__sign::after{{content:"";position:absolute;background:var(--accent);
  transition:transform .3s}}
.acc__sign::before{{left:0;top:10px;width:22px;height:2px}}
.acc__sign::after{{left:10px;top:0;width:2px;height:22px}}
.acc__item.is-open .acc__sign::after{{transform:scaleY(0)}}
.acc__panel{{overflow:hidden;height:0;transition:height .32s cubic-bezier(.22,.61,.36,1)}}
.acc__panel p{{padding-bottom:var(--s-3);color:var(--g700);max-width:70ch}}

/* ============================================================ contact */
.contact-band{{background:var(--g50)}}
.contact-card{{display:grid;grid-template-columns:auto 1fr auto;gap:var(--s-4);
  align-items:center;background:#fff;padding:var(--s-4);border:1px solid var(--g100)}}
@media (max-width:860px){{
  .contact-card{{grid-template-columns:1fr;text-align:left}}
}}

/* ============================================================ forms */
.field{{display:block;margin-bottom:var(--s-3)}}
.field span{{display:block;font-size:.82rem;font-weight:700;letter-spacing:.08em;
  text-transform:uppercase;margin-bottom:8px}}
.field input,.field textarea,.field select{{width:100%;padding:14px 16px;
  border:1px solid var(--g200);background:#fff;font:inherit;font-size:1rem}}
.field input:focus,.field textarea:focus{{border-color:var(--accent);outline:none}}
.field textarea{{min-height:150px;resize:vertical}}

/* ============================================================ footer */
.footer{{background:var(--ink);color:rgba(255,255,255,.72)}}
.footer a:hover{{color:#fff}}
.footer__main{{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:var(--s-5);
  padding-block:var(--s-7)}}
.footer h3{{font-size:.78rem;font-weight:700;letter-spacing:.12em;
  text-transform:uppercase;color:#fff;margin-bottom:var(--s-2)}}
.footer li + li{{margin-top:10px}}
.footer__legal{{border-top:1px solid rgba(255,255,255,.14);padding-block:var(--s-3);
  display:flex;flex-wrap:wrap;gap:var(--s-3);justify-content:space-between;
  font-size:.84rem}}
.footer__legal ul{{display:flex;flex-wrap:wrap;gap:var(--s-3)}}
@media (max-width:860px){{
  .footer__main{{grid-template-columns:1fr 1fr;gap:var(--s-4)}}
}}
@media (max-width:560px){{.footer__main{{grid-template-columns:1fr}}}}

/* ============================================================ motion */
[data-reveal]{{opacity:0;transform:translateY(18px)}}
[data-reveal].is-in{{opacity:1;transform:none;
  transition:opacity .7s ease,transform .7s cubic-bezier(.22,.61,.36,1)}}
@media (prefers-reduced-motion:reduce){{
  *,*::before,*::after{{animation-duration:.01ms!important;transition-duration:.01ms!important}}
  [data-reveal]{{opacity:1;transform:none}}
  html{{scroll-behavior:auto}}
}}
"""
