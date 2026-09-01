"""Remove every visible colour ramp from all four pages.

Kept deliberately: hard-stop line patterns (the graph paper, the rack's
ventilation slots, the two-tone palette swatches) and mask-images. Those use
gradient *syntax* but have no blend — they read as lines and split squares, not
as gradients. Everything that actually ramps between two colours is gone,
including the photographic scrims, which are now flat planes.
"""
import os

HERE = os.path.dirname(__file__)
R = lambda n: os.path.join(HERE, '..', n)


def edit(name, pairs):
    p = R(name)
    s = open(p, encoding='utf-8').read()
    for a, b in pairs:
        assert a in s, f'{name}: NO MATCH -> {a[:78]}'
        s = s.replace(a, b)
    open(p, 'w', encoding='utf-8').write(s)
    print(f'{name}: {len(pairs)} edits')


# ── index.html ───────────────────────────────────────────────────────────────
edit('index.html', [
    ("  --grad:linear-gradient(135deg,var(--bl),var(--az) 50%,var(--cy));",
     "  /* flat accent: no ramps anywhere in this set */\n  --acc:var(--cy);"),
    (".seg button.on{background:var(--grad);color:var(--ink);font-weight:700}",
     ".seg button.on{background:var(--acc);color:var(--ink);font-weight:700}"),
    ("h1 em{font-style:normal;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}",
     "h1 em{font-style:normal;color:var(--acc)}"),
    (".veil{position:absolute;inset:0;z-index:5;background:linear-gradient(rgba(6,8,10,.05),rgba(6,8,10,.4));",
     ".veil{position:absolute;inset:0;z-index:5;background:rgba(6,8,10,.28);"),
])

# ── direction 1 ──────────────────────────────────────────────────────────────
edit('direction-1-pressure.html', [
    ("  --grad:linear-gradient(135deg,var(--bl) 0%,var(--az) 48%,var(--cy) 100%);",
     "  /* flat accent: no ramps anywhere in this set */\n  --acc:var(--cy);"),
    (".btn{display:inline-flex;align-items:center;gap:9px;font-family:'Space Mono',monospace;font-size:11px;\n"
     "  letter-spacing:.16em;text-transform:uppercase;padding:11px 20px;background:var(--grad);color:var(--ink);",
     ".btn{display:inline-flex;align-items:center;gap:9px;font-family:'Space Mono',monospace;font-size:11px;\n"
     "  letter-spacing:.16em;text-transform:uppercase;padding:11px 20px;background:var(--acc);color:var(--ink);"),
    (".rail::before{content:'';position:absolute;left:0;top:0;width:1px;height:38%;background:var(--grad)}",
     ".rail::before{content:'';position:absolute;left:0;top:0;width:1px;height:38%;background:var(--acc)}"),
    # hero: flat plane instead of a two-stop scrim
    (".hero-scrim{position:absolute;inset:0;z-index:1;\n"
     "  background:linear-gradient(100deg,var(--ink) 6%,rgba(6,8,10,.9) 32%,rgba(6,8,10,.42) 62%,rgba(6,8,10,.72) 100%),\n"
     "             linear-gradient(0deg,var(--ink) 2%,transparent 42%)}",
     "/* flat plane, not a scrim. Two overlapping ramps were the softest thing on\n"
     "   the page; a single even wash keeps the type legible and reads harder. */\n"
     ".hero-scrim{position:absolute;inset:0;z-index:1;background:rgba(6,8,10,.66)}\n"
     "/* solid band under the masthead so the copy sits on ink, not on a fade */\n"
     ".hero-scrim::after{content:'';position:absolute;left:0;right:0;bottom:0;height:34%;background:var(--ink);opacity:.82}"),
    (".scroll-cue::after{content:'';width:1px;height:52px;background:linear-gradient(var(--cy),transparent);animation:drop 2.2s infinite var(--ease)}",
     ".scroll-cue::after{content:'';width:1px;height:52px;background:var(--acc);animation:drop 2.2s infinite var(--ease)}"),
    (".svc-row::before{content:'';position:absolute;left:calc(var(--gut) * -1);right:calc(var(--gut) * -1);top:0;bottom:0;z-index:-1;\n"
     "  background:linear-gradient(90deg,transparent,rgba(47,216,220,.05) 40%,transparent);",
     ".svc-row::before{content:'';position:absolute;left:calc(var(--gut) * -1);right:calc(var(--gut) * -1);top:0;bottom:0;z-index:-1;\n"
     "  background:rgba(47,216,220,.055);"),
    (".tile::after{content:attr(data-cap);position:absolute;left:0;bottom:0;right:0;padding:14px;\n"
     "  font-family:'Space Mono',monospace;font-size:9.5px;letter-spacing:.18em;text-transform:uppercase;\n"
     "  background:linear-gradient(transparent,rgba(6,8,10,.94));color:var(--paper);",
     ".tile::after{content:attr(data-cap);position:absolute;left:0;bottom:0;right:0;padding:14px;\n"
     "  font-family:'Space Mono',monospace;font-size:9.5px;letter-spacing:.18em;text-transform:uppercase;\n"
     "  background:rgba(6,8,10,.92);color:var(--paper);"),
    (".bay-hd{display:flex;align-items:center;gap:9px;padding:10px 13px;border-bottom:1px solid var(--steel-800);\n"
     "  background:linear-gradient(var(--steel-800),var(--steel-900))}",
     ".bay-hd{display:flex;align-items:center;gap:9px;padding:10px 13px;border-bottom:1px solid var(--steel-800);\n"
     "  background:var(--steel-800)}"),
    (".quote-big blockquote b{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent;font-weight:800}",
     ".quote-big blockquote b{color:var(--acc);font-weight:800}"),
    (".contact::before{content:'';position:absolute;inset:0;\n"
     "  background:radial-gradient(80% 130% at 12% 110%,rgba(47,216,220,.14),transparent 62%)}",
     "/* was a radial glow; now a hard accent rule along the top edge */\n"
     ".contact::before{content:'';position:absolute;left:0;right:0;top:0;height:2px;background:var(--acc)}"),
    (".bignum:hover{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}",
     ".bignum:hover{color:var(--acc)}"),
    ("h1 .gr{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}",
     "h1 .gr{color:var(--acc)}"),
    (".play{width:44px;height:44px;border-radius:50%;background:var(--grad);",
     ".play{width:44px;height:44px;border-radius:50%;background:var(--acc);"),
])

# ── direction 2 ──────────────────────────────────────────────────────────────
edit('direction-2-altitude.html', [
    ("  --grad:linear-gradient(135deg,var(--bl),var(--az) 50%,var(--cy));",
     "  /* flat accent: no ramps anywhere in this set */\n  --acc:var(--cy);"),
    (".hero-plate::after{content:'';position:absolute;inset:0;\n"
     "  background:linear-gradient(180deg,rgba(8,11,14,.72) 0,rgba(8,11,14,.12) 22%,\n"
     "    rgba(8,11,14,0) 42%,rgba(8,11,14,.58) 72%,rgba(8,11,14,.93) 100%)}",
     "/* flat wash + two solid bands instead of a five-stop scrim. The bands give\n"
     "   the nav and the masthead something hard to sit on. */\n"
     ".hero-plate::after{content:'';position:absolute;inset:0;background:rgba(8,11,14,.34)}\n"
     ".hero-plate::before{content:'';position:absolute;left:0;right:0;top:0;height:78px;z-index:2;\n"
     "  background:rgba(8,11,14,.62)}"),
    (".frost{position:absolute;top:-2px;bottom:-2px;left:-40%;width:170%;z-index:6;pointer-events:none;\n"
     "  backdrop-filter:blur(15px) brightness(1.3) saturate(.4);\n"
     "  -webkit-backdrop-filter:blur(15px) brightness(1.3) saturate(.4);\n"
     "  background:linear-gradient(101deg,rgba(206,228,240,.46) 0 84%,\n"
     "    rgba(255,255,255,.9) 90%,rgba(255,255,255,.22) 96%,rgba(255,255,255,0) 100%);\n"
     "  clip-path:polygon(0 0,100% 0,89% 100%,0 100%);",
     ".frost{position:absolute;top:-2px;bottom:-2px;left:-40%;width:170%;z-index:6;pointer-events:none;\n"
     "  backdrop-filter:blur(15px) brightness(1.3) saturate(.4);\n"
     "  -webkit-backdrop-filter:blur(15px) brightness(1.3) saturate(.4);\n"
     "  background:rgba(206,228,240,.46);\n"
     "  border-right:3px solid rgba(255,255,255,.92);\n"
     "  clip-path:polygon(0 0,100% 0,89% 100%,0 100%);"),
    (".frame figcaption{position:absolute;left:0;right:0;bottom:0;padding:14px 15px;\n"
     "  background:linear-gradient(transparent,rgba(8,11,14,.94));",
     ".frame figcaption{position:absolute;left:0;right:0;bottom:0;padding:14px 15px;\n"
     "  background:rgba(8,11,14,.92);"),
    (".pcell .v.cy{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}",
     ".pcell .v.cy{color:var(--acc)}"),
    (".btn::before{content:'';position:absolute;inset:0;background:var(--grad);",
     ".btn::before{content:'';position:absolute;inset:0;background:var(--acc);"),
    (".nav .btn{background:var(--grad);color:var(--ink)!important}",
     ".nav .btn{background:var(--acc);color:var(--ink)!important}"),
    # contact panel was the last sky ramp on the page
    (".c-sky{background:linear-gradient(168deg,var(--sky-2),var(--sky-3) 52%,var(--deep));",
     ".c-sky{background:var(--sky-3);"),
    (".c-sky::after{content:'';position:absolute;right:-24%;bottom:-30%;width:70%;aspect-ratio:1;border-radius:50%;\n"
     "  background:radial-gradient(circle,rgba(255,255,255,.55),transparent 68%)}",
     "/* was a radial bloom; now a flat offset plane, hard-edged */\n"
     ".c-sky::after{content:'';position:absolute;right:-18%;bottom:-22%;width:58%;aspect-ratio:1;\n"
     "  background:var(--sky-2);opacity:.55}"),
    (".play{width:46px;height:46px;border-radius:50%;background:var(--grad);",
     ".play{width:46px;height:46px;border-radius:50%;background:var(--acc);"),
])

# ── direction 3 ──────────────────────────────────────────────────────────────
edit('direction-3-spec-sheet.html', [
    ("  --grad:linear-gradient(135deg,var(--bl),var(--az) 50%,var(--cy));",
     "  /* flat accent: no ramps anywhere in this set */\n  --acc:var(--cy);"),
    ("h1 .u::after{content:'';position:absolute;left:0;right:0;bottom:.07em;height:.07em;background:var(--grad)}",
     "h1 .u::after{content:'';position:absolute;left:0;right:0;bottom:.07em;height:.07em;background:var(--acc)}"),
    (".btn::before{content:'';position:absolute;inset:0;background:var(--grad);translate:0 101%;",
     ".btn::before{content:'';position:absolute;inset:0;background:var(--acc);translate:0 101%;"),
    (".play{width:42px;height:42px;border-radius:50%;background:var(--grad);",
     ".play{width:42px;height:42px;border-radius:50%;background:var(--acc);"),
])

# nothing may still reference the removed token
for n in ('index.html', 'direction-1-pressure.html',
          'direction-2-altitude.html', 'direction-3-spec-sheet.html'):
    left = open(R(n), encoding='utf-8').read().count('var(--grad)')
    assert left == 0, f'{n} still references var(--grad) x{left}'
print('no var(--grad) references remain')
