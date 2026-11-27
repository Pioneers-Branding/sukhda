with open('dr-hemant-dahiya.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sidebar = re.search(r'<!-- SIDEBAR / APPOINTMENT BOOKING COLUMN -->[\s\S]*?</aside>', text)
if sidebar:
    print('Sidebar found, length:', len(sidebar.group(0)))
    print(sidebar.group(0)[:500])
else:
    print('No sidebar match')

colleague_section = re.search(r'<section class="section" style="background:#f8fafc;[\s\S]*?</section>', text)
if colleague_section:
    print('Colleague section found, length:', len(colleague_section.group(0)))
