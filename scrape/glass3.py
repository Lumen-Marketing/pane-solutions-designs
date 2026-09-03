"""Make Facade's glass actually behave like glass, and drop the amber side rule.

The nav island reads correctly and the panes below it do not, and the reason is
mechanical rather than aesthetic: the nav floats over a photograph, so
backdrop-filter has real pixels to blur and tint. The fact rows, the step cards
and the review panes sat on a flat dark section, and blurring a flat colour
returns the same flat colour. They were rendering as bordered rectangles with a
yellow bar, which is what got pointed at.

Three changes:

  1. A fixed photographic ground behind the whole page, blurred hard and pushed
     dark. Now every pane on the page has something to refract, everywhere, the
     way the nav does. It is a photograph rather than a gradient, so the
     no-ramps rule still holds.
  2. The amber left rule is gone. Amber survives only on the primary button and
     on the star ratings.
  3. The four stacked fact rows are replaced by a row of glass pills in the
     nav's own material and shape, since that is the component that was working.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-3-spec-sheet.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    s = s.replace(a, b)


# ── 1. the ground ──────────────────────────────────────────────────────────
swap("""body::after{
  content:'';position:fixed;inset:0;z-index:95;pointer-events:none;opacity:.05;""",
"""/* THE GROUND. A real photograph, blurred hard and pushed dark, fixed behind
   everything. This is what makes the glass on this page read as glass: a pane
   over a flat colour returns that same flat colour no matter how much you blur
   it. Scaled past the edges so the blur has no bleed at the borders. */
body::before{
  content:'';position:fixed;inset:-10%;z-index:-2;pointer-events:none;
  background:url("assets/photos/glass-corner.webp") center/cover no-repeat;
  filter:blur(64px) saturate(1.45) brightness(.4);
}
body::after{
  content:'';position:fixed;inset:0;z-index:95;pointer-events:none;opacity:.05;""")

# body needs to not paint over the ground
swap("""body{
  background:var(--bg);color:var(--paper);""",
"""body{
  background:transparent;color:var(--paper);""")
swap("""html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}""",
"""html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;background:var(--bg)}""")

# ── 2. the pane, retuned to the nav's recipe ───────────────────────────────
#   isolation:isolate was cutting the pane off from the backdrop it needs.
swap(""".pane{
  position:relative;isolation:isolate;padding:var(--tray);border-radius:var(--r);
  background:rgba(233,241,244,.055);
  backdrop-filter:blur(26px) saturate(150%);
  -webkit-backdrop-filter:blur(26px) saturate(150%);
  border:1px solid rgba(233,241,244,.1);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.22),
             0 1px 2px rgba(2,10,14,.5),
             0 14px 30px rgba(2,10,14,.45),
             0 44px 84px rgba(2,10,14,.5);
}
.core{
  position:relative;height:100%;border-radius:calc(var(--r) - var(--tray));
  background:rgba(18,38,48,.62);
  border:1px solid rgba(233,241,244,.08);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.16),
             inset 0 -1px 0 rgba(2,10,14,.5);
}
/* the amber edge. A hard 3px rule down the left of anything that matters. */
.edge>.core{border-left:3px solid var(--acc)}
@media(prefers-reduced-transparency:reduce){
  .pane{background:#16292F;backdrop-filter:none;-webkit-backdrop-filter:none}
  .core{background:#12242E}
}""",
"""/* Same recipe as the nav island, which is the one that reads right: a dark
   translucent fill, a heavy blur, a bright hairline rim and one lit top edge.
   No isolation:isolate here. It opens a stacking context that cuts the element
   off from the backdrop it is supposed to be sampling. */
.pane{
  position:relative;padding:var(--tray);border-radius:var(--r);
  background:rgba(13,26,33,.5);
  backdrop-filter:blur(30px) saturate(175%);
  -webkit-backdrop-filter:blur(30px) saturate(175%);
  border:1px solid rgba(233,241,244,.15);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.24),
             0 1px 2px rgba(2,10,14,.4),
             0 16px 34px rgba(2,10,14,.4),
             0 48px 90px rgba(2,10,14,.44);
}
.core{
  position:relative;height:100%;border-radius:calc(var(--r) - var(--tray));
  background:rgba(233,241,244,.05);
  border:1px solid rgba(233,241,244,.09);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.16);
}
@media(prefers-reduced-transparency:reduce){
  .pane{background:#16292F;backdrop-filter:none;-webkit-backdrop-filter:none}
  .core{background:#1A343F}
}""")

# ── 3. the fact rows become pills in the nav's material and shape ──────────
swap("""/* the dense fact stack. This is the page that packs in. */
.facts{display:grid;gap:8px}
.fact{padding:var(--tray)}
.fact .core{display:flex;justify-content:space-between;align-items:baseline;gap:16px;padding:13px 17px}
.fact b{font-family:'Syne',sans-serif;font-weight:700;font-size:15px}
.fact span{color:var(--mute);font-size:13.5px;text-align:right}""",
"""/* Glass pills, same material and same shape as the nav island. Four stacked
   bordered rows with a coloured bar down the side read as a settings screen,
   not as a hero. */
.facts{display:flex;flex-wrap:wrap;gap:9px}
.fact{
  display:inline-flex;align-items:baseline;gap:9px;padding:11px 19px;border-radius:999px;
  background:rgba(13,26,33,.5);
  backdrop-filter:blur(28px) saturate(170%);
  -webkit-backdrop-filter:blur(28px) saturate(170%);
  border:1px solid rgba(233,241,244,.15);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.24),0 12px 28px rgba(2,10,14,.4);
  transition:background .3s var(--ease),translate .3s var(--ease);
}
.fact:hover{background:rgba(233,241,244,.12);translate:0 -2px}
.fact b{font-weight:500;font-size:14px}
.fact span{color:var(--mute);font-size:13px}
@media(prefers-reduced-transparency:reduce){.fact{background:#16292F;backdrop-filter:none}}""")

swap("""    <div class="facts">
      <div class="fact pane edge"><div class="core"><b>Estimates are free</b><span>No charge to come and look</span></div></div>
      <div class="fact pane edge"><div class="core"><b>Homes and businesses</b><span>One visit or on a schedule</span></div></div>
      <div class="fact pane edge"><div class="core"><b>Water-fed pole reach</b><span>Second storey with no ladder marks</span></div></div>
      <div class="fact pane edge"><div class="core"><b>Phoenix, Arizona</b><span>Established 2023</span></div></div>
    </div>""",
"""    <div class="facts">
      <span class="fact"><b>Free estimates</b></span>
      <span class="fact"><b>Homes and businesses</b></span>
      <span class="fact"><b>Water-fed pole reach</b></span>
      <span class="fact"><b>Phoenix, Arizona</b><span>since 2023</span></span>
    </div>""")

# ── the amber edge comes off everything ────────────────────────────────────
s = s.replace('class="seam pane edge"', 'class="seam pane"')
s = s.replace('class="step-card pane edge"', 'class="step-card pane"')
s = s.replace('class="rev pane edge rv"', 'class="rev pane rv"')

# ── the right half of the split has to let the ground through ─────────────
swap(""".hero-copy{display:flex;flex-direction:column;justify-content:center;gap:clamp(16px,2vw,26px);""",
     """/* transparent on purpose: the fixed ground shows through here, which is what
   the panes on this side are refracting */
.hero-copy{display:flex;flex-direction:column;justify-content:center;gap:clamp(16px,2vw,26px);""")

# reels ground was a near-opaque veil over its own photo; lighten it so the
# plates have contrast to work with
swap(""".reels-bg::after{content:'';position:absolute;inset:0;background:rgba(13,26,33,.84)}""",
     """.reels-bg::after{content:'';position:absolute;inset:0;background:rgba(13,26,33,.66)}""")

# ── the masonry captions match the pane material ──────────────────────────
swap("""  background:rgba(13,26,33,.62);
  backdrop-filter:blur(18px) saturate(150%);-webkit-backdrop-filter:blur(18px) saturate(150%);
  border:1px solid rgba(233,241,244,.16);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.2);""",
"""  background:rgba(13,26,33,.5);
  backdrop-filter:blur(24px) saturate(170%);-webkit-backdrop-filter:blur(24px) saturate(170%);
  border:1px solid rgba(233,241,244,.18);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.26);""")

# ── the seam pane loses its edge, so give it the amber back as a number ────
swap(""".seam b{display:block;font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(1.5rem,2.3vw,2rem);line-height:1}""",
     """.seam b{display:block;font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(1.5rem,2.3vw,2rem);line-height:1;color:var(--acc)}""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Facade: ground added, amber edge removed, fact rows became pills')
