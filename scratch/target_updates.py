from bs4 import BeautifulSoup
import glob

files = sorted(glob.glob('*.html'))

doctor_map = {
    'manaswi': ('Dr. Manaswi Gupta', 'assets/images/doctors/latest/dr-manaswi-gupta.webp'),
    'sumit': ('Dr. Sumit Grover', 'assets/images/doctors/latest/dr-sumit-grover.webp'),
    'nikita': ('Dr. Nitika Grover', 'assets/images/doctors/latest/dr-nikita-grover.webp'),
    'nitika': ('Dr. Nitika Grover', 'assets/images/doctors/latest/dr-nikita-grover.webp'),
    'ankit': ('Dr. Ankit Gawri', 'assets/images/doctors/latest/dr-ankit-gawri.webp'),
    'priyanka': ('Dr. Priyanka Chhabra', 'assets/images/doctors/latest/dr-priyanka-chabra.webp'),
    'mohan lal': ('Dr. Mohan Lal', 'assets/images/doctors/latest/dr-mohanlal.webp'),
    'mohanlal': ('Dr. Mohan Lal', 'assets/images/doctors/latest/dr-mohanlal.webp'),
}

exact_updates = []

for f in files:
    content = open(f, encoding='utf-8').read()
    if 'unknown-doctor.webp' not in content:
        continue
    soup = BeautifulSoup(content, 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if 'unknown-doctor.webp' not in src:
            continue
        
        # Check text in card or article
        card = img.find_parent(['article', 'div', 'a', 'li'])
        card_text = card.get_text(separator=' ', strip=True) if card else ""
        alt = img.get('alt', '')
        search_str = (alt + " " + card_text).lower()
        
        matched_doc = None
        for k, (dname, new_img) in doctor_map.items():
            if k in search_str:
                matched_doc = (dname, new_img)
                break
        
        if matched_doc:
            exact_updates.append({
                'file': f,
                'doctor': matched_doc[0],
                'new_img': matched_doc[1],
                'old_tag': str(img),
                'alt': alt
            })
        else:
            print(f"UNKNOWN DOC NOT MATCHED: {f} -> alt='{alt}' text='{card_text[:100]}'")

print(f"\nTotal targets to update: {len(exact_updates)}")
for u in exact_updates:
    print(f"{u['file']}: {u['doctor']} -> {u['new_img']}")
