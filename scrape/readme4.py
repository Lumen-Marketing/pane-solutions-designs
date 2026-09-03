# -*- coding: utf-8 -*-
"""README catch-up: the ground is sharp now, and the splits alternate."""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'README.md')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:80]
    s = s.replace(a, b)


swap("""photographic ground**: one real photograph, blurred to 22px, saturated up and
pushed to just under half brightness, sitting behind everything.""",
"""photographic ground**: one real photograph, **sharp**, saturated up and pushed
to about a fifth brightness, sitting behind everything.""")

swap("""- Blur is a budget, not a dial to max out. At 46px the photograph stopped being
  a photograph and the page read as a brown wash. 22px keeps it recognisable,
  which is the whole point of putting it there.""",
"""- **Do not pre-blur the ground at all.** Look at a phone lock screen: the
  wallpaper behind the glass is sharp, and the tile is what frosts it. Blurring
  the photograph and then running `backdrop-filter` over it blurs the same
  pixels twice, and two blurs is mud. It went 46px, then 22px, then none, and
  none is the one that reads as glass. Darkness, not blur, is what keeps the
  type legible: `brightness(.22)` with no blur at all.""")

swap("""archetypes: **split-screen** for the hero and the contact, **sticky split** for
the services where the left photograph swaps as you scroll the right column
(which makes it an **interactive** layout too), and a **pane gallery** for the
job index.""",
"""archetypes: **split-screen** for the hero and the contact, **sticky split** for
the services where the photograph swaps as you scroll the column beside it
(which makes it an **interactive** layout too), and a **pane gallery** for the
job index.

**The three splits alternate and match.** Hero photograph left, services
photograph right, contact photograph left. Each photo half is exactly half the
width and one viewport tall, so the page reads as symmetrical top to bottom
rather than as one long left-hand column of pictures. The services flip is
`order`, not source order, so a phone still gets the photograph before the words
it belongs to.""")

io.open(p, 'w', encoding='utf-8').write(s)
print('README updated')
