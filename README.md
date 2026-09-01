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
direction-2-altitude.html      full-bleed photo plate + squeegee wipe
direction-3-spec-sheet.html    engineering drawing, 3 switchable stocks
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

## Tiers

The three directions are mapped onto the three packages. **The pages themselves
are not tier-differentiated** — all three are one page at the same scope with
the same motion. The tier names the package the client buys; the page on each
card is that package's homepage, and Standard/Premium add the pages listed on
the card.

| tier | direction | why |
|---|---|---|
| **Basic** — get found | 01 Pressure | The most conventional of the three. Established-contractor look, phone number the size of a headline, nothing the visitor has to work for. |
| **Standard** — look established | 03 Spec Sheet | Credibility through precision — part numbers, a spec schedule, a title block. Reads organised and professional, which is exactly what this tier sells. |
| **Premium** — stand out | 02 Altitude | The most memorable: full-bleed photography, the edge-to-edge masthead and the squeegee wipe. Literally the "stand out" brief. |

Worth re-reading before changing this: pairing look to price means choosing a
design also chooses a scope, and the cheap tier has to look plainer on purpose.
That trade-off was raised and accepted deliberately — it is not an oversight.

Gallery card order is Basic → Standard → Premium, and the furniture matrix
columns follow the same order.

## The three directions

### 01 — Pressure `direction-1-pressure.html`
The safe, premium one. Near-black throughout, strict engineering grid backdrop,
full-bleed hero photo under enormous expanded Archivo type with a measure rail
down the left edge. Reads like an established contractor.
**Type:** Archivo (expanded 125%) + Space Mono.

### 02 — Altitude `direction-2-altitude.html`
The memorable one. The photograph is the surface rather than a card floating on
one: a full-bleed plate with the masthead running edge to edge across it and
cropped by the viewport, straddling the boundary between plate and black. The
page arrives behind frosted glass that a squeegee wipes clear on load — the one
transition that means something for a window cleaner. One call to action.
**Type:** Anton + Barlow / Barlow Condensed.

The first version of this hero was the default template arrangement (rating
chip → headline → paragraph → solid button beside outlined button → photo card
on a smooth gradient) and was rejected on sight. Swapping the photo inside that
layout did not help; the layout was the problem.

### 03 — Spec Sheet `direction-3-spec-sheet.html`
The most distinctive. The whole page is an engineering drawing — a bordered
sheet with corner registration marks, dimension lines with arrowheads, part
numbers on each service, and a real title block. The hero is a drawing: a
dimensioned window elevation that the squeegee strokes draw themselves onto,
with the photograph demoted to a pinned `FIG. 1` reference.
**Type:** IBM Plex Mono + IBM Plex Sans Condensed.

**Three sheet stocks**, switchable from the dots in the title strip and
deep-linkable with `?theme=`: **blueprint** (default, cyanotype), **drafting**
(white stock) and **vellum** (warm). Every surface colour is a token — the
first pass hard-coded `.nav` and `.sheet` backgrounds and they painted a milky
slab over the blueprint ground. `--on-acc` carries text that sits on the accent
gradient, which inverts between stocks.

## Furniture matrix

All three share **one section order** — nav → hero → proof → services → work →
reels → reviews → contact → footer — so the client compares the *look*, not the
layout. **Share the order, never the components.** No cell below is reused
across two directions; any new direction fills in a column before it ships.

| section | 01 Pressure | 02 Altitude | 03 Spec Sheet |
|---|---|---|---|
| hero | full-bleed photo, type overlay, measure rail | photo plate, edge-to-edge masthead, squeegee wipe | dimensioned window elevation + pinned photo ref |
| proof | scrolling marquee strip | four-cell data table | rotated stamped seals |
| services | numbered full-width rows | three diagonal-cut columns | accordion with part numbers |
| work | asymmetric photo mosaic | drag-to-pan filmstrip | index table + cursor photo peek |
| reels | rack of three monitors | sticky caption + phone stack | three staggered tiles |
| reviews | big pull-quote + card grid | two drifting columns | note callout + ticker |
| contact | giant phone number band | sky panel + row list | engineering title block |

## Palette

Taken from the logo — a blue-to-cyan P on pure black.

**No gradients.** Not one colour ramp anywhere in the set: buttons, headline
accents, underlines, play buttons and the contact band are all flat `--acc`.
The photographic scrims went too — they are flat washes now, which suits the
hard-edged look better than a fade. What still uses gradient *syntax* is only
hard-stop patterning with no blend: the graph-paper rules, the equipment rack's
ventilation slots, the two-tone palette swatches, and a couple of mask-images.
If you add anything here, keep it flat.

```
--bl  #567CD3   --az  #40A3D4   --cy  #2FD8DC
```

`--cy` is only used as a fill or rule on dark surfaces. Wherever cyan carries
text on a light stock it drops to a darkened `--cy-ink` — the bright cyan fails
contrast on paper. Spec Sheet redefines the whole set per stock; run
`node shots/themes.mjs` to re-check every one (it computes real contrast ratios
against the actual painted background, walking up for the first opaque
ancestor).

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
