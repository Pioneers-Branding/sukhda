with open('dr-hemant-dahiya.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
schema = re.search(r'<script type="application/ld\+json">[\s\S]*?</script>', text)
if schema:
    print(schema.group(0))
