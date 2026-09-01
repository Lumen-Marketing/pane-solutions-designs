"""Rebuild of the Spec Sheet direction: three switchable palettes, and a hero
that is an actual drawing sheet rather than a landing-page split wearing a
drawing-sheet costume. Kept in the repo as the record of what changed."""
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-3-spec-sheet.html')
src = open(p, encoding='utf-8').read()
lines = src.split('\n')


def span(start_pred, end_pred):
    a = next(i for i, l in enumerate(lines) if start_pred(l))
    b = next(i for i, l in enumerate(lines) if i > a and end_pred(l))
    return a, b


# ── 1. tokens: three palettes ────────────────────────────────────────────────
NEW_TOKENS = r''':root{
  /* DRAFTING (default) — clean white stock, true black ink, logo cyan.
     Replaces the original pale green-grey paper + petrol teal, which read
     dingy and institutional rather than precise. */
  --paper:#F7F7F4; --paper-2:#EBEBE6; --card:#FFFFFE;
  --ink:#0B0C0C; --ink-2:#3D4244; --ink-3:#767B7C;
  --rule:#CFCFC8; --rule-2:#A3A39B;
  --grid-1:rgba(11,12,12,.055); --grid-2:rgba(11,12,12,.11);
  --cy:#12B8C4; --cy-ink:#0B7C86; --az:#2A6F9E; --bl:#3F5FA8;
  --stamp:#0B7C86;
  --grad:linear-gradient(135deg,var(--bl),var(--az) 50%,var(--cy));
  --gut:clamp(14px,3.4vw,52px);
  --ease:cubic-bezier(.2,1,.28,1);
}
/* BLUEPRINT — cyanotype. Prussian ground, white line work, cyan accent. */
:root[data-theme="blueprint"]{
  --paper:#0C2337; --paper-2:#123049; --card:#102B41;
  --ink:#EAF3F8; --ink-2:#A9C4D6; --ink-3:#6F90A6;
  --rule:#28506E; --rule-2:#3D6C8E;
  --grid-1:rgba(174,214,238,.075); --grid-2:rgba(174,214,238,.15);
  --cy:#4FE3E8; --cy-ink:#6FEDF1; --az:#5AB0E0; --bl:#7E9BE8;
  --stamp:#6FEDF1;
}
/* VELLUM — warm drawing-office stock, sepia rules, cyan kept as the one accent */
:root[data-theme="vellum"]{
  --paper:#F3EDE1; --paper-2:#E7DFCE; --card:#FBF7EF;
  --ink:#1A1611; --ink-2:#4A423A; --ink-3:#857B6D;
  --rule:#CFC3AC; --rule-2:#A89B83;
  --grid-1:rgba(90,70,40,.07); --grid-2:rgba(90,70,40,.13);
  --cy:#0F9AA6; --cy-ink:#0A6E78; --az:#2A6F9E; --bl:#3F5FA8;
  --stamp:#9A3B1E;
}'''

a, b = span(lambda l: l.startswith(':root{'), lambda l: l == '}')
lines[a:b + 1] = NEW_TOKENS.split('\n')

# ── 2. body graph paper reads from tokens so it repaints with the theme ──────
src = '\n'.join(lines)
old_bg = """  background-image:
    linear-gradient(rgba(43,90,110,.055) 1px,transparent 1px),
    linear-gradient(90deg,rgba(43,90,110,.055) 1px,transparent 1px),
    linear-gradient(rgba(43,90,110,.10) 1px,transparent 1px),
    linear-gradient(90deg,rgba(43,90,110,.10) 1px,transparent 1px);
  background-size:9px 9px,9px 9px,90px 90px,90px 90px;"""
new_bg = """  /* tokenised so the graph paper repaints with the palette */
  background-image:
    linear-gradient(var(--grid-1) 1px,transparent 1px),
    linear-gradient(90deg,var(--grid-1) 1px,transparent 1px),
    linear-gradient(var(--grid-2) 1px,transparent 1px),
    linear-gradient(90deg,var(--grid-2) 1px,transparent 1px);
  background-size:9px 9px,9px 9px,90px 90px,90px 90px;
  transition:background-color .5s var(--ease),color .5s var(--ease);"""
assert old_bg in src
src = src.replace(old_bg, new_bg)

# ── 3. hero CSS ──────────────────────────────────────────────────────────────
lines = src.split('\n')
NEW_HERO_CSS = r'''/* ── hero: an actual drawing sheet ───────────────
   The first version was type-left / photo-right with a solid button beside an
   outlined one — a landing-page split wearing a drawing-sheet costume. A real
   sheet is a drawing, dimensioned, with the photograph demoted to a pinned
   reference and a title block along the foot. That is what this is now. */
.hero{position:relative;display:grid;grid-template-columns:repeat(12,1fr);
  grid-template-areas:'d d d d d d d d n n n n';
  min-height:clamp(430px,62vh,640px)}
.h-draw{grid-area:d;position:relative;padding:clamp(20px,3vw,46px);
  border-right:1px solid var(--rule);display:flex;flex-direction:column;justify-content:center;
  overflow:hidden}
.docref{display:inline-flex;align-items:center;gap:9px;margin-bottom:clamp(12px,1.8vw,22px)}
.docref .sq{width:9px;height:9px;background:var(--cy);border:1px solid var(--ink)}
h1{font-size:clamp(2.2rem,6.6vw,5.9rem);letter-spacing:-.035em;position:relative;z-index:3}
h1 .u{position:relative;display:inline-block}
h1 .u::after{content:'';position:absolute;left:0;right:0;bottom:.07em;height:.07em;background:var(--grad)}
/* the line-art window elevation the headline is dimensioned against */
.elev{position:absolute;right:clamp(-30px,-2vw,0px);top:50%;translate:0 -50%;
  width:min(46%,340px);opacity:.9;z-index:1;pointer-events:none;color:var(--rule-2)}
.elev .pane{fill:var(--cy);opacity:.07}
.elev .wipe{stroke:var(--cy);stroke-width:2.5;fill:none;opacity:.85;
  stroke-dasharray:420;stroke-dashoffset:420;animation:draw 2.4s .5s var(--ease) forwards}
@keyframes draw{to{stroke-dashoffset:0}}
.h-sub{max-width:46ch;margin-top:clamp(12px,1.8vw,20px);color:var(--ink-2);
  font-size:clamp(14.5px,1.05vw,16.5px);position:relative;z-index:3}
.h-sub b{color:var(--ink);font-weight:600}
/* dimension line: the scope of work, drawn the way a drawing states a span */
.dim{display:flex;align-items:center;gap:8px;margin-top:clamp(14px,2vw,24px);color:var(--cy-ink);
  position:relative;z-index:3;max-width:640px}
.dim .ln{flex:1;height:1px;background:currentColor;position:relative}
.dim .ln::before,.dim .ln::after{content:'';position:absolute;top:-3px;width:0;height:0;
  border-block:3.5px solid transparent}
.dim .ln::before{left:0;border-right:6px solid currentColor}
.dim .ln::after{right:0;border-left:6px solid currentColor}
.dim span{font-family:'IBM Plex Mono',monospace;font-size:9.5px;letter-spacing:.16em;
  text-transform:uppercase;white-space:nowrap}
/* ONE call to action. A solid button next to an outlined button is the tell. */
.h-acts{display:flex;align-items:center;gap:clamp(14px,2.4vw,30px);flex-wrap:wrap;
  margin-top:clamp(16px,2.4vw,28px);position:relative;z-index:3}
.btn-line{display:inline-flex;align-items:center;gap:8px;font-family:'IBM Plex Mono',monospace;
  font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;
  color:var(--ink-2);border-bottom:1px solid var(--rule-2);padding-bottom:4px;
  transition:color .35s,border-color .35s}
.btn-line:hover{color:var(--cy-ink);border-color:var(--cy-ink)}

/* right column: pinned photo reference over the spec cells */
.h-ref{grid-area:n;display:grid;grid-template-rows:1fr auto}
.h-photo{position:relative;overflow:hidden;border-bottom:1px solid var(--rule);min-height:210px}
.h-photo img{width:100%;height:100%;object-fit:cover;object-position:56% 42%;
  filter:saturate(.95) contrast(1.04);scale:1.02;transition:scale 1.1s var(--ease)}
.h-photo:hover img{scale:1.08}
.h-photo .cap{position:absolute;left:9px;bottom:9px;background:var(--ink);color:var(--paper);
  padding:5px 9px;font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:.16em;
  text-transform:uppercase}
.h-spec{display:grid;grid-template-columns:1fr 1fr}
.h-spec div{padding:clamp(11px,1.4vw,18px);border-right:1px solid var(--rule);
  border-bottom:1px solid var(--rule)}
.h-spec div:nth-child(2n){border-right:0}
.h-spec div:nth-last-child(-n+2){border-bottom:0}
.h-spec .k{display:block;font-family:'IBM Plex Mono',monospace;font-size:9.5px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--ink-3);margin-bottom:6px}
.h-spec .v{display:block;font-size:clamp(15px,1.5vw,20px);font-weight:700;text-transform:uppercase;
  line-height:1.05}
.h-spec .v.cy{color:var(--cy-ink)}

/* palette switcher, sat in the sheet's own title strip */
.swatches{display:flex;align-items:center;gap:7px;margin-left:auto}
.swatches b{font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--ink-3);font-weight:500;margin-right:3px}
.sw{width:17px;height:17px;border:1.5px solid var(--rule-2);cursor:pointer;padding:0;
  transition:border-color .3s,transform .3s var(--ease)}
.sw:hover{transform:translateY(-2px)}
.sw[aria-pressed="true"]{border-color:var(--cy-ink);box-shadow:0 0 0 2px var(--paper),0 0 0 3px var(--cy-ink)}
.sw-drafting{background:linear-gradient(135deg,#F7F7F4 50%,#12B8C4 50%)}
.sw-blueprint{background:linear-gradient(135deg,#0C2337 50%,#4FE3E8 50%)}
.sw-vellum{background:linear-gradient(135deg,#F3EDE1 50%,#9A3B1E 50%)}'''

a, b = span(lambda l: l.startswith('/* ── hero: modular grid'),
            lambda l: l.startswith('/* ── proof: stamped seals'))
lines[a:b] = NEW_HERO_CSS.split('\n') + ['']

# ── 4. hero markup ───────────────────────────────────────────────────────────
src = '\n'.join(lines)
NEW_HERO_HTML = r'''<header class="sheet" id="top">
  <i class="cmark tl"></i><i class="cmark tr"></i><i class="cmark bl"></i><i class="cmark br"></i>
  <div class="hero">
    <div class="h-draw">
      <span class="docref"><i class="sq"></i><span class="lbl">DOC. PS-2023 / REV. A &mdash; <b>PHOENIX, AZ</b></span></span>
      <h1>Clean glass,<br><span class="u">to spec.</span></h1>
      <p class="h-sub">Window cleaning, pressure washing and gutter care for Phoenix homes and businesses. <b>Purified water, no streaking, a walkthrough before we leave</b> &mdash; and a free estimate before any of it starts.</p>
      <div class="dim"><span>SCOPE</span><i class="ln"></i><span>RESIDENTIAL + COMMERCIAL</span></div>
      <div class="h-acts">
        <a class="btn" href="#contact"><s>Request estimate</s></a>
        <a class="btn-line" href="#work">View job index &rarr;</a>
      </div>
      <!-- window elevation, dimensioned. The squeegee stroke draws itself in. -->
      <svg class="elev" viewBox="0 0 240 300" fill="none" aria-hidden="true">
        <rect class="pane" x="34" y="34" width="172" height="212"/>
        <rect x="34" y="34" width="172" height="212" stroke="currentColor" stroke-width="1.5"/>
        <rect x="41" y="41" width="158" height="198" stroke="currentColor" stroke-width="1"/>
        <path d="M120 41V239M41 140h158" stroke="currentColor" stroke-width="1"/>
        <path d="M34 20h172M34 15v10M206 15v10" stroke="currentColor" stroke-width="1"/>
        <path d="M222 34v212M217 34h10M217 246h10" stroke="currentColor" stroke-width="1"/>
        <path class="wipe" d="M48 62c34 0 34 26 68 26s34-26 68-26"/>
        <path class="wipe" d="M48 104c34 0 34 26 68 26s34-26 68-26" style="animation-delay:.85s"/>
        <circle cx="34" cy="34" r="3" fill="currentColor"/>
        <circle cx="206" cy="246" r="3" fill="currentColor"/>
      </svg>
    </div>
    <div class="h-ref">
      <figure class="h-photo">
        <img src="assets/photos/pole-entry.webp" alt="Pane Solutions technician cleaning entry glass with a water-fed pole in Phoenix">
        <figcaption class="cap">FIG. 1 &mdash; WATER-FED POLE, ENTRY GLAZING</figcaption>
      </figure>
      <div class="h-spec">
        <div><span class="k">Rating</span><span class="v cy">5.0 &#9733;</span></div>
        <div><span class="k">Reviews</span><span class="v">13</span></div>
        <div><span class="k">Established</span><span class="v">2023</span></div>
        <div><span class="k">Estimate</span><span class="v">Free</span></div>
      </div>
    </div>
  </div>
  <div class="seals">
    <div class="seal"><span class="st">&#9733;&#9733;&#9733;&#9733;&#9733;</span><span class="sm">Google<br>5.0 / 13 reviews</span></div>
    <div class="seal"><span class="big cy">FREE</span><span class="sm">Estimates<br>No charge to look</span></div>
    <div class="seal"><span class="big">LLC</span><span class="sm">Registered<br>Est. 2023</span></div>
    <div class="seal"><span class="big">AZ</span><span class="sm">Phoenix<br>&amp; surrounds</span></div>
    <div class="swatches">
      <b>Sheet stock</b>
      <button class="sw sw-drafting" data-theme="drafting" aria-pressed="true" title="Drafting — white stock"></button>
      <button class="sw sw-blueprint" data-theme="blueprint" aria-pressed="false" title="Blueprint — cyanotype"></button>
      <button class="sw sw-vellum" data-theme="vellum" aria-pressed="false" title="Vellum — warm stock"></button>
    </div>
  </div>
</header>'''

start = src.index('<header class="sheet" id="top">')
end = src.index('</header>', start) + len('</header>')
src = src[:start] + NEW_HERO_HTML + src[end:]

# ── 5. theme switcher behaviour ──────────────────────────────────────────────
old_js = "document.getElementById('yr').textContent=new Date().getFullYear();"
new_js = r'''document.getElementById('yr').textContent=new Date().getFullYear();

/* palette switcher. Reads ?theme= first so the gallery can deep-link a stock,
   then remembers the choice for this viewer only. */
(function(){
  var VALID={drafting:1,blueprint:1,vellum:1};
  function apply(t){
    if(!VALID[t])t='drafting';
    if(t==='drafting')document.documentElement.removeAttribute('data-theme');
    else document.documentElement.setAttribute('data-theme',t);
    document.querySelectorAll('.sw').forEach(function(b){
      b.setAttribute('aria-pressed',String(b.dataset.theme===t));
    });
    try{localStorage.setItem('ps-sheet-stock',t)}catch(e){}
  }
  var q=new URLSearchParams(location.search).get('theme');
  var saved=null; try{saved=localStorage.getItem('ps-sheet-stock')}catch(e){}
  apply(q||saved||'drafting');
  document.querySelectorAll('.sw').forEach(function(b){
    b.addEventListener('click',function(){apply(b.dataset.theme)});
  });
})();'''
assert old_js in src
src = src.replace(old_js, new_js, 1)

# ── 6. responsive for the new hero ───────────────────────────────────────────
old_r = """  .hero{grid-template-columns:1fr}
  .h-type{grid-column:1/-1;border-right:0;border-bottom:1px solid var(--rule);min-height:0}
  .h-rev{grid-column:1/-1}"""
new_r = """  .hero{grid-template-columns:1fr;grid-template-areas:'d' 'n';min-height:0}
  .h-draw{border-right:0;border-bottom:1px solid var(--rule)}
  .elev{width:min(38%,220px);opacity:.5}"""
assert old_r in src
src = src.replace(old_r, new_r)

old_r2 = """  .h-spec{grid-template-columns:1fr}
  .h-spec div{border-right:0}"""
new_r2 = """  .h-spec{grid-template-columns:1fr 1fr}
  .elev{display:none}
  .swatches{width:100%;margin-left:0;padding-top:4px}"""
assert old_r2 in src
src = src.replace(old_r2, new_r2)

open(p, 'w', encoding='utf-8').write(src)
print('spec sheet rebuilt: 3 palettes + drawing-sheet hero')
