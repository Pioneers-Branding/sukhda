import glob
import re

files = glob.glob('*.html')
pattern = re.compile(r'(<a\s+href="about\.html#vision">Vision\s*(?:&amp;|&)\s*Mission</a>)', re.IGNORECASE)
timeline_link = '\n                            <a href="about.html#timeline">Our Journey / Timeline</a>'

updated = []
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'about.html#timeline' not in content and 'about.html#vision' in content:
        # replace
        def repl(match):
            indent = re.findall(r'(\s*)<a', match.group(0))
            ind = indent[0] if indent else '                            '
            return match.group(0) + f'\n{ind}<a href="about.html#timeline">Our Journey / Timeline</a>'
        
        new_content = pattern.sub(repl, content)
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated.append(file)

print(f"Updated additional {len(updated)} files with timeline link.")
