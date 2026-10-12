with open('doctor.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Header
h_idx = html.find('<header class="nav"')
h_end = html.find('</header>') + len('</header>')
header_html = html[h_idx:h_end]

# Cashless strip
c_idx = html.find('<section class="cashless-strip">')
c_end = html.find('</section>', c_idx) + len('</section>') if c_idx != -1 else -1

# Footer
f_idx = html.find('<footer class="footer"')
footer_rest = html[f_idx:]

print(f"Header length: {len(header_html)}")
print(f"Cashless strip found: {c_idx != -1}")
print(f"Footer rest length: {len(footer_rest)}")

with open('temp_header.html', 'w', encoding='utf-8') as f:
    f.write(header_html)

with open('temp_footer.html', 'w', encoding='utf-8') as f:
    f.write(footer_rest)
