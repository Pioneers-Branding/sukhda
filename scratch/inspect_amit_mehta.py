with open('dr-amit-mehta.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
schema = re.search(r'<script type="application/ld\+json">[\s\S]*?</script>', text)
if schema:
    print('Schema in dr-amit-mehta.html:')
    print(schema.group(0)[:600])
else:
    print('No schema in dr-amit-mehta.html')
