# -*- coding: utf-8 -*-
"""README: the Daylight hero rebuild and the fourth kind of ground."""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'README.md')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    assert s.count(a) == 1, 'NOT UNIQUE -> %s' % a[:90]
    s = s.replace(a, b)


swap("""| hero | full-screen photo, glass card, two lapping plates |""",
     """| hero | asymmetric split, type on textured paper, one photograph |""")

swap("""| footer | four columns on paper | four columns on the fixed photograph | four columns on a raised ink band |
""",
"""| footer | four columns on paper | four columns on the fixed photograph | four columns on a raised ink band |

## The Daylight hero, rebuilt

The glass card with two tilted photo plates lapping its corner was rejected on
sight. Five things were wrong with it, and only the first is a matter of taste:

1. **The plates were decoration.** They said nothing, they overlapped each
   other so one was always half hidden, and a card only earns its place when
   elevation means something.
2. **The photograph showed almost no glass.** It was a close up of stucco and a
   brown door, on the homepage of a company that cleans windows.
3. **The pane picked up a warm pink cast** off the stucco behind it, which
   fought the brand blue on the button sitting inside it.
4. **A quarter of the screen above the card was empty wall.**
5. **A 5.0 / 13 / Free strip is a trust micro strip,** and those belong under
   the hero rather than inside it.

It is an **asymmetric split** now. Type on textured paper on the left, one
uninterrupted photograph on the right, no card and no plates. The headline sits
on real paper, so it stays legible no matter what the picture does, and the
photograph gets a whole half rather than being chopped into three pieces. The
frame is the one that shows the work, the glass and the result at once: a
cleaner squeegeeing an arched window that is reflecting the pool behind him.
The trust strip is its own solid band directly underneath.

The secondary button went from frosted glass to a plain outline in the same
move. **Glass over paper is a white rectangle**, and there is no photograph
behind it any more.
""")

swap("""Flat colour was the complaint, and "add texture everywhere" would have been the
wrong answer. Every section on every page is one of three kinds, and no page
uses one kind more than about twice in a row.

| kind | what it is | when |
|---|---|---|
| **IMAGE** | a real client photograph under one flat veil | when the section has no photographs of its own |
| **PLAIN** | flat colour, nothing on it | when the section's own content is already busy. The bento of ten photographs does not need a patterned ground behind it |
| **COLOUR + TEXTURE** | a block of the accent with a real photograph laid into it, greyscaled and held low | once per page, as the one place the page raises its voice |
""",
"""Flat colour was the complaint, and "add texture everywhere" would have been the
wrong answer. Every section on every page is one of **four** kinds, and no page
uses one kind more than about twice in a row.

| kind | what it is | when |
|---|---|---|
| **PICTURE** | a real client photograph under one flat veil | when the section has no photographs of its own |
| **SOLID** | flat colour, nothing on it | when the section's own content is already busy. The bento of ten photographs does not need a patterned ground behind it |
| **TEXTURE** | flat colour with a fine SVG pattern on it | the default working ground. Gives a plain section tooth without competing with anything |
| **TEXTURE OVER PICTURE** | a heavy paper wash **over** a photograph, then the pattern laid over the top of that | once or twice a page. The photograph reads as something under the page rather than behind it |
| **COLOUR + TEXTURE** | a block of the accent with a real photograph laid into it, greyscaled and held low | once per page, as the one place the page raises its voice |

Daylight runs all four inside its first four sections: the hero is textured
paper beside a photograph, the services are textured, the process is solid, and
the why us section is the picture read through the page.

**Two things make TEXTURE OVER PICTURE work rather than look like fog.** The
photograph is pulled most of the way to greyscale and lifted before the wash
goes on, because a full colour picture under heavy paper turns to grey mush and
what you want to survive is structure. And the contrast is measured off the
**rendered pixels**, not off the CSS: a ground with a picture in it has no
single background colour, so `shots/contrast.mjs` samples the real pixels
inside every text box and reports the worst patch. Daylight's worst case in
that section is 4.58:1, which clears AA for body text.
""")

io.open(p, 'w', encoding='utf-8').write(s)
print('README: hero rebuild and the fourth ground')
