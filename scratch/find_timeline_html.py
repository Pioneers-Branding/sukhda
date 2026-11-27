with open('about.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<[^>]*class="[^"]*timeline[^"]*"[^>]*>', text)
print('HTML elements with timeline class in about.html:', len(matches))
for m in matches:
    print(m)
