import glob
import re

print("=== CHECKING dr-mohan-lal.html ===")
with open('dr-mohan-lal.html', 'r', encoding='utf-8') as f:
    text = f.read()

assert 'Dr. Mohan Lal' in text
assert 'MBBS, MD (Radiation Oncology)' in text
assert '9268421705' in text
assert 'Fellowship in Precision External Beam Radiation Therapy' in text
assert 'MD in Radiation Oncology (Clinical Oncology)' in text
assert 'MBBS – Pt. B. D. Sharma University of Medical Sciences, Rohtak' in text
assert 'assets/images/doctors/latest/dr-mohanlal.webp' in text
print("dr-mohan-lal.html content assertions passed!")

print("\n=== CHECKING ALL FILES LINKING TO dr-mohan-lal.html ===")
linking = []
for p in glob.glob('*.html') + glob.glob('assets/js/*.js'):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if 'dr-mohan-lal.html' in c:
            linking.append(p)

print(f"Total files linking to dr-mohan-lal.html: {len(linking)}")
for l in linking:
    print(f" - {l}")

print("\n=== CHECKING UNLINKED REFERENCES TO MOHAN LAL ===")
for p in glob.glob('*.html'):
    if p == 'dr-mohan-lal.html':
        continue
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if 'mohan lal' in c.lower() and 'dr-mohan-lal.html' not in c:
            print(f"Unlinked reference in: {p}")
print("Check completed successfully!")
