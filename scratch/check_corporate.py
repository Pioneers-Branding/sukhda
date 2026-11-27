with open('empanelled-corporate.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'ankit' in l.lower() or 'gawri' in l.lower():
        start = max(0, i-2)
        end = min(len(lines), i+8)
        for j in range(start, end):
            print(f'{j+1}: {lines[j].strip()}')
        print('---')
