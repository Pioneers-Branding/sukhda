import glob
import re

files = glob.glob('*.html') + glob.glob('include/*.html')

target_old = '<a href="about.html">About Sukhda</a>'
target_new = '<a href="about.html">About Sukhda Healthcare</a>'

count_old = 0
count_new = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if target_old in c:
        print(f"OLD STILL FOUND in {f}")
        count_old += 1
    if target_new in c:
        count_new += 1

print(f"Old occurrences: {count_old}")
print(f"New occurrences: {count_new}")
if count_old == 0 and count_new == 63:
    print("ALL 63 DROPDOWNS VERIFIED SUCCESSFULLY!")
