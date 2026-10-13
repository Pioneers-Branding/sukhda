import urllib.request
import sys

sys.stdout.reconfigure(encoding='utf-8')
with urllib.request.urlopen('http://127.0.0.1:5500/include/header.html') as resp:
    data = resp.read().decode('utf-8')

# Find where mega-footer is or where Our Services ends
idx = data.find('mega-footer')
print(data[idx:idx+2000])
