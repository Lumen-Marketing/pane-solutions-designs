"""Label the three directions as Basic / Standard / Premium and reorder the
gallery to read cheapest-first.

The three pages are NOT rebuilt — all three remain the same scope (one page,
same sections, same motion). The tier now names the PACKAGE the client buys;
the page shown on each card is that package's homepage. Scope per tier is
listed on the card so the label means something.
"""
import os
import re

HERE = os.path.dirname(__file__)
p = os.path.join(HERE, '..', 'index.html')
s = open(p, encoding='utf-8').read()

# ── header copy ──────────────────────────────────────────────────────────────
old_h = """  <h1>Three homepage <em>directions.</em></h1>"""
new_h = """  <h1>Three packages, three <em>looks.</em></h1>"""
assert old_h in s
s = s.replace(old_h, new_h)

old_lead = """    <p>All three use the <b>same section order</b> and the <b>same real content</b> — Pane Solutions' own Instagram photos, the three real reels, and the 5.0★ Google reviews quoted as written. What changes is the art direction. Pick the one that feels like the business.</p>"""
new_lead = """    <p>Every one uses the <b>same real content</b> — Pane Solutions' own Instagram photos, their three real reels, and the 5.0★ Google reviews quoted as written. <b>What you see on each card is that package's homepage.</b> Basic stops there; Standard and Premium add the pages listed underneath.</p>"""
assert old_lead in s
s = s.replace(old_lead, new_lead)

# ── tier styling ─────────────────────────────────────────────────────────────
old_css = """.card-hd .no{font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.16em;color:var(--cy);font-weight:700}"""
new_css = """.card-hd .no{font-family:'Space Mono',monospace;font-size:11px;letter-spacing:.16em;color:var(--cy);font-weight:700}
.tier{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;padding:11px 17px;
  border-bottom:1px solid var(--steel-800);background:var(--ink)}
.tier b{font-family:'Space Mono',monospace;font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--ink);background:var(--acc);padding:5px 9px;font-weight:700}
.tier span{font-family:'Space Mono',monospace;font-size:10px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--steel-400)}
.incl{list-style:none;display:grid;gap:6px;padding-top:11px;margin-top:2px;border-top:1px solid var(--steel-800)}
.incl li{font-family:'Space Mono',monospace;font-size:10px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--steel-300);display:flex;gap:9px;align-items:baseline}
.incl li::before{content:'+';color:var(--acc);flex-shrink:0}
.incl li.off{color:var(--steel-600)}
.incl li.off::before{content:'−';color:var(--steel-600)}"""
assert old_css in s
s = s.replace(old_css, new_css)

# ── cards: reorder Basic -> Standard -> Premium ──────────────────────────────
BASIC = """  <article class="card">
    <div class="tier"><b>Basic</b><span>Get found</span></div>
    <div class="card-hd">
      <span class="no">01</span><h2>Pressure</h2>
      <a class="open" href="direction-1-pressure.html" target="_blank" rel="noopener">Open full screen ↗</a>
    </div>
    <div class="stage desktop" data-src="direction-1-pressure.html">
      <div class="loading"><span>Loading preview…</span></div>
      <div class="holder"></div>
      <div class="veil"><span>Click to interact</span></div>
    </div>
    <div class="card-bd">
      <p><b>Straightforward and credible.</b> Near-black throughout, a strict engineering grid, and a full-bleed hero photo under enormous expanded type. Services are numbered full-width rows; the phone number is the size of a headline. Reads like an established contractor without asking anyone to work for it.</p>
      <ul class="incl">
        <li>One page, everything on it</li>
        <li>Click-to-call and click-to-email</li>
        <li>Their real photos and reviews</li>
        <li class="off">No contact form</li>
        <li class="off">No extra pages</li>
      </ul>
      <div class="chips">
        <span class="chip cy">Dark</span><span class="chip">Archivo + Space Mono</span>
        <span class="chip">Full-bleed hero</span><span class="chip">Photo mosaic</span><span class="chip">Equipment rack</span>
      </div>
    </div>
  </article>"""

STANDARD = """  <article class="card">
    <div class="tier"><b>Standard</b><span>Look established</span></div>
    <div class="card-hd">
      <span class="no">02</span><h2>Spec Sheet</h2>
      <a class="open" href="direction-3-spec-sheet.html" target="_blank" rel="noopener">Open full screen ↗</a>
    </div>
    <div class="stage desktop" data-src="direction-3-spec-sheet.html">
      <div class="loading"><span>Loading preview…</span></div>
      <div class="holder"></div>
      <div class="veil"><span>Click to interact</span></div>
    </div>
    <div class="card-bd">
      <p><b>Precision as the sales pitch.</b> The whole page is an engineering drawing — a bordered sheet with corner marks, a dimensioned window elevation the squeegee strokes draw themselves onto, part numbers on each service and a real title block. <b>Three sheet stocks</b>: switch between blueprint, white drafting and warm vellum from the dots in the title strip.</p>
      <ul class="incl">
        <li>Homepage plus Services and Contact</li>
        <li>Working lead form to email + database</li>
        <li>Click-to-call and click-to-email</li>
        <li>Their real photos and reviews</li>
        <li class="off">No SEO / structured data build-out</li>
      </ul>
      <div class="chips">
        <span class="chip cy">3 switchable stocks</span><span class="chip">IBM Plex Mono + Condensed</span>
        <span class="chip">Drawing-sheet hero</span><span class="chip">Accordion</span><span class="chip">Cursor peek</span>
      </div>
    </div>
  </article>"""

PREMIUM = """  <article class="card">
    <div class="tier"><b>Premium</b><span>Stand out</span></div>
    <div class="card-hd">
      <span class="no">03</span><h2>Altitude</h2>
      <a class="open" href="direction-2-altitude.html" target="_blank" rel="noopener">Open full screen ↗</a>
    </div>
    <div class="stage desktop" data-src="direction-2-altitude.html">
      <div class="loading"><span>Loading preview…</span></div>
      <div class="holder"></div>
      <div class="veil"><span>Click to interact</span></div>
    </div>
    <div class="card-bd">
      <p><b>The one people remember.</b> The photograph is the surface, not a card on it — a full-bleed plate with the masthead running edge to edge across it, cropped by the viewport. The page arrives behind frosted glass that a squeegee wipes clear. One call to action, a drag-to-pan filmstrip, reels in phone frames.</p>
      <ul class="incl">
        <li>Full multi-page site</li>
        <li>Working lead form to email + database</li>
        <li>SEO groundwork and structured data</li>
        <li>Google Business schema for local search</li>
        <li>Full editorial motion throughout</li>
      </ul>
      <div class="chips">
        <span class="chip cy">Dark · photographic</span><span class="chip">Anton + Barlow</span>
        <span class="chip">Squeegee wipe</span><span class="chip">Drag filmstrip</span><span class="chip">Phone stack</span>
      </div>
    </div>
  </article>"""

start = s.index('<div class="cards" id="cards">')
end = s.index('</div>', s.rindex('</article>')) + len('</div>')
s = s[:start] + '<div class="cards" id="cards">\n\n' + BASIC + '\n\n' + STANDARD + '\n\n' + PREMIUM + '\n\n</div>' + s[end:]

# ── matrix header follows the new order ──────────────────────────────────────
old_th = """<thead><tr><th>Section</th><th>01 — Pressure</th><th>02 — Altitude</th><th>03 — Spec Sheet</th></tr></thead>"""
new_th = """<thead><tr><th>Section</th><th>Basic — Pressure</th><th>Standard — Spec Sheet</th><th>Premium — Altitude</th></tr></thead>"""
assert old_th in s
s = s.replace(old_th, new_th)

# swap the Altitude and Spec Sheet columns in every body row so the table
# matches the card order
rows = re.findall(r'<tr><td>(?!Section)([^<]+)</td><td>([^<]*)</td><td>([^<]*)</td><td>([^<]*)</td></tr>', s)
for label, c1, c2, c3 in rows:
    old = f'<tr><td>{label}</td><td>{c1}</td><td>{c2}</td><td>{c3}</td></tr>'
    new = f'<tr><td>{label}</td><td>{c1}</td><td>{c3}</td><td>{c2}</td></tr>'
    s = s.replace(old, new)

old_note = """  <span class="mono">Same order in all three · <b>no component reused between directions</b></span>"""
new_note = """  <span class="mono">Same order in all three · <b>no component reused between directions</b> · tier changes scope, not layout</span>"""
assert old_note in s
s = s.replace(old_note, new_note)

open(p, 'w', encoding='utf-8').write(s)
print(f'tiers applied; {len(rows)} matrix rows re-ordered')
