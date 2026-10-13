import urllib.request
import sys

sys.stdout.reconfigure(encoding='utf-8')
with urllib.request.urlopen('http://127.0.0.1:5500/include/header.html') as resp:
    data = resp.read().decode('utf-8')

print("Live Server length:", len(data))
print("Contains 'Doctors'?", "Doctors" in data)
print("Contains 'Resources'?", "Resources" in data)
print("Contains 'Book Appointment'?", "Book Appointment" in data)
print("Contains 'mega-footer'?", "mega-footer" in data)
idx = data.find('mega-footer')
print(data[idx:])
