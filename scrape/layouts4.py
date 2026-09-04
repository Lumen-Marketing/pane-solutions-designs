# -*- coding: utf-8 -*-
"""Parity. Three designs of one homepage have to carry one set of sections.

He is choosing a design, not a content set, so a why us panel that exists on
Reach and nowhere else makes the chooser a comparison of apples and oranges.
All three now run the same order:

  hero, services, process, why us, work, reels, reviews, FAQ, contact, footer

and no two of them lay a section out the same way. What each direction does
with the two new ones:

  process   DAYLIGHT  ruled 2x2 cells, outlined ghost numerals      wireframe 1
            REACH     staggered journey either side of a spine      wireframe 4
            FACADE    numbered rail on a hairline                   wireframe 3

  why us    DAYLIGHT  four columns ruled apart, no cards            wireframe 2
            REACH     nested cards inside the colour panel          wireframe 4
            FACADE    asymmetric 2x2 with a photograph in a cell    wireframe 2

Daylight's why us takes no cards at all, because it sits on plain paper and a
card on a flat ground is a rectangle. Vertical hairlines do the same job.
"""
import io
import os

HERE = os.path.dirname(__file__)


def load(name):
    p = os.path.join(HERE, '..', name)
    return p, io.open(p, encoding='utf-8').read()


def mk(s):
    box = {'s': s}

    def swap(a, b):
        assert a in box['s'], 'NO MATCH -> %s' % a[:90]
        assert box['s'].count(a) == 1, 'NOT UNIQUE -> %s' % a[:90]
        box['s'] = box['s'].replace(a, b)
    return box, swap


# ══════════════════════════════════════════════════════════════════════════
# DAYLIGHT: why us as four ruled columns on the band
# ══════════════════════════════════════════════════════════════════════════
p1, s1 = load('direction-1-pressure.html')
b1, sw1 = mk(s1)

sw1("""/* ── filter row on the job index ──""",
"""/* ── why us: four columns, ruled apart, no cards ──────────────────────────
   The band is flat, and a card on a flat ground is a rectangle whatever is
   done to it. Vertical hairlines separate the four just as well and leave the
   section reading as one run rather than as four objects. */
.why{padding-block:clamp(56px,7.5vw,108px);background:#E6EBEF;
  border-block:1px solid rgba(16,36,54,.1)}
.why-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}
.why-cell{padding-inline:clamp(16px,2.1vw,36px);
  border-left:1px solid rgba(16,36,54,.16)}
.why-cell:first-child{border-left:0;padding-left:0}
.why-cell:last-child{padding-right:0}
.why-cell h3{font-size:clamp(1.16rem,1.8vw,1.58rem);letter-spacing:-.02em;
  max-width:14ch;min-height:3.1em}
.why-cell p{margin-top:13px;font-size:14.6px;color:var(--ink-2)}
@media(max-width:940px){
  .why-grid{grid-template-columns:1fr 1fr;gap:clamp(22px,3vw,34px) 0}
  .why-cell:nth-child(odd){border-left:0;padding-left:0}
  .why-cell h3{min-height:0}
}
@media(max-width:560px){
  .why-grid{grid-template-columns:1fr}
  .why-cell{border-left:0;padding-inline:0}
}

/* ── filter row on the job index ──""")

WHY1 = """
<section id="why" class="why">
  <div class="wrap">
    <div class="sec-hd">
      <h2 class="rv">Why anyone calls us twice</h2>
      <p class="rv" data-d="1">Four things that decide whether glass still looks clean a week later.</p>
    </div>
    <div class="why-grid">
      <div class="why-cell rv">
        <h3>Reach without ladders</h3>
        <p>Purified water through a fed pole gets to second storey panes from the ground. No ladder feet in the planting and no marks down the wall.</p>
      </div>
      <div class="why-cell rv" data-d="1">
        <h3>Nothing left to dry into a spot</h3>
        <p>The water is purified before it touches the glass, so there are no minerals sitting on the pane waiting to show up as the sun takes the water off.</p>
      </div>
      <div class="why-cell rv" data-d="2">
        <h3>Pressure matched to the surface</h3>
        <p>A concrete driveway and a painted block wall do not take the same pressure, so they do not get the same pressure.</p>
      </div>
      <div class="why-cell rv" data-d="3">
        <h3>The price comes before the work</h3>
        <p>We come and look for nothing, and you have the number in your hand before anybody unrolls a hose.</p>
      </div>
    </div>
  </div>
</section>
"""

sw1("""<section id="work" class="work wrap">""", WHY1 + """
<section id="work" class="work wrap">""")

sw1("""      <a href="#how">How a job goes</a>
    </div>""", """      <a href="#how">How a job goes</a>
      <a href="#why">Why us</a>
    </div>""")

io.open(p1, 'w', encoding='utf-8').write(b1['s'])
print('Daylight: why us, four ruled columns')


# ══════════════════════════════════════════════════════════════════════════
# REACH: process as a staggered journey either side of a spine
# ══════════════════════════════════════════════════════════════════════════
p2, s2 = load('direction-2-altitude.html')
b2, sw2 = mk(s2)

sw2("""/* ── why: nested cards inside the colour panel ──""",
"""/* ── process: a staggered journey down a spine ────────────────────────────
   Wireframe four runs its Journey section as an off-grid stack with cards
   hanging either side of a centre line. Nothing floats here for the sake of
   floating: the stagger is what makes four steps read in order rather than as
   a grid you can enter anywhere. */
.how{padding-block:clamp(66px,9vw,130px);border-bottom:1px solid var(--line)}
.jrn{--jgap:clamp(30px,5vw,96px);position:relative;
  display:grid;grid-template-columns:1fr 1fr;column-gap:var(--jgap)}
.jrn::before{content:'';position:absolute;left:50%;top:8px;bottom:8px;width:1px;
  background:var(--line)}
.jstep{position:relative;padding-block:clamp(22px,2.6vw,40px)}
.jstep:nth-child(even){margin-top:clamp(44px,7vw,124px)}
.jstep::after{content:'';position:absolute;top:calc(clamp(22px,2.6vw,40px) + 6px);
  width:10px;height:10px;background:var(--blue)}
.jstep:nth-child(odd)::after{right:calc(var(--jgap) / -2 - 5px)}
.jstep:nth-child(even)::after{left:calc(var(--jgap) / -2 - 5px)}
.jstep h3{font-size:clamp(1.5rem,2.6vw,2.35rem);line-height:1;letter-spacing:.005em;
  max-width:14ch}
.jstep p{margin-top:14px;max-width:44ch;color:var(--mute);font-size:14.8px}
.jstep .free{display:inline-block;margin-top:16px;padding:6px 14px;
  font-size:11.5px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;
  background:var(--blue);color:var(--paper)}
@media(max-width:820px){
  .jrn{grid-template-columns:1fr;column-gap:0;padding-left:26px}
  .jrn::before{left:0}
  .jstep:nth-child(even){margin-top:0}
  .jstep::after{left:-31px;right:auto}
  .jstep:nth-child(odd)::after,.jstep:nth-child(even)::after{left:-31px;right:auto}
}

/* ── why: nested cards inside the colour panel ──""")

HOW2 = """
<section class="how rake" id="how">
  <div class="wrap">
    <div class="sec-hd">
      <h2 class="rv">How a job goes</h2>
      <p class="rv" data-d="1">Four steps, and you have paid nothing by the end of the second one.</p>
    </div>
    <div class="jrn">
      <article class="jstep rv">
        <h3>You tell us what needs cleaning</h3>
        <p>Call or text and describe the property. How many storeys, roughly how much glass, and whether you want the outside only or both sides.</p>
      </article>
      <article class="jstep rv">
        <h3>We come and look</h3>
        <p>We would rather see the glass than guess at it, so the price comes from a real look at the property.</p>
        <span class="free">No charge for this</span>
      </article>
      <article class="jstep rv">
        <h3>We clean</h3>
        <p>Purified water through a fed pole for the panes a ladder should not reach, and pressure matched to the surface on anything we wash.</p>
      </article>
      <article class="jstep rv">
        <h3>We check the work before we leave</h3>
        <p>Glass, tracks, sills and screens, and on a gutter job the run gets checked for sag and separation while we are up there. Anything we find, you hear about.</p>
      </article>
    </div>
  </div>
</section>
"""

sw2("""<section class="why tint" id="why">""", HOW2 + """
<section class="why tint" id="why">""")

sw2("""      <a href="#why">Why us</a>
    </div>""", """      <a href="#how">How a job goes</a>
      <a href="#why">Why us</a>
    </div>""")

io.open(p2, 'w', encoding='utf-8').write(b2['s'])
print('Reach: process, staggered down a spine')


# ══════════════════════════════════════════════════════════════════════════
# FACADE: tighten the photo cell so the card beside it is not half empty
# ══════════════════════════════════════════════════════════════════════════
p3, s3 = load('direction-3-spec-sheet.html')
b3, sw3 = mk(s3)

sw3("""  min-height:clamp(230px,21vw,300px);""",
    """  min-height:clamp(215px,17vw,250px);""")

io.open(p3, 'w', encoding='utf-8').write(b3['s'])
print('Facade: why photo cell tightened')
