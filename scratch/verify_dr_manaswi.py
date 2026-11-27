with open('dr-manaswi-gupta.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("File length:", len(text))
print("Occurrences of 'Manaswi':", len(re.findall(r'manaswi', text, re.I)))
print("Occurrences of 'Hemant':", len(re.findall(r'hemant', text, re.I)))

# Check all occurrences of Hemant to ensure they are ONLY in the colleague card
lines = text.split('\n')
for i, l in enumerate(lines):
    if 'hemant' in l.lower():
        print(f'Line {i+1}: {l.strip()[:100]}')
