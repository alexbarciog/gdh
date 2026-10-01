# -*- coding: utf-8 -*-
"""Sigla reală GDH: o pregătește pentru web și scoate variantele de care e nevoie.

Sursa e `gdh-logo-source.png` (fundal transparent). De aici ies:
  img/gdh-logo.png        — pentru fundal deschis (tuș negru)
  img/gdh-logo-light.png  — pentru fundal închis (tuș alb)
  img/gdh-mark.png        — doar litera G, pentru iconițe
"""
import os
from PIL import Image

RED_MIN = 90            # peste atât pe roșu și sub restul => e roșul siglei
DARK_MAX = 90           # sub atât pe toate canalele => e tușul negru
SATURATED = 40          # diferență între canale peste care pixelul e „colorat”


def trim(im, alpha=128):
    """Taie marginile goale.

    Nu folosim getbbox(): el pastreaza si pixelii aproape transparenti, iar o
    siglă exportata cu putin zgomot pe margini ramane cu randuri care arata
    goale dar nu sunt, ceea ce incurca apoi cautarea benzii dintre marca si
    descriptor. Taiem dupa o masca de opacitate reala.
    """
    mask = im.getchannel("A").point(lambda v: 255 if v >= alpha else 0)
    bb = mask.getbbox()
    return im.crop(bb) if bb else im


def recolor_ink(im, ink=(255, 255, 255)):
    """Tusul inchis devine alta culoare; culoarea siglei ramane neatinsa.

    Testul nu mai e "e rosu?", ci "e lipsit de culoare?". Sigla veche avea un
    singur accent rosu, asa ca mergea sa cautam rosul; cea noua e un degrade
    care trece prin turcoaz, albastru si magenta, iar un test pe rosu ar fi
    spalat jumatate din litere spre alb pe fundal inchis.
    """
    out = im.copy()
    px = out.load()
    w, h = out.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            hi, lo = max(r, g, b), min(r, g, b)
            chroma = hi - lo
            if chroma > SATURATED:
                continue                      # orice pixel colorat ramane cum e
            if hi < DARK_MAX:
                px[x, y] = (ink[0], ink[1], ink[2], a)
            else:
                # muchiile antialiasate, gri: amesteca spre noua culoare,
                # proportional cu cat de inchis era pixelul
                k = 1.0 - (hi / 255.0)
                px[x, y] = (int(r + (ink[0] - r) * k),
                            int(g + (ink[1] - g) * k),
                            int(b + (ink[2] - b) * k), a)
    return out


def _runs(values, is_empty):
    """Intervalele consecutive în care `is_empty` e adevărat."""
    out, run = [], 0
    for i, v in enumerate(values):
        if is_empty(v):
            run += 1
        else:
            if run:
                out.append((i - run, run))
            run = 0
    if run:
        out.append((len(values) - run, run))
    return out


def wordmark_only(im):
    """Taie descriptorul și lasă doar GDH.

    Banda goală dintre wordmark și textul mic e cea mai lată din imagine — nu
    „ultima", cum credeam: sub descriptor mai rămâne un rând gol care păcălea
    căutarea și tăia aproape nimic.
    """
    im = trim(im)
    w, h = im.size
    px = im.load()
    rows = [sum(1 for x in range(0, w, 2) if px[x, y][3] > 128) for y in range(h)]
    # doar benzile goale dinauntrul desenului: una lipita de marginea de sus sau
    # de jos nu desparte nimic, iar daca o alegem taiem sigla la inaltime zero
    gaps = [g for g in _runs(rows, lambda n: n == 0)
            if g[0] > 0 and g[0] + g[1] < h]
    if not gaps:
        return im
    cut = max(gaps, key=lambda g: g[1])[0]
    return trim(im.crop((0, 0, w, cut)))


def letter_g(im):
    """Doar litera G din wordmark, pentru iconițe."""
    word = wordmark_only(im)
    w, h = word.size
    px = word.load()
    cols = [sum(1 for y in range(0, h, 2) if px[x, y][3] > 128) for x in range(w)]
    valleys = [v for v in _runs(cols, lambda n: n <= h * 0.03) if v[0] > w * 0.1]
    # capătul e începutul văii, nu sfârșitul ei — altfel intră o fâșie din D
    end = valleys[0][0] if valleys else int(w / 3)
    return trim(word.crop((0, 0, end, h)))


def icon_from_mark(mark, size, pad=0.14, bg=(255, 255, 255), radius=0.22):
    """Litera G a siglei, centrată pe un pătrat cu colțuri rotunjite."""
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


def build(src_png, out_dir, width=520):
    """`width` acoperă de ~3 ori dimensiunea la care se afișează sigla (ecrane retina)."""
    src = trim(Image.open(src_png).convert("RGBA"))
    scale = width / src.width
    big = src.resize((width, max(1, round(src.height * scale))), Image.LANCZOS)

    squeeze(big).save(os.path.join(out_dir, "gdh-logo.png"), optimize=True)
    squeeze(recolor_ink(big, (255, 255, 255))).save(
        os.path.join(out_dir, "gdh-logo-light.png"), optimize=True)

    mark = letter_g(src)
    mark = mark.resize((512, round(mark.height * 512 / mark.width)), Image.LANCZOS)
    squeeze(mark).save(os.path.join(out_dir, "gdh-mark.png"), optimize=True)

    return {"w": big.width, "h": big.height,
            "ratio": round(big.width / big.height, 4),
            "mark": mark.size}
