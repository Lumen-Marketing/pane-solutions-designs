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
through clean glass, reaching panes nobody else can, and a glazed facade at dusk.

**Second pass, same day.** Daylight and the Standard direction came back as too
plain and too flat, with a request for the layout archetypes from the Figma
website-layout article and for glassmorphism. Both were rebuilt again around
named archetypes and real glass; the Standard direction was replaced outright
(the machined-steel version is in `.old/d3-v2.html`). Reach was left alone, and
deliberately takes no glass at all, which is what keeps the three apart.

Glass is not a borrowed effect here. The company cleans glass, so a pane of it
is the product rather than a trend, and every pane on both pages sits over a
photograph so the blur actually has something to do.

## Files

```
index.html                     gallery chooser, live scaled iframe previews
direction-1-pressure.html      DAYLIGHT   light glass, full-screen photography
direction-2-altitude.html      REACH      dark cinematic, sticky stack, no glass
direction-3-spec-sheet.html    FACADE     smoked glass, split screen, dense
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

Light, airy, glass over full-screen photography. Bricolage Grotesque over
Instrument Sans, brand blue, panes at 26px with pill buttons. Layout archetypes:
**full-screen** hero and contact, **zig-zag** for the three services, and an
**asymmetric bento** for the job index.

**Depth device: one glass slab, plus a Z-axis cascade.** The pane is a 48%
white tint with `brightness(1.5)` on its `backdrop-filter`, which washes the
photograph underneath toward white far enough for dark type to sit on it while
the picture still shows through. An opaque white card is not glass.
 Two photo plates lap
the hero pane's lower corner
at opposing rotations, mirrored about the pane so the pair reads as composition
rather than as one thing knocked askew.

**One hairline, never two.** Both glass directions used to be a tray holding a
core, each with its own 1px rim, six or seven pixels apart. It got called out on
sight: it reads as a rendering fault, not as machining. The fill and the rim now
live on the pane and the core carries nothing but its padding.

### Standard, FACADE `direction-3-spec-sheet.html`

A glazed building at dusk. Deep slate-teal, warm amber, smoked glass. Syne over
Outfit, panes at 18px. This is the **dense** one of the three. Layout
archetypes: **split-screen** for the hero and the contact, **sticky split** for
the services where the photograph swaps as you scroll the column beside it
(which makes it an **interactive** layout too), and a **pane gallery** for the
job index.

**The three splits alternate and match.** Hero photograph left, services
photograph right, contact photograph left. Each photo half is exactly half the
width and one viewport tall, so the page reads as symmetrical top to bottom
rather than as one long left-hand column of pictures. The services flip is
`order`, not source order, so a phone still gets the photograph before the words
it belongs to.

**The pane gallery.** Twelve jobs held as twelve upright panes in a row. Point
at one, tab to one or tap one and it opens to roughly three quarters of the
width while the other eleven stay stacked at the edge carrying their labels
turned on their sides. One photograph is always large and all twelve are always
on screen, which a grid of captioned rectangles cannot do. It is a `flex-grow`
transition, nothing heavier. Below 900px a 36px slat is not a touch target, so
it becomes a scroll-snap strip with the next pane peeking.

**Depth device: one smoked glass slab.** The nav island's exact material: dark
translucent fill, heavy blur, one bright hairline rim, one lit top edge.

**A pane needs something behind it.** The first version of this page put glass
on a flat dark section and it read as a bordered rectangle, because blurring a
flat colour returns that same flat colour. The page now carries a **fixed
photographic ground**: one real photograph, **sharp**, saturated up and held at
just under half brightness, sitting behind everything. Every pane on the page has
real hue and luminance variation to refract. It is a photograph, not a gradient,
so the no-ramps rule still holds. Two traps that cost time:

- `isolation: isolate` on the pane opens a stacking context and cuts the element
  off from the backdrop it is supposed to be sampling. Remove it.
- The first ground was too dark and too heavily blurred, and collapsed to a flat
  brown, which is the same problem again with extra steps. Pick a frame with
  sky in it and keep brightness around .5.
- **Do not pre-blur the ground at all.** Look at a phone lock screen: the
  wallpaper behind the glass is sharp, and the tile is what frosts it. Blurring
  the photograph and then running `backdrop-filter` over it blurs the same
  pixels twice, and two blurs is mud. It went 46px, then 22px, then none, and
  none is the one that reads as glass.
- **A tint only reads as glass if what is under it is bright enough to survive
  being tinted.** The ground went to `brightness(.22)` to keep type legible and
  every pane immediately went back to looking like a dark rectangle: dim picture
  times dark film is a rectangle, and no amount of rim or shadow fixes it. The
  ground sits at `.48` now and the panes are a `.44` tint with a heavy blur and
  no brightness trick in them, which is what the reference actually does.
- **Choose the ground frame for even luminance, not for subject.** The first two
  candidates each had a dark mass right where the cards land, so the cards went
  dark wherever they sat. `adobe-sky` is bright corner to corner.
- Type that sits loose on the ground rather than on a pane needs a wide soft
  `text-shadow`, and the two copy halves of the split screens carry a flat
  `rgba` film. The film is part of what the pills on top of it sample, so they
  still frost a real picture.

### Premium, REACH `direction-2-altitude.html`

Near-black, photography carries everything, brand blue is the single accent.
Big Shoulders Display over Sora. Built vertically because the business is about
height: the three services are full-screen panels that pin and stack on top of
one another as you scroll, in pure CSS `position: sticky`. **No glass on this
one**, which is what keeps it distinct from the other two.

**Depth device: three physical planes.** A photograph at the back, one flat
atmospheric wash over it, and a plate lifted above both and hung across the
hero's bottom edge so it occludes what is under it. Reviews sit behind glass
panes with a lit top edge, a dark foot and one reflection that sweeps on hover.

## Tiers

The three directions are mapped onto the three packages. **The pages themselves
are not tier-differentiated**: all three are one page at the same scope. The
tier names the package the client buys, the page on each card is that package's
homepage, and Standard/Premium add the pages listed on the card.

| tier | direction | why |
|---|---|---|
| **Basic**, get found | Daylight | The brightest and the calmest. Big legible glass panes over the client's own photography. |
| **Standard**, look established | Facade | Dense, dark, a lot of work on show. The split screen that follows what you are reading is the thing people remember. |
| **Premium**, stand out | Reach | Full-bleed cinematic photography and a sticky stack. Literally the "stand out" brief. |

Worth re-reading before changing this: pairing look to price means choosing a
design also chooses a scope, and the cheap tier has to look plainer on purpose.
That trade-off was raised and accepted deliberately, it is not an oversight.

Gallery card order is Basic, Standard, Premium, and the matrix columns follow.

## Furniture matrix

All three share **one section order**: nav, hero, services, **process**,
**why us**, work, reels, reviews, **FAQ**, contact, footer. So the client
compares the *look*, not the layout. **Share the order, never the components.**
No cell below is reused across two directions; any new direction fills in a
column before it ships.

| section | Basic, Daylight | Standard, Facade | Premium, Reach |
|---|---|---|---|
| theme | light, warm neutral | deep slate-teal | near black |
| glass | light frosted panes over photos | smoked panes over a fixed photographic ground | none, this one stays opaque |
| depth device | one glass slab, plus a Z-axis photo cascade | one smoked slab over a fixed blurred ground | three planes, foreground occlusion |
| hero | full-screen photo, glass card, two lapping plates | split screen, pane crossing the seam | full bleed photo, plate hung over the edge |
| services | zig-zag of three photographic bands | sticky split, photo swaps per service | full-screen sticky stack |
| work | asymmetric bento, ten tiles | pane gallery, twelve slats that open | drag-to-pan filmstrip |
| reels | three light glass plates | three smoked plates | three ink plates |
| reviews | glass panes over a photo band | smoked panes with an amber edge | glass panes with a reflection sweep |
| contact | full-screen photo, one big pane | split screen, bookending the hero | photograph with the number over it |
| process | ruled 2x2 cells, outlined ghost numerals | glass tiles threaded on a hairline rail | staggered either side of a centre spine |
| why us | four columns ruled apart, no cards | asymmetric 2x2 with a photo in one cell | solid cards nested inside a colour panel |
| FAQ | sticky title left, accordion right | one heading, questions in two columns | sticky title left, square accordion right |
| footer | four columns on paper | four columns on the fixed photograph | four columns on a raised ink band |

## The wireframe pass

He sent four layout wireframes and asked for those layouts. They are grey box
templates, so what came across is the **structural devices**, not the look:
overlapping and floating cards, tab filters, enormous ghost numerals, sticky
title columns, accordions, nested panels, asymmetric feature grids, and a real
footer with columns. Each one is built in the direction's own material.

Three of the sections the wireframes have and these pages did not are worth
having on their own merits:

| section | why it was missing and why it matters |
|---|---|
| **process** | the page told you what they sell and never what happens after you call. It is also where the free estimate earns its second mention without repeating a CTA. |
| **why us** | four differentiators that were buried inside service copy. Every claim in it is already made elsewhere on the page. |
| **FAQ** | the highest converting section a trade site can have, and all three ended without one. Native `details` and `summary`, so it opens with the JS off, it is already in the tab order, and find-in-page reaches closed answers. |
| **footer** | all four wireframes end on four columns. These pages ended on one line of grey type, throwing away the last screen. |

**Two devices were adopted and one was refused.** The tab filter went on
Daylight's job index, because sorting a client's own photographs invents
nothing. The stat rows in the wireframes did not, because filling `1.3k / 531 /
35` with real numbers is impossible here and filling it with anything else
breaks the content policy at the top of this file.

**The FAQ answers assert nothing new.** Every one is built out of a claim
already on the page: the fed pole, purified water, pressure matched to the
surface, free estimates, homes and businesses, Phoenix, screens and tracks and
sills. Questions whose honest answer is unknown, such as whether the customer
needs to be home, are simply not asked.

**Two bugs the pass produced, both caught in a screenshot.** Facade's why grid
put a 3:4 photograph in flow at five of twelve columns, so the row was sized to
780px and the card beside it carried 500px of empty glass; the image is now
absolutely positioned inside its figure and the type sizes the row. Daylight's
ghost numerals were a solid pale fill and body copy ran across the middle of a
3 and a 4; they are outlined now, which reads the same as a graphic device and
leaves nothing behind the words.

## Grounds: the rule the whole set now follows

Flat colour was the complaint, and "add texture everywhere" would have been the
wrong answer. Every section on every page is one of three kinds, and no page
uses one kind more than about twice in a row.

| kind | what it is | when |
|---|---|---|
| **IMAGE** | a real client photograph under one flat veil | when the section has no photographs of its own |
| **PLAIN** | flat colour, nothing on it | when the section's own content is already busy. The bento of ten photographs does not need a patterned ground behind it |
| **COLOUR + TEXTURE** | a block of the accent with a real photograph laid into it, greyscaled and held low | once per page, as the one place the page raises its voice |

That third one is not decoration. **A pane of glass over a flat colour is a
rectangle**, so any section carrying glass cards needs either a photograph or a
colour block with a photograph in it. A 4 percent SVG pattern is not enough:
blur turns fine texture into a flat field, which is the same problem again.
Texture gives a plain section tooth; only large scale variation makes glass read.

The per page rhythm:

| | Daylight | Facade | Reach |
|---|---|---|---|
| hero | image | image, over the fixed ground | image |
| services | plain with a dot field | fixed ground, sticky split | plain with a rake, sticky panels |
| work | plain | fixed ground | plain with a rake |
| reels | **colour block**, brand blue | fixed ground | plain with a rake |
| reviews | plain with a dot field | fixed ground | **colour block**, deep blue |
| contact | image | image | image |

**Two photographic grounds per page is the budget, and the hero and the contact
spend both.** The count is the thing that went wrong first: the services section
on each page was built as three full screen photographic bands, which on its own
put five of eight scroll moments on a photograph and made the whole page read as
one long wash. The chooser reads calmer than the pages did for exactly one
reason: it has ONE background photograph and everything else floats on it.

The distinction that was missing is **a photograph as a GROUND versus a
photograph as an OBJECT.** The chooser is full of imagery, all of it held inside
cards, and its ground never changes. Both services sections are now photographs
held in a section rather than behind it: contained plates on Daylight, a
square edged plate inside each sticky panel on Reach.

A second thing falls out of that. Daylight's first two service rows are type
beside a photograph with no card at all, because a glass card on flat paper is a
white rectangle for the same reason a dark pane on flat near-black is a dark
one. Only the third row laps a card across a photograph, where the material has
something to do. Cards where elevation means something, and nowhere else.

Facade is the exception on purpose: it carries one fixed photograph behind the
entire document, which is its whole depth device, so it does not need a
per section rhythm.

Each direction gets its own texture so they cannot be confused: a soft **dot
field** on Daylight, a hairline **rake** on Reach, and the fixed photograph on
Facade. Both are SVG data URIs, never `repeating-linear-gradient`, because the
no-ramps rule on this set is absolute.

## Glass, per direction

The same physics three times with a different edge each time, so the set does
not collapse into one look:

- **Daylight**: soft cornered, light. `rgba(255,255,255,.48)` with
  `brightness(1.5)` on the `backdrop-filter`, which washes the photograph
  underneath toward white far enough for dark type to sit on it.
- **Facade**: soft cornered, smoked. A `.44` dark tint over the fixed ground.
- **Reach**: **square cornered**, with a lit top rule and a dark foot so it
  reads as a bevelled sheet rather than a rounded chip.

## The chooser

`index.html` was the last thing still in the old language: cyan, Space Mono
chips, and two `linear-gradient` grids in the background. Rebuilt on the same
material as the pages it presents. One family, Archivo, in two roles, because
each direction owns a type pairing and the chooser cannot borrow one without
looking like a fourth entry in its own list. Live previews are unchanged: a
full size iframe scaled with a transform, so what you see is the real page at a
real viewport width.

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
Daylight   paper #EDF0F2   ink #101418    accent #1B54C8  (brand blue)
Facade     bg    #0D1A21   paper #E9F1F4  accent #FFB020  (warm amber, on the
                                                    button and the stars only)
Reach      ink   #0B0E11   paper #F4F6F8  accent #2E6FE0  (brand blue)
```

### The glass is gradient-free

The standing no-gradients rule and glassmorphism look like they conflict: the
usual recipe leans on a diagonal white gradient for its highlight. They do not
have to. Every fill here is one flat `rgba`, every lit edge is an
`inset box-shadow`, and every rim is a 1px border. `backdrop-filter` is not a
gradient. That reads as real glass and keeps the rule.

Three more things that matter for it not to look cheap:

- **Contrast floor.** Light panes are held at .62 to .74 white with a heavy
  blur so ink type stays readable over any photograph behind it.
- **`prefers-reduced-transparency`.** Every pane has a solid fallback.
- **Blur budget.** Blur costs GPU on every repaint. It is on the panes and the
  nav, never on a large scrolling container, and the grain stays on one fixed
  `pointer-events:none` layer.


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
