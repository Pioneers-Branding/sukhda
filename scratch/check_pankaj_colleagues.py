with open('dr-pankaj-sharma.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
colleagues = re.search(r'<div class="other-docs-grid">[\s\S]*?</div>\s*</div>\s*</section>', text)
if colleagues:
    print(colleagues.group(0)[:800])
