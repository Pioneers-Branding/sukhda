import glob
import re

files = glob.glob('*.html')
print(f"Scanning {len(files)} files...")

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # check if footer has footer-motto
    motto_matches = list(re.finditer(r'<div class="footer-motto">[\s\S]*?</div>', c))
    # check if footer has small with emergency helpline
    small_matches = list(re.finditer(r'<small>\s*24\*7 Emergency Helpline\s*</small>', c, re.IGNORECASE))
    
    if not motto_matches and 'footer' in c:
        print(f"{f}: NO footer-motto found!")
    if not small_matches and 'footer' in c:
        print(f"{f}: NO small emergency helpline found!")

print("Scan complete.")
