with open('about.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
items = re.findall(r'<div class="timeline-item">.*?<h3 class="timeline-title">(.*?)</h3>', text, re.DOTALL)
print(f'Total timeline items found: {len(items)}')
for i, item in enumerate(items, 1):
    print(f'  {i}. {item.strip()}')

# Check section tags
idx_start = text.find('<section class="section" id="timeline"')
idx_end = text.find('</section>', idx_start) + len('</section>')
section_content = text[idx_start:idx_end]

opens = re.findall(r'<([a-zA-Z0-9]+)(?:\s+[^>]*?)?>', section_content)
closes = re.findall(r'</([a-zA-Z0-9]+)>', section_content)
self_closing = {'img', 'br', 'hr', 'input', 'meta', 'link'}
non_self_opens = [t.lower() for t in opens if t.lower() not in self_closing]
non_self_closes = [t.lower() for t in closes]
print(f'Total non-self opens: {len(non_self_opens)}, closes: {len(non_self_closes)}')
has_mismatch = False
for t in sorted(set(non_self_opens + non_self_closes)):
    o_c = non_self_opens.count(t)
    c_c = non_self_closes.count(t)
    if o_c != c_c:
        print(f'Tag mismatch for <{t}>: open={o_c}, close={c_c}')
        has_mismatch = True

if not has_mismatch:
    print('ALL HTML TAGS PERFECTLY BALANCED!')
