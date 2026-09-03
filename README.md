# Pane Solutions, homepage directions

Three homepage design directions for **Pane Solutions LLC**, a window cleaning,
pressure washing and gutter cleaning business in Phoenix, Arizona.

**Live gallery:** https://lumen-marketing.github.io/pane-solutions-designs/

| | |
|---|---|
| **Client** | Pane Solutions LLC, Answer Gaye |
| **Phone** | +1 515-525-4127 |
| **Email** | answergaye22@gmail.com |
| **Instagram** | [@pane_solutions_llc](https://www.instagram.com/pane_solutions_llc/) |
| **Nextdoor** | [pane-solutions-phoenix-az](https://nextdoor.com/pages/pane-solutions-phoenix-az/) |
| **Rating** | 5.0 ★ from 13 Google reviews |
| **Established** | 2023 |

## The rebuild, and why

The first set of three was rejected for reading as machine-made. The audit found
every one of the standing tells across all three pages, so they were rebuilt
from scratch rather than patched. What was wrong, concretely:

| what was on the page | why it had to go |
|---|---|
| `01 / SERVICES`, `02 / RECENT WORK`, `SHEET 01`, `SHEET 05 OF 05` | a numbered eyebrow above every section. Budget is `ceil(sections / 3)`; the pages ran one per section. All three now use **zero**. |
| an equipment rack with `REEL 01` headers and pulsing LEDs | fake UI chrome, and the LEDs claimed live status on things that are not live |
| phone mockups with notches and a glowing status dot | same class of tell, and it is an app-marketing device on a trade site |
| `DOC. PS-2023 / REV. A`, `SCALE`, `DRAWN BY`, a title block | a fake engineering document. That concept belongs to a drafting firm. |
| 48 visible em-dashes, 27 middle-dot chains | zero em-dashes now, zero middle dots |
| `Scroll` cue with an animated line | the viewer knows what scrolling is |
| service thumbnails at 200px, tiles labelled `01`&ndash;`08` | photographs shrunk into cards, plus pagination on things the eye can count |

The deeper problem was not the checklist. **All three concepts were borrowed
from other briefs**: a devtool dashboard, an app landing page and a drafting
sheet. None of them came from window cleaning. Removing the glows would not have
saved any of them.

The three rebuilds all start from what the business actually sells: daylight
through clean glass, reaching panes nobody else can, and painted-steel trade
work.

## Files

```
index.html                     gallery chooser, live scaled iframe previews
direction-1-pressure.html      DAYLIGHT   light poster, sparse
direction-2-altitude.html      REACH      dark cinematic, sticky stack
direction-3-spec-sheet.html    STEEL      industrial, dense, machined plates
assets/photos/                 15 real job photos (1400w + 760w WebP)
assets/reels/                  3 real reel cover frames
assets/logo.png                logo, keyed to transparent
scrape/                        Instagram extraction + rewrite scripts (not deployed)
shots/                         headless verification harness (output gitignored)
.old/                          the rejected first set, kept for reference only
```

The filenames are unchanged so existing links keep working; the direction
**names** changed with the rebuild.

Every page is **standalone**. No build step, no framework, no CDN CSS. Open any
HTML file directly.

## Content policy, verified facts only

Nothing on these pages is invented. Everything is traceable:

- **5.0 ★ / 13 reviews**, **LLC est. 2023**, **Phoenix AZ** and the three
  services come from the client's own Google and Nextdoor listings.
- **Every review is quoted as written**, attributed to the real reviewer name.
- **Every photo is the client's own**, pulled from their Instagram grid at the
  highest resolution Instagram serves (1440px). No stock photography.
- There are **no invented statistics**. No "500+ homes", no "10 years
  experience", no fabricated service-area list. If a number appears on the page,
  it is real.

## The three directions

### Basic, DAYLIGHT `direction-1-pressure.html`

Light off-white paper, ink type, one saturated blue used on big surfaces.
Bricolage Grotesque over Instrument Sans. Density 2: this is a poster, not a
website. The hero sets type on bare paper against a photograph that runs off the
right edge of the viewport, and a paper plate laps across the boundary between
them. Services are three full-width bands, not a row of cards.

**Depth device: offset colour planes.** A flat blue plane sits behind each major
object, shifted down and right, so things stack. No blur, no glass, no glow.

### Standard, STEEL `direction-3-spec-sheet.html`

Painted steel, off-black, safety orange. Archivo Expanded over IBM Plex Sans.
Density 7: heavy rules, tight grids, everything lines up. The services are a
horizontal accordion of full-height photographs where one opens at a time. The
job index is a deliberately uniform eight-cell grid, which is the opposite of
Daylight's asymmetric mosaic.

**Depth device: machined plates.** Every object has a lit top edge, a dark foot
and a hard accent offset with no blur, so it reads as metal standing off the
panel behind it. Review quotes sit in cores recessed below the plate face.

**On the orange:** the accent is safety orange rather than the logo blue. That
is a deliberate option. It is the complementary colour to the mark, it is what
makes this direction read as different rather than as a recolour of the others,
and the logo itself still carries the brand blue. One word and it becomes blue.

### Premium, REACH `direction-2-altitude.html`

Near-black, photography carries everything, brand blue is the single accent.
Big Shoulders Display over Sora. Density 5. Built vertically because the
business is about height: the three services are full-screen panels that pin and
stack on top of one another as you scroll, in pure CSS `position: sticky`.

**Depth device: three physical planes.** A photograph at the back, one flat
atmospheric wash over it, and a plate lifted above both and hung across the
hero's bottom edge so it occludes what is under it. Reviews sit behind glass
panes with a lit top edge, a dark foot and one reflection that sweeps on hover,
which on a page about glass is the material the page is already made of.

## Tiers

The three directions are mapped onto the three packages. **The pages themselves
are not tier-differentiated**: all three are one page at the same scope. The
tier names the package the client buys, the page on each card is that package's
homepage, and Standard/Premium add the pages listed on the card.

| tier | direction | why |
|---|---|---|
| **Basic**, get found | Daylight | The plainest and the calmest. Sparse, legible, nothing to work out. |
| **Standard**, look established | Steel | Reads like a working trade with real equipment behind it. Dense and organised, which is what this tier sells. |
| **Premium**, stand out | Reach | The most memorable: full-bleed photography, a sticky stack, glass panes. Literally the "stand out" brief. |

Worth re-reading before changing this: pairing look to price means choosing a
design also chooses a scope, and the cheap tier has to look plainer on purpose.
That trade-off was raised and accepted deliberately, it is not an oversight.

Gallery card order is Basic, Standard, Premium, and the matrix columns follow.

## Furniture matrix

All three share **one section order**: nav, hero, services, work, reels,
reviews, contact, footer. So the client compares the *look*, not the layout.
**Share the order, never the components.** No cell below is reused across two
directions; any new direction fills in a column before it ships.

| section | Basic, Daylight | Standard, Steel | Premium, Reach |
|---|---|---|---|
| theme | light paper | painted steel | near black |
| depth device | offset colour planes | machined plates, lit edge, hard offset | three planes, foreground occlusion |
| hero | type left, photo bled off the right edge | dense split with a plate photo | full bleed photo, plate hung over the edge |
| services | three full-width bands | photo accordion, one opens at a time | full-screen sticky stack |
| work | asymmetric mosaic | uniform index grid, eight cells | drag-to-pan filmstrip |
| reels | three equal blue plates | three equal steel plates | three equal ink plates |
| reviews | paper plates over a blue plane | plate with a recessed core | glass panes with a reflection sweep |
| contact | solid blue block | ink block with an orange rule | photograph with the number over it |

## Standing rules for this set

These are constraints the client set, not preferences. Breaking one is a
regression.

- **No gradients.** Not one colour ramp anywhere. Buttons, headline accents,
  underlines, play buttons, contact bands and every photographic scrim are flat.
  A scrim under a caption is exactly the kind of ramp that got binned; use a
  flat plane with a hard rule instead.
- **Zero em-dashes and zero middle dots** in anything visible, including alt
  text, titles and meta descriptions. `grep -c` before shipping.
- **No numbered section eyebrows**, no mono micro-labels above headings, no
  scroll cues, no decorative status dots, no fake device or document chrome.
- **Photographs run at scale.** Never shrunk into small cards.
- **Captions live inside the enclosure**, as part of the object, never as a pill
  floating on top of a photograph.
- **Each direction gets its own depth device.** Never apply one treatment across
  the set, and after a depth pass walk every section so nothing is left flat.
- **Symmetry within a set of peers**, variety between sections. An unanchored
  stagger reads as a rendering fault.

### Palettes

One accent per page, locked across every section, and one radius system per page
(all three are zero).

```
Daylight   paper #EDEEF0   ink #14181C   accent #1B54C8  (brand blue)
Reach      ink   #0B0E11   paper #F4F6F8 accent #2E6FE0  (brand blue)
Steel      steel #D3D5D2   ink #121413   accent #E24E12  (safety orange)
```

## The Instagram reels

All three pages embed the client's three real reels using **Instagram's official
embed widget** (`embed.js`), which is what the client chose.

**Instagram's player does not auto-play.** It renders a cover frame with a play
button and the viewer taps to watch. This was verified three ways: the reel
pages serve no `og:video`, expose no `<video>` element, and issue zero video
network requests without a login. Reel MP4s are not obtainable unauthenticated,
so a self-hosted auto-playing version needs the client to export the three files
from the Instagram app.

Implementation notes:

- `embed.js` loads **only when the reel section scrolls near the viewport**
  (`IntersectionObserver`, 400px margin). It is a slow third-party script and
  should not block the rest of the page.
- Each panel shows the **real cover frame plus a direct link** underneath the
  embed slot. The fallback is hidden only once Instagram's iframe has actually
  reported a height, so a blocked script, an offline visitor or the account
  going private degrades to a real photo and a working link rather than an
  empty box. Treating mere iframe *presence* as rendered leaves three empty
  bays; require `getBoundingClientRect().height > 300`.
- **Instagram sizes every embed to its own video aspect.** Two of these reels
  are portrait and one is landscape, so their natural heights are 616px and
  392px. Left alone the row of three is visibly ragged. Every direction stretches
  the row, pins the plate to 642px and top-aligns the embeds, so the three
  Instagram headers line up. The short one keeps empty plate beneath it. That
  leftover is painted in the plate colour so it reads as plate rather than as a
  hole, because the white card inside cannot be restyled from outside its
  iframe.

**To swap in self-hosted auto-playing video later:** drop `reel-1.mp4`,
`reel-2.mp4`, `reel-3.mp4` into `assets/reels/`, then in each page replace the
`.screen` contents with `<video src="…" autoplay muted loop playsinline
poster="…">` and delete the `embed.js` block. Roughly a ten-line change per page.

## How the assets were obtained

Instagram serves no usable API and `curl` gets a login shell, so the grid was
rendered in **headless Chrome over CDP** and the signed CDN URLs read out of the
live DOM (`scrape/grid.mjs`, `scrape/posts.mjs`, `scrape/dl.mjs`).

Gotchas worth keeping:

- The **profile grid only serves 640px** thumbnails. Rendering each **post
  permalink** individually yields the **1440px** original, worth the extra
  twelve page loads.
- Signed CDN URLs **403 if you rebuild them**. The `oh=`/`oe=`/`_nc_ohc` params
  are a signature; take the URL verbatim from the DOM. Bumping `s150x150` to
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
node shots/shot.mjs                    # all four pages at 1440
W=390 SLICES=3 node shots/shot.mjs     # phone
node shots/reels.mjs                   # asserts no reel plate is empty
node shots/hover.mjs                   # real pointer hover, TOUCH=1 for coarse
node shots/live.mjs                    # renders the deployed URL
```

Two harness notes that cost time: a single tall `captureScreenshot` hangs on
pages with `position: fixed` grain and `backdrop-filter`, so it captures
viewport slices instead; and `setDeviceMetricsOverride` alone does **not** change
the pointer, so `hover: none` fallbacks look broken in every mobile capture
until `Emulation.setEmulatedMedia` is set explicitly.

Screenshot output in `shots/*.png` is gitignored.
