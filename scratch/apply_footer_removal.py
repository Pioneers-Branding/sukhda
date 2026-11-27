import glob
import re

files = glob.glob('*.html') + ['include/footer.html']
print(f"Applying removals across {len(files)} files...")

small_pattern = re.compile(r'^[ \t]*<small>\s*24\*7 Emergency Helpline\s*</small>\r?\n', re.MULTILINE | re.IGNORECASE)
motto_pattern = re.compile(r'^[ \t]*<div class="footer-motto">[\s\S]*?</div>\r?\n?', re.MULTILINE)

modified_files = []

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    if 'footer-emergency-box' not in c:
        continue
    
    c_new = small_pattern.sub('', c)
    c_new = motto_pattern.sub('', c_new)
    
    if c_new != c:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c_new)
        modified_files.append(f)

print(f"Successfully modified {len(modified_files)} files.")
