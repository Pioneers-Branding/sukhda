import glob
import re

files = glob.glob('*.html') + glob.glob('include/*.html')
matches = []
exact_matches = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    m = re.findall(r'<a\s+href="about\.html"[^>]*>\s*About Sukhda\s*</a>', c, re.IGNORECASE)
    if m:
        matches.append((f, len(m), m))
        
    m2 = re.findall(r'About Sukhda', c)
    if m2:
        exact_matches.append((f, len(m2)))

print(f"Total files with <a href='about.html'>About Sukhda</a>: {len(matches)}")
for f, count, m_list in matches[:5]:
    print(f"  {f}: {count} occurrences -> {m_list}")

print(f"Total files with 'About Sukhda': {len(exact_matches)}")
