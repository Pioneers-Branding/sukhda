from bs4 import BeautifulSoup

soup = BeautifulSoup(open('opd-schedule.html', encoding='utf-8'), 'html.parser')
rows = soup.select('.opd-table tbody tr, .opd-row, .opd-card')
print(f"Found {len(rows)} rows/cards")
for r in rows:
    texts = list(r.stripped_strings)
    print(texts[:4])
