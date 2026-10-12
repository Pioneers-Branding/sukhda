import os
import glob
import re

html_files = glob.glob("*.html")
print(f"Found {len(html_files)} HTML files to check.")

updated_footer_links = """                <ul class="footer-nav">
                    <li><a href="index.html"><span>›</span> Home</a></li>
                    <li><a href="about.html"><span>›</span> About Sukhda</a></li>
                    <li><a href="doctor.html"><span>›</span> Find Doctors</a></li>
                    <li><a href="patient-stories.html"><span>›</span> Patient Stories</a></li>
                    <li><a href="careers.html"><span>›</span> Careers</a></li>
                    <li><a href="csr.html"><span>›</span> CSR &amp; Community</a></li>
                    <li><a href="media-centre.html"><span>›</span> Media Centre</a></li>
                    <li><a href="contact.html"><span>›</span> Contact Us</a></li>
                </ul>"""

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Update Case Stories nav link in header if it points to index.html#cases
    # except on index.html where both can work
    new_content = re.sub(r'<a\s+href="index\.html#cases">Case Stories</a>', r'<a href="patient-stories.html">Case Stories</a>', new_content)
    
    # Update footer nav
    if '<ul class="footer-nav">' in new_content:
        new_content = re.sub(r'<ul class="footer-nav">[\s\S]*?</ul>', updated_footer_links, new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Successfully updated navigation & footer links across {count} files.")
