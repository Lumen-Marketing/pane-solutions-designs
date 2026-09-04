# -*- coding: utf-8 -*-
"""REACH: the nested panel, the accordion and a real footer.

Three structural devices out of the wireframes, in this page's own material.

  1. NESTED CARDS INSIDE A COLOUR PANEL. Wireframe four runs its strongest
     section as a dark rounded panel holding four light cards. This page is
     already dark, so it inverts: the panel is the brand block and the cards
     inside it are the page's own near-black, each with the lit top rule that
     is this direction's signature edge. It also fixes a real rhythm problem.
     Services, work and reels were three raked plain sections back to back.

  2. AN FAQ ACCORDION. Sticky title left, questions right, off wireframe two.
     Square, hairline ruled, no round corners anywhere, because nothing else on
     this page has one.

  3. A REAL FOOTER. All four wireframes end on columns. This ended on a line.

Every claim in the panel and every FAQ answer is already made elsewhere on the
page. Nothing new is asserted about the business.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-2-altitude.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    assert s.count(a) == 1, 'NOT UNIQUE (%d) -> %s' % (s.count(a), a[:90])
    s = s.replace(a, b)


CSS = """
/* ── why: nested cards inside the colour panel ────────────────────────────
   Wireframe four's device. A block of the accent, a real photograph laid into
   it at luminosity so the block has variation in it rather than being flat,
   and four solid cards sitting inside the block. The cards are the page's own
   near-black, so the panel reads as a container holding objects rather than as
   four tiles that happen to share a background. */
.why{padding-block:clamp(66px,9vw,130px);border-block:1px solid var(--line)}
.why .sec-hd h2,.why .sec-hd p{color:var(--paper)}
.why .sec-hd p{color:rgba(244,246,248,.72)}
.why-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));
  gap:clamp(12px,1.5vw,20px)}
.why-card{background:var(--ink);padding:clamp(24px,2.4vw,38px);
  border:1px solid rgba(244,246,248,.14);
  border-top-color:rgba(244,246,248,.4);
  box-shadow:inset 0 1px 0 rgba(244,246,248,.2),0 22px 48px rgba(4,7,10,.42);
  transition:translate .5s var(--ease),box-shadow .5s var(--ease)}
.why-card:hover{translate:0 -6px;box-shadow:inset 0 1px 0 rgba(244,246,248,.24),0 34px 66px rgba(4,7,10,.5)}
.why-card h3{font-size:clamp(1.32rem,1.9vw,1.72rem);line-height:1.04;
  letter-spacing:-.01em;max-width:13ch}
.why-card p{margin-top:14px;font-size:14.6px;color:var(--mute)}
@media(max-width:1080px){.why-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:600px){.why-grid{grid-template-columns:1fr}}

/* ── FAQ: sticky title, native accordion, square ──────────────────────────
   details and summary rather than buttons over hidden divs. It opens with the
   JS switched off, it is already in the tab order, and find-in-page reaches
   the closed answers. */
.faq{padding-block:clamp(66px,9vw,130px);background:var(--ink)}
.faq-in{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.42fr);
  gap:clamp(26px,4vw,84px);align-items:start}
.faq-hd{position:sticky;top:clamp(100px,9vw,128px)}
.faq-hd h2{font-size:clamp(2.6rem,5vw,4.4rem);line-height:.94;max-width:10ch}
.faq-hd p{margin-top:16px;max-width:32ch;color:var(--mute)}
.faq-hd a{color:var(--blue)}
.faq-shot{margin-top:clamp(28px,3.2vw,46px);overflow:hidden;
  border:1px solid rgba(244,246,248,.16);
  border-top-color:rgba(244,246,248,.4);
  border-bottom-color:rgba(0,0,0,.6);
  box-shadow:0 26px 60px rgba(4,7,10,.55)}
.faq-shot img{display:block;width:100%;aspect-ratio:5/4;object-fit:cover}
.q{border-top:1px solid var(--line)}
.q:last-child{border-bottom:1px solid var(--line)}
.q summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:22px;
  padding:clamp(20px,2.3vw,30px) 0;font-family:'Big Shoulders Display',sans-serif;
  font-weight:700;letter-spacing:.005em;line-height:1.05;
  font-size:clamp(1.32rem,2.1vw,1.92rem)}
.q summary::-webkit-details-marker{display:none}
.q summary:focus-visible{outline:1px solid var(--blue);outline-offset:6px}
.sign{margin-left:auto;position:relative;flex:0 0 30px;height:30px;
  border:1px solid rgba(244,246,248,.24);
  transition:background .35s var(--ease),border-color .35s var(--ease),rotate .5s var(--ease)}
.sign::before,.sign::after{content:'';position:absolute;left:50%;top:50%;
  translate:-50% -50%;background:var(--paper);transition:background .35s var(--ease)}
.sign::before{width:12px;height:1px}
.sign::after{width:1px;height:12px;transition:scale .4s var(--ease)}
.q[open] .sign{background:var(--blue);border-color:var(--blue);rotate:180deg}
.q[open] .sign::after{scale:1 0}
.q .a{padding-bottom:clamp(20px,2.3vw,32px);max-width:64ch;color:var(--mute)}
.q[open] .a{animation:qin .5s var(--ease) both}
@keyframes qin{from{opacity:0;translate:0 -8px}to{opacity:1;translate:0 0}}
@media(prefers-reduced-motion:reduce){.q[open] .a{animation:none}}
@media(max-width:900px){
  .faq-in{grid-template-columns:1fr;gap:26px}
  .faq-hd{position:static}
  .faq-shot{display:none}
}

/* ── footer ───────────────────────────────────────────────────────────────
   Every one of the four wireframes ends on a real footer. This page threw
   away its last screen on one line of grey type. */
footer{border-top:1px solid var(--line);padding-block:clamp(46px,5.8vw,84px) 30px;
  background:var(--ink-2)}
.f-grid{display:grid;grid-template-columns:minmax(0,1.6fr) repeat(3,minmax(0,1fr));
  gap:clamp(26px,3.2vw,56px)}
.f-brand{display:flex;align-items:center;gap:11px;font-family:'Big Shoulders Display',sans-serif;
  font-weight:800;font-size:1.5rem;letter-spacing:.01em;color:var(--paper)}
.f-brand img{height:32px;width:auto;display:block}
.f-say{margin-top:16px;max-width:36ch;color:var(--mute);font-size:14.4px}
.f-tel{display:inline-block;margin-top:22px;font-family:'Big Shoulders Display',sans-serif;
  font-weight:800;font-size:clamp(1.9rem,3.2vw,2.9rem);line-height:1;color:var(--blue)}
.f-col h4{font-size:11.5px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mute);margin-bottom:15px}
.f-col a,.f-col span{display:block;padding-block:5px;font-size:14.4px;color:var(--paper)}
.f-col a:hover{color:var(--blue)}
.f-bot{margin-top:clamp(34px,4.4vw,62px);padding-top:22px;border-top:1px solid var(--line);
  display:flex;justify-content:space-between;gap:18px;flex-wrap:wrap;
  font-size:12.5px;color:var(--mute)}
@media(max-width:900px){.f-grid{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.f-grid{grid-template-columns:1fr}}
"""

swap("""/* ── motion ──────────────────────────────────────────────────────────────""",
     CSS + """
/* ── motion ──────────────────────────────────────────────────────────────""")

swap("""footer{padding-block:32px;display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;
  font-size:13px;color:var(--mute);border-top:1px solid var(--line)}""", """""")

# ── nav ───────────────────────────────────────────────────────────────────
swap("""    <a href="#services">Services</a><a href="#work">Work</a><a href="#reels">Reels</a><a href="#reviews">Reviews</a>
  </div>""",
"""    <a href="#services">Services</a><a href="#why">Why us</a><a href="#work">Work</a><a href="#reels">Reels</a><a href="#faq">FAQ</a>
  </div>""")

swap("""  <a href="#services">Services</a><a href="#work">Work</a><a href="#reels">Reels</a>
  <a href="#reviews">Reviews</a><a href="#contact">Free estimate</a>""",
"""  <a href="#services">Services</a><a href="#why">Why us</a><a href="#work">Work</a><a href="#reels">Reels</a>
  <a href="#reviews">Reviews</a><a href="#faq">FAQ</a><a href="#contact">Free estimate</a>""")

# ── the colour panel, between the sticky stack and the job index ──────────
WHY = """
<section class="why tint" id="why">
  <div class="tint-bg"><img src="assets/photos/midcentury.webp" alt="" aria-hidden="true" loading="lazy"></div>
  <div class="wrap">
    <div class="sec-hd">
      <h2 class="rv">Why anyone<br>calls us twice</h2>
      <p class="rv" data-d="1">Four things that decide whether glass still looks clean a week later.</p>
    </div>
    <div class="why-grid">
      <article class="why-card rv">
        <h3>Reach without ladders</h3>
        <p>Purified water through a fed pole gets to second storey panes from the ground. No ladder feet in the planting and no marks down the wall.</p>
      </article>
      <article class="why-card rv" data-d="1">
        <h3>Nothing left to dry into a spot</h3>
        <p>The water is purified before it touches the glass, so there are no minerals on the pane waiting to show up as the sun takes the water off.</p>
      </article>
      <article class="why-card rv" data-d="2">
        <h3>Pressure matched to the surface</h3>
        <p>A concrete driveway and a painted block wall do not take the same pressure, so they do not get the same pressure.</p>
      </article>
      <article class="why-card rv" data-d="3">
        <h3>The price comes before the work</h3>
        <p>We come and look for nothing, and you have the number in your hand before anybody unrolls a hose.</p>
      </article>
    </div>
  </div>
</section>
"""

swap("""<section class="work rake" id="work">""", WHY + """
<section class="work rake" id="work">""")

# ── FAQ, after the reviews ────────────────────────────────────────────────
FAQ = """
<section class="faq" id="faq">
  <div class="wrap faq-in">
    <div class="faq-hd rv">
      <h2>Questions we get asked</h2>
      <p>If yours is not here, call <a href="tel:+15155254127">515.525.4127</a> and ask. Finding out costs nothing.</p>
      <figure class="faq-shot"><img src="assets/photos/french-doors.webp" alt="Black framed French doors cleaned by Pane Solutions in Phoenix" loading="lazy"></figure>
    </div>
    <div class="rv" data-d="1">
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
        <summary>Where do you work?<span class="sign" aria-hidden="true"></span></summary>
        <div class="a"><p>Phoenix, Arizona. Tell us where you are and you will get a straight yes or no on the phone.</p></div>
      </details>
    </div>
  </div>
</section>
"""

swap("""<section class="contact" id="contact">""", FAQ + """
<section class="contact" id="contact">""")

# ── the real footer ───────────────────────────────────────────────────────
swap("""<footer class="wrap">
  <span>Pane Solutions LLC, Phoenix Arizona. Established 2023.</span>
  <span>Window cleaning, pressure washing, gutter cleaning.</span>
</footer>""",
"""<footer>
  <div class="wrap">
  <div class="f-grid">
    <div>
      <span class="f-brand"><img src="assets/logo.png" alt="">Pane Solutions</span>
      <p class="f-say">Window cleaning, pressure washing and gutter cleaning across the Phoenix valley. Every photograph on this site is our own work.</p>
      <a class="f-tel" href="tel:+15155254127">515.525.4127</a>
    </div>
    <div class="f-col">
      <h4>Services</h4>
      <a href="#services">Window cleaning</a>
      <a href="#services">Pressure washing</a>
      <a href="#services">Gutter cleaning</a>
      <a href="#why">Why us</a>
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
  </div>
</footer>""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Reach: nested colour panel, FAQ accordion, real footer')
