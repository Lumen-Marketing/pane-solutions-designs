# -*- coding: utf-8 -*-
"""Three fixes on Facade.

  1. ONE border, not two. The double bezel put a hairline on the tray and a
     second hairline on the core, six pixels apart, and once the core went
     transparent there was nothing between them but a second ring. Every card
     is now a single glass slab.
  2. The ground comes back into focus. 46px of blur turned the photograph into
     mud, so the page read as a brown wash. Half the blur, and it reads as a
     real out of focus photograph.
  3. The job grid becomes a pane gallery. Twelve upright panes side by side;
     hover or tap one and it opens while the rest stay stacked at the edge.
     A grid of captioned rectangles is the layout every contractor site uses.
"""
import io
import os
import re

p = os.path.join(os.path.dirname(__file__), '..', 'direction-3-spec-sheet.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    s = s.replace(a, b)


def rswap(pat, b):
    """same, but for the rule headers, whose box rules are counted out to the
    column and so are miserable to type back exactly."""
    global s
    s2, n = re.subn(pat, lambda m: b, s, flags=re.S)
    assert n == 1, 'NO MATCH (%d) -> %s' % (n, pat[:90])
    s = s2


# 1. one border ------------------------------------------------------------
swap('  --tray:6px;', '  --tray:0px;')

swap("""/* Same recipe as the nav island, which is the one that reads right: a dark
   translucent fill, a heavy blur, a bright hairline rim and one lit top edge.
   No isolation:isolate here. It opens a stacking context that cuts the element
   off from the backdrop it is supposed to be sampling. */""",
"""/* ONE slab, ONE hairline. The tray plus core version drew a border on the
   outside and a second one six pixels in, which reads as a mistake rather than
   as machining. The core now carries no rim of its own, only its padding.
   No isolation:isolate here either. It opens a stacking context that cuts the
   element off from the backdrop it is supposed to be sampling. */""")

swap(""".core{
  position:relative;height:100%;border-radius:calc(var(--r) - var(--tray));
  background:transparent;
  border:1px solid rgba(233,241,244,.1);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.18);
}""",
""".core{position:relative;height:100%;border-radius:calc(var(--r) - var(--tray));background:transparent}""")

# 2. the ground, less blurred ---------------------------------------------
swap("""  filter:blur(46px) saturate(1.9) brightness(.52);""",
     """  filter:blur(22px) saturate(1.5) brightness(.46);""")
swap("""   over a flat colour returns that same flat colour no matter how much you blur
   it. Scaled past the edges so the blur has no bleed at the borders. */""",
"""   over a flat colour returns that same flat colour no matter how much you blur
   it. Kept at 22px: past about 40 the photograph stops being a photograph and
   turns into a wash, and the glass has nothing recognisable left to refract.
   Scaled past the edges so the blur has no bleed at the borders. */""")

# 3. masonry -> pane gallery ----------------------------------------------
rswap(r"/\* ─+ work: MAGAZINE masonry.*?\*/",
"""/* ── work: the pane gallery ─────────────────────────────────────────────
   Twelve jobs held as twelve upright panes. Hover, tab or tap one and it opens
   to full width while the others stay stacked at the edge, so one photograph is
   always large and all twelve are always on screen. The shape is the product: a
   run of glass, read one pane at a time. Below 900px those slats are thinner
   than a fingertip, so it becomes a swipeable strip instead. */""")

swap(""".mason{columns:4;column-gap:clamp(10px,1.3vw,18px)}
.mason figure{break-inside:avoid;position:relative;margin-bottom:clamp(10px,1.3vw,18px);
  overflow:hidden;border-radius:14px;border:1px solid rgba(233,241,244,.1);
  box-shadow:0 1px 2px rgba(2,10,14,.5),0 12px 26px rgba(2,10,14,.4),0 34px 64px rgba(2,10,14,.4);
  transition:translate .38s var(--ease),box-shadow .38s var(--ease)}
.mason figure:hover{translate:0 -6px;
  box-shadow:0 2px 4px rgba(2,10,14,.5),0 22px 42px rgba(2,10,14,.5),0 56px 104px rgba(2,10,14,.5)}
.mason img{width:100%;transition:scale 1.1s var(--ease)}
.mason figure:hover img{scale:1.05}
.mason figcaption{
  position:absolute;left:9px;right:9px;bottom:9px;padding:9px 13px;border-radius:9px;
  font-size:12.5px;font-weight:500;color:var(--paper);
  background:rgba(13,26,33,.5);
  backdrop-filter:blur(24px) saturate(170%);-webkit-backdrop-filter:blur(24px) saturate(170%);
  border:1px solid rgba(233,241,244,.18);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.26);
}
@media(prefers-reduced-transparency:reduce){.mason figcaption{background:#0D1A21;backdrop-filter:none}}""",
""".gal{display:flex;gap:6px;height:clamp(380px,58svh,600px)}
.slat{
  position:relative;flex:1 1 0;min-width:0;padding:0;border:0;cursor:pointer;
  background:none;overflow:hidden;border-radius:12px;
  box-shadow:0 1px 2px rgba(2,10,14,.5),0 14px 30px rgba(2,10,14,.42),0 40px 74px rgba(2,10,14,.36);
  transition:flex-grow .8s var(--ease),box-shadow .5s var(--ease);
}
.slat:focus-visible{outline:2px solid var(--acc);outline-offset:3px}
.slat.on{flex-grow:26;box-shadow:0 2px 4px rgba(2,10,14,.5),0 26px 52px rgba(2,10,14,.5),0 70px 120px rgba(2,10,14,.45)}
.slat img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  filter:brightness(.56) saturate(.82);transition:filter .8s var(--ease),scale 1.8s var(--ease)}
.slat.on img{filter:none;scale:1.04}
/* the closed panes carry their label turned on its side, the way a spine does */
.slat .tag{
  position:absolute;left:50%;bottom:16px;translate:-50% 0;rotate:180deg;
  writing-mode:vertical-rl;white-space:nowrap;
  font-size:12px;font-weight:500;letter-spacing:.03em;color:var(--paper);
  text-shadow:0 2px 12px rgba(2,10,14,.9);transition:opacity .3s var(--ease)}
.slat.on .tag{opacity:0}
/* the open pane gets its caption as a pill, same material as the nav island */
.slat .bar{
  position:absolute;left:14px;bottom:14px;padding:10px 17px;border-radius:999px;
  opacity:0;translate:0 10px;white-space:nowrap;font-size:13px;font-weight:500;
  background:rgba(13,26,33,.5);
  backdrop-filter:blur(28px) saturate(170%);-webkit-backdrop-filter:blur(28px) saturate(170%);
  border:1px solid rgba(233,241,244,.18);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.26),0 12px 28px rgba(2,10,14,.45);
  transition:opacity .5s var(--ease) .2s,translate .5s var(--ease) .2s}
.slat.on .bar{opacity:1;translate:0 0}
.gal-hint{margin-top:16px;font-size:13px;color:var(--mute)}
@media(prefers-reduced-transparency:reduce){.slat .bar{background:#16292F;backdrop-filter:none}}
@media(prefers-reduced-motion:reduce){.slat{transition:none}}""")

swap("""@media(max-width:1180px){.mason{columns:3}}
""", """""")
swap("""  .burger{display:block}
  .mason{columns:2}""", """  .burger{display:block}""")
swap("""@media(max-width:560px){
  .mason{columns:1}
  .rev-grid{grid-template-columns:1fr}""",
"""@media(max-width:560px){
  .rev-grid{grid-template-columns:1fr}""")

# the swipeable fallback, added next to the other breakpoints
rswap(r"/\* ─+ responsive ─+\*/",
"""/* ── responsive ─────────────────────────────────────────────────────*/
/* a 36px slat is not a touch target. On a phone the gallery is a strip you
   swipe, with the next pane peeking so it reads as scrollable without a cue. */
@media(max-width:900px){
  .gal{height:auto;gap:10px;overflow-x:auto;overflow-y:hidden;
    scroll-snap-type:x mandatory;padding-bottom:8px;scrollbar-width:none}
  .gal::-webkit-scrollbar{display:none}
  .slat{flex:0 0 78%;aspect-ratio:4/3;scroll-snap-align:center}
  .slat.on{flex-grow:0}
  .slat img,.slat.on img{filter:none;scale:1}
  .slat .tag{display:none}
  .slat .bar{opacity:1;translate:0 0}
}""")


# markup -------------------------------------------------------------------
def slat(src, alt, cap, on=False):
    return ('    <button type="button" class="slat%s" aria-label="%s">'
            '<img src="assets/photos/%s" alt="%s" loading="lazy">'
            '<span class="tag">%s</span><span class="bar">%s</span></button>\n'
            % (' on' if on else '', cap, src, alt, cap, cap))


JOBS = [
    ('interior-ladder.webp', 'Cleaning a tall interior pane from a ladder', 'Tall interior pane'),
    ('patio-row.webp', 'A covered patio run of glass after cleaning', 'Covered patio run'),
    ('glass-corner.webp', 'A glazed corner on a modern Phoenix courtyard home', 'Glazed corner'),
    ('pole-entry.webp', 'Entry glass cleaned with a water fed pole', 'Entry glass, water fed pole'),
    ('french-doors.webp', 'Black framed French doors after cleaning', 'French doors'),
    ('bay-pool.webp', 'A bay window looking out over a pool after cleaning', 'Bay window, poolside'),
    ('midcentury.webp', 'Mid century glazing on a Phoenix home', 'Mid century glazing'),
    ('glass-patio.webp', 'A full run of patio sliding doors after cleaning', 'Patio slider run'),
    ('entry-ladder.webp', 'Entry glazing worked from a ladder', 'Entry glazing'),
    ('patio-covered.webp', 'Shaded patio glass after cleaning', 'Shaded patio glass'),
    ('slider-interior.webp', 'Sliding doors seen from inside after cleaning', 'Slider, from inside'),
    ('modern-gray.webp', 'A modern grey Phoenix home after washing', 'Modern grey exterior'),
]

old_start = s.index('  <div class="mason">')
old_end = s.index('  </div>\n</section>', old_start) + len('  </div>\n')
new = '  <div class="gal rv" data-d="1">\n'
new += ''.join(slat(a, b, c, i == 3) for i, (a, b, c) in enumerate(JOBS))
new += '  </div>\n  <p class="gal-hint rv">Twelve recent jobs. Open any pane.</p>\n'
s = s[:old_start] + new + s[old_end:]

# behaviour ---------------------------------------------------------------
swap("""(function(){
  var els=document.querySelectorAll('.rv');""",
"""/* the pane gallery. Hover opens on a pointer, focus opens on a keyboard, tap
   opens on a phone, and one is always open so the section is never all slats. */
(function(){
  var g=document.querySelector('.gal');if(!g)return;
  var slats=[].slice.call(g.querySelectorAll('.slat'));
  function open(i){slats.forEach(function(el,n){el.classList.toggle('on',n===i)})}
  slats.forEach(function(el,i){
    el.addEventListener('mouseenter',function(){open(i)});
    el.addEventListener('focus',function(){open(i)});
    el.addEventListener('click',function(){open(i)});
  });
})();

(function(){
  var els=document.querySelectorAll('.rv');""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Facade: single border, ground refocused, masonry replaced by the pane gallery')
