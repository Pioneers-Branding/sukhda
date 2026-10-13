import re

with open('doctor.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<header class="nav">([\s\S]*?)</header>', text)
if m:
    print("Found header. Length:", len(m.group(0)))
    for line in m.group(0).splitlines():
        line_s = line.strip()
        if any(k in line_s for k in ['<a href', 'nav-group', 'mobile-nav-links', 'btn primary']):
            print(line_s[:100])
else:
    print("NO HEADER FOUND!")
