# GDH — Global Distribution Holdings

Folderul asta are două părți:

| Ce | Unde |
|---|---|
| **Site-ul final, pe care il publica Cloudflare** | `dist/` |
| Sursa (snapshot-ul original + scripturile de build) | restul folderului |

Totul sta pe ramura `main`. Detalii despre build si publicare: [SURSE.md](SURSE.md).

## Site-ul (`dist/`)

- **zero resurse externe** — fonturi, imagini, CSS și JS sunt toate în folder;
- **zero Webflow** — runtime-ul, jQuery, GSAP, badge-ul, atributele `data-w-*`,
  widget-ul de suport al template-ului și link-urile către `webflow.com` / WhatsApp
  au fost scoase; clasele `w-*` au fost redenumite `g-*`;
- interacțiunile (meniu mobil, slidere, FAQ, formulare) sunt rescrise de la zero în
  `js/site.js`;
- animațiile (titluri despicate în cuvinte care se aprind la scroll, intrările
  cardurilor, benzile care curg, paralaxul, contorul 68.000+, hover-ul pe butoane)
  sunt în `js/animations.js`, scrise peste GSAP + ScrollTrigger + SplitText servite
  local — aceleași valori măsurate în pagina-sursă;
- logo-ul GDH e SVG inline, în antet și în subsol, pe fiecare pagină;
- textele sunt scrise pentru o companie de distribuție de produse.

### Publicare pe Cloudflare Pages

Proiectul Pages e legat la repo: build command gol, build output directory `dist`.
Fiecare push pe `main` redeployeaza singur.

`dist/_headers` setează cache-ul și un CSP care blochează orice cerere în afara domeniului.

## Rulare locală

Dublu-click pe `START.bat` → http://localhost:8752

## Reconstruire

```bash
python3 -m pip install --user pillow fonttools
python3 build_gdh.py
```

Scripturile: `build_gdh.py` (resurse, CSS, logo), `pages_gdh.py` (paginile din snapshot),
`inner_gdh.py` (paginile interioare scrise de noi), `copy_gdh.py` (textele), `site_js.js` (JS-ul).

Snapshot-ul Webflow original e păstrat intact în `*_files/`.
