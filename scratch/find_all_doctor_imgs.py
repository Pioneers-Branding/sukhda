from bs4 import BeautifulSoup
import glob, re

files = sorted(glob.glob('*.html'))

doctor_keys = [
    'manaswi',
    'sumit',
    'nikita',
    'nitika',
    'ankit',
    'priyanka',
    'mohan lal',
    'mohanlal'
]

found = []

for f in files:
    soup = BeautifulSoup(open(f, encoding='utf-8'), 'html.parser')
    for img in soup.find_all('img'):
        parent = img.parent
        # check parent or ancestor up to 4 levels
        ancestors_text = ""
        curr = img
        for _ in range(4):
            if curr.parent:
                curr = curr.parent
                ancestors_text += " " + curr.get_text(separator=' ', strip=True)
        
        alt = img.get('alt', '')
        src = img.get('src', '')
        combined = (alt + " " + ancestors_text).lower()
        
        for k in doctor_keys:
            if k in combined:
                found.append({
                    'file': f,
                    'key': k,
                    'src': src,
                    'alt': alt
                })

print(f"Total img contexts found: {len(found)}")
for x in found:
    print(f"{x['file']}: src='{x['src']}' alt='{x['alt']}' (key: {x['key']})")
