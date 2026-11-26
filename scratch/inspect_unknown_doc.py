import glob, re

files = sorted(glob.glob('*.html'))

doctors_to_update = {
    'dr-manaswi-gupta': 'assets/images/doctors/latest/dr-manaswi-gupta.webp',
    'dr-sumit-grover': 'assets/images/doctors/latest/dr-sumit-grover.webp',
    'dr-nikita-grover': 'assets/images/doctors/latest/dr-nikita-grover.webp',
    'dr-ankit-gawri': 'assets/images/doctors/latest/dr-ankit-gawri.webp',
    'dr-priyanka-chhabra': 'assets/images/doctors/latest/dr-priyanka-chabra.webp',
    'dr-mohanlal': 'assets/images/doctors/latest/dr-mohanlal.webp'
}

for f in files:
    content = open(f, encoding='utf-8').read()
    # Check lines with unknown-doctor.webp
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'unknown-doctor.webp' in line:
            # show surrounding lines
            start = max(0, i - 5)
            end = min(len(lines), i + 6)
            block = '\n'.join(lines[start:end])
            print(f"=== {f}:{i+1} ===")
            print(block)
            print("-" * 50)
