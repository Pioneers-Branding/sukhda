import os, re

doctor_updates = [
    {
        'name': 'Dr. Manaswi Gupta',
        'key': 'manaswi',
        'img': 'assets/images/doctors/latest/dr-manaswi-gupta.webp'
    },
    {
        'name': 'Dr. Sumit Grover',
        'key': 'sumit',
        'img': 'assets/images/doctors/latest/dr-sumit-grover.webp'
    },
    {
        'name': 'Dr. Nitika Grover',
        'key': 'nitika',
        'img': 'assets/images/doctors/latest/dr-nikita-grover.webp'
    },
    {
        'name': 'Dr. Ankit Gawri',
        'key': 'ankit',
        'img': 'assets/images/doctors/latest/dr-ankit-gawri.webp'
    },
    {
        'name': 'Dr. Priyanka Chhabra',
        'key': 'priyanka',
        'img': 'assets/images/doctors/latest/dr-priyanka-chabra.webp'
    },
    {
        'name': 'Dr. Mohan Lal',
        'key': 'mohan',
        'img': 'assets/images/doctors/latest/dr-mohanlal.webp'
    }
]

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

total_replacements = 0

def process_file(file_path):
    global total_replacements
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    file_modified = False

    def replace_img(match):
        nonlocal file_modified
        global total_replacements
        full_tag = match.group(0)
        start = max(0, match.start() - 300)
        end = min(len(content), match.end() + 300)
        surrounding = content[start:end].lower()

        matched_doc = None
        for doc in doctor_updates:
            if doc['key'] in surrounding:
                matched_doc = doc
                break

        if matched_doc:
            new_tag = full_tag.replace('assets/images/unknown-doctor.webp', matched_doc['img'])
            new_tag = new_tag.replace(' (photo coming soon)', '')
            new_tag = new_tag.replace('(photo coming soon)', '')
            print(f"[{file_path}] Replaced for {matched_doc['name']}: {matched_doc['img']}")
            total_replacements += 1
            file_modified = True
            return new_tag

        return full_tag

    new_content = re.sub(r'<img[^>]+src=["\']assets/images/unknown-doctor\.webp["\'][^>]*>', replace_img, content)

    if file_modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Saved: {file_path}")

for fp in files:
    process_file(fp)

print(f"\nDone! Total replacements made: {total_replacements}")
