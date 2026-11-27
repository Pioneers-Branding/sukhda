import glob
import re

for p in sorted(glob.glob('dr-*.html')):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.search(r'<div class="timeline">([\s\S]*?)</div>\s*</article>', c)
    if m:
        print(f'=== {p} ===')
        items = re.findall(r'<div class="timeline-item">([\s\S]*?)</div>', m.group(1))
        for it in items:
            clean = ' '.join(it.split())
            print('  item:', clean)
