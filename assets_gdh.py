# -*- coding: utf-8 -*-
"""Etapa 4: iconițele, imaginea de partajare și manifestul.

Toate se desenează aici, din fonturile și fotografiile deja aduse local — nu
există niciun generator online în lanț.
"""
import os, io, math

from PIL import Image, ImageDraw, ImageFont, ImageFilter

RED = (254, 63, 3)      # vezi BRAND din build_gdh.py
INK = (17, 17, 17)
WHITE = (255, 255, 255)


# ---------------------------------------------------------------- fonturi
def load_fonts(out, cache):
    """woff2 -> ttf, ca să putem desena cu adevăratul Inter Tight."""
    from fontTools.ttLib import TTFont
    os.makedirs(cache, exist_ok=True)
    paths = {}
    for weight in (400, 500, 600, 700):
        src = os.path.join(out, "fonts", "inter-tight-%d-latin.woff2" % weight)
        dst = os.path.join(cache, "inter-tight-%d.ttf" % weight)
        if not os.path.exists(dst):
            f = TTFont(src)
            f.flavor = None
            f.save(dst)
        paths[weight] = dst
    return paths


def font(paths, weight, size):
    return ImageFont.truetype(paths[weight], size)


def text_size(draw, txt, fnt, spacing=0):
    if spacing:
        return sum(draw.textlength(ch, font=fnt) + spacing for ch in txt) - spacing
    return draw.textlength(txt, font=fnt)


def draw_tracked(draw, xy, txt, fnt, fill, spacing):
    """Text cu spațiere între litere, cum e descriptorul din siglă."""
    x, y = xy
    for ch in txt:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + spacing
    return x - spacing


# ---------------------------------------------------------------- iconițe
def build_icons(out, paths):
    """Iconițele, decupate din litera G a siglei reale."""
    import logo_gdh as LG
    img_dir = os.path.join(out, "img")
    mark = Image.open(os.path.join(img_dir, "gdh-mark.png")).convert("RGBA")

    for px in (16, 32, 48, 96, 192, 512):
        LG.icon_from_mark(mark, px).save(os.path.join(img_dir, "icon-%d.png" % px), optimize=True)

    # apple-touch: fundal opac, iOS taie singur colțurile
    apple = Image.new("RGB", (180, 180), WHITE)
    ic = LG.icon_from_mark(mark, 180, pad=0.16)
    apple.paste(ic, (0, 0), ic)
    apple.save(os.path.join(img_dir, "apple-touch-icon.png"), optimize=True)

    # maskable: Android taie pana la 20% din margine, deci sigla sta mai stransa
    mask = Image.new("RGB", (512, 512), WHITE)
    ic = LG.icon_from_mark(mark, 512, pad=0.26, radius=0.0)
    mask.paste(ic, (0, 0), ic)
    mask.save(os.path.join(img_dir, "icon-maskable-512.png"), optimize=True)

    ico = LG.icon_from_mark(mark, 256)
    ico.save(os.path.join(out, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    return True


# ------------------------------------------------------- imaginea de share
def cover(img, size):
    tw, th = size
    r = max(tw / img.width, th / img.height)
    img = img.resize((max(1, int(img.width * r)), max(1, int(img.height * r))), Image.LANCZOS)
    left = (img.width - tw) // 2
    top = (img.height - th) // 2
    return img.crop((left, top, left + tw, top + th))


def logo_lockup(canvas, x, y, out_dir, height=64):
    """Lipește sigla reală (varianta cu tuș alb) pe cartonașul de partajare."""
    logo = Image.open(os.path.join(out_dir, "img", "gdh-logo-light.png")).convert("RGBA")
    w = round(logo.width * height / logo.height)
    logo = logo.resize((w, height), Image.LANCZOS)
    canvas.alpha_composite(logo, (x, y)) if canvas.mode == "RGBA" else canvas.paste(logo, (x, y), logo)
    return w


def build_og(out, paths, tagline, kicker, domain, photo=None):
    W, H = 1200, 630
    img_dir = os.path.join(out, "img")
    base = None
    if photo and os.path.exists(os.path.join(img_dir, photo)):
        base = Image.open(os.path.join(img_dir, photo)).convert("RGB")
        base = cover(base, (W, H))
        base = base.filter(ImageFilter.GaussianBlur(1.2))
    else:
        base = Image.new("RGB", (W, H), (12, 12, 12))

    # voal întunecat, mai dens în stânga, ca textul să stea pe ceva calm
    veil = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(veil)
    for i in range(W):
        vd.line([(i, 0), (i, H)], fill=int(238 - 150 * min(1.0, i / (W * 0.78))))
    base = Image.composite(Image.new("RGB", (W, H), (8, 8, 8)), base, veil)

    # fundalul curat, înainte de orice text — din el se face miniatura pătrată
    clean = base.copy()

    # bandă roșie sus, semnătura vizuală a brandului
    d = ImageDraw.Draw(base)
    d.rectangle([0, 0, W, 8], fill=RED)

    logo_lockup(base, 70, 66, out, height=86)
    d = ImageDraw.Draw(base)

    f_tag = font(paths, 700, 76)
    words, lines, cur = tagline.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textlength(t, font=f_tag) > W - 150 and cur:
            lines.append(cur)
            cur = wd
        else:
            cur = t
    lines.append(cur)
    y = H - 150 - len(lines) * 84
    for ln in lines:
        d.text((70, y), ln, font=f_tag, fill=WHITE)
        y += 84

    f_k = font(paths, 500, 27)
    d.text((72, y + 16), kicker, font=f_k, fill=(214, 214, 214))

    dot = 9
    d.ellipse([72, H - 62, 72 + dot, H - 62 + dot], fill=RED)
    f_d = font(paths, 600, 26)
    d.text((72 + dot + 14, H - 68), domain, font=f_d, fill=WHITE)

    # JPEG, nu PNG: unele clienți (WhatsApp mai ales) sar peste previzualizările
    # de peste ~300 KB, iar aici e o fotografie, nu grafică plată
    path = os.path.join(img_dir, "og-image.jpg")
    base.save(path, quality=86, optimize=True, progressive=True)

    # Miniatura pătrată, pentru clienții care taie previzualizarea la 1:1. O
    # compunem separat: o simplă decupare din cea lată ar tăia exact sigla.
    sq = cover(clean, (600, 600))
    veil2 = Image.new("RGBA", (600, 600), (8, 8, 8, 150))
    sq = Image.alpha_composite(sq.convert("RGBA"), veil2).convert("RGB")
    logo = Image.open(os.path.join(img_dir, "gdh-logo-light.png")).convert("RGBA")
    lh = 132
    lw = round(logo.width * lh / logo.height)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    sq.paste(logo, ((600 - lw) // 2, 214), logo)
    sd = ImageDraw.Draw(sq)
    sd.rectangle([0, 0, 600, 7], fill=RED)
    f_sq = font(paths, 500, 24)
    tw = sd.textlength(domain, font=f_sq)
    sd.text(((600 - tw) / 2, 400), domain, font=f_sq, fill=(226, 226, 226))
    sq.save(os.path.join(img_dir, "og-square.jpg"), quality=88, optimize=True)
    return path


def build_manifest(out, name, short):
    import json
    manifest = {
        "name": name,
        "short_name": short,
        "start_url": "/",
        "scope": "/",
        "display": "standalone",
        "background_color": "#0d0d0d",
        "theme_color": "#fe3f03",
        "icons": [
            {"src": "/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/img/icon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "/img/icon-maskable-512.png", "sizes": "512x512", "type": "image/png",
             "purpose": "maskable"},
        ],
    }
    open(os.path.join(out, "site.webmanifest"), "w", encoding="utf-8").write(
        json.dumps(manifest, indent=2) + "\n")
