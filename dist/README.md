# GDH - Global Distribution Holdings (site generat)

Folderul asta e **generat**: il rescrie `python3 build_gdh.py` din radacina
repo-ului, la fiecare rulare. Nu edita nimic aici, se pierde la urmatorul build.
Sursele si instructiunile sunt in `../SURSE.md`.

Site static, fara nicio resursa externa: fonturile, imaginile, CSS-ul si JS-ul
sunt servite de pe acelasi domeniu.

| | |
|---|---|
| Pagini | 31 |
| Cereri catre alte domenii | 0 |
| Fonturi | Inter Tight + GDH Sans, locale |
| Animatii | GSAP + ScrollTrigger + SplitText, locale (`js/animations.js`) |

## Publicare

Cloudflare Pages e legat la repo, cu build command gol si build output
directory `dist`. Fiecare push pe `main` redeployeaza singur.

`_headers` seteaza cache-ul si o politica CSP care blocheaza orice cerere in
afara domeniului. `_redirects` tine in viata adresele vechi.
