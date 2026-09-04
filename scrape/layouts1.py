# -*- coding: utf-8 -*-
"""DAYLIGHT: four structural devices lifted from the wireframes he sent.

  1. NUMBERED PROCESS CELLS. Wireframe one runs its FEATURES section as two
     boxes carrying enormous ghost numerals. Here it becomes the section the
     page did not have at all: what actually happens when you book. Asymmetric,
     wide-narrow then narrow-wide, ruled apart by a 1px grid gap rather than by
     four floating cards, because the ground under it is plain.

  2. A FILTER ROW ON THE JOB INDEX. Wireframe one's EXPLORE tabs and wireframe
     four's department tabs are the same device. The bento holds its shape on
     ALL and falls to an even dense grid once a filter is on, because a bento
     with holes punched in it is not a bento.

  3. AN FAQ ACCORDION. Sticky title left, questions right, straight off
     wireframe two. Native details and summary, so it works with no JS and
     answers keyboard and screen readers for free.

  4. A REAL FOOTER. Every one of the four wireframes ends on a four column
     footer. This page ended on one grey line of type.

Every answer in the FAQ is built from a claim already made elsewhere on the
page. Nothing new is asserted about the business.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-1-pressure.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b, once=True):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    if once:
        assert s.count(a) == 1, 'NOT UNIQUE (%d) -> %s' % (s.count(a), a[:90])
    s = s.replace(a, b)


# ── CSS ───────────────────────────────────────────────────────────────────
CSS = """
/* ── how a job goes: ruled cells, ghost numerals ──────────────────────────
   The ground here is plain paper, so there are no cards. Cards on a flat
   ground are rectangles. A 1px grid gap over a line colour rules the cells
   apart instead, which is the same move a printed table makes. */
.how{padding-block:clamp(56px,7.5vw,108px)}
.how-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:1px;
  background:rgba(16,36,54,.14);border:1px solid rgba(16,36,54,.14);
  border-radius:calc(var(--r) - 6px);overflow:hidden}
.how-cell{position:relative;background:var(--paper);
  padding:clamp(26px,3.1vw,50px);overflow:hidden}
.how-cell:nth-child(1),.how-cell:nth-child(4){grid-column:span 3}
.how-cell:nth-child(2),.how-cell:nth-child(3){grid-column:span 2}
.how-cell .num{position:absolute;right:clamp(6px,1vw,20px);top:-.2em;
  font-family:'Bricolage Grotesque',sans-serif;font-weight:800;line-height:1;
  font-size:clamp(6.5rem,12vw,12rem);color:rgba(27,84,200,.11);
  pointer-events:none;user-select:none}
.how-cell h3{position:relative;font-size:clamp(1.28rem,2.1vw,1.85rem);
  letter-spacing:-.02em;max-width:14ch}
.how-cell p{position:relative;margin-top:12px;max-width:46ch;color:var(--ink-2)}
.how-cell .free{position:relative;display:inline-block;margin-top:16px;
  padding:6px 13px;border-radius:999px;font-size:12.5px;font-weight:600;
  letter-spacing:.04em;text-transform:uppercase;
  background:var(--blue);color:var(--on-blue)}
@media(max-width:860px){
  .how-grid{grid-template-columns:1fr}
  .how-cell:nth-child(n){grid-column:span 1}
}

/* ── filter row on the job index ──────────────────────────────────────────
   The bento's spans are hand placed, so a filtered bento would leave holes.
   On any filter but ALL the grid drops to even cells and packs dense. */
.tabs{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:clamp(18px,2.2vw,30px)}
.tab{font:inherit;font-weight:600;font-size:14px;cursor:pointer;
  padding:10px 21px;border-radius:999px;color:var(--ink);
  border:1px solid rgba(16,36,54,.2);background:transparent;
  transition:background .3s var(--ease),border-color .3s var(--ease),color .3s var(--ease)}
.tab:hover{border-color:rgba(16,36,54,.5)}
.tab.on{background:var(--blue);border-color:var(--blue);color:var(--on-blue)}
.gal{grid-auto-flow:dense}
.gal.filt .tile{grid-column:span 3;grid-row:span 2}
figure.tile[hidden]{display:none}
@media(max-width:820px){.gal.filt .tile{grid-column:span 6}}

/* ── FAQ: sticky title, native accordion ──────────────────────────────────
   details and summary rather than buttons and hidden divs: it opens with no
   JS at all, it is in the tab order already, and find-in-page reaches the
   closed answers. */
.faq{padding-block:clamp(56px,7.5vw,108px)}
.faq-in{display:grid;grid-template-columns:minmax(0,.82fr) minmax(0,1.4fr);
  gap:clamp(26px,4vw,80px);align-items:start}
.faq-hd{position:sticky;top:clamp(96px,9vw,124px)}
.faq-hd h2{font-size:clamp(2.1rem,4.2vw,3.5rem);max-width:11ch}
.faq-hd p{margin-top:15px;max-width:32ch;color:var(--ink-2)}
.faq-hd a{color:var(--blue);font-weight:600}
.q{border-top:1px solid rgba(16,36,54,.17)}
.q:last-child{border-bottom:1px solid rgba(16,36,54,.17)}
.q summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:20px;
  padding:clamp(19px,2.2vw,28px) 0;font-weight:600;letter-spacing:-.01em;
  font-size:clamp(1.02rem,1.55vw,1.3rem)}
.q summary::-webkit-details-marker{display:none}
.q summary:focus-visible{outline:2px solid var(--blue);outline-offset:4px}
.sign{margin-left:auto;position:relative;flex:0 0 28px;height:28px;border-radius:50%;
  border:1px solid rgba(16,36,54,.26);
  transition:background .35s var(--ease),border-color .35s var(--ease),rotate .45s var(--ease)}
.sign::before,.sign::after{content:'';position:absolute;left:50%;top:50%;
  translate:-50% -50%;background:var(--ink);transition:background .35s var(--ease)}
.sign::before{width:12px;height:1.6px}
.sign::after{width:1.6px;height:12px;transition:scale .4s var(--ease)}
.q[open] .sign{background:var(--blue);border-color:var(--blue);rotate:180deg}
.q[open] .sign::before,.q[open] .sign::after{background:var(--on-blue)}
.q[open] .sign::after{scale:1 0}
.q .a{padding-bottom:clamp(19px,2.2vw,30px);max-width:64ch;color:var(--ink-2)}
.q[open] .a{animation:qin .5s var(--ease) both}
@keyframes qin{from{opacity:0;translate:0 -8px}to{opacity:1;translate:0 0}}
@media(prefers-reduced-motion:reduce){.q[open] .a{animation:none}}
@media(max-width:860px){
  .faq-in{grid-template-columns:1fr;gap:26px}
  .faq-hd{position:static}
}

/* ── footer ───────────────────────────────────────────────────────────────
   All four wireframes end on a real footer with columns. This page ended on
   one line of grey type, which throws away the last screen of the page. */
footer{border-top:1px solid rgba(16,36,54,.14);
  padding-block:clamp(44px,5.6vw,80px) 28px}
.f-grid{display:grid;grid-template-columns:minmax(0,1.6fr) repeat(3,minmax(0,1fr));
  gap:clamp(26px,3.2vw,54px)}
.f-brand{display:flex;align-items:center;gap:11px;font-family:'Bricolage Grotesque',sans-serif;
  font-weight:800;font-size:1.15rem;letter-spacing:-.02em}
.f-brand img{height:32px;width:auto;display:block}
.f-say{margin-top:16px;max-width:34ch;color:var(--ink-2);font-size:14.5px}
.f-tel{display:inline-block;margin-top:20px;font-family:'Bricolage Grotesque',sans-serif;
  font-weight:800;letter-spacing:-.03em;font-size:clamp(1.5rem,2.5vw,2.1rem);
  color:var(--blue)}
.f-col h4{font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;
  color:var(--ink-2);margin-bottom:14px}
.f-col a,.f-col span{display:block;padding-block:5px;font-size:14.5px;color:var(--ink)}
.f-col a:hover{color:var(--blue)}
.f-bot{margin-top:clamp(32px,4.2vw,58px);padding-top:22px;
  border-top:1px solid rgba(16,36,54,.12);display:flex;justify-content:space-between;
  gap:18px;flex-wrap:wrap;font-size:13px;color:var(--ink-2)}
@media(max-width:900px){.f-grid{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.f-grid{grid-template-columns:1fr}}
"""

swap("""/* ── motion ────────────────────────────────────────────────────────────── */""",
     CSS + """
/* ── motion ────────────────────────────────────────────────────────────── */""")

# the old flex footer rule is replaced by the block above
swap("""footer{padding-block:30px;display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;
  font-size:13.5px;color:var(--ink-2)}""", """""")

# ── nav gets the new anchor ───────────────────────────────────────────────
swap("""    <a href="#services">Services</a><a href="#work">Work</a><a href="#reels">Reels</a><a href="#reviews">Reviews</a>
  </div>""",
"""    <a href="#services">Services</a><a href="#how">Process</a><a href="#work">Work</a><a href="#reels">Reels</a><a href="#faq">FAQ</a>
  </div>""")

swap("""  <a href="#services">Services</a><a href="#work">Work</a><a href="#reels">Reels</a>
  <a href="#reviews">Reviews</a><a href="#contact">Free estimate</a>""",
"""  <a href="#services">Services</a><a href="#how">Process</a><a href="#work">Work</a><a href="#reels">Reels</a>
  <a href="#reviews">Reviews</a><a href="#faq">FAQ</a><a href="#contact">Free estimate</a>""")

# ── the process section, after services ───────────────────────────────────
HOW = """
<section id="how" class="how wrap">
  <div class="sec-hd">
    <h2 class="rv">How a job goes</h2>
    <p class="rv" data-d="1">Four steps, and you have paid nothing by the end of the second one.</p>
  </div>
  <div class="how-grid rv" data-d="1">
    <article class="how-cell">
      <span class="num" aria-hidden="true">1</span>
      <h3>You tell us what needs cleaning</h3>
      <p>Call or text and describe the property. How many storeys, roughly how much glass, and whether you want the outside only or both sides.</p>
    </article>
    <article class="how-cell">
      <span class="num" aria-hidden="true">2</span>
      <h3>We come and look</h3>
      <p>We would rather see the glass than guess at it, so you get a price from a real look at the property.</p>
      <span class="free">No charge for this</span>
    </article>
    <article class="how-cell">
      <span class="num" aria-hidden="true">3</span>
      <h3>We clean</h3>
      <p>Purified water through a fed pole for the panes a ladder should not reach, and pressure matched to the surface on anything we wash.</p>
    </article>
    <article class="how-cell">
      <span class="num" aria-hidden="true">4</span>
      <h3>We check the work before we leave</h3>
      <p>Glass, tracks, sills and screens, and on a gutter job the run gets checked for sag and separation while we are up there. Anything we find, you hear about.</p>
    </article>
  </div>
</section>
"""

swap("""</section>

<section id="work" class="work wrap">""",
     """</section>
""" + HOW + """
<section id="work" class="work wrap">""")

# ── filter row + categories on the job index ──────────────────────────────
swap("""    <p class="rv" data-d="1">Every photograph on this page is our own work on a real property. No stock, nothing staged.</p>
  </div>
  <div class="gal">""",
"""    <p class="rv" data-d="1">Every photograph on this page is our own work on a real property. No stock, nothing staged.</p>
  </div>
  <div class="tabs rv" data-d="1" role="group" aria-label="Filter the job index">
    <button type="button" class="tab on" data-cat="all">Everything</button>
    <button type="button" class="tab" data-cat="interior">From inside</button>
    <button type="button" class="tab" data-cat="doors">Doors and patios</button>
    <button type="button" class="tab" data-cat="exterior">Exteriors</button>
  </div>
  <div class="gal" id="gal">""")

CATS = [
    ('interior-ladder.webp', 'interior'),
    ('french-doors.webp', 'doors'),
    ('glass-patio.webp', 'doors'),
    ('pole-entry.webp', 'exterior'),
    ('midcentury.webp', 'exterior'),
    ('patio-row.webp', 'doors'),
    ('bay-pool.webp', 'interior'),
    ('entry-ladder.webp', 'exterior'),
    ('patio-covered.webp', 'doors'),
    ('glass-corner.webp', 'exterior'),
]
for name, cat in CATS:
    old = 'rv"><img src="assets/photos/%s"' % name
    new = 'rv" data-cat="%s"><img src="assets/photos/%s"' % (cat, name)
    if old in s:
        s = s.replace(old, new, 1)
    else:
        old2 = 'rv" data-d='
        # tiles that carry a delay attribute
        import re
        pat = re.compile(r'(rv" data-d="\d")(><img src="assets/photos/%s")' % re.escape(name))
        s, n = pat.subn(lambda m: m.group(1) + ' data-cat="%s"' % cat + m.group(2), s, count=1)
        assert n == 1, 'no tile for %s' % name

# ── FAQ, after the reviews ────────────────────────────────────────────────
FAQ = """
<section id="faq" class="faq wrap">
  <div class="faq-in">
    <div class="faq-hd rv">
      <h2>Questions we get asked</h2>
      <p>If yours is not here, call <a href="tel:+15155254127">515.525.4127</a> and ask. It costs nothing to find out.</p>
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

# ── the filter, and only the filter ───────────────────────────────────────
swap("""/* Instagram embeds.""",
"""/* the job index filter. The bento holds its hand placed spans on ALL and
   falls to an even dense grid on anything else, because a bento with holes
   punched through it is just a broken bento. */
(function(){
  var gal=document.getElementById('gal');if(!gal)return;
  var tabs=[].slice.call(document.querySelectorAll('.tab'));
  var tiles=[].slice.call(gal.querySelectorAll('.tile'));
  tabs.forEach(function(t){
    t.addEventListener('click',function(){
      var c=t.dataset.cat;
      tabs.forEach(function(o){o.classList.toggle('on',o===t)});
      gal.classList.toggle('filt',c!=='all');
      tiles.forEach(function(f){
        f.hidden = (c!=='all' && f.dataset.cat!==c);
      });
    });
  });
})();

/* Instagram embeds.""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Daylight: process cells, filtered job index, FAQ accordion, real footer')
