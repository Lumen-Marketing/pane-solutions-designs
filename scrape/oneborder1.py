# -*- coding: utf-8 -*-
"""Daylight gets the same single border Facade just got.

The tray plus core version drew a hairline on the outside and a second one
seven pixels in. On Facade that read as a double ring and got called out; the
same thing is happening here, only paler. The fill moves up onto the pane so
the type stays readable over a photograph, and the core keeps nothing but its
padding. isolation:isolate comes off at the same time: it opens a stacking
context, which stops backdrop-filter from ever seeing the photograph it is
meant to be blurring.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-1-pressure.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    s = s.replace(a, b)


swap("""   A single flat card cannot read as an object however much shadow you give it.
   The tray is thin, translucent and blurred; the core sits inside it with its
   own fill and its own lit rim, and its radius is the tray's minus the tray's
   padding so the two curves stay concentric.
""",
"""   A single flat card cannot read as an object however much shadow you give it.
   ONE slab, ONE hairline: the fill and the rim live on the pane, and the core
   carries nothing but its padding. Two concentric hairlines seven pixels apart
   read as a mistake rather than as machining.
""")

swap(""".pane{
  position:relative;isolation:isolate;
  padding:var(--tray);
  border-radius:var(--r);
  background:rgba(255,255,255,.3);
  backdrop-filter:blur(30px) saturate(170%);
  -webkit-backdrop-filter:blur(30px) saturate(170%);
  border:1px solid rgba(255,255,255,.55);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.9),
             0 1px 2px rgba(20,36,56,.06),
             0 14px 30px rgba(20,36,56,.13),
             0 44px 84px rgba(20,36,56,.16);
}
.core{
  position:relative;height:100%;
  border-radius:calc(var(--r) - var(--tray));
  background:rgba(255,255,255,.72);
  border:1px solid rgba(255,255,255,.8);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.98),
             inset 0 -1px 0 rgba(255,255,255,.4);
}
@media(prefers-reduced-transparency:reduce){
  .pane{background:#E6EBEF;backdrop-filter:none;-webkit-backdrop-filter:none}
  .core{background:#FBFCFD}
}""",
""".pane{
  position:relative;
  padding:var(--tray);
  border-radius:var(--r);
  background:rgba(255,255,255,.78);
  backdrop-filter:blur(30px) saturate(170%);
  -webkit-backdrop-filter:blur(30px) saturate(170%);
  border:1px solid rgba(255,255,255,.7);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.98),
             inset 0 -1px 0 rgba(255,255,255,.45),
             0 1px 2px rgba(20,36,56,.06),
             0 14px 30px rgba(20,36,56,.13),
             0 44px 84px rgba(20,36,56,.16);
}
.core{position:relative;height:100%;border-radius:calc(var(--r) - var(--tray))}
@media(prefers-reduced-transparency:reduce){
  .pane{background:#F4F7F9;backdrop-filter:none;-webkit-backdrop-filter:none}
}""")

swap("  --tray:7px;      /* tray padding. The core's radius is --r minus this. */",
     "  --tray:0px;      /* kept as a variable so the radius maths still reads. */")

io.open(p, 'w', encoding='utf-8').write(s)
print('Daylight: one border, one rim, no isolation trap')
