# -*- coding: utf-8 -*-
"""Sigla GDH (steaua albastra + GDH + descriptor): o pregateste pentru web.

Sursele, cu fundal transparent:
  gdh-logo-source.png  — sigla completa, pe verticala, cu literele albe
  gdh-mark-source.png  — doar steaua, pentru favicon si iconite

Ies:
  img/gdh-logo.png                 — orizontala, litere inchise (fundal deschis)
  img/gdh-logo-light.png           — orizontala, litere albe (fundal inchis)
  img/gdh-logo-stacked.png         — verticala, ca in sursa, litere inchise
  img/gdh-logo-stacked-light.png   — verticala, litere albe
  img/gdh-mark.png                 — steaua

Varianta orizontala e compusa din aceleasi piese ale siglei: la 38 px inaltime
in antet, sigla verticala ar face descriptorul ilizibil.
"""
import os
from PIL import Image

INK = (10, 10, 10)
HAZE = 20               # sub atata opacitate e doar ceata exportului, nu desen
SATURATED = 40          # diferenta intre canale peste care pixelul e „colorat”


def clean(im):
    """Scoate ceata aproape transparenta pe care exportul a lasat-o in jurul
    literelor: pe alb, dupa ce literele se fac negre, ar deveni un halou gri."""
    r, g, b, a = im.split()
    a = a.point(lambda v: 0 if v < HAZE else v)
    return Image.merge("RGBA", (r, g, b, a))


def trim(im, alpha=128):
    """Taie marginile goale, dupa o masca de opacitate reala."""
    mask = im.getchannel("A").point(lambda v: 255 if v >= alpha else 0)
    bb = mask.getbbox()
    return im.crop(bb) if bb else im


def recolor_text(im, ink=INK):
    """Literele albe (fara culoare) devin `ink`; steaua ramane cum e."""
    out = im.copy()
    px = out.load()
    w, h = out.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a and max(r, g, b) - min(r, g, b) <= SATURATED:
                px[x, y] = (ink[0], ink[1], ink[2], a)
    return out


def bands(im):
    """Benzile orizontale opace: steaua, GDH, descriptorul."""
    w, h = im.size
    px = im.load()
    rows = [any(px[x, y][3] > 128 for x in range(0, w, 2)) for y in range(h)]
    out, start = [], None
    for y, full in enumerate(rows + [False]):
        if full and start is None:
            start = y
        elif not full and start is not None:
            out.append((start, y))
            start = None
    return out


def horizontal(src):
    """Steaua in stanga, blocul GDH + descriptor in dreapta, centrate vertical."""
    parts = bands(src)
    star = trim(src.crop((0, parts[0][0], src.width, parts[0][1])))
    text = trim(src.crop((0, parts[1][0], src.width, parts[-1][1])))
    sh = round(text.height * 1.08)
    star = star.resize((round(star.width * sh / star.height), sh), Image.LANCZOS)
    gap = round(text.height * 0.14)
    canvas = Image.new("RGBA", (star.width + gap + text.width, sh), (0, 0, 0, 0))
    canvas.alpha_composite(star, (0, 0))
    canvas.alpha_composite(text, (star.width + gap, (sh - text.height) // 2))
    return canvas


def icon_from_mark(mark, size, pad=0.14, bg=(255, 255, 255), radius=0.22):
    """Steaua, centrata pe un patrat; `bg=None` = fundal transparent."""
    from PIL import ImageDraw
    ss = 4
    S = size * ss
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if bg is not None:
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * radius), fill=bg + (255,))
    inner = int(S * (1 - 2 * pad))
    m = mark.copy()
    r = min(inner / m.width, inner / m.height)
    m = m.resize((max(1, round(m.width * r)), max(1, round(m.height * r))), Image.LANCZOS)
    img.alpha_composite(m, ((S - m.width) // 2, (S - m.height) // 2))
    return img.resize((size, size), Image.LANCZOS)


def squeeze(im, colors=256):
    """Reduce paleta, fara sa se vada.

    48 de culori ajungeau cand sigla avea trei culori plate. Pe un degrade
    produc dungi clare pe litere, deci urcam la 256: diferenta de marime e sub
    5 KB, iar trecerea ramane neteda.
    """
    q = im.quantize(colors=colors, method=Image.FASTOCTREE)
    return q


def fit(im, height):
    """Redimensionare la o inaltime data (≈3x cat se afiseaza, pentru retina)."""
    return im.resize((max(1, round(im.width * height / im.height)), height), Image.LANCZOS)


def build(src_png, out_dir, mark_png=None):
    src = trim(clean(Image.open(src_png).convert("RGBA")), alpha=8)

    wide = fit(horizontal(src), 132)
    tall = fit(trim(src, alpha=8), 420)
    for name, im in (("gdh-logo", wide), ("gdh-logo-stacked", tall)):
        # culori depline: paleta redusa pune dungi pe degradeul stelei
        recolor_text(im).save(os.path.join(out_dir, name + ".png"), optimize=True)
        im.save(os.path.join(out_dir, name + "-light.png"), optimize=True)

    if mark_png and os.path.exists(mark_png):
        mark = trim(clean(Image.open(mark_png).convert("RGBA")), alpha=8)
    else:
        parts = bands(src)
        mark = trim(src.crop((0, parts[0][0], src.width, parts[0][1])))
    mark = mark.resize((512, round(mark.height * 512 / mark.width)), Image.LANCZOS)
    mark.save(os.path.join(out_dir, "gdh-mark.png"), optimize=True)

    return {"w": wide.width, "h": wide.height, "ratio": round(wide.width / wide.height, 4),
            "stacked": tall.size, "mark": mark.size}
