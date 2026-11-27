import os
import glob
import re
from html.parser import HTMLParser

class TagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_tags:
            self.stack.append((tag.lower(), self.getpos()))

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower in self.void_tags:
            return
        if not self.stack:
            self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}")
            return
        last_tag, pos = self.stack.pop()
        if last_tag != tag_lower:
            self.errors.append(f"Mismatched tag: expected </{last_tag}> (from line {pos[0]}), got </{tag}> at line {self.getpos()[0]}")

print("=== CHECKING dr-manaswi-gupta.html TAGS ===")
with open('dr-manaswi-gupta.html', 'r', encoding='utf-8') as f:
    content = f.read()

checker = TagChecker()
checker.feed(content)
if checker.errors:
    print(f"Total tag mismatch warnings: {len(checker.errors)}")
    for err in checker.errors[:5]:
        print(" ", err)
else:
    print("Tag matching clean!")

print("\n=== CHECKING ASSET IMAGES IN dr-manaswi-gupta.html ===")
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
for src in set(img_srcs):
    # ignore external or data urls
    if src.startswith('http') or src.startswith('data:'):
        continue
    clean_src = src.split('?')[0].split('#')[0]
    exists = os.path.exists(clean_src)
    print(f"Image {clean_src}: {'EXISTS' if exists else 'MISSING'}")

print("\n=== FILES LINKING TO dr-manaswi-gupta.html ===")
linking_files = []
for p in glob.glob('*.html') + glob.glob('assets/js/*.js'):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if 'dr-manaswi-gupta.html' in c:
            linking_files.append(p)
print(f"Total files linking to dr-manaswi-gupta.html: {len(linking_files)}")
for f in linking_files:
    print(f" - {f}")

print("\n=== CHECKING UNLINKED REFERENCES TO MANASWI GUPTA ===")
for p in glob.glob('*.html'):
    if p in ['dr-manaswi-gupta.html']:
        continue
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if 'manaswi' in c.lower() and 'dr-manaswi-gupta.html' not in c:
            print(f"File {p} mentions Manaswi but does NOT link to dr-manaswi-gupta.html")

print("\nALL CHECKS COMPLETE")
