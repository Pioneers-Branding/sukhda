import glob
import re

files = glob.glob('*.html') + ['include/footer.html']

remaining_mottos = []
remaining_small = []

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    if 'footer-motto' in c:
        # Check if the class is used in HTML (not just CSS)
        if re.search(r'<div class="footer-motto"', c):
            remaining_mottos.append(f)
            
    if re.search(r'<small>\s*24\*7 Emergency Helpline\s*</small>', c, re.IGNORECASE):
        remaining_small.append(f)

print(f"Remaining HTML footer-motto elements: {len(remaining_mottos)}")
if remaining_mottos:
    print("Files with remaining motto:", remaining_mottos)

print(f"Remaining HTML small 24/7 Emergency Helpline elements: {len(remaining_small)}")
if remaining_small:
    print("Files with remaining small helpline:", remaining_small)

if not remaining_mottos and not remaining_small:
    print("VERIFICATION SUCCESS: All targeted texts and elements removed cleanly across all 63 files!")
