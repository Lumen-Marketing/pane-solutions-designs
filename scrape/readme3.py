# -*- coding: utf-8 -*-
"""README catch-up for the single-border pass and the pane gallery."""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'README.md')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:80]
    s = s.replace(a, b)


swap("""**Depth device: light glass in a tray, plus a Z-axis cascade.** Every pane is an
outer tray holding an inner core whose radius is the tray's minus its padding,
so the curves stay concentric. Two photo plates lap the hero pane's lower corner""",
"""**Depth device: one glass slab, plus a Z-axis cascade.** Two photo plates lap
the hero pane's lower corner""")

swap("""at opposing rotations, mirrored about the pane so the pair reads as composition
rather than as one thing knocked askew.""",
"""at opposing rotations, mirrored about the pane so the pair reads as composition
rather than as one thing knocked askew.

**One hairline, never two.** Both glass directions used to be a tray holding a
core, each with its own 1px rim, six or seven pixels apart. It got called out on
sight: it reads as a rendering fault, not as machining. The fill and the rim now
live on the pane and the core carries nothing but its padding.""")

swap("""(which makes it an **interactive** layout too), and **magazine masonry** for the
job index, twelve photographs packed at their own heights.

**Depth device: smoked glass in a tray.** Same concentric tray-and-core
construction as Daylight, inverted for a dark ground, in the nav island's exact
material: dark translucent fill, heavy blur, a bright hairline rim, one lit top
edge.""",
"""(which makes it an **interactive** layout too), and a **pane gallery** for the
job index.

**The pane gallery.** Twelve jobs held as twelve upright panes in a row. Point
at one, tab to one or tap one and it opens to roughly three quarters of the
width while the other eleven stay stacked at the edge carrying their labels
turned on their sides. One photograph is always large and all twelve are always
on screen, which a grid of captioned rectangles cannot do. It is a `flex-grow`
transition, nothing heavier. Below 900px a 36px slat is not a touch target, so
it becomes a scroll-snap strip with the next pane peeking.

**Depth device: one smoked glass slab.** The nav island's exact material: dark
translucent fill, heavy blur, one bright hairline rim, one lit top edge.""")

swap("""photographic ground**: one real photograph, blurred to 46px, saturated up and
pushed to half brightness, sitting behind everything.""",
"""photographic ground**: one real photograph, blurred to 22px, saturated up and
pushed to just under half brightness, sitting behind everything.""")

swap("""- The first ground was too dark and too heavily blurred, and collapsed to a flat
  brown, which is the same problem again with extra steps. Pick a frame with
  sky in it and keep brightness around .5.""",
"""- The first ground was too dark and too heavily blurred, and collapsed to a flat
  brown, which is the same problem again with extra steps. Pick a frame with
  sky in it and keep brightness around .5.
- Blur is a budget, not a dial to max out. At 46px the photograph stopped being
  a photograph and the page read as a brown wash. 22px keeps it recognisable,
  which is the whole point of putting it there.""")

swap("""| depth device | tray and core, plus a Z-axis photo cascade | tray and core inverted, over a fixed blurred ground | three planes, foreground occlusion |""",
"""| depth device | one glass slab, plus a Z-axis photo cascade | one smoked slab over a fixed blurred ground | three planes, foreground occlusion |""")

swap("""| work | asymmetric bento, ten tiles | magazine masonry, twelve tiles | drag-to-pan filmstrip |""",
"""| work | asymmetric bento, ten tiles | pane gallery, twelve slats that open | drag-to-pan filmstrip |""")

io.open(p, 'w', encoding='utf-8').write(s)
print('README updated')
