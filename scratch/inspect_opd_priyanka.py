with open('opd-schedule.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'priyanka' in l.lower():
        start = max(0, i-3)
        end = min(len(lines), i+30)
        for j in range(start, end):
            print(f'{j+1}: {repr(lines[j])}')
        break
