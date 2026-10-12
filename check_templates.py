import os

# Read the standard header and footer from temp files
with open('temp_header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

# Let's customize nav items to make sure Case Stories / Patient Stories, Careers, CSR, Media Centre are easily accessible
# In header_html:
# - Replace 'Case Stories' href="index.html#cases" with 'patient-stories.html'
# - Add or refine navigation links if needed

with open('temp_footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

print("Header length:", len(header_html))
print("Footer length:", len(footer_html))
