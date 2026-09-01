"""Rework the Spec Sheet around windows and glass.

Before: a generic drafting sheet that happened to mention windows. Now the
window IS the structural system —

  * the sheet is a frame with a head, jambs and a deeper SILL along the foot;
  * the hero's column division is a real MULLION, a solid bar with a bead
    highlight, not a hairline rule;
  * each service is a LITE in a sash, with glazing-bead corner marks;
  * the job index becomes a DIVIDED-LIGHT SASH — eight panes behind muntins,
    every one of them grimy until you hover it clean. That is the interaction
    the whole business is about.

No gradients: the frost is a blur plus desaturation on the image itself and an
SVG speckle, not a translucent card and not a light bloom.
"""
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-3-spec-sheet.html')
s = open(p, encoding='utf-8').read()
lines = s.split('\n')


def block(start_marker, end_marker, new):
    """Replace the CSS block between two section comments."""
    global lines
    a = next(i for i, l in enumerate(lines) if l.startswith(start_marker))
    b = next(i for i, l in enumerate(lines) if i > a and l.startswith(end_marker))
    lines[a:b] = new.split('\n') + ['']


# ── sheet becomes a window frame with a sill ─────────────────────────────────
block('/* ── drawing sheet frame', '/* ── hero: an actual drawing sheet', r'''/* ── the sheet is a window: head, jambs, sill ───
   A frame is not a uniform box. The foot is deeper than the head, the way a
   sill is deeper than a head jamb, and that alone stops it reading as a plain
   rectangle. */
.sheet{position:relative;border:1.5px solid var(--ink);border-bottom-width:0;
  background:var(--sheet-bg);margin-top:60px}
.sheet::before{content:'';position:absolute;inset:7px;bottom:7px;border:1px solid var(--rule-2);
  pointer-events:none}
/* the sill: a deeper bar along the foot, with a bead line proud of it */
.sill{display:flex;align-items:center;gap:clamp(10px,1.6vw,22px);flex-wrap:wrap;
  padding:clamp(9px,1.2vw,15px) clamp(14px,1.9vw,26px);
  border:1.5px solid var(--ink);border-top:3px solid var(--ink);background:var(--paper-2)}
.sill .lbl{white-space:nowrap}
.cmark{position:absolute;width:16px;height:16px;border:1.5px solid var(--ink);z-index:3}
.cmark.tl{top:-1px;left:-1px;border-right:0;border-bottom:0}
.cmark.tr{top:-1px;right:-1px;border-left:0;border-bottom:0}
.cmark.bl,.cmark.br{display:none}''')

# ── mullion between the hero lites ───────────────────────────────────────────
s = '\n'.join(lines)
old = """.h-draw{grid-area:d;position:relative;padding:clamp(20px,3vw,46px);
  border-right:1px solid var(--rule);display:flex;flex-direction:column;justify-content:center;
  overflow:hidden}"""
new = """/* MULLION, not a hairline. The bar carries a bead highlight down its face the
   way a glazing bar does, so the two halves read as separate lites. */
.h-draw{grid-area:d;position:relative;padding:clamp(20px,3vw,46px);
  border-right:9px solid var(--rule);display:flex;flex-direction:column;justify-content:center;
  overflow:hidden}
.h-draw::after{content:'';position:absolute;top:0;bottom:0;right:-5px;width:1px;
  background:var(--paper);opacity:.55}"""
assert old in s
s = s.replace(old, new)

# ── services become lites in a sash ──────────────────────────────────────────
old = """.acc{border-top:1.5px solid var(--ink);background:var(--card)}
.item{border-bottom:1px solid var(--rule)}
.item.open{background:rgba(41,201,204,.05)}"""
new = """/* each service is a LITE: a pane set into the sash, with glazing-bead corner
   marks at its top-left and bottom-right */
.acc{border:1.5px solid var(--ink);background:var(--card);padding:7px}
.item{border:1px solid var(--rule);position:relative}
.item+.item{margin-top:7px}
.item.open{background:rgba(41,201,204,.05);border-color:var(--cy-ink)}
.item::before,.item::after{content:'';position:absolute;width:9px;height:9px;
  border:1px solid var(--rule-2);pointer-events:none;z-index:2}
.item::before{top:5px;left:5px;border-right:0;border-bottom:0}
.item::after{bottom:5px;right:5px;border-left:0;border-top:0}
.item.open::before,.item.open::after{border-color:var(--cy)}"""
assert old in s
s = s.replace(old, new)

# ── work: divided-light sash, grimy until hovered clean ──────────────────────
lines = s.split('\n')
block('/* ── work: index table + cursor peek', '/* ── reels: staggered tiles', r'''/* ── work: a divided-light sash ─────────────────
   Eight panes behind muntins. Every pane is grimy until you hover it clean —
   the interaction the entire business is about, and the reason this section is
   a sash rather than another photo grid.

   The grime is a blur + desaturate on the photograph itself plus an SVG
   speckle. No translucent card, no light bloom, no gradient. */
.sash{border:1.5px solid var(--ink);background:var(--ink);
  display:grid;grid-template-columns:repeat(4,1fr);gap:6px;padding:6px}
.lite{position:relative;overflow:hidden;aspect-ratio:3/4;background:var(--paper-2);
  cursor:pointer;isolation:isolate}
.lite img{width:100%;height:100%;object-fit:cover;
  filter:blur(7px) saturate(.35) contrast(.85) brightness(1.12);
  scale:1.1;transition:filter .55s var(--ease),scale .9s var(--ease)}
.lite:hover img,.lite:focus-visible img{filter:none;scale:1.02}
/* the grime itself: a speckle that lifts as the pane clears */
.lite::before{content:'';position:absolute;inset:0;z-index:2;pointer-events:none;opacity:.5;
  transition:opacity .55s var(--ease);
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.55' numOctaves='3'/%3E%3C/filter%3E%3Crect width='140' height='140' filter='url(%23g)' opacity='.55'/%3E%3C/svg%3E")}
.lite:hover::before,.lite:focus-visible::before{opacity:0}
.lite figcaption{position:absolute;left:0;right:0;bottom:0;z-index:3;padding:9px 10px;
  background:var(--ink);color:var(--paper);
  font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:.13em;text-transform:uppercase;
  display:flex;justify-content:space-between;gap:8px;
  translate:0 100%;transition:translate .45s var(--ease)}
.lite:hover figcaption,.lite:focus-visible figcaption{translate:0 0}
.lite figcaption em{font-style:normal;color:var(--cy)}
/* pane number, etched top-left, fades out as the pane clears */
.lite .no{position:absolute;top:8px;left:9px;z-index:3;
  font-family:'IBM Plex Mono',monospace;font-size:9.5px;letter-spacing:.14em;
  color:var(--ink);background:var(--paper);padding:3px 6px;
  transition:opacity .4s var(--ease)}
.lite:hover .no,.lite:focus-visible .no{opacity:0}
.sash-note{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;margin-top:11px}''')

s = '\n'.join(lines)

# ── markup: index table -> sash ──────────────────────────────────────────────
start = s.index('    <div class="idx" id="idx">')
end = s.index('</section>', start)
JOBS = [
    ('pole-entry', 'Entry glazing', 'Water-fed pole'),
    ('bay-pool', 'Bay window', 'Poolside interior'),
    ('interior-ladder', 'Tall interior pane', 'Ladder work'),
    ('french-doors', 'French doors', 'Black frame'),
    ('glass-patio', 'Patio slider run', 'Full elevation'),
    ('modern-gray', 'Mid-century glazing', 'Exterior'),
    ('lawn-side', 'Side elevation', 'Full run'),
    ('glass-corner', 'Glazed corner', 'Courtyard'),
]
panes = '\n'.join(
    f'''      <figure class="lite" tabindex="0">
        <img src="assets/photos/{f}@sm.webp" alt="{t} cleaned by Pane Solutions in Phoenix" loading="lazy">
        <span class="no">{i:02d}</span>
        <figcaption><span>{t}</span><em>{d}</em></figcaption>
      </figure>'''
    for i, (f, t, d) in enumerate(JOBS, 1))
s = s[:start] + f'''    <div class="sash">
{panes}
    </div>
    <div class="sash-note">
      <span class="lbl">8 lites &middot; <b>hover to clean</b></span>
      <span class="lbl">All glazing our own work &middot; Phoenix, AZ</span>
    </div>
  ''' + s[end:]

# the cursor-peek script has nothing left to drive
a = s.index("/* job index — a photo that tracks the cursor.")
b = s.index('})();', s.index('idx.addEventListener(\'pointerleave\'')) + len('})();')
s = s[:a] + "/* the job index is a sash now — panes clear on hover in CSS, no script. */" + s[b:]

# ── glazing terminology + the sill markup ────────────────────────────────────
for a_, b_ in [
    ('<span class="lbl">SHEET 02 — JOB INDEX</span>',
     '<span class="lbl">SHEET 02 — GLAZING SCHEDULE</span>'),
    ('<span class="lbl">SHEET 01 — SERVICE SCHEDULE</span>',
     '<span class="lbl">SHEET 01 — SCOPE OF GLAZING</span>'),
    ('<p class="rv" data-d="2">Hover a line to see the photo. Every one is our own work in the Phoenix area.</p>',
     '<p class="rv" data-d="2">Eight lites, every one of them our own work in the Phoenix area. They start dirty — hover to clean one.</p>'),
    ('<h2 class="rv">Recent<br>jobs</h2>', '<h2 class="rv">Recent<br>glazing</h2>'),
    ('<div class="seals">', '<div class="sill">'),
]:
    assert a_ in s, f'NO MATCH: {a_[:60]}'
    s = s.replace(a_, b_)

s = s.replace('.seals{display:flex', '.seals-unused{display:flex')

open(p, 'w', encoding='utf-8').write(s)
print('spec sheet reworked around windows and glass')
