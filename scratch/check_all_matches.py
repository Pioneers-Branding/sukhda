import glob
import re

files = glob.glob('*.html') + glob.glob('include/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    m = re.findall(r'<a\s+href="about\.html"[^>]*>\s*About Sukhda\s*</a>', c, re.IGNORECASE)
    if m:
        print(f, len(m))
    else:
        print("NO MATCH:", f)
