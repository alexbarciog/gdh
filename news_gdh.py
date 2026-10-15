# -*- coding: utf-8 -*-
"""Stirile din industrie (retail, FMCG, distributie, stomatologie), pe gdh-group.com/news.

Un fisier Markdown pe stire, in folderul news/. Fiecare stire e scrisa de GDH
cu cuvintele noastre si trimite la sursa originala — nu copiem articolele
altora.

Fiecare fisier incepe cu un antet intre doua randuri `---`, apoi textul:

    ---
    title: Chilled storage extended at the Ghiroda hub
    date: 2026-10-16
    category: Retail
    summary: O fraza sau doua, 70-160 de caractere: apare in Google si la share.
    source: Romania Insider               (obligatoriu: cine a publicat stirea)
    source_url: https://...               (obligatoriu: articolul original)
    image: ghiroda-chilled.jpg        (optional, din news/images/)
    image_alt: Descrierea fotografiei (obligatoriu daca exista image)
    ---
    Textul stirii, in Markdown: paragrafe, ## subtitluri, liste, **bold**, [link](url).

Adresa stirii vine din numele fisierului, fara data din fata:
`2026-10-16-chilled-storage.md` -> https://gdh-group.com/news/chilled-storage

O stire cu data din viitor nu apare pana in ziua ei: build-ul zilnic din
GitHub Actions o publica singur (vezi .github/workflows/news.yml).

Fisierele care incep cu `_` (sablonul) si README.md nu sunt stiri.
"""
import datetime
import html
import os
import re

try:
    from zoneinfo import ZoneInfo
    TZ = ZoneInfo("Europe/Bucharest")
except Exception:                      # pragma: no cover — Python fara tzdata
    TZ = None

NEWS_DIR = "news"
IMAGES_DIR = os.path.join(NEWS_DIR, "images")
PER_PAGE = 12

TITLE_MAX = 90          # titlul afisat; in <title> se scurteaza daca trebuie
SUMMARY_MIN, SUMMARY_MAX = 70, 160
REQUIRED = ("title", "date", "category", "summary", "source", "source_url")

MONTHS = ("January February March April May June July August September October "
          "November December").split()


class NewsError(SystemExit):
    pass


def now():
    return datetime.datetime.now(TZ) if TZ else datetime.datetime.now()


def slug_from(filename):
    stem = os.path.splitext(os.path.basename(filename))[0]
    stem = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem)
    return re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")


def human_date(d):
    return "%d %s %d" % (d.day, MONTHS[d.month - 1], d.year)


def iso(d, hour=9):
    """Data stirii ca moment exact, cu fusul orar al Romaniei (Google il vrea)."""
    dt = datetime.datetime(d.year, d.month, d.day, hour, 0)
    if TZ:
        dt = dt.replace(tzinfo=TZ)
    return dt.isoformat()


def rfc822(d):
    dt = datetime.datetime(d.year, d.month, d.day, 9, 0, tzinfo=TZ) if TZ else \
        datetime.datetime(d.year, d.month, d.day, 9, 0)
    return dt.strftime("%a, %d %b %Y %H:%M:%S %z")


# ------------------------------------------------------------------- citire
def parse(path):
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise NewsError("%s: lipseste antetul intre randurile ---" % path)
    meta = {}
    for line in m.group(1).split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise NewsError("%s: rand de antet fara „:” — %r" % (path, line))
        key, value = line.split(":", 1)
        meta[key.strip().lower()] = value.strip().strip('"').strip("'")
    meta["body"] = m.group(2).strip()
    meta["file"] = path
    meta["slug"] = slug_from(path)
    return meta


def validate(post):
    path = post["file"]
    problems = []
    for key in REQUIRED:
        if not post.get(key):
            problems.append("lipseste „%s”" % key)
    try:
        post["date"] = datetime.date.fromisoformat(post.get("date", ""))
    except ValueError:
        problems.append("data trebuie scrisa AAAA-LL-ZZ (ex. 2026-10-16), nu %r" % post.get("date"))
    if post.get("updated"):
        try:
            post["updated"] = datetime.date.fromisoformat(post["updated"])
        except ValueError:
            problems.append("„updated” trebuie scrisa AAAA-LL-ZZ")
    if len(post.get("title", "")) > TITLE_MAX:
        problems.append("titlul are %d caractere (max %d)" % (len(post["title"]), TITLE_MAX))
    n = len(post.get("summary", ""))
    if post.get("summary") and not SUMMARY_MIN <= n <= SUMMARY_MAX:
        problems.append("rezumatul are %d caractere (%d-%d): e textul din Google si de la share"
                        % (n, SUMMARY_MIN, SUMMARY_MAX))
    if post.get("source_url") and not re.match(r"^https?://[^\s/]+\.[^\s]+$", post["source_url"]):
        problems.append("„source_url” trebuie sa fie adresa completa a articolului (https://...)")
    if post.get("image"):
        if not os.path.isfile(os.path.join(IMAGES_DIR, post["image"])):
            problems.append("imaginea %s nu exista in %s" % (post["image"], IMAGES_DIR))
        if not post.get("image_alt"):
            problems.append("„image_alt” lipseste: descrie fotografia in cateva cuvinte")
    if not post["slug"]:
        problems.append("numele fisierului nu da o adresa valida")
    if len(post.get("body", "")) < 200:
        problems.append("textul are sub 200 de caractere — prea scurt ca stire")
    if problems:
        raise NewsError("Stire invalida, %s:\n  - %s" % (path, "\n  - ".join(problems)))
    return post


def load(src_root, today=None):
    """Stirile publicate (data <= azi), de la cea mai noua, si cate sunt programate."""
    folder = os.path.join(src_root, NEWS_DIR)
    if not os.path.isdir(folder):
        return [], 0
    today = today or now().date()
    posts, seen = [], {}
    for fn in sorted(os.listdir(folder)):
        if not fn.endswith(".md") or fn.startswith("_") or fn.lower() == "readme.md":
            continue
        post = validate(parse(os.path.join(folder, fn)))
        if post["slug"] in seen:
            raise NewsError("Doua stiri cu aceeasi adresa /news/%s: %s si %s"
                            % (post["slug"], seen[post["slug"]], fn))
        seen[post["slug"]] = fn
        posts.append(post)
    published = [p for p in posts if p["date"] <= today]
    published.sort(key=lambda p: (p["date"], p["file"]), reverse=True)
    for p in published:
        p["words"] = len(re.findall(r"\w+", p["body"]))
        p["minutes"] = max(1, round(p["words"] / 200))
    return published, len(posts) - len(published)


# ------------------------------------------------------------------- Markdown
def _inline(text):
    """Bold, italic, cod si legaturi; totul scapat de HTML inainte."""
    t = html.escape(text, quote=True)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)

    def link(m):
        label, url = m.group(1), html.unescape(m.group(2))
        if not re.match(r"^(https?://|mailto:|tel:|/|#)", url):
            url = "https://" + url
        ext = url.startswith("http") and "gdh-group.com" not in url
        return '<a href="%s"%s>%s</a>' % (
            html.escape(url, quote=True), ' rel="noopener" target="_blank"' if ext else "", label)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, t)
    return t


def markdown(text):
    out, para, items, kind = [], [], [], None

    def flush():
        nonlocal para, items, kind
        if para:
            out.append("<p>%s</p>" % _inline(" ".join(para)))
            para = []
        if items:
            out.append("<%s>%s</%s>" % (kind, "".join("<li>%s</li>" % _inline(i) for i in items), kind))
            items, kind = [], None

    for raw in text.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        h = re.match(r"^(#{2,3})\s+(.*)$", line)
        ul = re.match(r"^\s*[-*]\s+(.*)$", line)
        ol = re.match(r"^\s*\d+[.)]\s+(.*)$", line)
        q = re.match(r"^>\s?(.*)$", line)
        if h:
            flush()
            level = len(h.group(1))
            out.append("<h%d>%s</h%d>" % (level, _inline(h.group(2)), level))
        elif ul or ol:
            want = "ul" if ul else "ol"
            if para or (kind and kind != want):
                flush()
            kind = want
            items.append((ul or ol).group(1))
        elif q:
            flush()
            out.append("<blockquote><p>%s</p></blockquote>" % _inline(q.group(1)))
        else:
            if items:
                flush()
            para.append(line.strip())
    flush()
    return "\n".join(out)


# ------------------------------------------------------------------- imagini
def build_images(posts, src_root, out_img_dir, max_width=1600):
    """Fotografiile stirilor: redimensionate, in WebP, cu numele stirii."""
    from PIL import Image
    for p in posts:
        if not p.get("image"):
            continue
        src = os.path.join(src_root, IMAGES_DIR, p["image"])
        im = Image.open(src).convert("RGB")
        if im.width > max_width:
            im = im.resize((max_width, round(im.height * max_width / im.width)), Image.LANCZOS)
        name = "news-%s.webp" % p["slug"]
        im.save(os.path.join(out_img_dir, name), "WEBP", quality=82, method=6)
        p["img"] = "img/" + name
        p["img_size"] = im.size
