import glob
import re

files = glob.glob('*.html')
patterns_helpline = set()
patterns_motto = set()

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # footer-emergency-box small
    m1 = re.findall(r'<small>[^<]*Emergency Helpline[^<]*</small>', c, re.IGNORECASE)
    for match in m1:
        patterns_helpline.add(match)
    
    # footer-motto
    m2 = re.findall(r'<div class="footer-motto">.*?</div>', c, re.DOTALL)
    for match in m2:
        norm = re.sub(r'\s+', ' ', match)
        patterns_motto.add(norm)

print("Unique helpline small patterns:")
for p in patterns_helpline:
    print(" ", repr(p))

print("Unique footer-motto patterns:")
for p in patterns_motto:
    print(" ", repr(p))
