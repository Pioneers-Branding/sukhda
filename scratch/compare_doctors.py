from bs4 import BeautifulSoup
import os

user_list = [
    ('Dr. Amit Mehta', 'dr-amit-mehta.html'),
    ('Dr. Manisha Mehta', 'dr-manisha-mehta.html'),
    ('Dr. Amit Kumar Garg', 'dr-amit-kumar-garg.html'),
    ('Dr. Anil Bansal', 'dr-anil-bansal.html'),
    ('Dr. Anil Khyalia', 'dr-anil-khyalia.html'),
    ('Dr. Ankur Kamra', 'dr-ankur-kamra.html'),
    ('Dr. Bharath', 'dr-bharath.html'),
    ('Dr. Deepam Das', 'dr-deepam-das.html'),
    ('Dr. Deepti Singh', 'dr-deepti-singh.html'),
    ('Dr. Devilal', 'dr-devilal.html'),
    ('Dr. Hemant Dahiya', 'dr-hemant-dahiya.html'),
    ('Dr. Megha Gupta', 'dr-megha-gupta.html'),
    ('Dr. Nidhi Mehta', 'dr-nidhi-mehta.html'),
    ('Dr. Pankaj Sharma', 'dr-pankaj-sharma.html'),
    ('Dr. Parveen', 'dr-parveen.html'),
    ('Dr. Sanjeet Sahu', 'dr-sanjeet-sahu.html'),
    ('Dr. Shubham Mehta', 'dr-shubham-mehta.html'),
    ('Dr. Trivikrama Rao', 'dr-trivikrama-rao.html'),
]

soup = BeautifulSoup(open('doctor.html', encoding='utf-8'), 'html.parser')
doc_cards = {}
for c in soup.select('.doc-card'):
    name_el = c.select_one('.doc-card-name')
    name = name_el.get_text(strip=True) if name_el else ''
    desig_el = c.select_one('.doc-card-desig')
    desig = desig_el.get_text(strip=True) if desig_el else ''
    qual_el = c.select_one('.doc-card-qual')
    qual = qual_el.get_text(strip=True) if qual_el else ''
    spec = c.get('data-speciality', '')
    btn = c.select_one('.doc-card-actions a')
    url = btn.get('href', '') if btn else ''
    doc_cards[name.lower()] = {
        'name': name,
        'desig': desig,
        'qual': qual,
        'spec': spec,
        'url': url
    }

print("=== USER LIST COMPARISON ===")
for name, url in user_list:
    found = None
    for k, v in doc_cards.items():
        if name.lower() in k or k in name.lower():
            found = v
            break
    if found:
        print(f"MATCH: {name}")
        print(f"  In doctor.html: name={found['name']}, desig={found['desig']}, qual={found['qual']}, spec={found['spec']}, url={found['url']}")
    else:
        print(f"NOT FOUND in doctor.html: {name} (url: {url})")
        # Check if individual page exists
        if os.path.exists(url):
            doc_soup = BeautifulSoup(open(url, encoding='utf-8'), 'html.parser')
            h1 = doc_soup.find('h1')
            h1_text = h1.get_text(strip=True) if h1 else ''
            role = doc_soup.find(class_='doc-role')
            role_text = role.get_text(strip=True) if role else ''
            deg = doc_soup.find(class_='doc-degrees')
            deg_text = deg.get_text(strip=True) if deg else ''
            dept = doc_soup.find(class_='pill-dept-link')
            dept_text = dept.get_text(strip=True) if dept else ''
            print(f"  From {url}: h1={h1_text}, role={role_text}, degrees={deg_text}, dept={dept_text}")

print("\n=== ALL DOCTORS IN DOCTOR.HTML ===")
for k, v in doc_cards.items():
    print(f"{v['name']} | {v['desig']} | {v['qual']} | {v['url']}")
