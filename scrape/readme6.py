# -*- coding: utf-8 -*-
"""README: the wireframe pass. Four new sections on every direction."""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'README.md')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    assert s.count(a) == 1, 'NOT UNIQUE -> %s' % a[:90]
    s = s.replace(a, b)


swap("""All three share **one section order**: nav, hero, services, work, reels,
reviews, contact, footer. So the client compares the *look*, not the layout.
**Share the order, never the components.** No cell below is reused across two
directions; any new direction fills in a column before it ships.""",
"""All three share **one section order**: nav, hero, services, **process**,
**why us**, work, reels, reviews, **FAQ**, contact, footer. So the client
compares the *look*, not the layout. **Share the order, never the components.**
No cell below is reused across two directions; any new direction fills in a
column before it ships.""")

swap("""| contact | full-screen photo, one big pane | split screen, bookending the hero | photograph with the number over it |
""",
"""| contact | full-screen photo, one big pane | split screen, bookending the hero | photograph with the number over it |
| process | ruled 2x2 cells, outlined ghost numerals | glass tiles threaded on a hairline rail | staggered either side of a centre spine |
| why us | four columns ruled apart, no cards | asymmetric 2x2 with a photo in one cell | solid cards nested inside a colour panel |
| FAQ | sticky title left, accordion right | one heading, questions in two columns | sticky title left, square accordion right |
| footer | four columns on paper | four columns on the fixed photograph | four columns on a raised ink band |

## The wireframe pass

He sent four layout wireframes and asked for those layouts. They are grey box
templates, so what came across is the **structural devices**, not the look:
overlapping and floating cards, tab filters, enormous ghost numerals, sticky
title columns, accordions, nested panels, asymmetric feature grids, and a real
footer with columns. Each one is built in the direction's own material.

Three of the sections the wireframes have and these pages did not are worth
having on their own merits:

| section | why it was missing and why it matters |
|---|---|
| **process** | the page told you what they sell and never what happens after you call. It is also where the free estimate earns its second mention without repeating a CTA. |
| **why us** | four differentiators that were buried inside service copy. Every claim in it is already made elsewhere on the page. |
| **FAQ** | the highest converting section a trade site can have, and all three ended without one. Native `details` and `summary`, so it opens with the JS off, it is already in the tab order, and find-in-page reaches closed answers. |
| **footer** | all four wireframes end on four columns. These pages ended on one line of grey type, throwing away the last screen. |

**Two devices were adopted and one was refused.** The tab filter went on
Daylight's job index, because sorting a client's own photographs invents
nothing. The stat rows in the wireframes did not, because filling `1.3k / 531 /
35` with real numbers is impossible here and filling it with anything else
breaks the content policy at the top of this file.

**The FAQ answers assert nothing new.** Every one is built out of a claim
already on the page: the fed pole, purified water, pressure matched to the
surface, free estimates, homes and businesses, Phoenix, screens and tracks and
sills. Questions whose honest answer is unknown, such as whether the customer
needs to be home, are simply not asked.

**Two bugs the pass produced, both caught in a screenshot.** Facade's why grid
put a 3:4 photograph in flow at five of twelve columns, so the row was sized to
780px and the card beside it carried 500px of empty glass; the image is now
absolutely positioned inside its figure and the type sizes the row. Daylight's
ghost numerals were a solid pale fill and body copy ran across the middle of a
3 and a 4; they are outlined now, which reads the same as a graphic device and
leaves nothing behind the words.
""")

io.open(p, 'w', encoding='utf-8').write(s)
print('README: wireframe pass documented, furniture matrix extended')
