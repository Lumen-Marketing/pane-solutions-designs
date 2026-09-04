# -*- coding: utf-8 -*-
"""Two corrections to the Daylight pass.

1. The ghost numerals were a solid pale fill, and body copy ran across the
   middle of a 3 and a 4. A filled glyph behind text muddies it however low the
   alpha goes. Outlined numerals carry the same weight as a graphic device and
   leave almost nothing behind the words.

2. The FAQ's left column is sticky, so it emptied out into half a screen of
   dead paper once the reader got three questions down. A contained plate fills
   it, and it is a photograph as an object rather than as a ground, so the
   section stays plain.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-1-pressure.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    assert s.count(a) == 1, 'NOT UNIQUE -> %s' % a[:90]
    s = s.replace(a, b)


swap("""  font-size:clamp(6.5rem,12vw,12rem);color:rgba(27,84,200,.11);
  pointer-events:none;user-select:none}""",
"""  font-size:clamp(6.5rem,12vw,12rem);pointer-events:none;user-select:none;
  color:transparent;-webkit-text-stroke:1.6px rgba(27,84,200,.3)}
@supports not ((-webkit-text-stroke:1px red)){
  .how-cell .num{color:rgba(27,84,200,.1);-webkit-text-stroke:0}
}""")

swap("""      <p>If yours is not here, call <a href="tel:+15155254127">515.525.4127</a> and ask. It costs nothing to find out.</p>
    </div>""",
"""      <p>If yours is not here, call <a href="tel:+15155254127">515.525.4127</a> and ask. It costs nothing to find out.</p>
      <figure class="plate faq-shot"><img src="assets/photos/french-doors.webp" alt="Black framed French doors cleaned by Pane Solutions in Phoenix" loading="lazy"></figure>
    </div>""")

swap(""".faq-hd a{color:var(--blue);font-weight:600}""",
""".faq-hd a{color:var(--blue);font-weight:600}
.faq-shot{margin-top:clamp(28px,3.4vw,46px)}
.faq-shot img{aspect-ratio:5/4}""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Daylight: outlined numerals, plate in the sticky FAQ column')
