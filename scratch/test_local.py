with open('e:/office-website/bp-project/sukhda/include/header.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Local length:", len(text))
print("Contains 'Doctors'?", "Doctors" in text)
print("Contains 'Resources'?", "Resources" in text)
print("Contains 'Book Appointment'?", "Book Appointment" in text)
print("Contains 'mega-footer'?", "mega-footer" in text)
idx = text.find('mega-footer')
print(text[idx:])
