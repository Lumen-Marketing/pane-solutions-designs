# -*- coding: utf-8 -*-
"""REACH: ground rhythm, texture, and its own square-cornered glass.

The complaint was flat plain colour, and Reach was the worst of the three: the
work section, the reels section and the reviews section were all a single flat
near-black, so a third of the page was an empty slab. It also had no glass at
all, and its glass panes were only called glass, being a 6 percent white fill
over a colour with no backdrop-filter behind it.

Ground rhythm down the page, one of each kind rather than six of the same:

  hero        IMAGE            photograph
  services    IMAGE            three sticky photograph panels
  work        PLAIN + rake     near-black, a hairline rake for tooth, and the
                               filmstrip photographs carry the section
  reels       IMAGE            photograph under a heavy flat veil
  reviews     COLOUR + TEXTURE deep blue block with a real photograph laid in
                               as its texture, greyscaled and low
  contact     IMAGE            photograph

That reviews block is the one colour moment on the page, and the texture in it
is what lets glass work there: a pane over a FLAT colour is a rectangle, and no
amount of blur changes that. A photograph laid into the colour gives the blur
something to carry.

Reach's glass is SQUARE. Daylight's is soft, Facade's is soft, and this page has
had sharp corners throughout from the start. Same physics, different edge, so
the three stay apart.
"""
import io
import os
import re

p = os.path.join(os.path.dirname(__file__), '..', 'direction-2-altitude.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    s = s.replace(a, b)


def rswap(pat, b, n=1):
    global s
    s2, c = re.subn(pat, lambda m: b, s, flags=re.S)
    assert c == n, 'NO MATCH (%d) -> %s' % (c, pat[:80])
    s = s2


# ── tokens ────────────────────────────────────────────────────────────────
swap("""  --blue:#2E6FE0;       /* the single accent. No second colour on this page. */
  --blue-d:#1E51AC;""",
"""  --blue:#2E6FE0;       /* the single accent. No second colour on this page. */
  --blue-d:#1E51AC;
  --blue-block:#173F86; /* the one colour block, a shade of the same accent */""")

# ── the two grounds this page needs ───────────────────────────────────────
swap("""h1,h2,h3,.disp{
  font-family:'Big Shoulders Display','Sora',sans-serif;font-weight:800;
  line-height:.86;letter-spacing:.005em;text-transform:uppercase;
}""",
"""h1,h2,h3,.disp{
  font-family:'Big Shoulders Display','Sora',sans-serif;font-weight:800;
  line-height:.86;letter-spacing:.005em;text-transform:uppercase;
}

/* ── grounds ──────────────────────────────────────────────────────────────
   Three kinds, used once each rather than one kind used six times.

   RAKE. Hairlines across a flat colour, wide apart and barely there, so a
   plain section has tooth without becoming a pattern. An SVG, not a repeating
   gradient, because the no-ramps rule on this set is absolute.

   TINT. A colour block with a real photograph laid into it, greyscaled and
   held low. This is the version of "coloured background" that glass can sit
   on: a pane over a flat colour is a rectangle no matter how it is tuned, and
   a photograph in the colour gives the blur something to carry. */
.rake{position:relative}
.rake::before{
  content:'';position:absolute;inset:0;z-index:0;pointer-events:none;opacity:.5;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='6' height='6'%3E%3Crect width='6' height='1' fill='%23F4F6F8' fill-opacity='.055'/%3E%3C/svg%3E");
}
.rake>*{position:relative;z-index:1}

.tint{position:relative;background:var(--blue-block);overflow:hidden}
.tint-bg{position:absolute;inset:0;z-index:0;pointer-events:none;
  opacity:.3;filter:grayscale(1) contrast(1.25) brightness(.9);mix-blend-mode:luminosity}
.tint-bg img{width:100%;height:100%;object-fit:cover}
.tint>.wrap,.tint>*:not(.tint-bg){position:relative;z-index:1}

/* ── this page's glass: square, not soft ─────────────────────────────────
   Same physics as the other two directions, different edge. A dark tint, a
   heavy blur, a lit top rule and a dark foot so it reads as a bevelled sheet
   rather than a rounded chip. Every use of it sits over a photograph or over
   the tinted block, never over a flat colour. */
.sheet{
  position:relative;
  background:rgba(11,14,17,.42);
  backdrop-filter:blur(26px) saturate(180%);
  -webkit-backdrop-filter:blur(26px) saturate(180%);
  border:1px solid rgba(244,246,248,.16);
  border-top-color:rgba(244,246,248,.4);
  border-bottom-color:rgba(0,0,0,.6);
  box-shadow:inset 0 1px 0 rgba(244,246,248,.24),0 26px 60px rgba(4,7,10,.5);
}
@media(prefers-reduced-transparency:reduce){
  .sheet{background:#131920;backdrop-filter:none;-webkit-backdrop-filter:none}
}""")

# ── nav: a detached square bar, not a strip glued to the top ──────────────
swap(""".nav{
  position:fixed;top:0;left:0;right:0;z-index:70;height:74px;display:flex;align-items:center;
  gap:26px;padding-inline:var(--gut);
  background:rgba(11,14,17,.72);backdrop-filter:blur(16px);border-bottom:1px solid var(--line);
}""",
"""/* Detached and inset, and square: Facade's nav is a pill, so this one cannot
   be. A bar glued edge to edge across the top is the default every site has. */
.nav{
  position:fixed;top:14px;left:var(--gut);right:var(--gut);z-index:70;height:66px;
  display:flex;align-items:center;gap:26px;padding-inline:20px;
  background:rgba(11,14,17,.5);
  backdrop-filter:blur(24px) saturate(180%);
  -webkit-backdrop-filter:blur(24px) saturate(180%);
  border:1px solid rgba(244,246,248,.16);
  border-top-color:rgba(244,246,248,.34);
  box-shadow:inset 0 1px 0 rgba(244,246,248,.2),0 20px 46px rgba(4,7,10,.55);
}
@media(prefers-reduced-transparency:reduce){.nav{background:#0F141A;backdrop-filter:none}}""")
swap(""".nav .btn{display:none}""", """.nav .btn{display:none}
  .nav{left:12px;right:12px;padding-inline:14px}""")

# ── the hero plate becomes real glass, since it laps the photograph ───────
swap("""  background:var(--ink-2);border:1px solid var(--line);
  display:grid;grid-template-columns:repeat(3,1fr);
}""",
"""  display:grid;grid-template-columns:repeat(3,1fr);
}""")
swap("""  position:relative;z-index:3;margin-inline:var(--gut);margin-bottom:clamp(-104px,-7.4vw,-62px);""",
"""  position:relative;z-index:3;margin-inline:var(--gut);margin-bottom:clamp(-104px,-7.4vw,-62px);
  /* .sheet carries the material. It laps the hero photograph, so the blur has
     a real picture to work on. */""")
swap("""<div class="hang">""", """<div class="hang sheet">""")
swap(""".hang div{padding:clamp(20px,2.3vw,30px) clamp(20px,2.4vw,32px);border-right:1px solid var(--line)}""",
     """.hang div{padding:clamp(20px,2.3vw,30px) clamp(20px,2.4vw,32px);border-right:1px solid rgba(244,246,248,.14)}""")

# ── work: plain with tooth, and a header that stops floating ──────────────
swap(""".work{padding-block:clamp(70px,9vw,130px);background:var(--ink)}
.sec-hd{display:flex;align-items:flex-end;justify-content:space-between;gap:30px;flex-wrap:wrap;margin-bottom:clamp(26px,3.4vw,46px)}
.sec-hd h2{font-size:clamp(2.6rem,6vw,5.4rem)}
.sec-hd p{max-width:38ch;color:var(--mute)}""",
""".work{padding-block:clamp(70px,9vw,130px);background:var(--ink)}
/* The sub-line used to float in the top right corner of the section with
   nothing aligned to it, which is what left the header reading as an empty
   slab. Stacked under the headline it is just a sentence. */
.sec-hd{margin-bottom:clamp(26px,3.4vw,46px)}
.sec-hd h2{font-size:clamp(2.6rem,6vw,5.4rem)}
.sec-hd p{margin-top:16px;max-width:52ch;color:var(--mute)}""")

swap("""<section class="work" id="work">""", """<section class="work rake" id="work">""")

# filmstrip captions become glass, since they sit on the photographs
swap(""".frame figcaption{padding:15px 17px;font-size:13.5px;font-weight:500;
  border-top:1px solid var(--line);background:var(--ink-2)}""",
"""/* the caption lies ON the photograph as a sheet of glass, rather than being a
   solid bar bolted under it */
.frame figcaption{position:absolute;left:0;right:0;bottom:0;
  padding:14px 17px;font-size:13.5px;font-weight:500;
  background:rgba(11,14,17,.42);
  backdrop-filter:blur(22px) saturate(180%);
  -webkit-backdrop-filter:blur(22px) saturate(180%);
  border-top:1px solid rgba(244,246,248,.34);
}
@media(prefers-reduced-transparency:reduce){.frame figcaption{background:#131920;backdrop-filter:none}}""")
swap(""".frame img{width:100%;aspect-ratio:3/4;object-fit:cover;transition:scale 1.2s var(--ease);""",
     """.frame img{display:block;width:100%;aspect-ratio:3/4;object-fit:cover;transition:scale 1.2s var(--ease);""")

# ── reels: a photograph ground so the plates can be glass ────────────────
swap(""".reels{padding-block:clamp(70px,9vw,130px);background:var(--ink-2);border-block:1px solid var(--line)}""",
""".reels{position:relative;overflow:hidden;padding-block:clamp(70px,9vw,130px);
  border-block:1px solid var(--line)}
.reels-bg{position:absolute;inset:0;z-index:0}
.reels-bg img{width:100%;height:100%;object-fit:cover;object-position:50% 40%}
.reels-bg::after{content:'';position:absolute;inset:0;background:rgba(8,11,14,.6)}
.reels>.wrap{position:relative;z-index:2}""")
swap(""".pane{position:relative;display:flex;background:var(--ink-3);padding:clamp(10px,1.1vw,16px);
  border:1px solid var(--line)}""",
""".pane{display:flex;padding:clamp(10px,1.1vw,16px)}""")
swap("""<section class="reels" id="reels">
  <div class="wrap">""",
"""<section class="reels" id="reels">
  <div class="reels-bg"><img src="assets/photos/glass-corner.webp" alt="" aria-hidden="true" loading="lazy"></div>
  <div class="wrap">""")
s = s.replace('<div class="pane rv"', '<div class="pane sheet rv"')

# ── reviews: the one colour block, with a photograph as its texture ──────
swap(""".reviews{padding-block:clamp(70px,9vw,130px)}""",
"""/* The one colour moment on the page. Three flat near-black sections in a row
   was the thing that read as unfinished. */
.reviews{padding-block:clamp(80px,10vw,140px)}
.reviews .wrap{position:relative;z-index:1}""")

swap("""<section class="reviews wrap" id="reviews">""",
"""<section class="reviews tint" id="reviews">
  <div class="tint-bg"><img src="assets/photos/patio-row.webp" alt="" aria-hidden="true" loading="lazy"></div>
  <div class="wrap">""")
swap("""    </article>
  </div>
</section>

<section class="contact" id="contact">""",
"""    </article>
  </div>
  </div>
</section>

<section class="contact" id="contact">""")

# the pull quote on blue: the accent word cannot be the accent colour any more
swap(""".pull blockquote em{font-style:normal;color:var(--blue)}""",
"""/* on the blue block the accent word cannot be the accent colour, so it is cut
   out of the same type instead */
.pull blockquote em{font-style:normal;color:transparent;
  -webkit-text-stroke:2px rgba(244,246,248,.85)}
@supports not (-webkit-text-stroke:1px #000){.pull blockquote em{color:#BBD3FF}}""")
swap(""".stars{color:var(--blue);letter-spacing:.14em;font-size:15px}""",
     """.stars{color:#8FB6FF;letter-spacing:.14em;font-size:15px}""")

# the review panes get the page's real glass
swap(""".gpane{
  position:relative;overflow:hidden;isolation:isolate;
  background:rgba(244,246,248,.06);
  border:1px solid rgba(244,246,248,.1);
  border-top-color:rgba(244,246,248,.42);      /* lit top edge */
  border-bottom-color:rgba(0,0,0,.72);         /* dark foot. Reads as a bevel. */
  box-shadow:inset 0 1px 0 rgba(244,246,248,.16), 0 26px 60px rgba(4,7,10,.55);
  padding:clamp(20px,2.2vw,30px);""",
""".gpane{
  position:relative;overflow:hidden;
  background:rgba(11,14,17,.34);
  backdrop-filter:blur(24px) saturate(180%);
  -webkit-backdrop-filter:blur(24px) saturate(180%);
  border:1px solid rgba(244,246,248,.18);
  border-top-color:rgba(244,246,248,.45);      /* lit top edge */
  border-bottom-color:rgba(0,0,0,.55);         /* dark foot. Reads as a bevel. */
  box-shadow:inset 0 1px 0 rgba(244,246,248,.2), 0 26px 60px rgba(4,7,10,.45);
  padding:clamp(20px,2.2vw,30px);""")
swap(""".gpane:hover{background:rgba(244,246,248,.07);translate:0 -5px}""",
     """.gpane:hover{background:rgba(11,14,17,.24);translate:0 -5px}""")
# the sweep sat at z-index -1, which an isolate context made visible. Without
# isolate it would sit behind the section, so it moves in front at low alpha.
swap("""  content:'';position:absolute;top:-40%;bottom:-40%;left:-70%;width:44%;z-index:-1;
  background:rgba(244,246,248,.09);rotate:14deg;""",
"""  content:'';position:absolute;top:-40%;bottom:-40%;left:-70%;width:44%;
  pointer-events:none;background:rgba(244,246,248,.07);rotate:14deg;""")
swap(""".gpane p{font-size:clamp(.94rem,1.02vw,1.04rem);line-height:1.55}""",
     """.gpane>*{position:relative}
.gpane p{font-size:clamp(.94rem,1.02vw,1.04rem);line-height:1.55}""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Reach: ground rhythm, rake texture, colour block, square glass')
