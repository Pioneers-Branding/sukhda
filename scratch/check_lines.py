with open('dr-manaswi-gupta.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'Dr. Manaswi Gupta' in l:
        print(f'{i+1}: {l.strip()[:100]}')
