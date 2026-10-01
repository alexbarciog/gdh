# Sursele site-ului GDH

Un singur repo, o singura ramura: `main` din `alexbarciog/gdh`. Aici stau si
fisierele **din care se genereaza** site-ul, si site-ul gata facut (`dist/`).

    .                 -> scripturile, textele, snapshot-ul Webflow
    dist/             -> site-ul gata, asta publica Cloudflare Pages

## Ce e fiecare fisier

| Fisier | Ce face |
|---|---|
| `build_gdh.py` | scriptul principal: ruleaza toate etapele, in ordine |
| `copy_gdh.py` | **toate textele** site-ului + `SITE_URL` (domeniul) |
| `pages_gdh.py` | curata paginile din snapshot: scoate Webflow, pune sigla, antetul |
| `inner_gdh.py` | paginile scrise de la zero + harta `RENAME` a adreselor |
| `logo_gdh.py` | pregateste sigla din `gdh-logo-source.png` |
| `assets_gdh.py` | iconitele, imaginea de partajare, manifestul |
| `site_js.js` | meniu, slidere, FAQ, formulare |
| `animations_js.js` | animatiile pe GSAP |
| `gdh-logo-source.png` | sigla originala, asa cum a fost primita |
| `*_files/` | snapshot-ul Webflow original, materia prima |

## Cum reconstruiesc site-ul

Are nevoie de Pillow si fontTools:

    python3 -m pip install --user pillow fonttools
    python3 build_gdh.py

Scrie peste folderul `dist`. Fara fontTools, etapa 8 crapa **dupa** ce `dist` a
fost deja golit, si raman lipsa favicon-ul si imaginea de partajare.

Apoi, din radacina:

    git add -A && git commit -m "..." && git push

## Cum public pe Cloudflare

Proiectul Pages e legat la acest repo:

- Framework preset: **None**
- Build command: **(gol)**
- Build output directory: **dist**

Fiecare push pe `main` redeployeaza singur. Pentru o publicare manuala, din `dist`:

    npx wrangler pages deploy . --project-name gdh --branch gbh --commit-dirty=true

Ramura de productie a proiectului Pages se numeste `gbh` (o scapare de tastare la
creare), deci numele ala trebuie folosit exact, altfel deploy-ul intra ca preview.

## Cum modific ceva

- **texte** -> `copy_gdh.py` (dictionarul `EXACT`, potrivire pe text integral)
- **domeniu** -> `SITE_URL` din `copy_gdh.py`, de acolo se iau canonical, og:url, sitemap
- **pagini interioare** -> `inner_gdh.py`
- **adresa unei pagini** -> `RENAME` din `inner_gdh.py`; vechea adresa ramane
  valida, intra automat in `dist/_redirects`
- **culori, spatii, sigla in CSS** -> blocul de la finalul lui `build_gdh.py`
- **animatii** -> `animations_js.js`

Nu edita direct fisierele din `dist`: se rescriu la fiecare build.
