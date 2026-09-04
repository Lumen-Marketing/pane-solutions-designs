# -*- coding: utf-8 -*-
"""DAYLIGHT hero, taken back to basics, plus the fourth kind of ground.

WHAT WAS WRONG WITH THE OLD HERO

  1. Two tilted photo plates lapped the corner of the glass card. They said
     nothing, they overlapped each other so one was half hidden, and a card
     only earns its place when elevation means something. That is decoration.
  2. The photograph was a close up of stucco and a brown door. For a company
     that cleans glass, the hero showed almost no glass.
  3. The pane picked up a warm pink cast off the stucco behind it, which
     fought the brand blue on the button sitting inside it.
  4. The card sat bottom left with a quarter of the screen of empty wall above
     it, and the message was inside a box rather than on the page.
  5. The 5.0 / 13 / Free strip is a trust micro strip, and those belong under
     the hero, not inside it.

WHAT IT IS NOW: an asymmetric split. Type on textured paper on the left, one
uninterrupted photograph on the right. No card, no plates, no glass. The
headline sits on real paper so it is dead legible at any brightness, and the
picture gets a whole half instead of being chopped into three pieces. The
photograph is the one that shows the work, the glass and the result at once.

THE FOUR GROUNDS he asked for, one of each, all four inside the first four
sections:

  hero        PICTURE + TEXTURE   textured paper beside a photograph
  services    TEXTURE             dot field on paper
  process     SOLID               a flat band, nothing on it
  why us      TEXTURE OVER PICTURE a photograph read THROUGH the page: a heavy
                                  paper wash over the picture, then the dot
                                  field laid over the top of that
  work        SOLID
  reels       COLOUR + TEXTURE    the brand block with a photo laid in
  reviews     TEXTURE
  FAQ         SOLID
  contact     PICTURE

The page stays light the whole way down. The photographic sections wash toward
paper and keep dark type rather than flipping to a dark section mid scroll.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-1-pressure.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    assert s.count(a) == 1, 'NOT UNIQUE (%d) -> %s' % (s.count(a), a[:90])
    s = s.replace(a, b)


# ══════════════════════════════════════════════════════════════════════════
# the hero
# ══════════════════════════════════════════════════════════════════════════
swap("""/* ── hero: FULL-SCREEN archetype ───────────────────────────────────────────
   The photograph is the page, the content is a pane floating on it, and a
   second pane hangs across the bottom edge into the section below. */
.hero{position:relative;min-height:100svh;display:flex;align-items:center;overflow:visible}
.hero-bg{position:absolute;inset:0;overflow:hidden;z-index:0}
.hero-bg img{width:100%;height:100%;object-fit:cover;object-position:64% 44%;
  animation:drift 30s ease-in-out infinite alternate}
@keyframes drift{to{scale:1.08}}
/* one flat wash so the glass has a predictable ground, never a ramp */
.hero-bg::after{content:'';position:absolute;inset:0;background:rgba(226,233,238,.34)}
.hero-in{position:relative;z-index:2;width:100%;padding-top:90px}
.hero-stack{position:relative;display:inline-block;max-width:100%}
/* the cascade. Opposing rotations, mirrored about the pane, so the pair reads
   as composition rather than as one thing knocked askew. */
.chip{position:absolute;overflow:hidden;border-radius:18px;border:5px solid rgba(255,255,255,.85);
  box-shadow:0 2px 5px rgba(20,36,56,.1),0 18px 38px rgba(20,36,56,.22),0 46px 80px rgba(20,36,56,.2);
  transition:translate .5s var(--ease),rotate .5s var(--ease)}
.chip img{width:100%;height:100%;object-fit:cover}
.chip-a{width:clamp(140px,15vw,215px);aspect-ratio:4/5;right:-6%;bottom:-13%;rotate:5deg;z-index:4}
.chip-b{width:clamp(120px,12.5vw,178px);aspect-ratio:1/1;right:16%;bottom:-24%;rotate:-6deg;z-index:3}
.hero-stack:hover .chip-a{translate:0 -8px;rotate:3deg}
.hero-stack:hover .chip-b{translate:0 -5px;rotate:-4deg}
.hero-card{max-width:min(650px,100%)}
.hero-card .core{padding:clamp(28px,3.4vw,50px)}
.hero-card h1{font-size:clamp(2.6rem,5vw,4.5rem);max-width:14ch}
.hero-card h1 i{font-style:normal;color:var(--blue)}
.hero-card p{margin-top:18px;max-width:34ch;font-size:clamp(1rem,1.16vw,1.16rem);color:var(--ink-2)}
.hero-acts{margin-top:clamp(22px,2.6vw,32px);display:flex;gap:12px;flex-wrap:wrap}
/* the strip hung across the bottom edge of the hero */
.strip{
  position:relative;z-index:3;margin:0 var(--gut);margin-top:clamp(-92px,-6vw,-58px);
}
.strip .core{display:grid;grid-template-columns:repeat(3,1fr);
  padding:clamp(18px,2vw,26px) clamp(10px,1.4vw,20px)}
.strip div{padding-inline:clamp(12px,1.6vw,24px);border-right:1px solid rgba(16,24,36,.12)}
.strip div:last-child{border-right:0}
.strip b{display:block;font-family:'Bricolage Grotesque',sans-serif;font-weight:800;
  font-size:clamp(1.5rem,2.5vw,2.2rem);line-height:1;letter-spacing:-.03em}
.strip span{display:block;margin-top:6px;font-size:13.5px;color:var(--ink-2)}""",
"""/* ── hero: ASYMMETRIC SPLIT ───────────────────────────────────────────────
   Type on textured paper, one uninterrupted photograph beside it. No card and
   no plates: the headline does not need a box to sit in when the ground under
   it is already paper, and two tilted photo chips lapping a card was
   decoration rather than composition. The picture gets a whole half. */
.hero{position:relative;min-height:100svh;
  display:grid;grid-template-columns:minmax(0,1.06fr) minmax(0,1fr);align-items:stretch}
.hero-copy{position:relative;display:flex;flex-direction:column;justify-content:center;
  padding:clamp(118px,12vw,152px) clamp(30px,4.6vw,88px) clamp(48px,6vw,92px) var(--gut)}
.hero-copy h1{font-size:clamp(2.7rem,5.3vw,4.9rem);max-width:13ch;letter-spacing:-.035em}
.hero-copy h1 i{font-style:normal;color:var(--blue)}
.hero-copy p{margin-top:20px;max-width:37ch;
  font-size:clamp(1.02rem,1.2vw,1.2rem);color:var(--ink-2)}
.hero-acts{margin-top:clamp(26px,3vw,38px);display:flex;gap:12px;flex-wrap:wrap}
.hero-shot{position:relative;overflow:hidden;background:#DCE3E8}
.hero-shot img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  object-position:54% 44%;animation:drift 34s ease-in-out infinite alternate}
@keyframes drift{to{scale:1.07}}
@media(prefers-reduced-motion:reduce){.hero-shot img{animation:none}}

/* the 5.0 / 13 / Free row. It used to hang inside the hero as a glass card,
   which is a trust strip sitting in the one place a trust strip should not be.
   It is its own solid band now, directly under. */
.strip{background:#E3E8EC;border-block:1px solid rgba(16,36,54,.12)}
.strip-in{display:grid;grid-template-columns:repeat(3,1fr);
  padding-block:clamp(22px,2.6vw,32px)}
.strip div{padding-inline:clamp(14px,2vw,36px);border-left:1px solid rgba(16,36,54,.14)}
.strip div:first-child{border-left:0;padding-left:0}
.strip b{display:block;font-family:'Bricolage Grotesque',sans-serif;font-weight:800;
  font-size:clamp(1.5rem,2.5vw,2.2rem);line-height:1;letter-spacing:-.03em}
.strip span{display:block;margin-top:6px;font-size:13.5px;color:var(--ink-2)}

@media(max-width:900px){
  .hero{grid-template-columns:1fr;min-height:0}
  .hero-copy{padding:clamp(106px,26vw,132px) var(--gut) clamp(34px,7vw,52px)}
  .hero-shot{aspect-ratio:4/3}
  .strip-in{grid-template-columns:1fr;padding-block:clamp(20px,5vw,28px)}
  .strip div{border-left:0;padding-left:0;padding-inline:0;
    border-top:1px solid rgba(16,36,54,.14);padding-top:14px;margin-top:14px}
  .strip div:first-child{border-top:0;padding-top:0;margin-top:0}
}""")

swap("""<header class="hero" id="top">
  <div class="hero-bg"><img src="assets/photos/pole-entry.webp" alt="Pane Solutions cleaning the entry glass of a Phoenix home with a water-fed pole" fetchpriority="high"></div>
  <div class="hero-in wrap">
    <div class="hero-stack">
    <div class="hero-card pane">
      <div class="core">
      <h1>Glass this clean <i>disappears.</i></h1>
      <p>Window cleaning, pressure washing and gutters for Phoenix homes and businesses.</p>
      <div class="hero-acts">
        <a class="btn" href="#contact">Free estimate</a>
        <a class="btn-glass" href="#work">See the work</a>
      </div>
      </div>
    </div>
    <!-- two plates in front of the pane, at opposing angles, so something is
         genuinely occluding something else rather than sitting beside it -->
    <figure class="chip chip-a"><img src="assets/photos/entry-ladder@sm.webp" alt="Cleaning entry glass on a Phoenix home" loading="lazy"></figure>
    <figure class="chip chip-b"><img src="assets/photos/patio-covered@sm.webp" alt="A covered patio run of glass after cleaning" loading="lazy"></figure>
    </div>
  </div>
</header>

<div class="strip pane">
  <div class="core">
    <div><b>5.0</b><span>Rating on Google</span></div>
    <div><b>13</b><span>Reviews, every one five star</span></div>
    <div><b>Free</b><span>No charge to come and look</span></div>
  </div>
</div>""",
"""<header class="hero" id="top">
  <div class="hero-copy dots">
    <h1>Glass this clean <i>disappears.</i></h1>
    <p>Window cleaning, pressure washing and gutters for Phoenix homes and businesses.</p>
    <div class="hero-acts">
      <a class="btn" href="#contact">Free estimate</a>
      <a class="btn-out" href="#work">See the work</a>
    </div>
  </div>
  <figure class="hero-shot">
    <img src="assets/photos/arch-reflect.webp" alt="A Pane Solutions cleaner squeegeeing a tall arched window in Phoenix that reflects the pool and the palms behind him" fetchpriority="high">
  </figure>
</header>

<div class="strip">
  <div class="wrap strip-in">
    <div><b>5.0</b><span>Rating on Google</span></div>
    <div><b>13</b><span>Reviews, every one five star</span></div>
    <div><b>Free</b><span>No charge to come and look</span></div>
  </div>
</div>""")

# The secondary CTA was .btn-glass, which needs a photograph under it to read
# as anything. On paper it is an outline button.
swap(""".btn-glass{""",
"""/* the hero's secondary action sits on paper now, not on a photograph, so it
   is a plain outline button. Glass over paper is a white rectangle. */
.btn-out{
  display:inline-flex;align-items:center;gap:10px;
  padding:14px 26px;border-radius:999px;font-weight:600;font-size:15px;
  border:1px solid rgba(16,36,54,.28);color:var(--ink);background:transparent;
  transition:border-color .3s var(--ease),background .3s var(--ease),translate .3s var(--ease)}
.btn-out:hover{border-color:rgba(16,36,54,.6);background:rgba(16,36,54,.05)}
.btn-out:active{translate:0 1px}
.btn-glass{""")

# ══════════════════════════════════════════════════════════════════════════
# the fourth ground: a photograph read THROUGH the page
# ══════════════════════════════════════════════════════════════════════════
swap("""/* ── why us: four columns, ruled apart, no cards ──""",
"""/* ── ground: TEXTURE OVER PICTURE ─────────────────────────────────────────
   The fourth kind. Not a photograph behind the section and not a flat colour
   with a pattern on it, but both: a heavy paper wash over the picture so the
   photograph reads as something under the page rather than behind it, then
   the same dot field laid over the top of that. Dark type stays legible and
   the page never flips to a dark section mid scroll. */
.pict{position:relative;overflow:hidden}
.pict-bg{position:absolute;inset:0;z-index:0}
.pict-bg img{width:100%;height:100%;object-fit:cover;object-position:50% 42%}
.pict-bg::after{content:'';position:absolute;inset:0;background:rgba(235,239,241,.85)}
.pict::before{content:'';position:absolute;inset:0;z-index:1;pointer-events:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='22' height='22'%3E%3Ccircle cx='2' cy='2' r='1.4' fill='%23102436' fill-opacity='.11'/%3E%3C/svg%3E");
}
.pict>*:not(.pict-bg){position:relative;z-index:2}

/* ── why us: four columns, ruled apart, no cards ──""")

swap(""".why{padding-block:clamp(56px,7.5vw,108px);background:#E6EBEF;
  border-block:1px solid rgba(16,36,54,.1)}""",
""".why{padding-block:clamp(56px,7.5vw,108px);
  border-block:1px solid rgba(16,36,54,.12)}""")

swap("""<section id="why" class="why">
  <div class="wrap">""",
"""<section id="why" class="why pict">
  <div class="pict-bg"><img src="assets/photos/midcentury.webp" alt="" aria-hidden="true" loading="lazy"></div>
  <div class="wrap">""")

# ══════════════════════════════════════════════════════════════════════════
# process becomes the SOLID band the why us section gave up
# ══════════════════════════════════════════════════════════════════════════
swap(""".how{padding-block:clamp(56px,7.5vw,108px)}""",
"""/* SOLID. A flat band and nothing on it. Not every section needs a material,
   and the ruled cells below carry this one on their own. */
.how{padding-block:clamp(56px,7.5vw,108px);background:#E6EBEF;
  border-block:1px solid rgba(16,36,54,.1)}""")

swap(""".how-cell{position:relative;background:var(--paper);""",
     """.how-cell{position:relative;background:#E6EBEF;""")

# services keeps the dot field, so the hero's textured half does not sit
# directly against a second dotted section
swap("""<section id="how" class="how wrap">""",
     """<section id="how" class="how">
  <div class="wrap">""")
swap("""    </article>
  </div>
</section>


<section id="why" class="why pict">""",
"""    </article>
  </div>
  </div>
</section>


<section id="why" class="why pict">""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Daylight: split hero, trust strip moved out, four grounds')
