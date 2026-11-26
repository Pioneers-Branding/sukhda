import os, glob, re

keywords = {
    'manaswi': ('Manaswi Gupta', 'assets/images/doctors/latest/dr-manaswi-gupta.webp'),
    'sumit': ('Sumit Grover', 'assets/images/doctors/latest/dr-sumit-grover.webp'),
    'nikita': ('Nikita Grover', 'assets/images/doctors/latest/dr-nikita-grover.webp'),
    'nitika': ('Nitika Grover', 'assets/images/doctors/latest/dr-nikita-grover.webp'),
    'ankit': ('Ankit Gawri', 'assets/images/doctors/latest/dr-ankit-gawri.webp'),
    'priyanka': ('Priyanka Chhabra', 'assets/images/doctors/latest/dr-priyanka-chabra.webp'),
    'mohan': ('Mohan Lal', 'assets/images/doctors/latest/dr-mohanlal.webp'),
}

html_files = sorted(glob.glob('*.html'))
results = []

for f in html_files:
    content = open(f, encoding='utf-8').read()
    for kw, (display_name, img_path) in keywords.items():
        if kw in content.lower():
            # Find context around match
            matches = [m.start() for m in re.finditer(re.escape(kw), content, re.IGNORECASE)]
            for pos in matches:
                start = max(0, pos - 400)
                end = min(len(content), pos + 400)
                snippet = content[start:end]
                # Look for img tag nearby
                img_tag = re.search(r'<img[^>]+>', snippet)
                results.append({
                    'file': f,
                    'kw': kw,
                    'doctor': display_name,
                    'new_img': img_path,
                    'has_img': bool(img_tag),
                    'img': img_tag.group(0) if img_tag else None,
                    'snippet': snippet
                })

print(f"Total occurrences found: {len(results)}")
for r in results:
    print(f"File: {r['file']} | Doctor: {r['doctor']} | Img tag: {r['img']}")
