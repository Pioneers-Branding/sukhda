import glob
import re

print("=== CHECKING dr-sumit-grover.html ===")
with open('dr-sumit-grover.html', 'r', encoding='utf-8') as f:
    text = f.read()

assert 'Dr. Sumit Grover' in text
assert 'MBBS, D.A. (Anaesthesiology)' in text
assert '7015380751' in text
assert 'Diploma in Anaesthesia – Himalayan Institute of Medical Sciences' in text
assert 'MBBS – Tribhuvan University (2010)' in text
assert 'Senior Secondary (CBSE) – Hisar, Haryana (2001)' in text
assert 'Secondary (CBSE) – Hisar, Haryana (1999)' in text
assert 'assets/images/doctors/latest/dr-sumit-grover.webp' in text
print("dr-sumit-grover.html content assertions passed!")

print("\n=== CHECKING ALL FILES LINKING TO dr-sumit-grover.html ===")
linking = []
for p in glob.glob('*.html') + glob.glob('assets/js/*.js'):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if 'dr-sumit-grover.html' in c:
            linking.append(p)

print(f"Total files linking to dr-sumit-grover.html: {len(linking)}")
for l in linking:
    print(f" - {l}")

print("\n=== CHECKING UNLINKED REFERENCES TO SUMIT GROVER ===")
for p in glob.glob('*.html'):
    if p == 'dr-sumit-grover.html':
        continue
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if 'sumit grover' in c.lower() and 'dr-sumit-grover.html' not in c:
            print(f"Unlinked reference in: {p}")
print("Check completed successfully!")
