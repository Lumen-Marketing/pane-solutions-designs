# -*- coding: utf-8 -*-
"""FACADE: process, why us, FAQ and a real footer, all in smoked glass.

Same four sections the other two directions gained, laid out with different
devices, because the whole point of three directions is that they share an
order and never share a component.

  1. PROCESS as a NUMBERED RAIL. Four glass tiles in a row threaded by a
     hairline spine, with an amber index on each. Wireframe three runs its
     Advantages row this way. Daylight got a ruled 2x2 with outlined numerals
     instead, so the two do not collide.

  2. WHY US as an ASYMMETRIC 2x2. Wide then narrow, narrow then wide, straight
     out of wireframe two's Features block, with a real photograph occupying
     one of the four cells so the grid is not four boxes of type.

  3. FAQ as a TWO COLUMN ACCORDION. Wireframe two puts the title left and the
     questions right. This is the dense direction, so the heading runs across
     the top the way every other heading on this page does and the questions
     split into two columns underneath.

  4. A REAL FOOTER, four columns, on the same fixed photograph as everything
     else.

Every claim is already made elsewhere on the page. Nothing new is asserted.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-3-spec-sheet.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    assert s.count(a) == 1, 'NOT UNIQUE (%d) -> %s' % (s.count(a), a[:90])
    s = s.replace(a, b)


CSS = """
/* ── process: a numbered rail ─────────────────────────────────────────────
   Four glass tiles threaded by one hairline. The spine sits behind the row at
   the height of the index chips, so the four steps read as one run rather than
   as four cards that happen to be side by side. */
.how{padding-block:clamp(52px,7vw,100px)}
.rail{position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));
  gap:clamp(12px,1.4vw,20px)}
.rail::before{content:'';position:absolute;left:0;right:0;
  top:calc(clamp(22px,2.4vw,34px) + 17px);height:1px;
  background:rgba(233,241,244,.2);z-index:0}
.step-tile{position:relative;z-index:1;display:flex;flex-direction:column}
.step-tile .core{padding:clamp(22px,2.4vw,34px)}
.idx{display:inline-flex;align-items:center;justify-content:center;
  width:34px;height:34px;border-radius:50%;background:var(--acc);color:var(--on-acc);
  font-family:Syne,sans-serif;font-weight:800;font-size:15px;line-height:1}
.step-tile h3{margin-top:18px;font-size:clamp(1.12rem,1.6vw,1.44rem);
  letter-spacing:-.01em;max-width:15ch;min-height:2.3em}
.step-tile p{margin-top:11px;font-size:14.4px;color:var(--mute)}
.step-tile .free{display:inline-block;margin-top:14px;padding:5px 12px;border-radius:999px;
  font-size:11.5px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;
  background:var(--acc);color:var(--on-acc)}
@media(max-width:980px){
  .rail{grid-template-columns:repeat(2,minmax(0,1fr))}
  .rail::before{display:none}
  .step-tile h3{min-height:0}
}
@media(max-width:560px){.rail{grid-template-columns:1fr}}

/* ── why us: asymmetric 2x2, one cell is a photograph ─────────────────────
   Wireframe two's Features block. Wide then narrow, narrow then wide, so the
   grid has a diagonal in it rather than four equal boxes. */
.why{padding-block:clamp(52px,7vw,100px)}
.why-grid{display:grid;grid-template-columns:repeat(12,1fr);
  gap:clamp(12px,1.4vw,20px)}
.why-grid>*{min-width:0}
.why-a{grid-column:span 7}
.why-b{grid-column:span 5}
.why-c{grid-column:span 5}
.why-d{grid-column:span 7}
.why-card .core{padding:clamp(24px,2.6vw,40px)}
.why-card h3{font-size:clamp(1.2rem,1.8vw,1.6rem);letter-spacing:-.01em;max-width:18ch}
.why-card p{margin-top:13px;font-size:14.6px;color:var(--mute);max-width:52ch}
.why-shot{position:relative;overflow:hidden;border-radius:var(--r);
  border:1px solid rgba(233,241,244,.2);
  box-shadow:0 1px 2px rgba(2,10,14,.4),0 18px 40px rgba(2,10,14,.42),0 52px 96px rgba(2,10,14,.4)}
.why-shot img{display:block;width:100%;height:100%;min-height:230px;object-fit:cover}
@media(max-width:900px){
  .why-a,.why-b,.why-c,.why-d{grid-column:span 12}
  .why-shot img{min-height:220px}
}

/* ── FAQ: two columns of accordion ────────────────────────────────────────
   details and summary, not buttons over hidden divs. It opens with the JS off,
   it is already in the tab order, and find-in-page reaches closed answers. */
.faq{padding-block:clamp(52px,7vw,100px)}
.faq-cols{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));
  gap:0 clamp(28px,4vw,72px);align-items:start}
.q{border-top:1px solid rgba(233,241,244,.16)}
.q:last-child{border-bottom:1px solid rgba(233,241,244,.16)}
.q summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:18px;
  padding:clamp(16px,1.8vw,22px) 0;font-family:Syne,sans-serif;font-weight:700;
  letter-spacing:-.01em;font-size:clamp(1rem,1.4vw,1.16rem);line-height:1.25}
.q summary::-webkit-details-marker{display:none}
.q summary:focus-visible{outline:2px solid var(--acc);outline-offset:4px}
.sign{margin-left:auto;position:relative;flex:0 0 26px;height:26px;border-radius:50%;
  border:1px solid rgba(233,241,244,.26);
  transition:background .35s var(--ease),border-color .35s var(--ease),rotate .45s var(--ease)}
.sign::before,.sign::after{content:'';position:absolute;left:50%;top:50%;
  translate:-50% -50%;background:var(--paper);transition:background .35s var(--ease)}
.sign::before{width:11px;height:1.4px}
.sign::after{width:1.4px;height:11px;transition:scale .4s var(--ease)}
.q[open] .sign{background:var(--acc);border-color:var(--acc);rotate:180deg}
.q[open] .sign::before,.q[open] .sign::after{background:var(--on-acc)}
.q[open] .sign::after{scale:1 0}
.q .a{padding-bottom:clamp(16px,1.8vw,24px);max-width:56ch;color:var(--mute);font-size:14.6px}
.q[open] .a{animation:qin .5s var(--ease) both}
@keyframes qin{from{opacity:0;translate:0 -8px}to{opacity:1;translate:0 0}}
@media(prefers-reduced-motion:reduce){.q[open] .a{animation:none}}
@media(max-width:820px){.faq-cols{grid-template-columns:1fr}}

/* ── footer ───────────────────────────────────────────────────────────────
   All four wireframes end on a real footer. This page ended on one line. */
footer{border-top:1px solid rgba(233,241,244,.14);
  padding-block:clamp(42px,5.4vw,76px) 26px}
.f-grid{display:grid;grid-template-columns:minmax(0,1.6fr) repeat(3,minmax(0,1fr));
  gap:clamp(24px,3vw,52px)}
.f-brand{display:flex;align-items:center;gap:10px;font-family:Syne,sans-serif;
  font-weight:800;font-size:1.1rem;letter-spacing:-.02em}
.f-brand img{height:30px;width:auto;display:block}
.f-say{margin-top:15px;max-width:36ch;color:var(--mute);font-size:14.2px}
.f-tel{display:inline-block;margin-top:20px;font-family:Syne,sans-serif;font-weight:800;
  letter-spacing:-.03em;font-size:clamp(1.6rem,2.6vw,2.3rem);color:var(--acc)}
.f-col h4{font-size:11px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mute);margin-bottom:14px}
.f-col a,.f-col span{display:block;padding-block:5px;font-size:14.2px;color:var(--paper)}
.f-col a:hover{color:var(--acc)}
.f-bot{margin-top:clamp(30px,4vw,54px);padding-top:20px;
  border-top:1px solid rgba(233,241,244,.12);display:flex;justify-content:space-between;
  gap:18px;flex-wrap:wrap;font-size:12.5px;color:var(--mute)}
@media(max-width:900px){.f-grid{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.f-grid{grid-template-columns:1fr}}
"""

swap("""/* ── motion ──────────────────────────────────────────────────────────────*/""",
     CSS + """
/* ── motion ──────────────────────────────────────────────────────────────*/""")

swap("""footer{padding-block:26px;display:flex;justify-content:space-between;gap:18px;flex-wrap:wrap;
  font-size:13px;color:var(--mute);border-top:1px solid rgba(233,241,244,.12)}""", """""")

# loose type on the fixed photograph. New sections join the shadow list; the
# panes and their contents opt back out.
swap(""".sec-hd,.pull,.hero-copy,.contact-copy,footer{text-shadow:""",
     """.sec-hd,.pull,.hero-copy,.contact-copy,footer,.f-grid,.f-bot{text-shadow:""")
swap(""".pane,.pane *,.btn,.fact,.slat{text-shadow:none}""",
     """.pane,.pane *,.btn,.fact,.slat,.idx,.why-shot,.q,.q *{text-shadow:none}""")

# ── nav ───────────────────────────────────────────────────────────────────
swap("""    <a href="#services">Services</a><a href="#work">Work</a><a href="#reels">Reels</a><a href="#reviews">Reviews</a>
  </div>""",
"""    <a href="#services">Services</a><a href="#how">Process</a><a href="#why">Why us</a><a href="#work">Work</a><a href="#faq">FAQ</a>
  </div>""")

swap("""  <a href="#services">Services</a><a href="#work">Work</a><a href="#reels">Reels</a>
  <a href="#reviews">Reviews</a><a href="#contact">Free estimate</a>""",
"""  <a href="#services">Services</a><a href="#how">Process</a><a href="#why">Why us</a><a href="#work">Work</a>
  <a href="#reels">Reels</a><a href="#reviews">Reviews</a><a href="#faq">FAQ</a><a href="#contact">Free estimate</a>""")

# ── process + why us, between the services split and the job index ────────
NEW = """
<section id="how" class="how wrap">
  <div class="sec-hd">
    <h2 class="rv">How a job goes</h2>
    <p class="rv" data-d="1">Four steps, and you have paid nothing by the end of the second one.</p>
  </div>
  <div class="rail">
    <article class="step-tile pane rv"><div class="core">
      <span class="idx" aria-hidden="true">1</span>
      <h3>You tell us what needs cleaning</h3>
      <p>Call or text and describe the property. How many storeys, roughly how much glass, and whether you want the outside only or both sides.</p>
    </div></article>
    <article class="step-tile pane rv" data-d="1"><div class="core">
      <span class="idx" aria-hidden="true">2</span>
      <h3>We come and look</h3>
      <p>We would rather see the glass than guess at it, so the price comes from a real look at the property.</p>
      <span class="free">No charge for this</span>
    </div></article>
    <article class="step-tile pane rv" data-d="2"><div class="core">
      <span class="idx" aria-hidden="true">3</span>
      <h3>We clean</h3>
      <p>Purified water through a fed pole for the panes a ladder should not reach, and pressure matched to the surface on anything we wash.</p>
    </div></article>
    <article class="step-tile pane rv" data-d="3"><div class="core">
      <span class="idx" aria-hidden="true">4</span>
      <h3>We check the work before we leave</h3>
      <p>Glass, tracks, sills and screens, and on a gutter job the run gets checked for sag and separation. Anything we find, you hear about.</p>
    </div></article>
  </div>
</section>

<section id="why" class="why wrap">
  <div class="sec-hd">
    <h2 class="rv">Why anyone calls us twice</h2>
    <p class="rv" data-d="1">Four things that decide whether glass still looks clean a week later.</p>
  </div>
  <div class="why-grid">
    <article class="why-card why-a pane rv"><div class="core">
      <h3>Reach without ladders</h3>
      <p>Purified water through a fed pole gets to second storey panes from the ground. No ladder feet in the planting, no marks down the wall, and nobody standing where they should not be standing.</p>
    </div></article>
    <figure class="why-shot why-b rv" data-d="1"><img src="assets/photos/pole-entry.webp" alt="A water-fed pole reaching the entry glass of a Phoenix home" loading="lazy"></figure>
    <article class="why-card why-c pane rv"><div class="core">
      <h3>Nothing left to dry into a spot</h3>
      <p>The water is purified before it touches the glass, so there are no minerals sitting on the pane waiting to show up as the sun takes the water off.</p>
    </div></article>
    <article class="why-card why-d pane rv" data-d="1"><div class="core">
      <h3>Pressure matched to the surface, and a price before the work</h3>
      <p>A concrete driveway and a painted block wall do not take the same pressure, so they do not get the same pressure. And we come and look for nothing, so the number is in your hand before anybody unrolls a hose.</p>
    </div></article>
  </div>
</section>
"""

swap("""<section id="work" class="work wrap">""", NEW + """
<section id="work" class="work wrap">""")

# ── FAQ, after the reviews ────────────────────────────────────────────────
FAQ = """
<section id="faq" class="faq wrap">
  <div class="sec-hd">
    <h2 class="rv">Questions we get asked</h2>
    <p class="rv" data-d="1">If yours is not here, call <a href="tel:+15155254127">515.525.4127</a> and ask. Finding out costs nothing.</p>
  </div>
  <div class="faq-cols">
    <div class="rv">
      <details class="q" open>
        <summary>Do you clean second storey windows?<span class="sign" aria-hidden="true"></span></summary>
        <div class="a"><p>Yes. Purified water through a fed pole reaches upper panes from the ground, so there are no ladder marks down the wall and no spotting once the glass dries.</p></div>
      </details>
      <details class="q">
        <summary>Do you work on businesses as well as homes?<span class="sign" aria-hidden="true"></span></summary>
        <div class="a"><p>Both. One visit, or on a schedule if you would rather not think about it again.</p></div>
      </details>
      <details class="q">
        <summary>What does an estimate cost?<span class="sign" aria-hidden="true"></span></summary>
        <div class="a"><p>Nothing. There is no charge to come and look, and you get the price before any work starts.</p></div>
      </details>
      <details class="q">
        <summary>Where do you work?<span class="sign" aria-hidden="true"></span></summary>
        <div class="a"><p>Phoenix, Arizona. Tell us where you are and you will get a straight yes or no on the phone.</p></div>
      </details>
    </div>
    <div class="rv" data-d="1">
      <details class="q">
        <summary>Will pressure washing damage my driveway or patio?<span class="sign" aria-hidden="true"></span></summary>
        <div class="a"><p>Pressure is matched to the surface every time. Desert dust and hard water staining come off without chewing up what is underneath.</p></div>
      </details>
      <details class="q">
        <summary>Are screens, tracks and sills included?<span class="sign" aria-hidden="true"></span></summary>
        <div class="a"><p>Yes. A window clean is interior and exterior glass plus the tracks, the sills and the screens.</p></div>
      </details>
      <details class="q">
        <summary>Are the photographs on this site your own work?<span class="sign" aria-hidden="true"></span></summary>
        <div class="a"><p>Every one of them. Real Phoenix properties we have cleaned, straight off our own camera. There is no stock photography anywhere on this page.</p></div>
      </details>
      <details class="q">
        <summary>What happens if I am not happy with the glass?<span class="sign" aria-hidden="true"></span></summary>
        <div class="a"><p>Say so before we drive off. We check the work before we leave for exactly this reason, and it is a great deal easier to put right while the kit is still out.</p></div>
      </details>
    </div>
  </div>
</section>
"""

swap("""<section id="contact" class="contact">""", FAQ + """
<section id="contact" class="contact">""")

# ── the real footer ───────────────────────────────────────────────────────
swap("""<footer class="wrap">
  <span>Pane Solutions LLC, Phoenix Arizona. Established 2023.</span>
  <span>Window cleaning, pressure washing, gutter cleaning.</span>
</footer>""",
"""<footer class="wrap">
  <div class="f-grid">
    <div>
      <span class="f-brand"><img src="assets/logo.png" alt="">Pane Solutions</span>
      <p class="f-say">Window cleaning, pressure washing and gutter cleaning for Phoenix homes and businesses. Every photograph on this site is our own work.</p>
      <a class="f-tel" href="tel:+15155254127">515.525.4127</a>
    </div>
    <div class="f-col">
      <h4>Services</h4>
      <a href="#services">Window cleaning</a>
      <a href="#services">Pressure washing</a>
      <a href="#services">Gutter cleaning</a>
      <a href="#how">How a job goes</a>
    </div>
    <div class="f-col">
      <h4>Have a look</h4>
      <a href="#work">Recent jobs</a>
      <a href="#reels">Reels</a>
      <a href="#reviews">Reviews</a>
      <a href="#faq">Questions</a>
    </div>
    <div class="f-col">
      <h4>Get in touch</h4>
      <a href="tel:+15155254127">515.525.4127</a>
      <a href="mailto:answergaye22@gmail.com">answergaye22@gmail.com</a>
      <a href="https://www.instagram.com/pane_solutions_llc/" target="_blank" rel="noopener">@pane_solutions_llc</a>
      <span>Phoenix, Arizona</span>
    </div>
  </div>
  <div class="f-bot">
    <span>Pane Solutions LLC, Phoenix Arizona. Established 2023.</span>
    <span>Rated 5.0 on Google from 13 reviews.</span>
  </div>
</footer>""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Facade: numbered rail, asymmetric why grid, two column FAQ, real footer')
