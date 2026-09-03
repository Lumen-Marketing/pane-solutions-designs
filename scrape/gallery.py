"""Rewrite the chooser gallery for the rebuilt directions.

The three pages were rebuilt from scratch after the old set was rejected for
reading as machine-made, so every card, chip and matrix row here described
something that no longer exists. The gallery also carried the same tells the
pages did: numbered eyebrows on each card, em-dashes and middle-dot chains.
Those are gone too.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'index.html')
s = io.open(p, encoding='utf-8').read()
DASH = '—'
DOT = '·'

s = s.replace(
    '<span class="mono">Window Cleaning ' + DOT + ' Phoenix, AZ ' + DOT + ' Est. 2023</span>',
    '<span class="mono">Window cleaning in Phoenix, Arizona</span>')

s = s.replace('<h1>Three packages, three <em>looks.</em></h1>',
              '<h1>Three homepages, three <em>looks.</em></h1>')

old_lead = ("<p>Every one uses the <b>same real content</b> " + DASH + " Pane Solutions' own "
            "Instagram photos, their three real reels, and the 5.0★ Google reviews quoted as "
            "written. <b>What you see on each card is that package's homepage.</b> Basic stops "
            "there; Standard and Premium add the pages listed underneath.</p>")
new_lead = ("<p>Every one uses the <b>same real content</b>: Pane Solutions' own Instagram "
            "photos, their three real reels, and the 5.0★ Google reviews quoted as written. "
            "<b>What you see on each card is that package's homepage.</b> Basic stops there. "
            "Standard and Premium add the pages listed underneath.</p>")
assert old_lead in s, 'lead paragraph not found'
s = s.replace(old_lead, new_lead)

BASIC = """  <article class="card">
    <div class="tier"><b>Basic</b><span>Get found</span></div>
    <div class="card-hd">
      <h2>Daylight</h2>
      <a class="open" href="direction-1-pressure.html" target="_blank" rel="noopener">Open full screen &#8599;</a>
    </div>
    <div class="stage desktop" data-src="direction-1-pressure.html">
      <div class="loading"><span>Loading preview&#8230;</span></div>
      <div class="holder"></div>
      <div class="veil"><span>Click to interact</span></div>
    </div>
    <div class="card-bd">
      <p><b>A light poster.</b> The one that looks like an ad in a magazine rather than a website. Nothing is boxed. The photographs run at full size and a hard blue plane sits behind each one, shifted, so things physically stack. Sparse, confident, and the easiest of the three to read on a phone.</p>
      <ul class="incl">
        <li>One page, everything on it</li>
        <li>Click to call and click to email</li>
        <li>Their real photos and reviews</li>
        <li class="off">No contact form</li>
        <li class="off">No extra pages</li>
      </ul>
      <div class="chips">
        <span class="chip cy">Light</span><span class="chip">Bricolage Grotesque</span>
        <span class="chip">Offset colour planes</span><span class="chip">Photo mosaic</span><span class="chip">Poster scale</span>
      </div>
    </div>
  </article>"""

STANDARD = """  <article class="card">
    <div class="tier"><b>Standard</b><span>Look established</span></div>
    <div class="card-hd">
      <h2>Steel</h2>
      <a class="open" href="direction-3-spec-sheet.html" target="_blank" rel="noopener">Open full screen &#8599;</a>
    </div>
    <div class="stage desktop" data-src="direction-3-spec-sheet.html">
      <div class="loading"><span>Loading preview&#8230;</span></div>
      <div class="holder"></div>
      <div class="veil"><span>Click to interact</span></div>
    </div>
    <div class="card-bd">
      <p><b>Industrial and dense.</b> Painted steel, heavy black rules and safety orange. Every object is a machined plate with a lit top edge and a hard offset behind it. The three services are full-height photographs that open when you point at one. This is the option that looks like a working trade rather than a brochure.</p>
      <ul class="incl">
        <li>Homepage plus Services and Contact</li>
        <li>Working lead form to email and database</li>
        <li>Click to call and click to email</li>
        <li>Their real photos and reviews</li>
        <li class="off">No SEO build-out</li>
      </ul>
      <div class="chips">
        <span class="chip cy">Steel and orange</span><span class="chip">Archivo Expanded</span>
        <span class="chip">Machined plates</span><span class="chip">Photo accordion</span><span class="chip">Dense index grid</span>
      </div>
    </div>
  </article>"""

PREMIUM = """  <article class="card">
    <div class="tier"><b>Premium</b><span>Stand out</span></div>
    <div class="card-hd">
      <h2>Reach</h2>
      <a class="open" href="direction-2-altitude.html" target="_blank" rel="noopener">Open full screen &#8599;</a>
    </div>
    <div class="stage desktop" data-src="direction-2-altitude.html">
      <div class="loading"><span>Loading preview&#8230;</span></div>
      <div class="holder"></div>
      <div class="veil"><span>Click to interact</span></div>
    </div>
    <div class="card-bd">
      <p><b>The one people remember.</b> Dark and cinematic, built vertically because the business is about reaching glass nobody else can. The three services are full screen panels that stack on top of each other as you scroll, and the reviews sit behind glass panes that catch a reflection when you touch them.</p>
      <ul class="incl">
        <li>Full multi-page site</li>
        <li>Working lead form to email and database</li>
        <li>SEO groundwork and structured data</li>
        <li>Google Business schema for local search</li>
        <li>Full editorial motion throughout</li>
      </ul>
      <div class="chips">
        <span class="chip cy">Dark and photographic</span><span class="chip">Big Shoulders and Sora</span>
        <span class="chip">Sticky stack</span><span class="chip">Drag filmstrip</span><span class="chip">Glass panes</span>
      </div>
    </div>
  </article>"""

start = s.index('<div class="cards" id="cards">')
end = s.index('</div>', s.rindex('</article>')) + len('</div>')
s = (s[:start] + '<div class="cards" id="cards">\n\n'
     + BASIC + '\n\n' + STANDARD + '\n\n' + PREMIUM + '\n\n</div>' + s[end:])

# ── the furniture matrix ────────────────────────────────────────────────────
old_head = ('<thead><tr><th>Section</th><th>Basic ' + DASH + ' Pressure</th>'
            '<th>Standard ' + DASH + ' Spec Sheet</th><th>Premium ' + DASH + ' Altitude</th></tr></thead>')
new_head = ('<thead><tr><th>Section</th><th>Basic, Daylight</th>'
            '<th>Standard, Steel</th><th>Premium, Reach</th></tr></thead>')
assert old_head in s, 'matrix header not found'
s = s.replace(old_head, new_head)

ROWS = [
    ('Theme', 'Light paper', 'Painted steel', 'Near black'),
    ('Depth device', 'Offset colour planes',
     'Machined plates, lit edge and hard offset', 'Three planes, foreground occlusion'),
    ('Hero', 'Type left, photo bled off the right edge',
     'Dense split with a plate photo', 'Full bleed photo, plate hung over the edge'),
    ('Services', 'Three full-width bands',
     'Photo accordion, one opens at a time', 'Full-screen sticky stack'),
    ('Work', 'Asymmetric mosaic', 'Uniform index grid, eight cells', 'Drag-to-pan filmstrip'),
    ('Reels', 'Three equal blue plates', 'Three equal steel plates', 'Three equal ink plates'),
    ('Reviews', 'Paper plates over a blue plane',
     'Plate with a recessed core', 'Glass panes with a reflection sweep'),
    ('Contact', 'Solid blue block', 'Ink block with an orange rule',
     'Photograph with the number over it'),
]
body_start = s.index('<tbody>')
body_end = s.index('</tbody>') + len('</tbody>')
rows = '\n      '.join(
    '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in ROWS)
s = s[:body_start] + '<tbody>\n      ' + rows + '\n    </tbody>' + s[body_end:]

s = s.replace(
    '  <span class="mono">Same order in all three ' + DOT + ' <b>no component reused between '
    'directions</b> ' + DOT + ' tier changes scope, not layout</span>',
    '  <span class="mono">Same content in all three. <b>No component reused between '
    'directions.</b> The tier changes scope, not layout.</span>')

old_reels = ("<p>All three pages embed the three real reels from <b>@pane_solutions_llc</b> using "
             "Instagram's official embed widget. Instagram's player <b>does not auto-play</b> "
             + DASH + " it shows the cover frame with a play button and the viewer taps to watch. "
             "Until the widget loads, each panel shows the real cover frame with a link straight "
             "to the reel, so nothing ever renders as an empty box.</p>")
new_reels = ("<p>All three pages embed the three real reels from <b>@pane_solutions_llc</b> using "
             "Instagram's official embed widget. Instagram's player <b>does not auto-play</b>. It "
             "shows the cover frame with a play button and the viewer taps to watch. Until the "
             "widget loads, each panel shows the real cover frame with a link straight to the "
             "reel, so nothing ever renders as an empty box. Send the three video files over and "
             "they can be self-hosted for genuine autoplay.</p>")
assert old_reels in s, 'reels paragraph not found'
s = s.replace(old_reels, new_reels)

s = s.replace(
    '<span class="mono">Pane Solutions LLC ' + DOT + ' +1 515-525-4127 ' + DOT + ' Phoenix, AZ</span>',
    '<span class="mono">Pane Solutions LLC, Phoenix Arizona. +1 515-525-4127</span>')

io.open(p, 'w', encoding='utf-8').write(s)
print('gallery rewritten')
