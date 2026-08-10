# Sursele site-ului GDH

Branch-ul `source` din repo-ul `ghbr`. Aici stau fișierele **din care se generează**
site-ul; site-ul propriu-zis e pe branch-ul `main` și doar acela ajunge pe Cloudflare.

    main    -> site-ul gata (folderul dist)   -> Cloudflare Pages publica asta
    source  -> scripturile si textele         -> nu se publica niciodata

## Ce e fiecare fișier

| Fișier | Ce face |
|---|---|
| `build_gdh.py` | scriptul principal: rulează toate etapele, în ordine |
| `copy_gdh.py` | **toate textele** site-ului + `SITE_URL` (domeniul) |
| `pages_gdh.py` | curăță paginile din snapshot: scoate Webflow, pune sigla, antetul |
| `inner_gdh.py` | paginile scrise de la zero (about, servicii, studii de caz, articole) |
| `logo_gdh.py` | pregătește sigla din `gdh-logo-source.png` |
| `assets_gdh.py` | iconițele, imaginea de partajare, manifestul |
| `site_js.js` | meniu, slidere, FAQ, formulare |
| `animations_js.js` | animațiile pe GSAP |
| `gdh-logo-source.png` | sigla originală, așa cum a fost primită |
| `*_files/` | snapshot-ul Webflow original, materia primă |

## Cum reconstruiesc site-ul

    python build_gdh.py

Scrie peste folderul `dist`, fără să atingă `.git`-ul lui. Apoi, din `dist`:

    git add -A && git commit -m "..." && git push

## Cum public pe Cloudflare

Proiectul Pages `gdh` e creat prin upload direct, iar ramura lui de producție se
numește `gbh` (o scăpare de tastare la creare). Deci publicarea se face **exact**
cu numele ăla, altfel deploy-ul intră ca preview și adresa principală nu se
schimbă. Din folderul `dist`:

    npx wrangler pages deploy . --project-name gdh --branch gbh --commit-dirty=true

Adresa: https://gdh-4ns.pages.dev

## Cum modific ceva

- **texte** → `copy_gdh.py` (dicționarul `EXACT`, potrivire pe text integral)
- **domeniu** → `SITE_URL` din `copy_gdh.py`, de acolo se iau canonical, og:url, sitemap
- **pagini interioare** → `inner_gdh.py`
- **culori, spații, siglă în CSS** → blocul de la finalul lui `build_gdh.py`
- **animații** → `animations_js.js`

Nu edita direct fișierele din `dist`: se rescriu la fiecare build.
