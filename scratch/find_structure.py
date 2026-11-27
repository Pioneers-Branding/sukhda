with open('dr-hemant-dahiya.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'doc-main-col' in l or 'doc-layout' in l or 'appointment' in l.lower() or 'colleague' in l.lower():
        print(f'{i+1}: {l.strip()[:80]}')
