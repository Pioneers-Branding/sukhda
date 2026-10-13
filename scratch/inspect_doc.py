import urllib.request
import sys

sys.stdout.reconfigure(encoding='utf-8')
url = 'http://127.0.0.1:5500/doctor.html'
with urllib.request.urlopen(url) as response:
    html = response.read().decode('utf-8')

idx = html.find('<!-- MAIN HEADER & NAVIGATION -->')
end_idx = html.find('<!-- /INCLUDE: header -->', idx)
print(html[idx:end_idx])
