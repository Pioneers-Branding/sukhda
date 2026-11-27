import glob

target = """                            <a href="about.html">About Sukhda</a>
                            <a href="about.html#leadership">Leadership</a>
                            <a href="about.html#vision">Vision &amp; Mission</a>"""

replacement = """                            <a href="about.html">About Sukhda</a>
                            <a href="about.html#leadership">Leadership</a>
                            <a href="about.html#vision">Vision &amp; Mission</a>
                            <a href="about.html#timeline">Our Journey / Timeline</a>"""

files = glob.glob('*.html')
updated = []
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if target in content:
        content = content.replace(target, replacement)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        updated.append(file)

print(f"Updated {len(updated)} files with timeline in About Us nav dropdown.")
print("Updated files:", updated[:10])
