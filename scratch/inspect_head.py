with open('dr-hemant-dahiya.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
head = text[:text.find('</head>') + 7]
print(head[:1500])
