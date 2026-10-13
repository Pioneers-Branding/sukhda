import urllib.request

with urllib.request.urlopen("http://127.0.0.1:5500/doctor.html") as r:
    html = r.read().decode("utf-8")
idx = html.find('class="mobile-nav-links"')
print(html[idx+5500:idx+8500].encode("ascii", errors="replace").decode("ascii"))
