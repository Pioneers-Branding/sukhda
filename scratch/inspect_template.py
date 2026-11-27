with open('dr-hemant-dahiya.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
titles = re.findall(r'<article class="content-card">[\s\S]*?<h3>(.*?)</h3>', text)
print('Content card titles in dr-hemant-dahiya.html:')
for t in titles:
    print(' -', t)

sections = re.findall(r'<section class="([^"]*)">', text)
print('Sections:', sections)
