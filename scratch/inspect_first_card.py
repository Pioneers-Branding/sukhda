with open('medicine-and-critical-care.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
cards = re.findall(r'<article class="hd-card">[\s\S]*?</article>', text)
print(f'Total hd-cards: {len(cards)}')
if len(cards) > 0:
    print('First card:\n', cards[0])
