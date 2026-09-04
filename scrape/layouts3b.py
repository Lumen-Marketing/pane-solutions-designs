# -*- coding: utf-8 -*-
"""Three corrections to the Facade pass.

1. The photograph in the why grid was setting the row height. Its natural 3:4
   at five twelfths of the page is 780px tall, so the text card beside it
   stretched to match and carried 500px of empty glass. Absolutely positioning
   the image inside the figure hands the row height back to the type.

2. Rail headings run to two or three lines, so the copy under them started at
   three different heights. Three lines reserved on all four.

3. Five nav links plus a phone plus a button no longer fit this nav, and
   Why us wrapped onto a second line inside the pill. Four links, and they no
   longer wrap.
"""
import io
import os

p = os.path.join(os.path.dirname(__file__), '..', 'direction-3-spec-sheet.html')
s = io.open(p, encoding='utf-8').read()


def swap(a, b):
    global s
    assert a in s, 'NO MATCH -> %s' % a[:90]
    assert s.count(a) == 1, 'NOT UNIQUE -> %s' % a[:90]
    s = s.replace(a, b)


# 1. the photo must not drive the row
swap(""".why-shot{position:relative;overflow:hidden;border-radius:var(--r);""",
""".why-shot{position:relative;overflow:hidden;border-radius:var(--r);
  min-height:clamp(230px,21vw,300px);""")

swap(""".why-shot img{display:block;width:100%;height:100%;min-height:230px;object-fit:cover}""",
"""/* absolute, so the figure has no intrinsic height and the row is sized by the
   type beside it. Left in flow this photograph is 3:4 at 5 columns wide, which
   is 780px, and the card next to it stretched to match. */
.why-shot img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}""")

swap("""@media(max-width:900px){
  .why-a,.why-b,.why-c,.why-d{grid-column:span 12}
  .why-shot img{min-height:220px}
}""",
"""@media(max-width:900px){
  .why-a,.why-b,.why-c,.why-d{grid-column:span 12}
  .why-shot{min-height:clamp(210px,42vw,300px)}
}""")

# 2. rail headings on one baseline
swap("""  letter-spacing:-.01em;max-width:15ch;min-height:2.3em}""",
"""  letter-spacing:-.01em;max-width:15ch;
  /* three lines reserved on every tile, so the four paragraphs under them all
     start on the same line rather than stepping down the row */
  min-height:3.2em}""")

swap("""  .rail::before{display:none}
  .step-tile h3{min-height:0}""",
"""  .rail::before{display:none}
  .step-tile h3{min-height:2.2em}""")

# 3. the nav no longer fits five
swap("""    <a href="#services">Services</a><a href="#how">Process</a><a href="#why">Why us</a><a href="#work">Work</a><a href="#faq">FAQ</a>
  </div>""",
"""    <a href="#services">Services</a><a href="#why">Why us</a><a href="#work">Work</a><a href="#faq">FAQ</a>
  </div>""")

swap(""".nav-links a{""", """.nav-links a{white-space:nowrap;""")

io.open(p, 'w', encoding='utf-8').write(s)
print('Facade: row height back to the type, rail baselines, nav fits')
