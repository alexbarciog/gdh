# GDH — Global Distribution Holdings

Folderul asta are două părți:

| Ce | Unde |
|---|---|
| **Site-ul final, de urcat pe Cloudflare** | `dist/` |
| Sursa (snapshot-ul original + scripturile de build) | restul folderului |

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

1. Dashboard → Workers & Pages → Create → Pages → **Upload assets**.
2. Trage folderul `dist` în zona de upload. Fără build command.

Sau din linia de comandă, din interiorul `dist`:

```bash
npx wrangler pages deploy .
```

`dist/_headers` setează cache-ul și un CSP care blochează orice cerere în afara domeniului.

## Rulare locală

Dublu-click pe `START.bat` → http://localhost:8752

## Reconstruire

```bash
python build_gdh.py
```

Scripturile: `build_gdh.py` (resurse, CSS, logo), `pages_gdh.py` (paginile din snapshot),
`inner_gdh.py` (paginile interioare scrise de noi), `copy_gdh.py` (textele), `site_js.js` (JS-ul).

Snapshot-ul Webflow original e păstrat intact la `../e-backup-webflow`.
