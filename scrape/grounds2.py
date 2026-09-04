# -*- coding: utf-8 -*-
"""Cut the number of photographic GROUNDS on Daylight and Reach.

The chooser reads better than the pages it presents, and the reason is countable
rather than aesthetic. The chooser has ONE background photograph and everything
else floats on it. Daylight had five full bleed photographs out of eight scroll
moments; Reach had six. Three of each were the services section, which was built
as three full screen photographic bands.

The distinction that was missing: a photograph as a GROUND versus a photograph
as an OBJECT. The chooser is full of imagery, all of it contained inside cards.
Its ground never changes.

So the services sections stop being photographic grounds and become photographs
held IN a section, and both pages land on two grounds, one colour block, and
three plain or textured sections.

  Daylight   image hero, plain services, plain work, colour reels,
             plain reviews, image contact
  Reach      image hero, plain services, plain work, plain reels,
             colour reviews, image contact

A second thing falls out of this. Rows one and two of Daylight's services no
longer put a glass card on flat paper, which was a white rectangle for the same
reason a dark pane on flat near-black was a dark one. Those rows are just type
beside a photograph. Only the third row laps a card over a photograph, where
glass has something to do. Cards where elevation means something, and nowhere
else.
"""
import io
import os

HERE = os.path.dirname(__file__)


def load(name):
    p = os.path.join(HERE, '..', name)
    return p, io.open(p, encoding='utf-8').read()


def save(p, s):
    io.open(p, 'w', encoding='utf-8').write(s)


# ══════════════════════════════════════════════════════════════════════════
# DAYLIGHT
# ══════════════════════════════════════════════════════════════════════════
p1, s1 = load('direction-1-pressure.html')


def sw1(a, b):
    global s1
    assert a in s1, 'D1 NO MATCH -> %s' % a[:90]
    s1 = s1.replace(a, b)


sw1("""/* ── services: ZIG-ZAG archetype ───────────────────────────────────────────
   Three full-bleed photographic bands. The glass panel sits left, then right,
   then centred, so the alternation never runs three deep. */
.band{position:relative;min-height:clamp(460px,64svh,660px);display:flex;align-items:center;
  overflow:hidden;padding-block:clamp(50px,7vw,100px)}
.band-bg{position:absolute;inset:0;z-index:0}
.band-bg img{width:100%;height:100%;object-fit:cover}
.band-bg::after{content:'';position:absolute;inset:0;background:rgba(224,232,238,.3)}
.band-in{position:relative;z-index:2;width:100%;display:flex}
.band-l .band-in{justify-content:flex-start}
.band-r .band-in{justify-content:flex-end}
.band-c .band-in{justify-content:center}
.band-card{max-width:min(575px,100%)}
.band-card .core{padding:clamp(26px,3vw,44px)}
.band-card h2{font-size:clamp(2rem,3.6vw,3.3rem);max-width:12ch}
.band-card p{margin-top:15px;max-width:42ch;color:var(--ink-2)}
.band-card .also{margin-top:16px;font-weight:600;color:var(--ink)}
.band-c .band-card{text-align:center}
.band-c .band-card h2,.band-c .band-card p{margin-inline:auto}""",
"""/* ── services: photographs IN the section, not behind it ──────────────────
   This used to be three full bleed photographic bands, which on its own put
   three photographic grounds in a row and made the whole page read as one long
   wash. The photographs are now plates held on the paper.

   Two calm editorial rows, then one that laps: the third row is a wide plate
   with a glass card pulled up over its lower corner, which is the only place in
   this section where a card earns itself. Rows one and two are type beside a
   photograph, because a pane of glass on flat paper is a white rectangle for
   exactly the same reason a dark pane on flat near-black is a dark one. */
.svc{padding-block:clamp(56px,7.5vw,108px)}
.svc-row{display:grid;grid-template-columns:minmax(0,1.02fr) minmax(0,1fr);
  gap:clamp(24px,3.6vw,62px);align-items:center;padding-block:clamp(26px,3.4vw,50px)}
.svc-row+.svc-row{border-top:1px solid rgba(16,36,54,.13)}
.svc-row.flip .plate{order:2}
.svc-copy h2{font-size:clamp(2rem,3.6vw,3.3rem);max-width:12ch}
.svc-copy p{margin-top:15px;max-width:44ch;color:var(--ink-2)}
.svc-copy .also{margin-top:16px;font-weight:600;color:var(--ink)}
.plate{position:relative;overflow:hidden;border-radius:20px;
  border:1px solid rgba(255,255,255,.75);
  box-shadow:0 1px 2px rgba(20,36,56,.07),
             0 18px 38px rgba(20,36,56,.15),
             0 54px 94px rgba(20,36,56,.16)}
.plate img{width:100%;aspect-ratio:4/3;object-fit:cover;transition:scale 1.3s var(--ease)}
.plate:hover img{scale:1.05}
/* the lap. The card is half on the photograph and half on the paper, which is
   the clearest way to show that the material is actually transparent. */
.svc-lap{padding-top:clamp(26px,3.4vw,50px);border-top:1px solid rgba(16,36,54,.13)}
.svc-lap .plate img{aspect-ratio:2.4/1}
.svc-lap .svc-card{position:relative;z-index:2;max-width:min(560px,88%);
  margin-top:clamp(-132px,-9vw,-76px);margin-left:clamp(16px,4vw,64px)}
.svc-lap .svc-card .core{padding:clamp(24px,2.8vw,40px)}
.svc-lap h2{font-size:clamp(2rem,3.6vw,3.3rem);max-width:12ch}
.svc-lap p{margin-top:15px;max-width:42ch;color:var(--ink-2)}
.svc-lap .also{margin-top:16px;font-weight:600;color:var(--ink)}""")

sw1("""  <div class="band band-l">
    <div class="band-bg"><img src="assets/photos/arch-reflect.webp" alt="An arched Phoenix window reflecting the pool and sky after cleaning" loading="lazy"></div>
    <div class="band-in wrap">
      <div class="band-card pane rv">
        <div class="core">
        <h2>Window cleaning</h2>
        <p>Interior and exterior glass, tracks, sills and screens. Purified water through a fed pole reaches second storey panes with no ladder marks on the wall and no spotting once it dries.</p>
        <p class="also">Homes and businesses. One visit or on a schedule.</p>
        </div>
      </div>""",
"""  <div class="svc-row rv">
    <figure class="plate"><img src="assets/photos/arch-reflect.webp" alt="An arched Phoenix window reflecting the pool and sky after cleaning" loading="lazy"></figure>
    <div class="svc-copy">
      <h2>Window cleaning</h2>
      <p>Interior and exterior glass, tracks, sills and screens. Purified water through a fed pole reaches second storey panes with no ladder marks on the wall and no spotting once it dries.</p>
      <p class="also">Homes and businesses. One visit or on a schedule.</p>""")

sw1("""  <div class="band band-r">
    <div class="band-bg"><img src="assets/photos/lawn-side.webp" alt="The side elevation of a Phoenix home after a pressure wash" loading="lazy"></div>
    <div class="band-in wrap">
      <div class="band-card pane rv">
        <div class="core">
        <h2>Pressure washing</h2>
        <p>Driveways, walkways, patios, pool decks and block walls. Desert dust and hard water staining come off without chewing up the surface underneath.</p>
        <p class="also">Pressure matched to the surface, every time.</p>
        </div>
      </div>""",
"""  <div class="svc-row flip rv">
    <figure class="plate"><img src="assets/photos/lawn-side.webp" alt="The side elevation of a Phoenix home after a pressure wash" loading="lazy"></figure>
    <div class="svc-copy">
      <h2>Pressure washing</h2>
      <p>Driveways, walkways, patios, pool decks and block walls. Desert dust and hard water staining come off without chewing up the surface underneath.</p>
      <p class="also">Pressure matched to the surface, every time.</p>""")

sw1("""  <div class="band band-c">
    <div class="band-bg"><img src="assets/photos/adobe-sky.webp" alt="Roofline and gutters against the sky on an Arizona adobe home" loading="lazy"></div>
    <div class="band-in wrap">
      <div class="band-card pane rv">
        <div class="core">
        <h2>Gutter cleaning</h2>
        <p>Debris cleared, downspouts flushed, and the run checked for sag and separation while we are up there. Monsoon season is a bad time to find out a gutter is packed.</p>
        <p class="also">Checked and reported before we leave.</p>
        </div>
      </div>""",
"""  <div class="svc-lap rv">
    <figure class="plate"><img src="assets/photos/adobe-sky.webp" alt="Roofline and gutters against the sky on an Arizona adobe home" loading="lazy"></figure>
    <div class="svc-card pane">
      <div class="core">
      <h2>Gutter cleaning</h2>
      <p>Debris cleared, downspouts flushed, and the run checked for sag and separation while we are up there. Monsoon season is a bad time to find out a gutter is packed.</p>
      <p class="also">Checked and reported before we leave.</p>""")

save(p1, s1)
print('Daylight services rewritten')


# ══════════════════════════════════════════════════════════════════════════
# REACH
# ══════════════════════════════════════════════════════════════════════════
p2, s2 = load('direction-2-altitude.html')


def sw2(a, b):
    global s2
    assert a in s2, 'D2 NO MATCH -> %s' % a[:90]
    s2 = s2.replace(a, b)


sw2(""".panel{position:sticky;top:0;min-height:100svh;display:flex;align-items:flex-end;
  overflow:hidden;border-top:1px solid var(--line)}
.panel-bg{position:absolute;inset:0;z-index:0}
.panel-bg img{width:100%;height:100%;object-fit:cover}
.panel-bg::after{content:'';position:absolute;inset:0;background:rgba(8,11,14,.56)}
.panel-in{position:relative;z-index:2;padding:clamp(34px,6vw,96px) var(--gut);width:100%;
  display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(20px,4vw,64px);align-items:end}
.panel-in h2{font-size:clamp(2.8rem,7.6vw,7rem)}
.panel-in p{max-width:44ch;font-size:clamp(1rem,1.1vw,1.1rem);color:#D6DEE5}""",
"""/* The panels used to be full screen photographs, which put three photographic
   grounds in a row and made the page read as one long wash. The stack still
   pins and covers, the photograph is now a plate held IN the panel, and the
   ground is the page's own near-black with its rake. A panel has to be opaque
   or the one underneath shows through it. */
.panel{position:sticky;top:0;min-height:100svh;display:flex;align-items:center;
  overflow:hidden;border-top:1px solid var(--line);background:var(--ink)}
.panel:nth-of-type(even){background:var(--ink-2)}
.panel-in{position:relative;z-index:2;padding:clamp(34px,6vw,80px) var(--gut);width:100%;
  display:grid;grid-template-columns:minmax(0,1.06fr) minmax(0,1fr);
  gap:clamp(22px,4vw,64px);align-items:center}
.panel-in h2{font-size:clamp(2.6rem,6.4vw,6rem)}
.panel-in p{max-width:44ch;font-size:clamp(1rem,1.1vw,1.1rem);color:#D6DEE5}
/* square edged, lit along the top, dark at the foot: the same bevel the glass
   on this page uses, so a solid plate and a transparent sheet read as the same
   family of object */
.panel-plate{position:relative;overflow:hidden;
  border:1px solid rgba(244,246,248,.16);
  border-top-color:rgba(244,246,248,.4);
  border-bottom-color:rgba(0,0,0,.6);
  box-shadow:0 30px 70px rgba(4,7,10,.6)}
.panel-plate img{width:100%;aspect-ratio:5/4;object-fit:cover;
  transition:scale 1.4s var(--ease)}
.panel-plate:hover img{scale:1.05}""")

for n, (a, b) in enumerate([
    ('arch-reflect.webp', 'An arched Phoenix window reflecting the pool after cleaning'),
    ('lawn-side.webp', 'The side elevation of a Phoenix home after a pressure wash'),
    ('adobe-sky.webp', 'Roofline and gutters on an Arizona adobe home'),
]):
    sw2("""    <div class="panel-bg"><img src="assets/photos/%s" alt="%s" loading="lazy"></div>
    <div class="panel-in">""" % (a, b),
        """    <div class="panel-in">""")

# put the plate back inside each panel, after its copy column
for h2, src, alt in [
    ('Window<br>cleaning', 'arch-reflect.webp', 'An arched Phoenix window reflecting the pool after cleaning'),
    ('Pressure<br>washing', 'lawn-side.webp', 'The side elevation of a Phoenix home after a pressure wash'),
    ('Gutter<br>cleaning', 'adobe-sky.webp', 'Roofline and gutters on an Arizona adobe home'),
]:
    old = """      <h2>%s</h2>
      <div>""" % h2
    new = """      <div>
        <h2>%s</h2>""" % h2
    assert old in s2
    s2 = s2.replace(old, new, 1)

sw2("""        <p class="also">Homes and businesses. One visit or on a schedule.</p>
      </div>
    </div>""",
"""        <p class="also">Homes and businesses. One visit or on a schedule.</p>
      </div>
      <figure class="panel-plate"><img src="assets/photos/arch-reflect.webp" alt="An arched Phoenix window reflecting the pool after cleaning" loading="lazy"></figure>
    </div>""")
sw2("""        <p class="also">Pressure matched to the surface, every time.</p>
      </div>
    </div>""",
"""        <p class="also">Pressure matched to the surface, every time.</p>
      </div>
      <figure class="panel-plate"><img src="assets/photos/lawn-side.webp" alt="The side elevation of a Phoenix home after a pressure wash" loading="lazy"></figure>
    </div>""")
sw2("""        <p class="also">Checked and reported before we leave.</p>
      </div>
    </div>""",
"""        <p class="also">Checked and reported before we leave.</p>
      </div>
      <figure class="panel-plate"><img src="assets/photos/adobe-sky.webp" alt="Roofline and gutters on an Arizona adobe home" loading="lazy"></figure>
    </div>""")

sw2("""<section class="stack" id="services">""", """<section class="stack rake" id="services">""")

# reels: back to a plain ground. Two photographic grounds a page is the budget,
# and the hero and the contact already spend both.
sw2(""".reels{position:relative;overflow:hidden;padding-block:clamp(70px,9vw,130px);
  border-block:1px solid var(--line)}
.reels-bg{position:absolute;inset:0;z-index:0}
.reels-bg img{width:100%;height:100%;object-fit:cover;object-position:50% 40%}
.reels-bg::after{content:'';position:absolute;inset:0;background:rgba(8,11,14,.6)}
.reels>.wrap{position:relative;z-index:2}""",
""".reels{padding-block:clamp(70px,9vw,130px);background:var(--ink-2);
  border-block:1px solid var(--line)}
/* solid plates here, not glass. There is no photograph behind this section for
   a pane to refract, and glass over a flat colour is a rectangle. */
.pane{background:var(--ink-3);border:1px solid rgba(244,246,248,.14);
  border-top-color:rgba(244,246,248,.34)}""")
sw2("""<section class="reels" id="reels">
  <div class="reels-bg"><img src="assets/photos/glass-corner.webp" alt="" aria-hidden="true" loading="lazy"></div>
  <div class="wrap">""",
"""<section class="reels rake" id="reels">
  <div class="wrap">""")
s2 = s2.replace('<div class="pane sheet rv"', '<div class="pane rv"')

save(p2, s2)
print('Reach panels and reels rewritten')
