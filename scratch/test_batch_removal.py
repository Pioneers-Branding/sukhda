import glob
import re

files = glob.glob('*.html') + ['include/footer.html']
print(f"Testing regex across {len(files)} files...")

small_pattern = re.compile(r'^[ \t]*<small>\s*24\*7 Emergency Helpline\s*</small>\r?\n', re.MULTILINE | re.IGNORECASE)
motto_pattern = re.compile(r'^[ \t]*<div class="footer-motto">[\s\S]*?</div>\r?\n?', re.MULTILINE)

mismatches = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Check if this file has footer
    if 'footer-emergency-box' not in c:
        continue
    
    s_matches = list(small_pattern.finditer(c))
    m_matches = list(motto_pattern.finditer(c))
    
    if len(s_matches) != 1 or len(m_matches) != 1:
        mismatches.append((f, len(s_matches), len(m_matches)))

if mismatches:
    print("Files with unexpected match counts:")
    for m in mismatches:
        print(f"  {m[0]}: small={m[1]}, motto={m[2]}")
else:
    print(f"PERFECT! All target files have exactly 1 small match and 1 motto match.")
