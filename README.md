# Pane Solutions — Homepage Directions

Three homepage design directions for **Pane Solutions LLC**, a window cleaning,
pressure washing and gutter cleaning business in Phoenix, Arizona.

**Live gallery:** https://lumen-marketing.github.io/pane-solutions-designs/

| | | |
|---|---|---|
| **Client** | Pane Solutions LLC · Answer Gaye | |
| **Phone** | +1 515-525-4127 | |
| **Email** | answergaye22@gmail.com | |
| **Instagram** | [@pane_solutions_llc](https://www.instagram.com/pane_solutions_llc/) | |
| **Nextdoor** | [pane-solutions-phoenix-az](https://nextdoor.com/pages/pane-solutions-phoenix-az/) | |
| **Rating** | 5.0 ★ from 13 Google reviews | |
| **Established** | 2023 | |

## Files

```
index.html                     gallery chooser — live scaled iframe previews
direction-1-pressure.html      dark industrial editorial
direction-2-altitude.html      sky-to-black descent poster
direction-3-spec-sheet.html    engineering drawing on paper stock
assets/photos/                 15 real job photos (1400w + 760w WebP)
assets/reels/                  3 real reel cover frames
assets/logo.png                logo, keyed to transparent
scrape/                        the Instagram extraction scripts (not deployed)
shots/                         headless verification harness (gitignored output)
```

Every page is **standalone** — no build step, no framework, no CDN CSS. Open any
HTML file directly.

## Content policy — verified facts only

Nothing on these pages is invented. Everything traceable:

- **5.0 ★ / 13 reviews**, **LLC est. 2023**, **Phoenix AZ**, and the three
  services come from the client's own Google and Nextdoor listings.
- **Every review is quoted as written**, attributed to the real reviewer name.
- **Every photo is the client's own**, pulled from their Instagram grid at the
  highest resolution Instagram serves (1440px). No stock photography.
- There are **no invented statistics** — no "500+ homes", no "10 years
  experience", no fabricated service-area list. If a number appears on the page,
  it is real.

## The three directions

### 01 — Pressure `direction-1-pressure.html`
The safe, premium one. Near-black throughout, strict engineering grid backdrop,
full-bleed hero photo under enormous expanded Archivo type with a measure rail
down the left edge. Reads like an established contractor.
**Type:** Archivo (expanded 125%) + Space Mono.

### 02 — Altitude `direction-2-altitude.html`
The memorable one. Opens in a bright Arizona sky and descends into black as you
scroll, built around the shot of the water-fed pole reaching a second-storey
window. The nav inverts from light to dark at the fold.
**Type:** Anton + Barlow / Barlow Condensed.

### 03 — Spec Sheet `direction-3-spec-sheet.html`
The most distinctive. The whole page is an engineering drawing — graph-paper
stock, a bordered sheet with corner registration marks, dimension lines with
arrowheads, part numbers on each service, and a real title block at the bottom.
**Type:** IBM Plex Mono + IBM Plex Sans Condensed.

## Furniture matrix

All three share **one section order** — nav → hero → proof → services → work →
reels → reviews → contact → footer — so the client compares the *look*, not the
layout. **Share the order, never the components.** No cell below is reused
across two directions; any new direction fills in a column before it ships.

| section | 01 Pressure | 02 Altitude | 03 Spec Sheet |
|---|---|---|---|
| hero | full-bleed photo, type overlay, measure rail | split: sky panel + tall photo column | 12-col drawing sheet, type cell + photo cell |
| proof | scrolling marquee strip | four-cell data table | rotated stamped seals |
| services | numbered full-width rows | three diagonal-cut columns | accordion with part numbers |
| work | asymmetric photo mosaic | drag-to-pan filmstrip | index table + cursor photo peek |
| reels | rack of three monitors | sticky caption + phone stack | three staggered tiles |
| reviews | big pull-quote + card grid | two drifting columns | note callout + ticker |
| contact | giant phone number band | sky panel + row list | engineering title block |

## Palette

Taken from the logo — a blue→cyan gradient P on pure black.

```
--bl  #567CD3   --az  #40A3D4   --cy  #2FD8DC
```

`--cy` is only used as a fill or rule on dark surfaces. On the light Spec Sheet
page, cyan-as-text uses a darkened `--cy-ink #0A6E78` — the bright cyan fails
contrast on paper.

## The Instagram reels

All three pages embed the client's three real reels using **Instagram's official
embed widget** (`embed.js`), which is what the client chose.

**Instagram's player does not auto-play.** It renders a cover frame with a play
button and the viewer taps to watch. This was verified before building, three
ways: the reel pages serve no `og:video`, expose no `<video>` element, and issue
zero video network requests without a login. Reel MP4s are not obtainable
unauthenticated, so a self-hosted auto-playing version needs the client to
export the three files from the Instagram app.

Implementation notes:

- `embed.js` is loaded **only when the reel section scrolls near the viewport**
  (`IntersectionObserver`, 400px margin) — it is a slow third-party script and
  should not block the rest of the page.
- Each panel shows the **real cover frame plus a direct link** underneath the
  embed slot. The fallback is only hidden once Instagram's iframe has actually
  rendered, so a blocked script, an offline visitor, or the account going
  private degrades to a real photo and a working link rather than an empty box.
- The white Instagram player is framed deliberately — as a rack-mounted monitor
  (01), a phone (02), or a bordered panel (03) — so it reads as designed rather
  than pasted on.

**To swap in self-hosted auto-playing video later:** drop `reel-1.mp4`,
`reel-2.mp4`, `reel-3.mp4` into `assets/reels/`, then in each page replace the
`.screen` contents with `<video src="…" autoplay muted loop playsinline
poster="…">` and delete the `embed.js` block. Roughly a ten-line change per
page.

## How the assets were obtained

Instagram serves no usable API and `curl` gets a login shell, so the grid was
rendered in **headless Chrome over CDP** and the signed CDN URLs read out of the
live DOM (`scrape/grid.mjs`, `scrape/posts.mjs`, `scrape/dl.mjs`).

Gotchas worth keeping:

- The **profile grid only serves 640px** thumbnails. Rendering each **post
  permalink** individually yields the **1440px** original — worth the extra
  twelve page loads.
- Signed CDN URLs **403 if you rebuild them**. The `oh=`/`oe=`/`_nc_ohc` params
  are a signature; take the URL verbatim from the DOM. Bumping `s150x150` →
  `s640x640` inside an otherwise-untouched URL does still work.
- The three reel posts expose **only their cover frame**, never the video.
- Sorting a post page's images by area picks up *other* posts' thumbnails from
  the "more posts" rail. Filter on the `alt` text (`Video by…`) instead.

## Verification

`shots/shot.mjs` renders every page in headless Chrome, scrolls the full
surface, awaits `decode()` on each image, then reports page height, horizontal
overflow, broken images, any element past the right edge, and the fonts that
actually resolved.

```
node shots/shot.mjs
```

Screenshot output in `shots/*.png` is gitignored.
