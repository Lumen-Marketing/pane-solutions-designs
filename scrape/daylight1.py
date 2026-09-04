# -*- coding: utf-8 -*-
"""DAYLIGHT: a ground rhythm instead of six washed photographs in a row.

Every section on this page was the same move: a client photograph under a heavy
pale veil. It reads as one long wash, and the one section that was not a
photograph was flat paper with nothing in it at all.

Ground rhythm now, one of each kind:

  hero        IMAGE            photograph
  services    IMAGE            three photograph bands
  work        PLAIN            flat paper. The bento is ten photographs; the
                               ground should get out of the way.
  reels       COLOUR + TEXTURE brand blue block with a real photograph laid in
                               as texture, so the reel plates can be real glass
  reviews     PLAIN + TEXTURE  paper with a soft dot field, the light-mode
                               equivalent of tooth
  contact     IMAGE            photograph

The blue block is the one colour moment on the page and the one place the page
raises its voice. It also solves a real problem: a pane over flat paper is a
white rectangle, and the reel plates had nothing to refract.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-1-pressure.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    s = s.replace(a, b)


# ── tokens ────────────────────────────────────────────────────────────────
swap("""  --tray:0px;      /* kept as a variable so the radius maths still reads. */""",
"""  --tray:0px;      /* kept as a variable so the radius maths still reads. */
  --blue-block:#1B4FBE;   /* the one colour block. A shade of the same accent. */""")

# ── the two grounds ───────────────────────────────────────────────────────
swap(""".btn{""",
"""/* ── grounds ──────────────────────────────────────────────────────────────
   DOT. A soft, wide dot field. Light through frosted glass, near enough. An
   SVG rather than a repeating gradient, because the no-ramps rule on this set
   is absolute, and wide enough apart that it never reads as a pattern swatch.

   TINT. A colour block with a real photograph laid into it, held low. This is
   the version of a coloured background that glass can sit on: a pane over a
   flat colour is a rectangle no matter how it is tuned. */
.dots{position:relative}
.dots::before{
  content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='22' height='22'%3E%3Ccircle cx='2' cy='2' r='1.4' fill='%23102436' fill-opacity='.09'/%3E%3C/svg%3E");
}
.dots>*{position:relative;z-index:1}

.tint{position:relative;background:var(--blue-block);overflow:hidden;color:var(--on-blue)}
.tint-bg{position:absolute;inset:0;z-index:0;pointer-events:none;
  opacity:.34;filter:grayscale(1) contrast(1.2);mix-blend-mode:luminosity}
.tint-bg img{width:100%;height:100%;object-fit:cover}
.tint>*:not(.tint-bg){position:relative;z-index:1}

.btn{""")

# ── work: plain. The bento carries it. ────────────────────────────────────
swap("""<section id="work" class="work wrap">""",
     """<section id="work" class="work wrap">""")

# ── reels: the colour block ───────────────────────────────────────────────
swap("""/* ── reels: glass plates over a photographic ground ──────────────────────── */
.reels{position:relative;padding-block:clamp(60px,8vw,116px);overflow:hidden}
.reels-bg{position:absolute;inset:0;z-index:0}
.reels-bg img{width:100%;height:100%;object-fit:cover}
.reels-bg::after{content:'';position:absolute;inset:0;background:rgba(222,231,237,.62)}
.reels>.wrap{position:relative;z-index:2}""",
"""/* ── reels: the one colour block, glass plates over it ───────────────────
   Six pale sections in a row was the problem. This one raises its voice, and
   the photograph laid into the blue is what gives the plates something to
   refract. */
.reels{padding-block:clamp(66px,9vw,124px)}
.reels .sec-hd h2,.reels .sec-hd p,.reels .sec-hd a{color:var(--on-blue)}
.reels .sec-hd a{text-decoration:underline;text-underline-offset:3px}
.reels .sec-hd{border-bottom-color:rgba(242,246,253,.3)}""")

swap("""<section id="reels" class="reels">
  <div class="reels-bg"><img src="assets/photos/slider-interior.webp" alt="" aria-hidden="true" loading="lazy"></div>""",
"""<section id="reels" class="reels tint">
  <div class="tint-bg"><img src="assets/photos/slider-interior.webp" alt="" aria-hidden="true" loading="lazy"></div>""")

# ── reviews: paper with tooth ─────────────────────────────────────────────
swap("""/* ── reviews: panes floating over a band ────────────────────────────────── */
.reviews{position:relative;padding-block:clamp(60px,8vw,116px);overflow:hidden}
.rev-bg{position:absolute;inset:0;z-index:0}
.rev-bg img{width:100%;height:100%;object-fit:cover;object-position:50% 60%}
.rev-bg::after{content:'';position:absolute;inset:0;background:rgba(220,229,236,.66)}
.reviews>.wrap{position:relative;z-index:2}""",
"""/* ── reviews: paper with tooth ───────────────────────────────────────────
   Plain, but not bare. The dot field is the light-mode answer to grain. */
.reviews{position:relative;padding-block:clamp(66px,9vw,124px);
  background:#E6EBEF;border-block:1px solid rgba(16,36,54,.1)}""")

swap("""<section id="reviews" class="reviews">
  <div class="rev-bg"><img src="assets/photos/modern-gray.webp" alt="" aria-hidden="true" loading="lazy"></div>
  <div class="wrap">""",
"""<section id="reviews" class="reviews dots">
  <div class="wrap">""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Daylight: ground rhythm, blue colour block on the reels, dot tooth on the reviews')
