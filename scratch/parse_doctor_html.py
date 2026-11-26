from bs4 import BeautifulSoup

soup = BeautifulSoup(open('doctor.html', encoding='utf-8'), 'html.parser')
cards = soup.select('.doc-card')
for i, c in enumerate(cards):
    name = c.select_one('.doc-card-name').get_text(strip=True)
    desig = c.select_one('.doc-card-desig').get_text(strip=True) if c.select_one('.doc-card-desig') else ''
    qual = c.select_one('.doc-card-qual').get_text(strip=True) if c.select_one('.doc-card-qual') else ''
    spec = c.get('data-speciality', '')
    btn = c.select_one('.doc-card-actions a')
    url = btn.get('href', '') if btn else ''
    print(f'{i+1}. name="{name}" | desig="{desig}" | qual="{qual}" | spec="{spec}" | url="{url}"')
