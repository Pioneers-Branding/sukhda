with open('dr-ankit-gawri.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("File length:", len(text))
print("Occurrences of 'Ankit':", len(re.findall(r'ankit', text, re.I)))
print("Occurrences of 'Manaswi':", len(re.findall(r'manaswi', text, re.I)))

lines = text.split('\n')
for i, l in enumerate(lines):
    if 'manaswi' in l.lower():
        print(f'Line {i+1}: {l.strip()[:100]}')
