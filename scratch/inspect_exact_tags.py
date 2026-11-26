import re

files = [
    'anaesthesia-and-pain-management.html',
    'critical-care.html',
    'doctor.html',
    'index.html',
    'medicine-and-critical-care.html',
    'orthopaedic-and-robotic-joint-replacement.html',
    'pathology.html',
    'radiation-oncology.html',
    'radiodiagnosis-and-imaging.html',
    'sukhda-medpark-hospital.html',
    'sukhda-multispecialty-hospital.html'
]

docs = [
    ('dr-manaswi-gupta', 'Manaswi Gupta', 'assets/images/doctors/latest/dr-manaswi-gupta.webp'),
    ('dr-sumit-grover', 'Sumit Grover', 'assets/images/doctors/latest/dr-sumit-grover.webp'),
    ('dr-nikita-grover', 'Nitika Grover', 'assets/images/doctors/latest/dr-nikita-grover.webp'),
    ('dr-ankit-gawri', 'Ankit Gawri', 'assets/images/doctors/latest/dr-ankit-gawri.webp'),
    ('dr-priyanka-chhabra', 'Priyanka Chhabra', 'assets/images/doctors/latest/dr-priyanka-chabra.webp'),
    ('dr-mohanlal', 'Mohan Lal', 'assets/images/doctors/latest/dr-mohanlal.webp')
]

for f in files:
    content = open(f, encoding='utf-8').read()
    print(f"=== {f} ===")
    for key, name, img_path in docs:
        if name.lower() in content.lower():
            # Find the card or img tag containing unknown-doctor.webp associated with this doctor
            # Let's search for lines around name or unknown-doctor.webp
            pattern = re.compile(rf'(<article[^>]*>[\s\S]*?{re.escape(name)}[\s\S]*?</article>|<div class=\"doc-card\"[^>]*>[\s\S]*?{re.escape(name)}[\s\S]*?</div>\s*</div>)', re.IGNORECASE)
            # Or simpler: find img tag with unknown-doctor.webp where alt contains name or nearby text has name
            for m in re.finditer(r'<img[^>]+src=["\']assets/images/unknown-doctor\.webp["\'][^>]*>', content):
                img_tag = m.group(0)
                # check if name is in img_tag or in surrounding 300 chars
                start = max(0, m.start() - 250)
                end = min(len(content), m.end() + 250)
                surrounding = content[start:end]
                if name.lower() in surrounding.lower():
                    print(f"  [{name}] -> {img_tag}")
