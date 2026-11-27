import glob
import re

files = glob.glob('*.html') + glob.glob('include/*.html')
print(f"Checking {len(files)} files...")

target = '<a href="about.html">About Sukhda</a>'
replacement = '<a href="about.html">About Sukhda Healthcare</a>'

updated_files = []

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    if target in c:
        c_new = c.replace(target, replacement)
        
        # If in include/header.html, also ensure timeline is in nav-drop
        if f.replace('\\', '/') == 'include/header.html':
            if 'about.html#timeline' not in c_new:
                c_new = c_new.replace(
                    '<a href="about.html#vision">Vision &amp; Mission</a>',
                    '<a href="about.html#vision">Vision &amp; Mission</a>\n                        <a href="about.html#timeline">Our Journey / Timeline</a>'
                )
        
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c_new)
        updated_files.append(f)

print(f"Updated {len(updated_files)} files with 'About Sukhda Healthcare'.")
