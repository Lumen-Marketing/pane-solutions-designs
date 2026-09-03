"""Add real depth to Daylight, and put a lot more photography on it.

Two complaints to answer: it looks flat, and there are not enough pictures.

Depth, in order of how much it actually contributes:

  1. DOUBLE BEZEL. Every pane becomes an outer tray holding an inner core, with
     the inner radius computed smaller so the curves stay concentric. A single
     flat card cannot read as an object no matter what shadow you put on it.
  2. LAYERED AMBIENT SHADOW, tinted to the page rather than neutral black, in
     three stops from a tight contact shadow to a wide soft one. One shadow is
     what makes a card look pasted on.
  3. Z-AXIS CASCADE. Two photo cards overlap the hero pane's lower corner at
     slight opposing rotations, so something is genuinely in front of something
     else.

Pictures: the job index becomes an asymmetric bento of ten tiles, and every
remaining photograph in the library is used somewhere on the page. All fifteen
are now on it.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-1-pressure.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    s = s.replace(a, b)


# ── the pane becomes a tray plus a core ─────────────────────────────────────
swap("""/* ── the pane ───────────────────────────────────────────────────────────────
   One flat fill, one rim, two inset edges. No gradient anywhere in it. */
.pane{
  position:relative;isolation:isolate;
  background:rgba(255,255,255,.62);
  backdrop-filter:blur(30px) saturate(165%);
  -webkit-backdrop-filter:blur(30px) saturate(165%);
  border:1px solid rgba(255,255,255,.62);
  border-radius:var(--r);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.95),
             inset 0 -1px 0 rgba(255,255,255,.35),
             0 26px 64px rgba(16,24,36,.24);
}
/* a pane sitting on the page rather than on a photograph gets a touch more
   fill, because there is nothing behind it for the blur to work on */
.pane-solid{background:rgba(255,255,255,.86)}
@media(prefers-reduced-transparency:reduce){
  .pane,.pane-solid{background:#FBFCFD;backdrop-filter:none;-webkit-backdrop-filter:none}
}""",
"""/* ── the pane: an outer tray holding an inner core ──────────────────────────
   A single flat card cannot read as an object however much shadow you give it.
   The tray is thin, translucent and blurred; the core sits inside it with its
   own fill and its own lit rim, and its radius is the tray's minus the tray's
   padding so the two curves stay concentric.

   The shadow is three stops, tinted to the page rather than neutral black: a
   tight contact shadow, a mid lift and a wide ambient. One shadow is what makes
   a card look pasted on. */
.pane{
  position:relative;isolation:isolate;
  padding:var(--tray);
  border-radius:var(--r);
  background:rgba(255,255,255,.3);
  backdrop-filter:blur(30px) saturate(170%);
  -webkit-backdrop-filter:blur(30px) saturate(170%);
  border:1px solid rgba(255,255,255,.55);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.9),
             0 1px 2px rgba(20,36,56,.06),
             0 14px 30px rgba(20,36,56,.13),
             0 44px 84px rgba(20,36,56,.16);
}
.core{
  position:relative;height:100%;
  border-radius:calc(var(--r) - var(--tray));
  background:rgba(255,255,255,.72);
  border:1px solid rgba(255,255,255,.8);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.98),
             inset 0 -1px 0 rgba(255,255,255,.4);
}
@media(prefers-reduced-transparency:reduce){
  .pane{background:#E6EBEF;backdrop-filter:none;-webkit-backdrop-filter:none}
  .core{background:#FBFCFD}
}""")

swap("""  --r:20px;""", """  --r:26px;
  --tray:7px;      /* tray padding. The core's radius is --r minus this. */""")

# ── padding moves from the pane onto the core ───────────────────────────────
swap(".hero-card{max-width:min(640px,100%);padding:clamp(28px,3.4vw,50px)}",
     ".hero-card{max-width:min(650px,100%)}\n"
     ".hero-card .core{padding:clamp(28px,3.4vw,50px)}")
swap(".band-card{max-width:min(560px,100%);padding:clamp(26px,3vw,44px)}",
     ".band-card{max-width:min(575px,100%)}\n"
     ".band-card .core{padding:clamp(26px,3vw,44px)}")
swap("""  padding:clamp(18px,2vw,26px) clamp(10px,1.4vw,20px);
}""",
     """}
.strip .core{display:grid;grid-template-columns:repeat(3,1fr);
  padding:clamp(18px,2vw,26px) clamp(10px,1.4vw,20px)}""")
swap(""".rev{padding:clamp(20px,2.2vw,28px);display:flex;flex-direction:column;gap:12px;
  transition:translate .3s var(--ease),box-shadow .3s var(--ease)}
.rev:hover{translate:0 -6px;box-shadow:inset 0 1px 0 rgba(255,255,255,.95),0 34px 70px rgba(16,24,36,.3)}""",
     """.rev{transition:translate .38s var(--ease),box-shadow .38s var(--ease)}
.rev .core{padding:clamp(20px,2.2vw,28px);display:flex;flex-direction:column;gap:12px}
.rev:hover{translate:0 -7px;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.9),
             0 2px 4px rgba(20,36,56,.07),
             0 22px 44px rgba(20,36,56,.16),
             0 60px 110px rgba(20,36,56,.2)}""")
swap(""".contact-card{padding:clamp(28px,3.6vw,54px);display:grid;
  grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(26px,4vw,64px);align-items:end}""",
     """.contact-card .core{padding:clamp(28px,3.6vw,54px);display:grid;
  grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(26px,4vw,64px);align-items:end}""")
swap(".pane-reel{display:flex;padding:clamp(10px,1.1vw,15px)}",
     ".pane-reel .core{display:flex;padding:clamp(9px,1vw,13px)}")

# ── Z-axis cascade: two photo cards lapping the hero pane's lower corner ────
swap("""<div class="hero-in wrap">
    <div class="hero-card pane">""",
     """<div class="hero-in wrap">
    <div class="hero-stack">
    <div class="hero-card pane">""")
swap("""        <a class="btn-glass" href="#work">See the work</a>
      </div>
    </div>
  </div>
</header>""",
     """        <a class="btn-glass" href="#work">See the work</a>
      </div>
      </div>
    </div>
    <!-- two plates in front of the pane, at opposing angles, so something is
         genuinely occluding something else rather than sitting beside it -->
    <figure class="chip chip-a"><img src="assets/photos/entry-ladder@sm.webp" alt="Cleaning entry glass on a Phoenix home" loading="lazy"></figure>
    <figure class="chip chip-b"><img src="assets/photos/patio-covered@sm.webp" alt="A covered patio run of glass after cleaning" loading="lazy"></figure>
    </div>
  </div>
</header>""")

swap(""".hero-in{position:relative;z-index:2;width:100%;padding-top:90px}""",
     """.hero-in{position:relative;z-index:2;width:100%;padding-top:90px}
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
.hero-stack:hover .chip-b{translate:0 -5px;rotate:-4deg}""")

# ── the job index becomes an asymmetric bento, and gets far more of it ──────
swap(""".gal{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(12px,1.5vw,22px)}
figure.tile{position:relative;overflow:hidden;border-radius:var(--r);aspect-ratio:4/3;
  box-shadow:0 18px 44px rgba(16,24,36,.18);transition:translate .35s var(--ease),box-shadow .35s var(--ease)}
figure.tile:hover{translate:0 -6px;box-shadow:0 28px 60px rgba(16,24,36,.26)}""",
     """/* Asymmetric bento. Fixed row height plus row spans, never a per-tile
   aspect-ratio: mixed ratios in one grid resolve to different heights and every
   row comes out ragged. */
.gal{display:grid;grid-template-columns:repeat(6,1fr);
  grid-auto-rows:clamp(88px,10.2vw,150px);gap:clamp(10px,1.3vw,18px)}
figure.tile{position:relative;overflow:hidden;border-radius:var(--r);
  border:1px solid rgba(255,255,255,.5);
  box-shadow:0 1px 2px rgba(20,36,56,.07),
             0 14px 30px rgba(20,36,56,.15),
             0 40px 76px rgba(20,36,56,.16);
  transition:translate .4s var(--ease),box-shadow .4s var(--ease)}
figure.tile:hover{translate:0 -7px;
  box-shadow:0 2px 4px rgba(20,36,56,.08),
             0 24px 46px rgba(20,36,56,.2),
             0 64px 116px rgba(20,36,56,.22)}
.g-a{grid-column:span 3;grid-row:span 3}
.g-b{grid-column:span 3;grid-row:span 2}
.g-c,.g-d,.g-e{grid-column:span 2;grid-row:span 2}
.g-f{grid-column:span 2;grid-row:span 3}
.g-g{grid-column:span 4;grid-row:span 3}
.g-h,.g-i{grid-column:span 3;grid-row:span 2}
.g-j{grid-column:span 6;grid-row:span 2}""")

TILES = [
    ('g-a', 'interior-ladder', 'Tall interior pane'),
    ('g-b', 'french-doors', 'French doors'),
    ('g-c', 'glass-patio', 'Patio slider run'),
    ('g-d', 'pole-entry', 'Entry glass, water-fed pole'),
    ('g-e', 'midcentury', 'Mid-century glazing'),
    ('g-f', 'patio-row', 'Covered patio run'),
    ('g-g', 'bay-pool', 'Bay window, poolside'),
    ('g-h', 'entry-ladder', 'Entry glazing'),
    ('g-i', 'patio-covered', 'Shaded patio glass'),
    ('g-j', 'glass-corner', 'Glazed corner, courtyard'),
]
tiles = '\n    '.join(
    '<figure class="tile %s rv"%s><img src="assets/photos/%s.webp" alt="%s cleaned by Pane '
    'Solutions in Phoenix" loading="lazy"><figcaption>%s</figcaption></figure>'
    % (cls, '' if i % 3 == 0 else ' data-d="%d"' % (i % 3), f, t, t)
    for i, (cls, f, t) in enumerate(TILES))

a = s.index('  <div class="gal">')
b = s.index('</div>', s.index('Covered patio run</figcaption></figure>')) + len('</div>')
s = s[:a] + '  <div class="gal">\n    ' + tiles + '\n  </div>' + s[b:]

# ── panes gain their inner core in the markup ───────────────────────────────
for cls in ('hero-card pane', 'band-card pane', 'contact-card pane'):
    pass  # handled individually below, the closing tags differ

swap('<div class="hero-card pane">\n      <h1>',
     '<div class="hero-card pane">\n      <div class="core">\n      <h1>')

s = s.replace('<div class="band-card pane rv">\n        <h2>',
              '<div class="band-card pane rv">\n        <div class="core">\n        <h2>')
s = s.replace("""schedule.</p>
      </div>""", """schedule.</p>
        </div>
      </div>""")
s = s.replace("""every time.</p>
      </div>""", """every time.</p>
        </div>
      </div>""")
s = s.replace("""before we leave.</p>
      </div>""", """before we leave.</p>
        </div>
      </div>""")

swap("""    <div class="contact-card pane">
      <div>""", """    <div class="contact-card pane">
      <div class="core">
      <div>""")
swap("""      </div>
    </div>
  </div>
</section>

</main>""", """      </div>
      </div>
    </div>
  </div>
</section>

</main>""")

swap("""<div class="strip pane">
  <div><b>5.0</b><span>Rating on Google</span></div>
  <div><b>13</b><span>Reviews, every one five star</span></div>
  <div><b>Free</b><span>No charge to come and look</span></div>
</div>""",
     """<div class="strip pane">
  <div class="core">
    <div><b>5.0</b><span>Rating on Google</span></div>
    <div><b>13</b><span>Reviews, every one five star</span></div>
    <div><b>Free</b><span>No charge to come and look</span></div>
  </div>
</div>""")

s = s.replace('<div class="pane pane-reel rv">\n        <div class="screen"',
              '<div class="pane pane-reel rv">\n        <div class="core">\n        <div class="screen"')
s = s.replace('<div class="pane pane-reel rv" data-d="1">\n        <div class="screen"',
              '<div class="pane pane-reel rv" data-d="1">\n        <div class="core">\n        <div class="screen"')
s = s.replace('<div class="pane pane-reel rv" data-d="2">\n        <div class="screen"',
              '<div class="pane pane-reel rv" data-d="2">\n        <div class="core">\n        <div class="screen"')
s = s.replace("""          </a>
        </div>
      </div>""", """          </a>
        </div>
        </div>
      </div>""")

for who in ('Aminata TC Demaih', 'Marcus Baye', 'Gee Nayou', 'Michael Morford'):
    a = s.index('<span class="who">%s</span>' % who)
    open_i = s.rindex('<article class="rev pane rv', 0, a)
    close_i = s.index('</article>', a)
    inner = s[s.index('>', s.index('>', open_i) + 0) + 1:close_i]
    head_end = s.index('>', open_i) + 1
    s = (s[:head_end] + '<div class="core">' + s[head_end:close_i]
         + '</div>' + s[close_i:])

# ── nav CTA gets a nested trailing icon, not a naked arrow ─────────────────
swap("""  <a class="btn" href="#contact">Free estimate</a>
  <button class="burger\"""",
     """  <a class="btn nav-cta" href="#contact">Free estimate<i></i></a>
  <button class="burger\"""")
swap(""".btn:active{translate:0 1px}""",
     """.btn:active{translate:0 1px;scale:.985}
/* nested trailing icon rather than a naked arrow beside the label */
.nav-cta{display:inline-flex;align-items:center;gap:10px;padding-right:8px}
.nav-cta i{width:28px;height:28px;border-radius:50%;background:rgba(255,255,255,.2);
  display:grid;place-items:center;transition:translate .3s var(--ease),background .3s var(--ease)}
.nav-cta i::after{content:'';width:7px;height:7px;border-top:1.5px solid currentColor;
  border-right:1.5px solid currentColor;rotate:45deg;margin-left:-2px}
.nav-cta:hover i{translate:3px 0;background:rgba(255,255,255,.32)}""")

# ── entry animation resolves out of blur, which suits a page about glass ───
swap(""".rv{opacity:0;translate:0 30px;transition:opacity .85s var(--ease),translate .85s var(--ease)}
.rv.in{opacity:1;translate:0 0}""",
     """.rv{opacity:0;translate:0 34px;filter:blur(10px);
  transition:opacity .9s var(--ease),translate .9s var(--ease),filter .9s var(--ease)}
.rv.in{opacity:1;translate:0 0;filter:blur(0)}""")
swap("""  .rv{opacity:1;translate:0 0;transition:none}""",
     """  .rv{opacity:1;translate:0 0;filter:none;transition:none}""")

# ── responsive: the cascade and the bento have to unwind on a phone ────────
swap("""@media(max-width:860px){
  .nav-links,.nav-tel{display:none}""",
     """@media(max-width:1080px){
  .gal{grid-template-columns:repeat(4,1fr)}
  .g-a,.g-b,.g-g,.g-h,.g-i,.g-j{grid-column:span 4}
  .g-c,.g-d,.g-e,.g-f{grid-column:span 2}
}
@media(max-width:860px){
  .nav-links,.nav-tel{display:none}
  /* overlapping plates become touch-target conflicts on a phone */
  .chip{display:none}
  .gal{grid-template-columns:repeat(2,1fr);grid-auto-rows:clamp(76px,22vw,130px)}
  .g-a,.g-b,.g-g,.g-h,.g-i,.g-j{grid-column:span 2}
  .g-c,.g-d,.g-e,.g-f{grid-column:span 1}""")
swap("""@media(max-width:1080px){
  .gal{grid-template-columns:repeat(2,1fr)}
  .rev-grid{grid-template-columns:repeat(2,1fr)}""",
     """@media(max-width:1080px){
  .rev-grid{grid-template-columns:repeat(2,1fr)}""")
swap("""@media(max-width:560px){
  .gal{grid-template-columns:1fr}
  .rev-grid{grid-template-columns:1fr}""",
     """@media(max-width:560px){
  .rev-grid{grid-template-columns:1fr}""")
swap("""  .contact-card{grid-template-columns:1fr}""",
     """  .contact-card .core{grid-template-columns:1fr}
  .strip .core{grid-template-columns:1fr}""")
swap("""  .strip{grid-template-columns:1fr;gap:2px}
  .strip div{border-right:0;""",
     """  .strip div{border-right:0;""")

io.open(p, 'w', encoding='utf-8').write(s)
print('depth pass applied to Daylight')
