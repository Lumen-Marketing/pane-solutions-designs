# -*- coding: utf-8 -*-
"""Make Facade's panes actually behave like glass.

The card was reading as a plain dark rectangle and the diagnosis is arithmetic,
not taste. The ground sat at brightness .22, which is nearly black, and the pane
put a 50 percent dark fill on top of that. Blurring near-black gives near-black.
There was nothing to see through.

Three numbers move:

  ground     .22 -> .42   there has to be a picture down there worth blurring
  pane fill  .50 -> .30   the fill is a tint, not a lid
  pane       + brightness(1.22) on the backdrop-filter

That last one is the trick that makes this work on a dark page. backdrop-filter
takes brightness as well as blur, so the pane can LIFT the ground it samples.
The result is a panel that is visibly brighter and softer than the sharp, dark
page around it, which is exactly what reads as a piece of glass lying on top of
a photograph. The rim and the lit top edge come up to match.

Deliberately NOT touched: the nav island and the gallery caption pills. Those
float over the job photographs rather than over the fixed ground, and brightening
a backdrop that is already bright blows the white text off them.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-3-spec-sheet.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    s = s.replace(a, b)


# the ground has to be a picture, not a shadow
swap("  filter:saturate(1.25) brightness(.22);",
     "  filter:saturate(1.4) brightness(.42);")

swap("""   here and then running backdrop-filter over it blurs the same pixels twice,
   and two blurs is mud. One blur, and it belongs to the pane. */""",
"""   here and then running backdrop-filter over it blurs the same pixels twice,
   and two blurs is mud. One blur, and it belongs to the pane.
   Brightness matters as much as sharpness: at .22 this was near black, and a
   pane over near black is a dark rectangle however it is tuned. */""")

# the pane: a tint plus a lift, not a lid
swap(""".pane{
  position:relative;padding:var(--tray);border-radius:var(--r);
  background:rgba(13,26,33,.5);
  backdrop-filter:blur(30px) saturate(175%);
  -webkit-backdrop-filter:blur(30px) saturate(175%);
  border:1px solid rgba(233,241,244,.15);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.24),
             0 1px 2px rgba(2,10,14,.4),
             0 16px 34px rgba(2,10,14,.4),
             0 48px 90px rgba(2,10,14,.44);
}""",
""".pane{
  position:relative;padding:var(--tray);border-radius:var(--r);
  background:rgba(13,26,33,.3);
  backdrop-filter:blur(26px) saturate(210%) brightness(1.22);
  -webkit-backdrop-filter:blur(26px) saturate(210%) brightness(1.22);
  border:1px solid rgba(233,241,244,.26);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.36),
             inset 0 -1px 0 rgba(233,241,244,.1),
             0 1px 2px rgba(2,10,14,.4),
             0 16px 34px rgba(2,10,14,.4),
             0 48px 90px rgba(2,10,14,.44);
}""")

# the pills follow the pane, since they sit on the same ground
swap("""  background:rgba(13,26,33,.5);
  backdrop-filter:blur(28px) saturate(170%);
  -webkit-backdrop-filter:blur(28px) saturate(170%);
  border:1px solid rgba(233,241,244,.15);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.24),0 12px 28px rgba(2,10,14,.4);
  transition:background .3s var(--ease),translate .3s var(--ease);""",
"""  background:rgba(13,26,33,.3);
  backdrop-filter:blur(24px) saturate(210%) brightness(1.22);
  -webkit-backdrop-filter:blur(24px) saturate(210%) brightness(1.22);
  border:1px solid rgba(233,241,244,.26);
  box-shadow:inset 0 1px 0 rgba(233,241,244,.36),0 12px 28px rgba(2,10,14,.4);
  transition:background .3s var(--ease),translate .3s var(--ease);""")

# the hero and contact photo halves carry a heavier scrim now that the ground
# beside them is brighter, or the two halves stop reading as one picture plane
swap(""".hero-shot::after{content:'';position:absolute;inset:0;background:rgba(13,26,33,.3)}""",
     """.hero-shot::after{content:'';position:absolute;inset:0;background:rgba(13,26,33,.22)}""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Facade: ground lifted, panes tint and lift instead of covering')
