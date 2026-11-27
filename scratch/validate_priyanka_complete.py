import glob
import re

print("=== CHECKING dr-priyanka-chhabra.html ===")
with open('dr-priyanka-chhabra.html', 'r', encoding='utf-8') as f:
    text = f.read()

assert 'Dr. Priyanka Chhabra' in text
assert 'MBBS, DMRD, EDiR, DICRI' in text
assert '9466638426' in text or '94666' in text
assert 'MBA (Hospital Administration &amp; Healthcare Management) – DY Patil, Pune (2022)' in text or 'MBA (Hospital Administration' in text
assert 'EDiR (European Diploma in Radiology) – ESR (2020)' in text
assert 'DICRI – IRIA (2020)' in text
assert 'DMRD – PGIMS, Rohtak (2005)' in text
assert 'MBBS – JLN Medical College, Ajmer (2002)' in text
assert 'assets/images/doctors/latest/dr-priyanka-chabra.webp' in text
print("dr-priyanka-chhabra.html assertions passed!")

print("\n=== CHECKING ALL FILES LINKING TO dr-priyanka-chhabra.html ===")
linking = []
for p in glob.glob('*.html') + glob.glob('assets/js/*.js'):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if 'dr-priyanka-chhabra.html' in c:
            linking.append(p)

print(f"Total files linking to dr-priyanka-chhabra.html: {len(linking)}")
for l in linking:
    print(f" - {l}")

print("\n=== CHECKING UNLINKED REFERENCES TO PRIYANKA CHHABRA ===")
for p in glob.glob('*.html'):
    if p == 'dr-priyanka-chhabra.html':
        continue
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if ('priyanka chhabra' in c.lower() or 'priyanka chabra' in c.lower()) and 'dr-priyanka-chhabra.html' not in c:
            print(f"Unlinked reference in: {p}")
print("Check completed successfully!")
