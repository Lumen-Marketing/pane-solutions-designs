# -*- coding: utf-8 -*-
"""Second pass. Lifting the pane was the wrong lever; lifting the ground is right.

Look again at the reference: the panel is DARKER than the bright photograph
around it, and you can still see the waterfall through it. Nothing about it
brightens. It reads as glass because the picture underneath is bright enough to
survive a 40 percent tint. Mine was a 30 percent tint over a ground at .42,
which is a dim picture behind a dark film, and dim times dark is a rectangle.

So the ground goes up to .55 and the pane goes back to a plain tint with no
brightness trick in it. The blur and the saturation do the work.

Bright ground costs legibility for the type that sits loose on it rather than on
a pane, so headings, hero copy, contact copy and the footer get a wide, soft
text shadow. Invisible at a glance, and it is what keeps white type readable
over a photograph.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-3-spec-sheet.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    s = s.replace(a, b)


swap("  filter:saturate(1.4) brightness(.42);",
     "  filter:saturate(1.45) brightness(.55);")

swap("""   Brightness matters as much as sharpness: at .22 this was near black, and a
   pane over near black is a dark rectangle however it is tuned. */""",
"""   Brightness matters as much as sharpness. At .22 this was near black, and a
   pane over near black is a dark rectangle however you tune the pane. A tint
   only reads as glass if what is under it is bright enough to survive being
   tinted. */""")

swap("""  background:rgba(13,26,33,.3);
  backdrop-filter:blur(26px) saturate(210%) brightness(1.22);
  -webkit-backdrop-filter:blur(26px) saturate(210%) brightness(1.22);
  border:1px solid rgba(233,241,244,.26);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.36),
             inset 0 -1px 0 rgba(233,241,244,.1),""",
"""  background:rgba(13,26,33,.44);
  backdrop-filter:blur(26px) saturate(190%);
  -webkit-backdrop-filter:blur(26px) saturate(190%);
  border:1px solid rgba(233,241,244,.28);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.38),
             inset 0 -1px 0 rgba(233,241,244,.1),""")

swap("""  background:rgba(13,26,33,.3);
  backdrop-filter:blur(24px) saturate(210%) brightness(1.22);
  -webkit-backdrop-filter:blur(24px) saturate(210%) brightness(1.22);
  border:1px solid rgba(233,241,244,.26);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.36),0 12px 28px rgba(2,10,14,.4);""",
"""  background:rgba(13,26,33,.44);
  backdrop-filter:blur(24px) saturate(190%);
  -webkit-backdrop-filter:blur(24px) saturate(190%);
  border:1px solid rgba(233,241,244,.28);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.38),0 12px 28px rgba(2,10,14,.4);""")

# type that sits loose on the ground rather than on a pane
swap(""".wrap{max-width:1500px;margin:0 auto;padding-inline:var(--gut)}""",
""".wrap{max-width:1500px;margin:0 auto;padding-inline:var(--gut)}

/* The ground is a real photograph at better than half brightness, which is what
   makes the glass work, and which white type cannot sit on unaided. A wide soft
   shadow is invisible at a glance and holds the contrast. Panes carry their own
   backdrop, so anything inside one opts back out. */
.sec-hd,.pull,.hero-copy,.contact-copy,footer{text-shadow:0 1px 18px rgba(2,10,14,.85)}
.pane,.pane *,.btn,.fact,.slat{text-shadow:none}""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Facade: ground to .55, pane back to a plain tint, loose type shadowed')
