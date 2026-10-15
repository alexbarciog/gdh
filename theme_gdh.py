# -*- coding: utf-8 -*-
"""Sistemul vizual GDH, pe limbajul referintei Deluix.

Alb, negru si trei griuri; culoarea vine dintr-un singur loc, degradeul in
miscare din banner (si din butonul de final), care rimeaza cu degradeul
siglei. Doua familii: un grotesc strans pentru titluri si text (Inter Tight,
in locul lui Creato Display) si un mono pentru etichete, cifre si navigatia
fina (IBM Plex Mono, exact ca in referinta).

Ritmul e cel masurat pe referinta: container pe toata latimea cu 15 px pe
margini, sectiuni de 140 px, titluri de 70-90 px cu litere stranse, butoane
pastila, etichete mono pe pastile gri de 4 px, colturi de 8 px peste tot.
"""

TOKENS = {
    # culori
    "black": "#000000",
    "ink": "#0a0a0a",
    "dark-two": "#262626",
    "white": "#ffffff",
    "light-1": "#f1f1f1",
    "light-2": "#f7f7f7",
    "light-3": "#ebebeb",
    # Referinta foloseste #7f7f7f pentru text, care are doar 3.9:1 pe alb.
    # #6b6b6b arata la fel si trece AA (5.3:1).
    "text": "#6b6b6b",
    # focusul de tastatura: singura culoare de interfata, turcoazul folosit
    # pana acum, ca sa ramana vizibil si pe alb si pe negru
    "focus": "#33c1bd",
    # tipografie
    "sans": "'GDH Sans', 'Inter Tight', system-ui, -apple-system, 'Segoe UI', Arial, sans-serif",
    "mono": "'GDH Mono', 'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, monospace",
    # ritm
    "container": "1750px",
}


def css():
    """Foaia de stil completa a site-ului."""
    t = TOKENS
    return f"""
/* ============================================================ tokens */
:root{{
  --black:{t['black']};
  --ink:{t['ink']};
  --dark-two:{t['dark-two']};
  --white:{t['white']};
  --light-1:{t['light-1']};
  --light-2:{t['light-2']};
  --light-3:{t['light-3']};
  --text:{t['text']};
  --focus:{t['focus']};
  --line:rgba(0,0,0,.08);
  --line-strong:rgba(0,0,0,.15);
  --w-06:rgba(255,255,255,.06);
  --w-12:rgba(255,255,255,.12);
  --w-15:rgba(255,255,255,.15);
  --w-20:rgba(255,255,255,.2);
  --w-40:rgba(255,255,255,.4);
  --w-60:rgba(255,255,255,.6);
  --w-70:rgba(255,255,255,.7);
  --sans:{t['sans']};
  --mono:{t['mono']};
  --container:{t['container']};
  --gutter:15px;
  --radius:8px;
  --ease:cubic-bezier(.22,.61,.36,1);

  /* scara masurata pe referinta la 1440 px, stransa fluid pe telefon */
  --t-display:clamp(2.9rem,6.25vw,5.625rem);    /* 90 */
  --t-banner:clamp(2.6rem,5.3vw,4.75rem);       /* 76 */
  --t-h2:clamp(2.3rem,4.9vw,4.375rem);          /* 70 */
  --t-h3:clamp(1.9rem,3.6vw,3.25rem);           /* 52 */
  --t-h4:clamp(1.6rem,2.5vw,2.25rem);           /* 36 */
  --t-h5:clamp(1.35rem,1.95vw,1.75rem);         /* 28 */
  --t-h6:clamp(1.15rem,1.67vw,1.5rem);          /* 24 */
  --t-sub:1.25rem;                              /* 20 */
  --t-large:1.125rem;                           /* 18 */
  --t-body:1rem;                                /* 16 */
  --t-label:.875rem;                            /* 14 */
  --t-label-s:.75rem;                           /* 12 */
  --t-giant:clamp(5rem,16.7vw,15rem);           /* 240 */

  --gap-section:clamp(88px,9.75vw,140px);
}}

/* ============================================================ reset */
*,*::before,*::after{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%;text-size-adjust:100%}}
body{{margin:0;background:var(--white);color:var(--black);
  font-family:var(--sans);font-size:var(--t-body);line-height:1.4;
  -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;
  text-rendering:optimizeLegibility}}
img,svg,video{{max-width:100%;height:auto;display:block}}
a{{color:inherit;text-decoration:none}}
button{{font:inherit;color:inherit}}
h1,h2,h3,h4,p,figure,blockquote,ul,ol{{margin:0}}
h1,h2,h3,h4{{font-weight:500}}
ul,ol{{padding:0;list-style:none}}
::selection{{background:var(--black);color:var(--white)}}

:focus-visible{{outline:2px solid var(--focus);outline-offset:3px;border-radius:4px}}
.gdh-skip{{position:absolute;left:-9999px;top:0;z-index:400;background:var(--black);
  color:#fff;padding:14px 22px;font-family:var(--mono);font-size:var(--t-label);
  text-transform:uppercase;border-radius:0 0 var(--radius) 0}}
.gdh-skip:focus{{left:0}}
.sr-only{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;
  clip:rect(0,0,0,0);white-space:nowrap;border:0}}

/* ============================================================ layout */
.wrap{{width:100%;max-width:var(--container);margin-inline:auto;
  padding-inline:var(--gutter)}}
.section{{padding-block:var(--gap-section)}}
.section--tight{{padding-block:calc(var(--gap-section) * .65)}}
.section--grey{{background:var(--light-2)}}
.section--ink{{background:var(--black);color:#fff;overflow-x:clip}}
.grid{{display:grid;gap:20px}}
.grid--2{{grid-template-columns:repeat(2,1fr)}}
.grid--3{{grid-template-columns:repeat(3,1fr)}}
.grid--4{{grid-template-columns:repeat(4,1fr)}}
@media (max-width:991px){{
  .grid--3,.grid--4{{grid-template-columns:repeat(2,1fr)}}
}}
@media (max-width:767px){{
  .grid--2,.grid--3,.grid--4{{grid-template-columns:1fr}}
}}

/* ============================================================ type */
/* eticheta mono pe pastila gri — „subtitle” in referinta */
.eyebrow{{display:inline-block;font-family:var(--mono);font-size:var(--t-label-s);
  font-weight:500;line-height:1;letter-spacing:-.04em;text-transform:uppercase;
  background:var(--light-3);color:var(--black);border-radius:4px;padding:8px 10px;
  margin-bottom:25px}}
.eyebrow--muted{{background:var(--light-1)}}
.is-dark .eyebrow,.section--ink .eyebrow,.hero .eyebrow,.statement .eyebrow{{
  background:var(--w-15);color:#fff}}
.mono{{font-family:var(--mono);font-size:var(--t-label);font-weight:500;
  letter-spacing:-.04em;text-transform:uppercase}}
.hero-title{{font-size:var(--t-display);font-weight:700;line-height:1.1;
  letter-spacing:-.033em}}
.h1{{font-size:var(--t-h2);font-weight:500;line-height:1;letter-spacing:-.03em}}
.h2{{font-size:var(--t-h5);font-weight:500;line-height:1.2;letter-spacing:-.01em}}
.h3{{font-size:var(--t-sub);font-weight:500;line-height:1.2}}
.lede{{font-size:var(--t-body);line-height:1.4;color:var(--text);max-width:62ch}}
.lede strong{{color:var(--black);font-weight:600}}
.is-dark strong,.hero strong,.section--ink strong,.statement strong{{color:#fff}}
.prose{{max-width:68ch}}
.prose p + p{{margin-top:20px}}
.muted{{color:var(--text);line-height:1.5}}
.is-dark .muted,.section--ink .muted,.section--ink .lede{{color:var(--w-60)}}

/* ============================================================ buttons */
/* Pastila cu eticheta care se rostogoleste la hover: textul e pus de doua ori,
   unul sub altul, si coloana urca cu o linie. A doua copie e aria-hidden. */
.btn{{display:inline-flex;align-items:center;gap:10px;border:1px solid transparent;
  border-radius:100px;padding:14px 22px;font-size:var(--t-body);font-weight:600;
  line-height:1.5;cursor:pointer;white-space:nowrap;
  transition:background .3s,color .3s,border-color .3s,translate .5s var(--ease)}}
.btn__clip{{display:block;height:1.5em;overflow:hidden}}
.btn__track{{display:flex;flex-direction:column;transition:transform .45s var(--ease)}}
.btn__track > span{{display:block;height:1.5em}}
.btn:hover .btn__track,.btn:focus-visible .btn__track{{transform:translateY(-50%)}}
.btn__icon{{display:block;width:18px;height:18px;overflow:hidden;position:relative;flex:none}}
.btn__icon svg{{position:absolute;inset:0;width:18px;height:18px;
  transition:transform .45s var(--ease)}}
.btn__icon svg + svg{{transform:translate(-120%,120%)}}
.btn:hover .btn__icon svg:first-child{{transform:translate(120%,-120%)}}
.btn:hover .btn__icon svg + svg{{transform:none}}
.btn--primary,.btn--grad{{background:var(--black);color:#fff}}
.btn--ghost{{background:transparent;color:var(--black);border-color:var(--line-strong)}}
.btn--ghost:hover{{border-color:var(--black)}}
.btn--light{{background:#fff;color:var(--black)}}
.btn--on-dark{{background:transparent;color:#fff;border-color:var(--w-20)}}
.btn--on-dark:hover{{border-color:#fff}}
.is-dark .btn--primary,.hero .btn--primary,.section--ink .btn--primary,
.cta .btn--primary,.statement .btn--primary{{background:#fff;color:var(--black)}}
.btn--sm{{padding:10px 17px;font-weight:500}}
.btn-row{{display:flex;flex-wrap:wrap;gap:12px;margin-top:32px}}

/* legatura subliniata, mono — „link-block” in referinta */
.link-arrow{{display:inline-flex;align-items:center;justify-content:space-between;
  gap:30px;border-bottom:1px solid currentColor;padding-bottom:8px;
  font-family:var(--mono);font-size:var(--t-label);font-weight:500;line-height:1.1;
  letter-spacing:-.04em;text-transform:uppercase;transition:gap .3s var(--ease)}}
.link-arrow:hover{{gap:42px}}
.link-arrow svg{{width:16px;height:16px;flex:none}}

/* ============================================================ header */
.chrome{{position:fixed;top:0;left:0;right:0;z-index:200;
  transition:transform .45s var(--ease)}}
.chrome.is-hidden{{transform:translateY(-100%)}}
.header{{position:relative;color:var(--black);
  transition:background .35s,color .35s,border-color .35s,backdrop-filter .35s;
  border-bottom:1px solid transparent}}
.header > .wrap{{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;
  gap:15px;min-height:84px;transition:min-height .3s}}
/* peste banner (doar pe prima pagina) antetul e alb pe transparent */
.chrome--over .header{{color:#fff}}
.chrome.is-scrolled .header{{background:rgba(255,255,255,.86);color:var(--black);
  -webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);
  border-bottom-color:var(--line)}}
.chrome.is-scrolled .header > .wrap{{min-height:68px}}
.brand{{position:relative;display:inline-flex;justify-self:start}}
.brand img{{height:38px;width:auto}}
.brand__light{{position:absolute;inset:0;opacity:0;transition:opacity .3s}}
.brand__ink{{transition:opacity .3s}}
.chrome--over:not(.is-scrolled):not(.mega-open) .brand__ink{{opacity:0}}
.chrome--over:not(.is-scrolled):not(.mega-open) .brand__light{{opacity:1}}

.nav{{display:flex;align-items:center;gap:clamp(28px,4.4vw,80px)}}
.nav__link{{display:inline-flex;align-items:flex-start;gap:4px;font-size:var(--t-body);
  line-height:1;padding:12px 0;white-space:nowrap;transition:opacity .25s}}
.nav__link sup{{font-family:var(--mono);font-size:.625rem;line-height:1;
  letter-spacing:-.02em;opacity:.9;top:-.1em;position:relative}}
.nav:hover .nav__link{{opacity:.55}}
.nav .nav__link:hover,.nav .nav__link[aria-expanded="true"]{{opacity:1}}
.nav__link.is-current{{text-decoration:underline;text-underline-offset:6px;
  text-decoration-thickness:1px}}
.header__actions{{display:flex;align-items:center;justify-content:flex-end;gap:10px}}
.nav__cta{{background:var(--black);color:#fff}}
.chrome--over:not(.is-scrolled):not(.mega-open) .nav__cta{{background:#fff;color:var(--black)}}
/* butonul „Menu”: pastila conturata, doua linii */
.burger{{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--line-strong);
  background:none;border-radius:100px;padding:9px 17px;cursor:pointer;color:inherit;
  font-size:var(--t-body);font-weight:500;line-height:1.5;transition:border-color .3s}}
.chrome--over:not(.is-scrolled):not(.mega-open) .burger{{border-color:var(--w-15)}}
.burger:hover{{border-color:currentColor}}
.burger__lines{{display:flex;flex-direction:column;gap:4px;width:16px}}
.burger__lines i{{display:block;height:2px;background:currentColor;transition:transform .3s}}
.burger[aria-expanded="true"] .burger__lines i:first-child{{transform:translateY(3px) rotate(45deg)}}
.burger[aria-expanded="true"] .burger__lines i:last-child{{transform:translateY(-3px) rotate(-45deg)}}
@media (max-width:1180px){{
  .header > .wrap{{grid-template-columns:auto 1fr}}
  .nav{{display:none}}
}}
@media (max-width:560px){{
  .nav__cta{{display:none}}
  .brand img{{height:32px}}
}}

/* mega-meniu: panou alb, rotunjit, sub antet */
.mega{{position:absolute;left:var(--gutter);right:var(--gutter);top:calc(100% + 8px);
  display:none;color:var(--black);background:#fff;border-radius:var(--radius);
  max-height:calc(100vh - var(--chrome-h,84px) - 24px);overflow-y:auto;
  box-shadow:0 30px 80px rgba(0,0,0,.18),0 0 0 1px var(--line)}}
.mega.is-open{{display:block;animation:mega-in .35s var(--ease)}}
@keyframes mega-in{{from{{opacity:0;transform:translateY(-8px)}}to{{opacity:1;transform:none}}}}
.mega .wrap{{padding:40px 40px 40px;max-width:none}}
.mega__top{{display:flex;justify-content:space-between;align-items:flex-start;
  gap:20px;margin-bottom:40px;padding-bottom:30px;border-bottom:1px solid var(--line)}}
.mega__eyebrow{{display:inline-block;font-family:var(--mono);font-size:var(--t-label-s);
  font-weight:500;letter-spacing:-.04em;text-transform:uppercase;background:var(--light-3);
  border-radius:4px;padding:8px 10px;margin-bottom:18px}}
.mega__title{{font-size:var(--t-h4);font-weight:500;line-height:1.1;letter-spacing:-.03em}}
.mega__close{{display:inline-flex;align-items:center;gap:8px;background:none;
  border:1px solid var(--line-strong);border-radius:100px;color:var(--black);
  cursor:pointer;font-size:var(--t-body);font-weight:500;padding:9px 17px}}
.mega__close:hover{{border-color:var(--black)}}
.mega__close svg{{width:14px;height:14px}}
.mega__grid{{display:grid;width:100%;grid-template-columns:repeat(4,1fr);gap:34px 30px;
  counter-reset:mega}}
.mega__item{{display:block;counter-increment:mega}}
.mega__label{{display:flex;align-items:baseline;gap:10px;font-size:var(--t-sub);
  font-weight:500;line-height:1.2;transition:opacity .25s}}
.mega__label::before{{content:"/" counter(mega,decimal-leading-zero);font-family:var(--mono);
  font-size:var(--t-label-s);color:var(--text);letter-spacing:-.04em}}
.mega__chev{{display:none}}
.mega__grid:hover .mega__label{{opacity:.45}}
.mega__item:hover .mega__label{{opacity:1}}
.mega__desc{{display:block;margin-top:8px;padding-left:34px;font-size:.9rem;
  line-height:1.45;color:var(--text);max-width:34ch}}
.mega__cta{{display:flex;align-items:center;justify-content:space-between;gap:20px;
  margin-top:40px;padding:22px 26px;border-radius:var(--radius);color:#fff;
  background:var(--black) url(../img/banner-poster.webp) center/cover no-repeat}}
.mega__cta-title{{display:inline-flex;align-items:center;gap:10px;font-weight:600;
  font-size:var(--t-sub)}}
.mega__cta-title svg{{width:16px;height:16px;flex:none}}
.mega__cta-text{{display:block;color:var(--w-70);font-size:.95rem;text-align:right}}
@media (max-width:1400px){{
  .mega__grid{{grid-template-columns:repeat(3,1fr)}}
}}
/* cat timp panoul e deschis, antetul e alb, ca sa se lege de panou */
.chrome.mega-open .header{{background:#fff;color:var(--black);border-bottom-color:var(--line)}}

/* meniul complet (butonul „Menu”): panou alb peste pagina */
.drawer{{position:fixed;inset:0;z-index:300;background:rgba(0,0,0,.45);display:none;
  -webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}}
.drawer.is-open{{display:block}}
.drawer__panel{{position:absolute;top:var(--gutter);left:var(--gutter);right:var(--gutter);
  max-height:calc(100% - 2 * var(--gutter));overflow-y:auto;background:#fff;
  border-radius:var(--radius);padding:24px clamp(20px,3vw,40px) 40px;
  animation:mega-in .4s var(--ease)}}
.drawer__head{{display:flex;justify-content:space-between;align-items:center;
  padding-bottom:24px;margin-bottom:36px;border-bottom:1px solid var(--line)}}
.drawer__head img{{height:34px;width:auto}}
.drawer__cols{{display:grid;grid-template-columns:repeat(3,1fr) minmax(240px,.8fr);gap:40px 30px}}
.drawer__title{{font-family:var(--mono);font-size:var(--t-label);font-weight:500;
  letter-spacing:-.04em;text-transform:uppercase;color:var(--text);margin-bottom:22px}}
.drawer__list li + li{{margin-top:10px}}
.drawer__list a{{font-size:var(--t-h5);font-weight:500;letter-spacing:-.01em;line-height:1.15;
  transition:opacity .25s}}
.drawer__list:hover a{{opacity:.45}}
.drawer__list a:hover{{opacity:1}}
.drawer__aside{{background:var(--light-2);border-radius:var(--radius);padding:24px;
  display:flex;flex-direction:column;gap:14px;align-self:start}}
.drawer__aside a{{font-size:var(--t-sub);font-weight:500}}
.drawer__aside p{{color:var(--text);font-size:.95rem}}
@media (max-width:991px){{
  .drawer__cols{{grid-template-columns:1fr 1fr}}
}}
@media (max-width:560px){{
  .drawer__cols{{grid-template-columns:1fr;gap:34px}}
  .drawer__list a{{font-size:1.4rem}}
}}
html.nav-open{{overflow:hidden}}

/* ============================================================ hero (home) */
.hero{{position:relative;min-height:max(100vh,680px);color:#fff;background:var(--black);
  overflow:hidden;isolation:isolate}}
.hero__media{{position:absolute;inset:0;z-index:-1}}
.hero__media video,.hero__media img{{width:100%;height:100%;object-fit:cover}}
/* un voal mic: degradeul e intunecat oricum, dar zonele roz trebuie domolite
   sub textul alb */
.hero__media::after{{content:"";position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(0,0,0,.35),rgba(0,0,0,.05) 40%,rgba(0,0,0,.45))}}
.hero__inner{{min-height:max(100vh,680px);display:flex;flex-direction:column;
  justify-content:space-between;gap:40px;padding-top:150px;padding-bottom:40px;position:relative}}
.hero__top{{display:flex;align-items:flex-start;justify-content:space-between;gap:40px}}
.hero__copy{{max-width:960px}}
.hero .hero-title{{mix-blend-mode:exclusion;margin-bottom:40px;padding-bottom:6px}}
.hero__side{{width:100%;max-width:417px;display:flex;flex-direction:column;gap:56px;
  padding-top:140px}}
.hero__list-title{{display:flex;align-items:center;gap:8px;font-family:var(--mono);
  font-size:var(--t-label);font-weight:500;letter-spacing:-.04em;color:#fff;margin-bottom:18px}}
.hero__list-title::before{{content:"";width:8px;height:8px;border:1px solid #fff;
  transform:rotate(45deg)}}
.hero__list li{{display:block}}
.hero__list a{{display:flex;align-items:center;gap:10px;padding:9px 0;
  font-family:var(--mono);font-size:var(--t-label);font-weight:500;letter-spacing:-.04em;
  text-transform:uppercase}}
.hero__list .n{{flex:none}}
.hero__list .rule{{flex:1;height:1px;background:var(--w-70);opacity:.2}}
.hero__list .t{{flex:none;color:var(--w-70);transition:color .25s}}
.hero__list a:hover .t{{color:#fff}}
.hero__list svg{{width:12px;height:12px;flex:none;transition:transform .3s var(--ease)}}
.hero__list a:hover svg{{transform:rotate(45deg)}}
.hero .lede{{font-size:var(--t-h5);font-weight:500;line-height:1.2;letter-spacing:-.01em;
  color:#fff;max-width:540px}}
.hero .lede strong{{font-weight:500;color:var(--w-70)}}
.hero__info{{display:flex;align-items:center;justify-content:space-between;gap:20px;
  border-top:1px solid var(--w-15);padding-top:40px}}
.hero__badge{{display:flex;align-items:center;gap:14px}}
.hero__badge img{{height:48px;width:auto}}
.hero__badge strong{{display:block;font-size:var(--t-large);font-weight:500;color:#fff}}
.hero__badge span{{display:block;margin-top:4px;font-family:var(--mono);
  font-size:var(--t-label-s);font-weight:500;letter-spacing:-.04em;text-transform:uppercase;
  color:var(--w-70)}}
.hero__where{{border-left:1px solid var(--w-20);padding-left:12px;display:flex;
  flex-direction:column;gap:8px;font-family:var(--mono);font-size:var(--t-label);
  font-weight:500;letter-spacing:-.04em;text-transform:uppercase}}
.hero__where span:first-child{{color:var(--w-70)}}
.hero__where .dot{{display:inline-block;width:4px;height:4px;border-radius:50%;
  background:#fff;margin:0 8px;vertical-align:middle}}
/* linia verticala din mijloc, cu crucea */
.hero__axis{{position:absolute;top:0;bottom:0;left:50%;width:13px;margin-left:-6px;
  display:flex;align-items:center;justify-content:center;pointer-events:none;z-index:0}}
.hero__axis::before{{content:"";position:absolute;top:0;bottom:0;left:6px;width:1px;
  background:var(--w-20)}}
.hero__axis svg{{position:relative;width:13px;height:13px}}
@media (max-width:991px){{
  .hero__top{{flex-direction:column}}
  .hero__side{{padding-top:0;max-width:540px;gap:36px}}
  .hero__axis{{display:none}}
  .hero .hero-title{{mix-blend-mode:normal}}
}}
@media (max-width:640px){{
  .hero__inner{{padding-top:120px}}
  .hero__info{{flex-direction:column;align-items:flex-start}}
}}

/* ============================================================ inner banner */
.pagehead{{background:#fff;color:var(--black);padding-top:clamp(140px,13.2vw,190px);
  padding-bottom:clamp(30px,4vw,60px)}}
.pagehead__grid{{display:flex;justify-content:space-between;align-items:flex-end;gap:40px}}
.pagehead__title{{max-width:1100px}}
.pagehead .h1{{font-size:var(--t-display);font-weight:500;line-height:1;letter-spacing:-.04em}}
.pagehead__lede{{margin-top:26px;max-width:480px}}
.pagehead__title .btn-row{{margin-top:28px}}
.pagehead__fig{{flex:none;font-size:var(--t-display);font-weight:500;line-height:.9;
  letter-spacing:-.05em;white-space:nowrap;font-variant-numeric:tabular-nums}}
.pagehead__media{{margin-top:clamp(40px,4.2vw,60px);border-radius:var(--radius);overflow:hidden;
  background:var(--light-2);transform-origin:center top}}
.pagehead__media img{{width:100%;aspect-ratio:21/9;object-fit:cover}}
/* fatada GDH: firma e sus, in stanga — taietura lata nu trebuie sa o retezeze */
img[src*="gdh-warehouse-front"]{{object-position:center 12%}}
@media (max-width:991px){{
  .pagehead__grid{{flex-direction:column;align-items:flex-start}}
  .pagehead__fig{{font-size:var(--t-h3)}}
  .pagehead__media img{{aspect-ratio:16/10}}
}}

/* ============================================================ detail page */
/* „service details” din referinta: card gri lipit in stanga, randuri in dreapta */
.detail{{display:grid;grid-template-columns:minmax(260px,1fr) 2.7fr;gap:clamp(20px,2.5vw,40px);
  align-items:start}}
.dcard{{position:sticky;top:100px;background:var(--light-1);border-radius:var(--radius);
  padding:20px;min-height:405px;display:flex;flex-direction:column;justify-content:space-between;
  gap:60px}}
.dcard__label{{font-family:var(--mono);font-size:var(--t-label-s);font-weight:500;
  letter-spacing:-.04em;text-transform:uppercase}}
.dcount .dcard__label{{color:var(--text);margin-top:10px}}
.dcard__tags{{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}}
.dcard__tags > *{{background:#fff;border-radius:4px;padding:8px 10px;font-family:var(--mono);
  font-size:var(--t-label-s);font-weight:500;letter-spacing:-.04em;text-transform:uppercase;
  line-height:1.2;transition:background .25s,color .25s}}
.dcard__tags a:hover{{background:var(--black);color:#fff}}
.dcard__mail{{display:block;margin-top:10px;font-size:var(--t-sub);font-weight:500;
  word-break:break-word}}
.dcard__mail:hover{{text-decoration:underline;text-underline-offset:4px}}
.count{{font-size:clamp(3.5rem,6vw,5.6rem);font-weight:500;line-height:.9;letter-spacing:-.05em;
  font-variant-numeric:tabular-nums}}
.dinfo{{margin:0;display:flex;flex-direction:column;gap:14px}}
.dinfo > div{{border-top:1px solid var(--line-strong);padding-top:12px}}
.dinfo dt{{font-family:var(--mono);font-size:var(--t-label-s);font-weight:500;letter-spacing:-.04em;
  text-transform:uppercase;color:var(--text)}}
.dinfo dd{{margin:6px 0 0;font-size:var(--t-large);font-weight:500}}
.drows > div{{display:grid;grid-template-columns:1fr 2.2fr;gap:20px;padding-block:0 60px;
  scroll-margin-top:110px}}
.drows .h2{{font-size:var(--t-h5);line-height:1.1;letter-spacing:-.02em}}
.drows .muted{{line-height:1.6}}
.pcards{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:0 0 70px}}
.pcard{{background:var(--light-1);border-radius:var(--radius);padding:20px;min-height:330px;
  display:flex;flex-direction:column;justify-content:space-between;gap:40px}}
.pcards > .pcard:last-child:nth-child(odd){{grid-column:1 / -1;min-height:240px}}
.pcard__top{{display:flex;justify-content:space-between;align-items:flex-start;gap:16px}}
.pcard h3{{position:relative;padding-left:16px;font-size:var(--t-h6);line-height:1.15;
  letter-spacing:-.01em;max-width:14ch}}
.pcard h3::before{{content:"";position:absolute;left:0;top:2px;bottom:2px;width:4px;
  background:var(--black);transform-origin:top}}
.pcard__n{{font-family:var(--mono);font-size:var(--t-label-s);font-weight:500;letter-spacing:-.04em}}
.pcard p{{color:var(--text);line-height:1.5;max-width:42ch}}
.duo{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}
.duo__img{{border-radius:var(--radius);overflow:hidden}}
.duo__img img{{width:100%;aspect-ratio:4/3;object-fit:cover}}
.detail .article{{margin:0;max-width:820px}}
@media (max-width:991px){{
  .detail{{grid-template-columns:1fr}}
  .dcard{{position:relative;top:0;min-height:0;gap:40px}}
}}
@media (max-width:640px){{
  .drows > div{{grid-template-columns:1fr;gap:12px;padding-bottom:44px}}
  .pcards,.duo{{grid-template-columns:1fr}}
  .pcards > .pcard{{min-height:0}}
}}

/* ============================================================ breadcrumb */
.crumbs{{font-family:var(--mono);font-size:var(--t-label-s);font-weight:500;
  letter-spacing:-.04em;text-transform:uppercase;color:var(--text);margin-bottom:28px}}
.crumbs ol{{display:flex;flex-wrap:wrap;gap:8px}}
.crumbs li + li::before{{content:"/";margin-right:8px;opacity:.5}}
.crumbs a:hover{{color:var(--black)}}
.crumbs [aria-current]{{color:var(--black)}}

/* ============================================================ section head */
.shead{{display:flex;justify-content:space-between;align-items:flex-start;gap:20px;
  margin-bottom:clamp(44px,5.2vw,75px)}}
.shead__title{{max-width:920px}}
.shead__side{{width:100%;max-width:320px;display:flex;flex-direction:column;
  align-items:flex-end;gap:24px;text-align:right}}
.shead__side .lede{{color:var(--text)}}
.section--ink .shead__side .lede,.is-dark .shead__side .lede{{color:var(--w-60)}}
.shead--center{{flex-direction:column;align-items:center;text-align:center}}
.shead--center .shead__title{{margin-inline:auto}}
@media (max-width:767px){{
  .shead{{flex-direction:column}}
  .shead__side{{align-items:flex-start;text-align:left}}
}}

/* ============================================================ cards */
.card{{display:flex;flex-direction:column;height:100%;position:relative;color:var(--black)}}
.card__media{{border-radius:var(--radius);overflow:hidden;margin-bottom:20px;
  aspect-ratio:4/3;background:var(--light-2);position:relative}}
.card__media img{{width:100%;height:100%;object-fit:cover;transition:transform .8s var(--ease)}}
a.card:hover .card__media img{{transform:scale(1.05)}}
.card__tag{{position:absolute;top:10px;left:10px;z-index:1;background:#fff;
  font-family:var(--mono);font-size:var(--t-label-s);font-weight:500;letter-spacing:-.04em;
  text-transform:uppercase;border-radius:4px;padding:8px 10px;line-height:1}}
.card__body{{display:flex;flex-direction:column;gap:12px;flex:1}}
.card__meta{{display:flex;flex-wrap:wrap;align-items:center;gap:10px;font-family:var(--mono);
  font-size:var(--t-label-s);font-weight:500;letter-spacing:-.04em;text-transform:uppercase;
  line-height:1}}
.card__meta .chip{{background:var(--light-3);border-radius:4px;padding:8px 10px}}
.card .h3{{font-size:var(--t-h6);font-weight:500;line-height:1.2}}
.card__foot{{margin-top:auto;padding-top:8px}}
.card__foot .link-arrow{{border-bottom-color:transparent;padding-bottom:0}}
a.card:hover .card__foot .link-arrow{{gap:42px}}
/* carduri fara imagine: un bloc gri, cu legatura jos */
.card--text{{background:var(--light-2);border-radius:var(--radius);padding:30px;
  min-height:330px;transition:background .35s}}
a.card--text:hover{{background:var(--light-3)}}
.card--text .card__body{{gap:18px}}
.card--text .h3{{font-size:var(--t-h5);letter-spacing:-.01em}}

/* fise de subiect, fara imagine */
.tile{{display:flex;flex-direction:column;justify-content:space-between;gap:60px;
  padding:28px;background:var(--light-2);border-radius:var(--radius);height:100%;
  min-height:300px;color:var(--black);transition:background .35s,color .35s}}
.tile__top{{display:flex;justify-content:space-between;align-items:flex-start;gap:20px}}
.tile__num{{font-family:var(--mono);font-size:var(--t-label-s);font-weight:500;
  letter-spacing:-.04em;text-transform:uppercase}}
.tile .h3{{font-size:var(--t-h5);letter-spacing:-.01em}}
.tile svg{{width:18px;height:18px;transition:transform .35s var(--ease)}}
a.tile:hover{{background:var(--black);color:#fff}}
a.tile:hover .muted{{color:var(--w-60)}}
a.tile:hover svg{{transform:rotate(45deg)}}

/* lista „de unde incep” — randuri numerotate, ca lista din banner */
.topics{{display:grid;grid-template-columns:repeat(3,1fr);gap:0 30px;counter-reset:topic;
  border-top:1px solid var(--line)}}
.topics a{{display:flex;align-items:center;gap:16px;padding:26px 0;
  border-bottom:1px solid var(--line);counter-increment:topic;font-size:var(--t-sub);
  font-weight:500;transition:padding .35s var(--ease)}}
.topics a::before{{content:"/" counter(topic,decimal-leading-zero);font-family:var(--mono);
  font-size:var(--t-label);color:var(--text);letter-spacing:-.04em;flex:none;width:42px}}
.topics a:hover{{padding-left:10px}}
.topics__arrow{{margin-left:auto;display:inline-flex;transition:transform .35s var(--ease)}}
.topics__arrow svg{{width:16px;height:16px}}
.topics a:hover .topics__arrow{{transform:rotate(-45deg)}}
@media (max-width:991px){{.topics{{grid-template-columns:1fr 1fr}}}}
@media (max-width:640px){{.topics{{grid-template-columns:1fr}}}}

/* ============================================================ figures */
/* „about counter”: chenar, eticheta sus, cifra mare jos in dreapta, banda gri */
.stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:15px}}
.stat{{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:var(--radius);
  overflow:hidden;background:#fff}}
.stat__top{{display:flex;flex-direction:column;justify-content:space-between;gap:56px;
  padding:20px 20px 16px;flex:1}}
.stat__num{{font-family:var(--mono);font-size:var(--t-label-s);font-weight:500;
  letter-spacing:-.04em;text-transform:uppercase}}
.stat__value{{align-self:flex-end;font-size:clamp(3rem,5.6vw,5rem);font-weight:500;
  line-height:.9;letter-spacing:-.05em}}
.stat__label{{background:var(--light-2);padding:14px 20px;font-family:var(--mono);
  font-size:var(--t-label-s);font-weight:500;letter-spacing:-.04em;text-transform:uppercase;
  color:var(--text)}}
.section--ink .stat{{background:transparent;border-color:var(--w-15)}}
.section--ink .stat__label{{background:var(--w-06);color:var(--w-60)}}
@media (max-width:991px){{.stats{{grid-template-columns:1fr 1fr}}}}
@media (max-width:480px){{.stats{{grid-template-columns:1fr}}}}

/* titlul urias, alb pe negru — „awards + recognition” in referinta */
.giant{{font-size:clamp(3.6rem,10.5vw,9.5rem);font-weight:500;line-height:.9;
  letter-spacing:-.045em;text-transform:uppercase;margin-bottom:clamp(50px,6vw,90px)}}
.giant span{{display:block}}
.giant span + span{{padding-left:clamp(40px,25vw,420px)}}

/* banda care curge: text urias, gri deschis */
.marquee{{overflow:hidden;white-space:nowrap;user-select:none;pointer-events:none;
  padding-block:10px}}
.marquee__track{{display:inline-flex;animation:marquee 38s linear infinite}}
.marquee__track span{{font-size:var(--t-giant);font-weight:500;line-height:.8;
  letter-spacing:-.05em;text-transform:uppercase;color:rgba(0,0,0,.12);padding-right:.35em}}
@keyframes marquee{{to{{transform:translateX(-50%)}}}}

/* ============================================================ split */
.split{{display:grid;grid-template-columns:1fr 1fr;gap:clamp(30px,5vw,80px);align-items:center}}
.split--reverse .split__media{{order:2}}
.split__media{{border-radius:var(--radius);overflow:hidden}}
.split__media img{{width:100%;aspect-ratio:4/3;object-fit:cover}}
.split .h1{{font-size:var(--t-h3);letter-spacing:-.02em;line-height:1.05}}
@media (max-width:860px){{
  .split{{grid-template-columns:1fr}}
  .split--reverse .split__media{{order:0}}
}}

/* proiectele din referinta: imagine, nume + eticheta in dreapta, text sub */
.feature{{display:block;color:var(--black)}}
.feature__media{{border-radius:var(--radius);overflow:hidden;position:relative;
  margin-bottom:15px;background:var(--light-3)}}
.feature__media img{{width:100%;aspect-ratio:16/10;object-fit:cover;
  transition:transform .8s var(--ease)}}
a.feature:hover .feature__media img{{transform:scale(1.04)}}
.feature__row{{display:flex;justify-content:space-between;align-items:center;gap:10px;
  margin-bottom:4px}}
.feature__name{{font-size:var(--t-sub);font-weight:500}}
.feature__where{{font-family:var(--mono);font-size:var(--t-label);font-weight:500;
  letter-spacing:-.04em;text-transform:uppercase;color:var(--text)}}
.features{{display:grid;grid-template-columns:1fr 1.35fr;gap:20px;align-items:end}}
.features > :nth-child(2){{margin-top:clamp(0px,10vw,160px)}}
@media (max-width:767px){{
  .features{{grid-template-columns:1fr;gap:40px}}
  .features > :nth-child(2){{margin-top:0}}
}}

/* ============================================================ services (home) */
.svc{{display:grid;grid-template-columns:minmax(260px,400px) 1fr;gap:clamp(20px,2.5vw,40px);
  align-items:start}}
.svc__aside{{position:sticky;top:110px}}
.svc__label{{font-family:var(--mono);font-size:var(--t-label);font-weight:500;
  letter-spacing:-.04em;text-transform:uppercase;margin-bottom:15px;color:#fff}}
.svc__media{{border-radius:var(--radius);overflow:hidden;background:var(--dark-two);
  aspect-ratio:4/3;position:relative}}
.svc__media img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  opacity:0;transition:opacity .5s var(--ease)}}
.svc__media img{{transform:scale(1.08);transition:opacity .6s var(--ease),transform 1.4s var(--ease)}}
.svc__media img.is-on{{opacity:1;transform:none}}
.svc__list{{display:flex;flex-direction:column;gap:10px}}
.svc__item{{border-radius:var(--radius);border:1px solid var(--w-12);
  transition:background .4s var(--ease),border-color .4s}}
.svc__head{{display:block;width:100%;text-align:left;background:none;border:0;cursor:pointer;
  padding:18px 22px;font-size:var(--t-h3);font-weight:500;line-height:1.05;
  letter-spacing:-.02em;color:var(--w-40);transition:color .3s}}
.svc__head:hover{{color:#fff}}
.svc__body{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .45s var(--ease)}}
.svc__body > div{{overflow:hidden}}
.svc__inner{{padding:0 22px 22px;display:flex;flex-direction:column;gap:22px}}
.svc__inner p{{color:var(--text);max-width:52ch}}
.svc__tags{{display:flex;flex-wrap:wrap;gap:8px}}
.svc__tags span{{background:var(--light-3);border-radius:4px;padding:8px 10px;
  font-family:var(--mono);font-size:var(--t-label-s);font-weight:500;letter-spacing:-.04em;
  text-transform:uppercase;color:var(--black);line-height:1}}
.svc__more{{display:flex;justify-content:space-between;align-items:center;
  border-top:1px solid var(--line);padding-top:18px;font-family:var(--mono);
  font-size:var(--t-label);font-weight:500;letter-spacing:-.04em;text-transform:uppercase;
  color:var(--black)}}
.svc__more svg{{width:16px;height:16px;transition:transform .35s var(--ease)}}
.svc__more:hover svg{{transform:translateX(6px)}}
.svc__item.is-active{{background:#fff;border-color:#fff}}
.svc__item.is-active .svc__head{{color:var(--black)}}
.svc__item.is-active .svc__body{{grid-template-rows:1fr}}
@media (max-width:860px){{
  .svc{{grid-template-columns:1fr}}
  .svc__aside{{position:relative;top:0}}
  .svc__media{{aspect-ratio:16/9}}
}}

/* ============================================================ process */
/* cele patru romburi in jurul crucii — „how we works” */
.process{{position:relative;display:grid;grid-template-columns:1fr auto 1fr;
  grid-template-rows:auto auto auto;gap:30px 0;justify-items:center;align-items:center;
  max-width:1200px;margin-inline:auto}}
.process::before,.process::after{{content:"";position:absolute;background:var(--line);z-index:0}}
.process::before{{left:50%;top:0;bottom:0;width:1px}}
.process::after{{top:50%;left:0;right:0;height:1px}}
.process__core{{grid-column:2;grid-row:2;position:relative;z-index:1;background:#fff;
  padding:30px;text-align:center;display:flex;flex-direction:column;align-items:center;gap:16px}}
.process__core p{{font-size:var(--t-h6);font-weight:500;line-height:1.2}}
.process__core p span{{display:block;color:var(--text)}}
.process__step{{position:relative;z-index:1;display:flex;flex-direction:column;
  align-items:center;gap:20px;text-align:center;max-width:300px;background:#fff;padding:14px}}
.process__step:nth-child(1){{grid-column:2;grid-row:1}}
.process__step:nth-child(2){{grid-column:1;grid-row:2;justify-self:start}}
.process__step:nth-child(3){{grid-column:3;grid-row:2;justify-self:end}}
.process__step:nth-child(4){{grid-column:2;grid-row:3}}
.diamond{{width:150px;height:150px;display:grid;place-items:center;position:relative}}
.diamond::before{{content:"";position:absolute;inset:22px;background:var(--light-1);
  border-radius:22px;transform:rotate(45deg);transition:background .35s,transform .6s var(--ease)}}
.process__step:hover .diamond::before{{background:var(--black);transform:rotate(135deg)}}
.diamond > span{{position:relative;display:flex;flex-direction:column;align-items:center;gap:6px;
  transition:color .35s}}
.process__step:hover .diamond > span{{color:#fff}}
.diamond b{{font-family:var(--mono);font-size:var(--t-label-s);font-weight:500;
  letter-spacing:-.04em}}
.diamond i{{font-style:normal;font-size:var(--t-body);font-weight:600;max-width:9ch;line-height:1.15}}
.process__step p{{color:var(--text);font-size:.95rem;line-height:1.45}}
@media (max-width:860px){{
  .process{{grid-template-columns:1fr;gap:10px}}
  .process::before,.process::after{{display:none}}
  .process__step,.process__core{{grid-column:1!important;grid-row:auto!important;
    justify-self:center!important}}
  .process__core{{order:5;padding-top:20px}}
}}

/* ============================================================ treatments
   Paginile de sector si de serviciu au acelasi model de continut, deci daca
   randam mereu la fel ies identice. Astea sunt formele din care se compune
   ritmul fiecarei pagini. */

/* declaratia de deschidere: text mare, cu cuvintele care se aprind la derulare */
.lead-say{{display:grid;grid-template-columns:minmax(120px,1fr) 3fr;gap:20px}}
.lead-say__label{{padding-top:12px}}
.lead-say .words{{font-size:var(--t-h3);line-height:1.1;font-weight:500;letter-spacing:-.02em;
  color:var(--black);max-width:30ch}}
.lead-say .words strong{{font-weight:500}}
.words .w{{transition:color .3s}}
html.js .words .w{{color:rgba(0,0,0,.18)}}
html.js .words .w.is-lit{{color:inherit}}
.lead-rule{{display:none}}
@media (max-width:767px){{.lead-say{{grid-template-columns:1fr}}}}

/* pasi numerotati */
.step{{display:grid;grid-template-columns:minmax(80px,1fr) 2fr 2fr;gap:20px;
  padding-block:34px;border-top:1px solid var(--line)}}
.step:last-child{{border-bottom:1px solid var(--line)}}
.step__num{{font-family:var(--mono);font-size:var(--t-label);font-weight:500;
  letter-spacing:-.04em}}
.step h3{{font-size:var(--t-h5);font-weight:500;letter-spacing:-.01em;line-height:1.15}}
@media (max-width:767px){{
  .step{{grid-template-columns:1fr;gap:10px}}
}}

/* banda cu o singura fraza, pe degradeul din banner */
.statement{{padding-block:15px;background:#fff}}
.statement__box{{border-radius:var(--radius);color:#fff;padding:clamp(40px,6vw,90px) clamp(24px,4vw,60px);
  background:var(--black) url(../img/banner-poster.webp) center/cover no-repeat}}
.statement__text{{font-size:var(--t-h5);line-height:1.25;font-weight:500;letter-spacing:-.01em;
  max-width:46ch}}

/* proza pe doua coloane */
.prose--two{{max-width:none;display:grid;grid-template-columns:1fr 1fr;gap:50px clamp(30px,5vw,80px)}}
.prose--two .h2{{margin-bottom:14px}}
@media (max-width:860px){{.prose--two{{grid-template-columns:1fr}}}}

/* randuri de proza: titlul in stanga, textul in dreapta */
.rows > div{{display:grid;grid-template-columns:2fr 3fr;gap:20px;padding-block:34px;
  border-top:1px solid var(--line)}}
.rows > div:last-child{{border-bottom:1px solid var(--line)}}
.rows .muted{{font-size:var(--t-large);line-height:1.5}}
.section--ink .rows > div{{border-color:var(--w-15)}}
@media (max-width:767px){{.rows > div{{grid-template-columns:1fr}}}}
/* articolele: o coloana de citit */
.article{{max-width:760px;margin-inline:auto}}
.article p{{font-size:var(--t-large);line-height:1.6;color:var(--text)}}
.article p + p{{margin-top:26px}}

/* ---------- stiri ---------- */
/* stirea cea mai noua, mare: imagine in stanga, text in dreapta */
.news-lead{{display:grid;grid-template-columns:1.25fr 1fr;gap:clamp(24px,3vw,50px);align-items:center;
  color:var(--black)}}
.news-lead__media{{position:relative;border-radius:var(--radius);overflow:hidden;background:var(--light-2)}}
.news-lead__media img,.news-lead__poster{{width:100%;aspect-ratio:16/10;object-fit:cover;
  transition:transform .8s var(--ease)}}
.news-lead__poster{{background:var(--black) url(../img/banner-poster.webp) center/cover}}
a.news-lead:hover .news-lead__media img,a.news-lead:hover .news-lead__poster{{transform:scale(1.04)}}
.news-lead__body{{display:flex;flex-direction:column;align-items:flex-start;gap:20px}}
.news-lead__title{{font-size:var(--t-h3);line-height:1.05;letter-spacing:-.02em}}
.news-lead .muted{{font-size:var(--t-large);max-width:48ch}}
@media (max-width:860px){{.news-lead{{grid-template-columns:1fr}}}}

.pager{{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-top:clamp(50px,6vw,80px);
  font-family:var(--mono);font-size:var(--t-label);font-weight:500;letter-spacing:-.04em;
  text-transform:uppercase}}
.pager a,.pager span{{display:inline-flex;align-items:center;justify-content:center;min-width:44px;
  height:44px;padding:0 14px;border-radius:100px;border:1px solid var(--line-strong)}}
.pager a:hover{{border-color:var(--black)}}
.pager .is-current{{background:var(--black);color:#fff;border-color:var(--black)}}

.newsnav{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:60px;max-width:820px}}
.newsnav__item{{display:flex;flex-direction:column;gap:10px;background:var(--light-2);
  border-radius:var(--radius);padding:20px;font-weight:500;transition:background .3s}}
.newsnav__item:hover{{background:var(--light-3)}}
.newsnav__item .mono{{font-size:var(--t-label-s);color:var(--text)}}
.newsnav__item--next{{grid-column:2;text-align:right;align-items:flex-end}}
@media (max-width:640px){{.newsnav{{grid-template-columns:1fr}}.newsnav__item--next{{grid-column:1}}}}

/* textul stirii: subtitluri, liste, citate, legaturi */
.news-body h2{{font-size:var(--t-h5);font-weight:500;line-height:1.15;letter-spacing:-.02em;
  margin:44px 0 16px;color:var(--black)}}
.news-body h3{{font-size:var(--t-sub);font-weight:600;margin:32px 0 12px;color:var(--black)}}
.news-body h2:first-child,.news-body h3:first-child{{margin-top:0}}
.news-body ul,.news-body ol{{margin:20px 0;padding-left:22px;color:var(--text);
  font-size:var(--t-large);line-height:1.6}}
.news-body ul{{list-style:disc}} .news-body ol{{list-style:decimal}}
.news-body li + li{{margin-top:8px}}
.news-body blockquote{{margin:30px 0;padding:6px 0 6px 22px;border-left:4px solid var(--black)}}
.news-body blockquote p{{color:var(--black);font-size:var(--t-h6);line-height:1.35}}
.news-body a{{color:var(--black);text-decoration:underline;text-underline-offset:3px}}
.news-body strong{{color:var(--black);font-weight:600}}
.news-source{{display:flex;flex-wrap:wrap;align-items:center;gap:14px;margin-top:44px !important;
  padding-top:20px;border-top:1px solid var(--line);font-size:var(--t-body) !important}}
.news-source .mono{{font-size:var(--t-label-s);color:var(--text)}}
.news-source a{{display:inline-flex;align-items:center;gap:8px;font-weight:600;text-decoration:none}}
.news-source a:hover{{text-decoration:underline}}
.news-source svg{{width:14px;height:14px}}
.news-body code{{font-family:var(--mono);font-size:.9em;background:var(--light-2);padding:2px 6px;
  border-radius:4px}}

/* fise incadrate */
.facts{{display:grid;grid-template-columns:repeat(3,1fr);gap:15px;counter-reset:fact}}
.fact{{border:1px solid var(--line);border-radius:var(--radius);padding:24px;
  display:flex;flex-direction:column;gap:12px;counter-increment:fact;background:#fff}}
.fact::before{{content:"/" counter(fact,decimal-leading-zero);font-family:var(--mono);
  font-size:var(--t-label-s);font-weight:500;letter-spacing:-.04em;margin-bottom:30px}}
.fact h3{{font-size:var(--t-h6);font-weight:500}}
@media (max-width:860px){{.facts{{grid-template-columns:1fr}}}}

/* pagini inrudite: randurile din lista de servicii a referintei */
.related{{border-top:1px solid var(--line)}}
.related a{{display:grid;grid-template-columns:2fr 3fr auto;gap:20px;align-items:center;
  padding:26px 0;border-bottom:1px solid var(--line);transition:padding .35s var(--ease)}}
.related a:hover{{padding-inline:12px}}
.related__label{{font-size:var(--t-h5);font-weight:500;letter-spacing:-.01em}}
.related__desc{{color:var(--text)}}
.related__go{{font-family:var(--mono);font-size:var(--t-label);font-weight:500;
  letter-spacing:-.04em;text-transform:uppercase;display:inline-flex;align-items:center;gap:14px}}
.related__go svg{{width:16px;height:16px}}
@media (max-width:767px){{
  .related a{{grid-template-columns:1fr}}
}}

/* ============================================================ accordion */
.acc{{display:flex;flex-direction:column;gap:10px;max-width:920px;margin-left:auto}}
.acc__item{{background:var(--light-2);border-radius:var(--radius)}}
.acc__item h3{{font-weight:500}}
.acc__top{{display:flex;align-items:center;gap:20px;width:100%;padding:25px;background:none;
  border:0;cursor:pointer;text-align:left;font-size:var(--t-h6);font-weight:500;
  line-height:1.2;color:var(--black)}}
.acc__sign{{order:-1;flex:none;width:30px;height:30px;border-radius:50%;background:#fff;
  position:relative}}
.acc__sign::before,.acc__sign::after{{content:"";position:absolute;left:50%;top:50%;
  background:var(--black);transition:transform .35s var(--ease)}}
.acc__sign::before{{width:12px;height:1.5px;transform:translate(-50%,-50%)}}
.acc__sign::after{{width:1.5px;height:12px;transform:translate(-50%,-50%)}}
.acc__item.is-open .acc__sign::after{{transform:translate(-50%,-50%) scaleY(0)}}
.acc__panel{{overflow:hidden;height:0;transition:height .4s var(--ease)}}
.acc__panel p{{margin:0 10px 10px;background:#fff;border-radius:var(--radius);
  padding:18px 20px;color:var(--text);line-height:1.55}}
.acc__panel p > *{{max-width:70ch}}

/* ============================================================ contact */
.contact-card{{display:grid;grid-template-columns:1fr 1.4fr auto;gap:30px;
  align-items:center;background:#fff;padding:30px;border-radius:var(--radius)}}
.contact-card .h2{{font-size:var(--t-h4);letter-spacing:-.03em}}
@media (max-width:860px){{.contact-card{{grid-template-columns:1fr}}}}

/* ============================================================ forms */
.field{{display:block;margin-bottom:16px}}
.field span{{display:block;font-family:var(--mono);font-size:var(--t-label-s);font-weight:500;
  letter-spacing:-.04em;text-transform:uppercase;margin-bottom:10px}}
.field input,.field textarea,.field select{{width:100%;padding:16px 18px;border:1px solid transparent;
  background:var(--light-2);border-radius:var(--radius);font:inherit;font-size:1rem;color:var(--black);
  transition:border-color .25s,background .25s}}
.field input:focus,.field textarea:focus{{outline:none;border-color:var(--black);background:#fff}}
.field textarea{{min-height:170px;resize:vertical}}
.field select{{appearance:none;-webkit-appearance:none;cursor:pointer;padding-right:44px;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' fill='none'%3E%3Cpath d='M1 1.5l5 5 5-5' stroke='%23000' stroke-width='1.5'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 18px center}}
/* formularul pe fundal gri: campurile trec pe alb, ca sa se vada */
.form-card{{background:#fff;border-radius:var(--radius);padding:clamp(20px,3vw,36px)}}
.section--grey .form-card .field input,.section--grey .form-card .field textarea,
.section--grey .form-card .field select{{background-color:var(--light-2)}}
#sales-form{{scroll-margin-top:20px}}

/* ============================================================ cta */
/* blocul de final: degradeul in miscare, intr-o cutie rotunjita pe negru */
.cta{{background:var(--black);padding:15px 15px 0}}
.cta__box{{position:relative;overflow:hidden;border-radius:var(--radius);color:#fff;
  isolation:isolate;background:var(--black) url(../img/banner-poster.webp) center/cover}}
.cta__box video{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-1}}
.cta__inner{{display:flex;justify-content:space-between;align-items:flex-start;gap:30px;
  padding:60px clamp(20px,3vw,40px)}}
.cta__copy{{max-width:820px}}
.cta .eyebrow{{background:#fff;color:var(--black);margin-bottom:35px}}
.cta__title{{font-size:var(--t-h3);font-weight:500;line-height:1.05;letter-spacing:-.02em}}
.cta__text{{margin-top:18px;color:var(--w-70);max-width:56ch;font-size:var(--t-large)}}
.cta .btn-row{{margin-top:35px}}
.cta__year{{font-family:var(--mono);font-size:var(--t-label);font-weight:500;
  letter-spacing:-.04em;flex:none}}
@media (max-width:640px){{.cta__year{{display:none}}}}

/* ============================================================ footer */
.footer{{background:var(--black);color:#fff;padding-top:100px}}
.footer__main{{display:flex;justify-content:space-between;gap:40px 20px}}
.footer__info{{max-width:340px;display:flex;flex-direction:column;gap:22px}}
.footer__info img{{height:110px;width:auto}}
.footer__info p{{color:var(--w-60);line-height:1.5}}
.footer__menus{{display:flex;justify-content:space-between;gap:30px;width:100%;max-width:900px}}
.footer h3{{font-family:var(--mono);font-size:var(--t-label);font-weight:500;
  letter-spacing:-.04em;text-transform:uppercase;color:var(--w-60);margin-bottom:30px}}
.footer__menus li + li{{margin-top:12px}}
.footer__menus a{{font-weight:500;transition:opacity .25s}}
.footer__menus ul:hover a{{opacity:.5}}
.footer__menus ul a:hover{{opacity:1}}
.footer__legal{{margin-top:100px;border-top:1px solid var(--w-15);padding-block:26px;
  display:flex;flex-wrap:wrap;gap:16px 30px;justify-content:space-between;align-items:center;
  font-size:.9rem;color:var(--w-60)}}
.footer__legal ul{{display:flex;flex-wrap:wrap;gap:8px 22px}}
.footer__legal a:hover{{color:#fff}}
@media (max-width:991px){{
  .footer__main{{flex-direction:column}}
  .footer__menus{{flex-wrap:wrap;justify-content:flex-start;gap:40px 60px}}
}}

/* ============================================================ motion */
/* Ascunderea se aplica doar daca scriptul a pornit si a pus clasa `js` pe
   <html>. Altfel continutul e vizibil din start: inainte, orice eroare de
   JavaScript lasa toata pagina de sub antet invizibila, fara nicio scapare. */
html.js [data-reveal]{{opacity:0;transform:translateY(30px)}}
html.js [data-reveal].is-in{{opacity:1;transform:none;
  transition:opacity .9s var(--ease),transform .9s var(--ease)}}
/* titlurile mari urca din spatele unei masti, rand cu rand */
html.js .rise{{display:block;overflow:hidden;padding-bottom:.08em;margin-bottom:-.08em}}
html.js .rise > span{{display:block;transform:translateY(105%);
  transition:transform 1.05s var(--ease)}}
html.js .is-risen .rise > span{{transform:none}}
html.js .is-risen .rise:nth-child(2) > span{{transition-delay:.08s}}
html.js .is-risen .rise:nth-child(3) > span{{transition-delay:.16s}}
html.js .is-risen .rise:nth-child(4) > span{{transition-delay:.24s}}

/* ---------- intrari pe componente (clasele le pune site.js) ---------- */
/* animatie, nu tranzitie: asa nu calca peste tranzitiile de hover ale
   componentei, iar dupa final elementul revine la stilul lui obisnuit */
html.js .m-up:not(.is-in){{opacity:0}}
.m-up.is-in{{animation:m-up 1s var(--ease) var(--d,0s) backwards}}
@keyframes m-up{{from{{opacity:0;transform:translateY(46px)}}to{{opacity:1;transform:none}}}}
@keyframes m-up-sm{{from{{opacity:0;transform:translateY(18px)}}to{{opacity:1;transform:none}}}}

/* imaginile se descopera de jos in sus si se aseaza din zoom */
html.js .m-img:not(.is-in){{clip-path:inset(100% 0 0 0)}}
.m-img.is-in{{animation:m-clip 1.3s var(--ease) var(--d,0s) backwards}}
.m-img.is-in img{{animation:m-zoom 1.8s var(--ease) var(--d,0s) backwards}}
@keyframes m-clip{{from{{clip-path:inset(100% 0 0 0)}}to{{clip-path:inset(0 0 0 0)}}}}
@keyframes m-zoom{{from{{transform:scale(1.3)}}to{{transform:none}}}}
/* paralaxa: imaginile sunt putin mai mari decat rama si alunecă la derulare */
html.js .pagehead__media img,html.js .split__media img,html.js .feature__media img{{scale:1.12}}

/* liniile din lista bannerului se traseaza */
.hero__list li.is-in .rule{{transform-origin:left;
  animation:m-line 1.1s var(--ease) calc(var(--d,0s) + .15s) backwards}}
@keyframes m-line{{from{{transform:scaleX(0)}}to{{transform:none}}}}
.hero__info{{position:relative}}

/* crucea din „How it works” se traseaza, romburile se rotesc pe pozitie */
.process::before{{transform-origin:top;transition:transform 1.6s var(--ease)}}
.process::after{{transition:transform 1.6s var(--ease) .2s}}
html.js .process:not(.is-in)::before{{transform:scaleY(0)}}
html.js .process:not(.is-in)::after{{transform:scaleX(0)}}
.process__step.is-in .diamond::before{{
  animation:m-diamond 1.3s var(--ease) calc(var(--d,0s) + .1s) backwards}}
@keyframes m-diamond{{from{{transform:rotate(-135deg) scale(.3);opacity:0}}
  to{{transform:rotate(45deg) scale(1);opacity:1}}}}

/* bara neagra a fiselor de proces se traseaza */
.pcard.is-in h3::before{{animation:m-bar 1s var(--ease) calc(var(--d,0s) + .25s) backwards}}
@keyframes m-bar{{from{{transform:scaleY(0)}}to{{transform:none}}}}

/* antetul coboara la incarcare */
.chrome{{animation:m-drop 1s var(--ease) .15s backwards}}
@keyframes m-drop{{from{{transform:translateY(-110%)}}to{{transform:none}}}}

/* panourile de meniu: intrarile vin una dupa alta */
.drawer.is-open .drawer__list li,.drawer.is-open .drawer__aside,
.mega.is-open .mega__grid li,.mega.is-open .mega__cta{{
  animation:m-up-sm .6s var(--ease) calc(var(--i,0) * 35ms + .08s) backwards}}

/* blocul de final se deschide ca o fereastra cand urca pe ecran */
html.js .cta__box{{transform-origin:center bottom;will-change:scale}}
/* legaturile din navigatie se rostogolesc ca butoanele */
.nav__link .btn__clip{{height:1.5em;margin-block:-.25em}}
.nav__link:hover .btn__track,.nav__link:focus-visible .btn__track{{transform:translateY(-50%)}}
@media (prefers-reduced-motion:reduce){{
  *,*::before,*::after{{animation-duration:.01ms!important;animation-iteration-count:1!important;
    transition-duration:.01ms!important}}
  html.js [data-reveal]{{opacity:1;transform:none}}
  html.js .rise > span{{transform:none}}
  html.js .m-up,html.js .m-img{{opacity:1;clip-path:none}}
  html.js .process::before,html.js .process::after{{transform:none}}
  .chrome{{animation:none}}
  html.js .words .w{{color:inherit}}
}}
"""
