files = [
    'doctor.html',
    'index.html',
    'opd-schedule.html',
    'radiodiagnosis-and-imaging.html',
    'sukhda-medpark-hospital.html',
    'assets/js/site-search.js'
]

for p in files:
    try:
        with open(p, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print(f'=== {p} ===')
        for i, line in enumerate(lines):
            if 'priyanka' in line.lower() or 'chhabra' in line.lower() or 'chabra' in line.lower():
                start = max(0, i-2)
                end = min(len(lines), i+8)
                for j in range(start, end):
                    print(f'{j+1}: {lines[j].strip()}')
                print('---')
    except Exception as e:
        print(f'Error reading {p}: {e}')
