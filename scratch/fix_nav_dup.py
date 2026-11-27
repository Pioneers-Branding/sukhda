import glob

files = glob.glob('*.html')
dup_target = """                            <a href="about.html#timeline">Our Journey / Timeline</a>
                            <a href="about.html#timeline">Our Journey / Timeline</a>"""
single_target = """                            <a href="about.html#timeline">Our Journey / Timeline</a>"""

fixed = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if dup_target in c:
        c = c.replace(dup_target, single_target)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        fixed.append(f)

print(f"Fixed duplicates in {len(fixed)} files: {fixed}")
