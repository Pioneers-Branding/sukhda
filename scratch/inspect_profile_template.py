with open('dr-hemant-dahiya.html', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '<div class="doc-page-layout">' in l:
        print(f"HTML body doc-page-layout starts at line {i+1}")
        for j in range(i, min(len(lines), i + 250)):
            print(lines[j], end='')
        break
