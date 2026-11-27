import glob
import re

files = glob.glob('*.html') + glob.glob('include/*.html')
variations = set()

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    matches = re.findall(r'<a[^>]*href=["\']about\.html["\'][^>]*>[\s\S]*?</a>', c, re.IGNORECASE)
    for m in matches:
        if 'about sukhda' in m.lower():
            variations.add(m)

print("Unique variations found:")
for v in variations:
    print(" ", repr(v))
