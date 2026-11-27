with open('opd-schedule.html', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'Dr\. Manaswi Gupta[\s\S]*?</tr>', text)
if m:
    print("In opd-schedule.html:")
    print(m.group(0))

with open('doctor.html', encoding='utf-8') as f:
    text2 = f.read()
m2 = re.search(r'data-name="dr\. manaswi gupta"[\s\S]*?</article>', text2)
if m2:
    print("In doctor.html:")
    print(m2.group(0))
