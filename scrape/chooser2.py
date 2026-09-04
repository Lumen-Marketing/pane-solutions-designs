# -*- coding: utf-8 -*-
"""The chooser now has to describe pages that gained four sections each.

All three run the same nine section order, and no two lay a section out the
same way, so the card copy leads on what each direction DOES with the sections
rather than on what sections exist.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'index.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    assert s.count(a) == 1, 'NOT UNIQUE -> %s' % a[:90]
    s = s.replace(a, b)


swap("""<b>What you see on each card is that package's homepage,</b> running live. Basic stops there. Standard and Premium add the pages listed underneath.</p>""",
"""<b>What you see on each card is that package's homepage,</b> running live. All three run the <b>same nine sections in the same order</b>, and no two of them lay a section out the same way, so what you are choosing between is the design. Basic stops at the homepage. Standard and Premium add the pages listed underneath.</p>""")

# ── Daylight ──────────────────────────────────────────────────────────────
swap("""      <p><b>Bright frosted glass on full screen photography.</b> The airy one. Every panel is a sheet of glass over a photograph, and two smaller plates lap across the hero at opposing angles so things are genuinely in front of each other. Services run as a zig zag of full bleed bands, the job index is an asymmetric bento, and the reels sit on a deep blue block.</p>""",
"""      <p><b>Bright frosted glass on full screen photography.</b> The airy one. Every pane is a sheet of glass over a photograph, and two smaller plates lap across the hero at opposing angles so things are genuinely in front of each other. Services zig zag down the page. The four steps of a job sit in ruled cells behind outlined numerals, the reasons to call are four columns ruled apart with no cards at all, and the job index has filter tabs that drop the bento to an even grid when you use one. Questions open on an accordion at the end.</p>""")

swap("""        <span class="tag key">Light glass</span><span class="tag">Bricolage Grotesque</span>
        <span class="tag">Full screen hero</span><span class="tag">Zig zag bands</span><span class="tag">Bento index</span>""",
"""        <span class="tag key">Light glass</span><span class="tag">Bricolage Grotesque</span>
        <span class="tag">Full screen hero</span><span class="tag">Outlined numerals</span>
        <span class="tag">Filter tabs</span><span class="tag">Bento index</span><span class="tag">FAQ accordion</span>""")

# ── Facade ────────────────────────────────────────────────────────────────
swap("""      <p><b>Smoked glass at dusk.</b> The dense one. Deep slate teal over a photograph that runs behind the whole page, which is what the glass refracts. Three split screens alternate down the page, and the services keep the split: the photograph changes as you scroll the column beside it. The job index is twelve upright panes that open when you point at them.</p>""",
"""      <p><b>Smoked glass at dusk.</b> The dense one. Deep slate teal over a photograph that runs behind the whole page, which is what the glass refracts. Three split screens alternate down the page, and the services keep the split: the photograph changes as you scroll the column beside it. The four steps of a job are glass tiles threaded on a hairline, the reasons to call are an asymmetric grid with a photograph occupying one cell, and the job index is twelve upright panes that open when you point at them. Questions run in two columns.</p>""")

swap("""        <span class="tag key">Smoked glass</span><span class="tag">Syne and Outfit</span>
        <span class="tag">Split screen</span><span class="tag">Sticky photo swap</span><span class="tag">Pane gallery</span>""",
"""        <span class="tag key">Smoked glass</span><span class="tag">Syne and Outfit</span>
        <span class="tag">Split screen</span><span class="tag">Sticky photo swap</span>
        <span class="tag">Numbered rail</span><span class="tag">Pane gallery</span><span class="tag">Two column FAQ</span>""")

# ── Reach ─────────────────────────────────────────────────────────────────
swap("""      <p><b>The one people remember.</b> Dark and cinematic, built vertically because the business is about reaching glass nobody else can. Its glass is square edged rather than soft. The three services are full screen panels that stack on each other as you scroll, the work is a filmstrip you drag, and the reviews sit on a deep blue block behind panes that catch a reflection when you touch them.</p>""",
"""      <p><b>The one people remember.</b> Dark and cinematic, built vertically because the business is about reaching glass nobody else can. Its glass is square edged rather than soft. The three services are full screen panels that stack on each other as you scroll. The four steps of a job stagger either side of a spine, the reasons to call are four solid cards nested inside a brand colour panel, the work is a filmstrip you drag, and the reviews sit on a deep blue block behind panes that catch a reflection when you touch them.</p>""")

swap("""        <span class="tag key">Square glass</span><span class="tag">Big Shoulders and Sora</span>
        <span class="tag">Sticky stack</span><span class="tag">Drag filmstrip</span><span class="tag">Colour block</span>""",
"""        <span class="tag key">Square glass</span><span class="tag">Big Shoulders and Sora</span>
        <span class="tag">Sticky stack</span><span class="tag">Journey spine</span>
        <span class="tag">Nested panel</span><span class="tag">Drag filmstrip</span><span class="tag">Colour block</span>""")

io.open(p, 'w', encoding='utf-8').write(s)
print('chooser: card copy and tags describe the new sections')
