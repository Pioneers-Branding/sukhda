import os
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

with open('dr-priyanka-chhabra.html', 'r', encoding='utf-8') as f:
    content = f.read()

checker = TagChecker()
checker.feed(content)
if checker.errors:
    print(f"Total tag mismatch warnings: {len(checker.errors)}")
    for err in checker.errors[:5]:
        print(" ", err)
else:
    print("Tag matching clean!")

print("Occurrences of 'Priyanka':", len(re.findall(r'priyanka', content, re.I)))
# Mohan should ONLY be in the colleague card
lines = content.split('\n')
for i, l in enumerate(lines):
    if 'mohan' in l.lower():
        print(f'Line {i+1}: {l.strip()[:100]}')

print("\n=== CHECKING ASSET IMAGES IN dr-priyanka-chhabra.html ===")
img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
for src in set(img_srcs):
    if src.startswith('http') or src.startswith('data:'):
        continue
    clean_src = src.split('?')[0].split('#')[0]
    exists = os.path.exists(clean_src)
    print(f"Image {clean_src}: {'EXISTS' if exists else 'MISSING'}")
