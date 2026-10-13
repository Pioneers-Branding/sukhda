import urllib.request
import re

with urllib.request.urlopen('http://127.0.0.1:5500/doctor.html') as r:
    html = r.read().decode('utf-8')

print("HTML length from 5500:", len(html))

# Search for any nav or header tag
nav_tags = re.findall(r'<nav\b[^>]*>', html)
print("Nav tags found:", nav_tags)

header_tags = re.findall(r'<header\b[^>]*>', html)
print("Header tags found:", header_tags)

# Find where the top bar or header starts
start_idx = html.find('class="nav"')
if start_idx != -1:
    print("Found class=\"nav\" at:", start_idx)
    print(html[start_idx-50:start_idx+1200].encode('ascii', errors='replace').decode('ascii'))
else:
    print("class=\"nav\" not found!")
    # Find any links
    for l in html.splitlines():
        if 'About Us' in l:
            print("Line with About Us:", l[:200])
