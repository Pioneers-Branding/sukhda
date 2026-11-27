with open('dr-amit-kumar-garg.html', 'r', encoding='utf-8') as f:
    c1 = f.read()
with open('dr-manaswi-gupta.html', 'r', encoding='utf-8') as f:
    c2 = f.read()

import re
def get_timeline_css(html):
    m = re.findall(r'(\.timeline[^{]*\{[^}]*\})', html)
    return m

css1 = get_timeline_css(c1)
css2 = get_timeline_css(c2)

print("CSS in dr-amit-kumar-garg.html:")
for s in css1:
    print(" ", s.strip().replace('\n', ' '))

print("\nCSS in dr-manaswi-gupta.html:")
for s in css2:
    print(" ", s.strip().replace('\n', ' '))
