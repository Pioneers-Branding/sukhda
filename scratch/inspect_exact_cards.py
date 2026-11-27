files = ['medicine-and-critical-care.html', 'sukhda-multispecialty-hospital.html', 'sukhda-medpark-hospital.html']
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f'=== {path} ===')
    for i, line in enumerate(lines):
        if 'manaswi' in line.lower():
            start = max(0, i-5)
            end = min(len(lines), i+15)
            for j in range(start, end):
                print(f'{j+1}: {repr(lines[j])}')
            break
