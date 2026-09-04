# -*- coding: utf-8 -*-
"""Two corrections to the Reach pass.

1. Three of the four panel headings wrap to two lines and one wraps to three,
   so the body copy under them started at three different heights across the
   row. Reserving three lines on every heading puts all four paragraphs on one
   line.

2. Measured off the rendered pixels, the contact section's row labels came out
   around 2.4:1 against the pool photograph behind them. That is under AA for
   body text. The scrim goes up and the loose type on that ground gets the same
   wide soft shadow the other directions use.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-2-altitude.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    assert s.count(a) == 1, 'NOT UNIQUE -> %s' % a[:90]
    s = s.replace(a, b)


swap(""".why-card h3{font-size:clamp(1.32rem,1.9vw,1.72rem);line-height:1.04;
  letter-spacing:-.01em;max-width:13ch}""",
""".why-card h3{font-size:clamp(1.32rem,1.9vw,1.72rem);line-height:1.04;
  letter-spacing:-.01em;max-width:13ch;
  /* three lines reserved on every card, so the four paragraphs under them all
     start on the same line rather than stepping down the row */
  min-height:3.12em}
@media(max-width:600px){.why-card h3{min-height:0}}""")

swap(""".contact-bg::after{content:'';position:absolute;inset:0;background:rgba(8,11,14,.74)}""",
""".contact-bg::after{content:'';position:absolute;inset:0;background:rgba(8,11,14,.84)}
/* loose type on a photographic ground. Measured off the pixels, the row labels
   were coming out around 2.4:1 against the pool behind them. */
.contact-in h2,.contact-in .bignum,.contact-in .crow{text-shadow:0 2px 12px rgba(4,7,10,.9),0 2px 36px rgba(4,7,10,.75)}
.contact-in .crow span{color:#B9C4CD}""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Reach: panel headings aligned, contact ground darkened')
