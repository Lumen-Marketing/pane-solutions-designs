"""One-shot rewrite of the Altitude hero. Kept in the repo as the record of what
changed and why — the original hero was the default template arrangement."""
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-2-altitude.html')
lines = open(p, encoding='utf-8').read().split('\n')

NEW_CSS = r'''/* ── hero: full-bleed plate + squeegee wipe ──────
   Rebuilt. The first version was the default landing-page hero — rating chip,
   giant headline, paragraph, two buttons, photo card floating on a smooth
   gradient. Every one of those is a template tell, and the smooth gradient was
   the loudest. Now: the photograph IS the surface, the masthead runs edge to
   edge across it and is cropped by the viewport, there is ONE call to action,
   and the page arrives behind frosted glass that a squeegee wipes clear. */
.hero{position:relative;min-height:100svh;display:flex;flex-direction:column;
  justify-content:flex-end;background:var(--ink);overflow:hidden;isolation:isolate}
.hero-plate{position:absolute;inset:0;z-index:0}
.hero-plate img{width:100%;height:100%;object-fit:cover;object-position:52% 46%;
  filter:saturate(1.05) contrast(1.06);scale:1.04;
  animation:drift 30s var(--ease) infinite alternate}
@keyframes drift{to{scale:1.12;translate:-1.2% 0}}
/* top scrim keeps the nav legible over the photograph; bottom scrim lands the
   masthead on something solid without turning the whole plate into a gradient */
.hero-plate::after{content:'';position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(8,11,14,.72) 0,rgba(8,11,14,.12) 22%,
    rgba(8,11,14,0) 42%,rgba(8,11,14,.58) 72%,rgba(8,11,14,.93) 100%)}
/* grain — the single most effective antidote to a smooth synthetic surface */
.hero-grain{position:absolute;inset:0;z-index:1;pointer-events:none;opacity:.16;
  mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23n)'/%3E%3C/svg%3E")}

/* the squeegee. A tilted slab of frosted glass covering the whole hero that
   travels off to the right, with a wet highlight on its leading edge. */
.frost{position:absolute;top:-2px;bottom:-2px;left:-40%;width:170%;z-index:6;pointer-events:none;
  backdrop-filter:blur(15px) brightness(1.3) saturate(.4);
  -webkit-backdrop-filter:blur(15px) brightness(1.3) saturate(.4);
  background:linear-gradient(101deg,rgba(206,228,240,.46) 0 84%,
    rgba(255,255,255,.9) 90%,rgba(255,255,255,.22) 96%,rgba(255,255,255,0) 100%);
  clip-path:polygon(0 0,100% 0,89% 100%,0 100%);
  animation:squeegee 1.65s .25s cubic-bezier(.7,0,.28,1) forwards}
@keyframes squeegee{to{translate:138% 0}}
.frost.done{display:none}

.hero-kick{position:absolute;top:clamp(96px,13vh,150px);right:clamp(10px,1.6vw,22px);z-index:4;
  writing-mode:vertical-rl;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;
  letter-spacing:.44em;font-size:11.5px;font-weight:600;color:rgba(238,244,248,.62);
  display:flex;align-items:center;gap:16px}
.hero-kick::before{content:'';width:1px;height:64px;background:rgba(238,244,248,.42)}

.mast{position:relative;z-index:4;padding:0 0 clamp(18px,3vh,34px)}
/* one fitted line, sized in vw so it spans the viewport at every width and is
   cropped by the left gutter rather than politely centred inside a column */
.mast h1{font-size:14.4vw;line-height:.8;margin-left:calc(var(--gut) - .055em);
  color:var(--paper);white-space:nowrap;
  text-shadow:0 6px 40px rgba(8,11,14,.5)}
.mast .second{display:flex;align-items:baseline;gap:clamp(14px,3.4vw,58px);flex-wrap:wrap;
  padding:clamp(8px,1.4vh,18px) var(--gut) 0;
  border-top:1px solid rgba(238,244,248,.22);margin-top:clamp(10px,1.6vh,20px)}
.mast .no{font-family:'Anton',sans-serif;font-weight:400;text-transform:uppercase;
  font-size:clamp(2rem,6.6vw,6.2rem);line-height:.86;letter-spacing:-.012em;
  color:var(--cy);flex-shrink:0;margin-left:-.03em}
.hero-lede{max-width:42ch;color:rgba(238,244,248,.86);font-size:clamp(14.5px,1.1vw,17px);
  line-height:1.6;padding-bottom:.35em}
.hero-lede b{color:#fff;font-weight:600}
/* one CTA, as a rule-and-arrow link. A solid button next to an outlined button
   is the other half of the template tell. */
.cta{display:inline-flex;align-items:center;gap:14px;margin-left:auto;flex-shrink:0;
  font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;letter-spacing:.18em;
  font-size:clamp(14px,1.15vw,17px);font-weight:700;color:#fff;
  padding-bottom:7px;border-bottom:2px solid var(--cy);align-self:flex-end}
.cta i{font-style:normal;color:var(--cy);transition:translate .45s var(--ease)}
.cta:hover i{translate:9px 0}

/* ── proof: data table, butted flush to the plate ─ */
.proof{background:var(--ink);position:relative;z-index:4}
.ptable{display:grid;grid-template-columns:repeat(4,1fr);
  border-top:1px solid var(--slate);background:var(--ink)}
.pcell{border-right:1px solid var(--slate);padding:clamp(16px,2.2vw,30px) clamp(14px,2vw,26px)}
.pcell:last-child{border-right:0}
.pcell .k{font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;letter-spacing:.2em;
  font-size:11.5px;font-weight:600;color:var(--grey);display:block;margin-bottom:10px}
.pcell .v{font-family:'Anton',sans-serif;text-transform:uppercase;font-size:clamp(1.5rem,3.1vw,2.6rem);
  line-height:.9;display:block}
.pcell .v.cy{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.pcell .n{font-family:'Barlow Condensed',sans-serif;font-size:12.5px;letter-spacing:.1em;color:var(--grey);
  display:block;margin-top:8px;text-transform:uppercase}'''

NEW_HTML = r'''<header class="hero" id="top">
  <div class="hero-plate">
    <img src="assets/photos/arch-reflect.webp" alt="Pane Solutions technician squeegeeing a large arched window at a Phoenix home, the pool and palms reflected in the glass">
  </div>
  <div class="hero-grain"></div>
  <div class="frost" id="frost"></div>
  <div class="hero-kick">Phoenix &middot; Arizona &mdash; Est. 2023</div>

  <div class="mast">
    <h1 class="disp">Second storey?</h1>
    <div class="second">
      <span class="no">No problem.</span>
      <p class="hero-lede">Purified water-fed poles reach the glass a ladder shouldn't. <b>Window cleaning, pressure washing and gutter care</b> across Phoenix &mdash; free estimate before anyone touches a pane.</p>
      <a class="cta" href="#contact">Get a free estimate <i>&rarr;</i></a>
    </div>
  </div>
</header>

<div class="proof">
  <div class="ptable">
    <div class="pcell"><span class="k">Google rating</span><span class="v cy">5.0 &#9733;</span><span class="n">All reviews</span></div>
    <div class="pcell"><span class="k">Reviews</span><span class="v">13</span><span class="n">Verified on Google</span></div>
    <div class="pcell"><span class="k">Established</span><span class="v">2023</span><span class="n">Pane Solutions LLC</span></div>
    <div class="pcell"><span class="k">Estimates</span><span class="v">Free</span><span class="n">No charge to look</span></div>
  </div>
</div>'''

# anchor on content, not line numbers — earlier edits shifted the offsets
a = next(i for i, l in enumerate(lines) if l.startswith('/* ── hero: sky, split'))
b = next(i for i, l in enumerate(lines) if l.startswith('/* ── section heads'))
lines[a:b] = NEW_CSS.split('\n') + ['']

txt = '\n'.join(lines)
start = txt.index('<header class="hero" id="top">')
end = txt.index('<main class="wrap">')
assert '<div class="proof">' in txt[start:end]
txt = txt[:start] + NEW_HTML + '\n\n' + txt[end:]
open(p, 'w', encoding='utf-8').write(txt)
print('hero rebuilt OK')
