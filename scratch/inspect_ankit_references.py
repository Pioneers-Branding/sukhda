import glob

files = [
    'doctor.html',
    'index.html',
    'opd-schedule.html',
    'orthopaedic-and-robotic-joint-replacement.html',
    'sukhda-multispecialty-hospital.html',
    'assets/js/site-search.js'
]

for p in files:
    try:
        with open(p, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print(f'=== {p} ===')
        for i, line in enumerate(lines):
            if 'ankit' in line.lower() or 'gawri' in line.lower():
                start = max(0, i-2)
                end = min(len(lines), i+8)
                for j in range(start, end):
                    print(f'{j+1}: {lines[j].strip()}')
                print('---')
    except Exception as e:
        print(f'Error reading {p}: {e}')
