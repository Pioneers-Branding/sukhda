import re

with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Pattern for small helpline
small_pattern = re.compile(r'^[ \t]*<small>\s*24\*7 Emergency Helpline\s*</small>\r?\n', re.MULTILINE | re.IGNORECASE)
# Pattern for footer-motto block
motto_pattern = re.compile(r'^[ \t]*<div class="footer-motto">[\s\S]*?</div>\r?\n?', re.MULTILINE)

c_new = small_pattern.sub('', c)
c_new = motto_pattern.sub('', c_new)

# Let's inspect the diff around footer-emergency-box
idx = c_new.find('class="footer-emergency-box"')
print("Snippet from about.html after change:")
print(c_new[idx-50:idx+600])
