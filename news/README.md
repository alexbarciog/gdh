# Posting news on gdh-group.com

Every file in this folder is one news item. Add a file, and about two minutes later
it is live at **gdh-group.com/news**, on the home page, in the RSS feed and in the
sitemaps Google reads. Nobody needs to run anything.

## Post a news item (from the browser)

1. Open this folder on GitHub: `github.com/alexbarciog/gdh/tree/main/news`.
2. Open `_template.md`, click **Copy raw file** (the copy icon).
3. Go back to the folder, click **Add file → Create new file**.
4. Name the file: the date, then a few words for the web address, with dashes:
   `2026-10-16-new-hub-in-cluj.md` → published at `gdh-group.com/news/new-hub-in-cluj`
5. Paste the template, fill it in, delete the lines that start with `#` in the header.
6. Click **Commit changes** → **Commit directly to the main branch** → **Commit changes**.

Done. Check the **Actions** tab: a green tick means it is live; a red cross means
something in the file needs fixing (see below) and the website stays as it was.

## What each header line does

| Line | What to write |
|---|---|
| `title` | The headline. Up to 90 characters. Say what happened. |
| `date` | Publication date, written `YYYY-MM-DD`, e.g. `2026-10-16`. |
| `category` | One of: Company, Network, Retail, Dental, Partnerships, Press. |
| `summary` | 70–160 characters. **This is the text Google, WhatsApp and LinkedIn show** — make it a full, specific sentence. |
| `image` | Optional. Upload the photo to `news/images/` first, then write its file name. |
| `image_alt` | Required when there is an image: what the photo shows, in a few words. |
| `updated` | Optional. If you correct a published item later, the date of the change. |

## Writing the text

Below the second `---`, write normally. Leave an empty line between paragraphs.

- `## Subheading` for a section title
- `**bold**`, `*italic*`
- `[link text](https://gdh-group.com/contact-sales)`
- lines starting with `-` become a bulleted list, `1.` a numbered list
- a line starting with `>` becomes a quote

The text must be at least a few sentences (200 characters). Write the most important
fact in the first sentence — that is what people and search engines read first.

## Schedule a post

Give it a future date. It stays hidden until that day; the site rebuilds every morning
at about 7:00 (Romanian time) and publishes whatever is due.

## Add a photo

In `news/images/`, click **Add file → Upload files**, upload a JPG/PNG/WebP (landscape,
at least 1600 px wide is best), commit. Then use its exact file name in `image:`.
The photo is resized automatically and also becomes the preview image when the link
is shared.

## Fix or remove a post

- **Fix:** open the file, click the pencil, edit, commit. Add `updated: YYYY-MM-DD`.
- **Remove:** open the file, **⋯ → Delete file**, commit. Avoid this once a post has
  been shared — the link will stop working. Prefer correcting it.
- **Do not rename** a published file: the name is the web address.

## If the Actions tab shows a red cross

Open the failed run → **Build the site**. The last lines say exactly which file and
what is wrong (in Romanian, e.g. *data trebuie scrisa AAAA-LL-ZZ* = the date must be
written YYYY-MM-DD; *rezumatul are N caractere* = the summary is too short or too long).
Fix the file and commit again. The live site is never affected by a broken file.

## Files in this folder that are not news

`README.md` (this guide), `_template.md` and anything starting with `_` are ignored.
