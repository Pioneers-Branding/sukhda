import glob
import re

print("=== CHECKING dr-ankit-gawri.html ===")
with open('dr-ankit-gawri.html', 'r', encoding='utf-8') as f:
    text = f.read()

assert 'Dr. Ankit Gawri' in text
assert 'MBBS, MS (Orthopaedics), FNB (Arthroplasty)' in text
assert '8168394634' in text
assert 'FNB Arthroplasty (2024–2026) (From Aadhar Hospital Hisar)' in text
assert 'MS Orthopaedics – Government Medical College, Aurangabad (2019–2022)' in text
assert 'MBBS – SDM Medical College, Dharwad (2017)' in text
assert 'assets/images/doctors/latest/dr-ankit-gawri.webp' in text
print("dr-ankit-gawri.html content assertions passed!")

print("\n=== CHECKING ALL FILES LINKING TO dr-ankit-gawri.html ===")
linking = []
for p in glob.glob('*.html') + glob.glob('assets/js/*.js'):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if 'dr-ankit-gawri.html' in c:
            linking.append(p)

print(f"Total files linking to dr-ankit-gawri.html: {len(linking)}")
for l in linking:
    print(f" - {l}")

print("\n=== CHECKING UNLINKED REFERENCES TO ANKIT GAWRI ===")
for p in glob.glob('*.html'):
    if p == 'dr-ankit-gawri.html':
        continue
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if 'ankit gawri' in c.lower() and 'dr-ankit-gawri.html' not in c:
            print(f"Unlinked reference in: {p}")
print("Check completed successfully!")
