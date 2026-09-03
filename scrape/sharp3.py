# -*- coding: utf-8 -*-
"""Facade: a sharp ground, and splits that alternate at a matched size.

1. THE GROUND STOPS BEING BLURRED. On a phone lock screen the wallpaper behind
   the glass is sharp; the tile is what frosts it. Pre-blurring the photograph
   AND then running backdrop-filter over it blurs the same pixels twice, which
   is why it came out as mud. The photograph is now sharp and dark, and every
   pane does its own frosting. That is also the honest version of the effect.

2. THE SPLITS ALTERNATE. Hero, services and contact were three split-screens
   with the photograph on the left every time, which reads as one long left
   column. Now: hero left, services right, contact left.

3. THE THREE PHOTO HALVES ARE THE SAME SIZE. Each is exactly half the width and
   a full viewport tall, so the alternation reads as symmetry rather than as
   three unrelated sections.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-3-spec-sheet.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    s = s.replace(a, b)


# 1. the ground, sharp -----------------------------------------------------
swap("""/* THE GROUND. A real photograph, blurred hard and pushed dark, fixed behind
   everything. This is what makes the glass on this page read as glass: a pane
   over a flat colour returns that same flat colour no matter how much you blur
   it. Kept at 22px: past about 40 the photograph stops being a photograph and
   turns into a wash, and the glass has nothing recognisable left to refract.
   Scaled past the edges so the blur has no bleed at the borders. */
body::before{
  content:'';position:fixed;inset:-10%;z-index:-2;pointer-events:none;
  background:url("assets/photos/arch-reflect.webp") center/cover no-repeat;
  filter:blur(22px) saturate(1.5) brightness(.46);
}""",
"""/* THE GROUND. A real photograph, SHARP, pushed dark, fixed behind everything.
   This is what makes the glass on this page read as glass: a pane over a flat
   colour returns that same flat colour no matter how much you blur it.
   NOT pre-blurred, deliberately. On a phone lock screen the wallpaper behind
   the glass is sharp and the tile is what frosts it. Blurring the photograph
   here and then running backdrop-filter over it blurs the same pixels twice,
   and two blurs is mud. One blur, and it belongs to the pane. */
body::before{
  content:'';position:fixed;inset:0;z-index:-2;pointer-events:none;
  background:url("assets/photos/arch-reflect.webp") center/cover no-repeat;
  filter:saturate(1.3) brightness(.3);
}""")

# 2 + 3. the splits -------------------------------------------------------
swap("""/* ── hero: SPLIT-SCREEN ────────────────────────────────────────────────────
   Photograph one side, a dense stack of panes the other. */
.hero{position:relative;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.02fr);min-height:100svh;align-items:stretch}""",
"""/* ── hero: SPLIT-SCREEN, photograph LEFT ──────────────────────────────────
   Photograph one side, a dense stack of panes the other. Three split screens
   run down this page and they alternate: hero left, services right, contact
   left. Each photo half is exactly half the width and one viewport tall, so
   they match each other going down. */
.hero{position:relative;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);min-height:100svh;align-items:stretch}""")

swap(""".split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);position:relative}
.split-media{position:sticky;top:0;height:100svh;overflow:hidden}""",
""".split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);position:relative}
/* photograph RIGHT here, against the hero's left. order, not source order, so
   a phone still gets the photograph before the words it belongs to. */
.split-media{order:2;position:sticky;top:0;height:100svh;overflow:hidden}
.steps{order:1}""")

swap(""".step{min-height:100svh;display:flex;align-items:center;padding:clamp(40px,6vw,90px) var(--gut) clamp(40px,6vw,90px) clamp(30px,4.4vw,70px)}""",
     """.step{min-height:100svh;display:flex;align-items:center;padding:clamp(40px,6vw,90px) clamp(30px,4.4vw,70px) clamp(40px,6vw,90px) var(--gut)}""")

swap("""  .split{grid-template-columns:1fr}
  .split-media{position:relative;height:52svh}""",
"""  .split{grid-template-columns:1fr}
  .split-media{order:0;position:relative;height:52svh}
  .steps{order:0}""")

swap(""".contact{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);align-items:stretch;
  border-top:1px solid rgba(233,241,244,.12)}
.contact-shot{position:relative;overflow:hidden;min-height:clamp(320px,46svh,540px)}""",
"""/* photograph LEFT again, closing the alternation, and the same size as the
   hero's so the page is symmetrical top to bottom. */
.contact{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);align-items:stretch;
  min-height:100svh;border-top:1px solid rgba(233,241,244,.12)}
.contact-shot{position:relative;overflow:hidden}""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Facade: sharp ground, alternating splits, matched photo halves')
