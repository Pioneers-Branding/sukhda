import glob
import re

files = glob.glob('*.html')
print(f"Scanning {len(files)} files...")

counts_motto = 0
counts_small = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    motto_matches = list(re.finditer(r'<div class="footer-motto">[\s\S]*?</div>', c))
    small_matches = list(re.finditer(r'<small>\s*24\*7 Emergency Helpline\s*</small>', c, re.IGNORECASE))
    
    counts_motto += len(motto_matches)
    counts_small += len(small_matches)
    if len(motto_matches) == 0:
        print(f"File {f} has 0 motto matches")
    if len(small_matches) == 0:
        print(f"File {f} has 0 small matches")

print(f"Total motto matches: {counts_motto}")
print(f"Total small emergency helpline matches: {counts_small}")
