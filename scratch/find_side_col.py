with open('dr-hemant-dahiya.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'<div class="doc-main-col">[\s\S]*?(<div class="doc-side-col">[\s\S]*?</div>\s*</div>\s*</div>\s*</section>)', text)
if match:
    print('Found doc-side-col!')
    print(match.group(1)[:400])
else:
    print('Could not find doc-side-col')
