import re

pages = [
    'cardiology.html',
    'gastroenterology.html',
    'laparoscopic-and-general-surgery.html',
    'gynaecology-and-obstetrics.html',
    'nephrology-and-dialysis.html',
    'neurosurgery-and-spine.html',
    'orthopaedic-and-robotic-joint-replacement.html'
]

for p in pages:
    c = open(p, encoding='utf-8').read()
    hero_m = re.search(r'<div class="hero-media">[\s\S]*?</div>\s*</div>', c)
    intro_m = re.search(r'<div class="intro-media">[\s\S]*?</div>\s*</div>', c)
    print(f"=== {p} ===")
    if hero_m:
        print("  Hero:", hero_m.group(0).strip())
    else:
        print("  Hero: NOT FOUND")
    if intro_m:
        print("  Intro:", intro_m.group(0).strip())
    else:
        print("  Intro: NOT FOUND")
