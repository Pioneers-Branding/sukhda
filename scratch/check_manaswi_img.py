import os
for f in os.listdir('assets/images/doctors/latest'):
    if 'manaswi' in f.lower():
        size = os.path.getsize(os.path.join('assets/images/doctors/latest', f))
        print(f'{f}: {size} bytes')
