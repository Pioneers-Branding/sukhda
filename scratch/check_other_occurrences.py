import glob
import re

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # check occurrences of Compassionate Care for the Whole Family
    matches = [m.start() for m in re.finditer(r'Compassionate Care for the Whole Family', c, re.IGNORECASE)]
    for pos in matches:
        snippet = c[max(0, pos-50):min(len(c), pos+100)].replace('\n', ' ')
        if 'footer-motto' not in snippet:
            print(f"Non-footer-motto occurrence in {f}: {snippet}")

    # check occurrences of 24*7 Emergency Helpline
    matches2 = [m.start() for m in re.finditer(r'24\*7 Emergency Helpline', c, re.IGNORECASE)]
    for pos in matches2:
        snippet2 = c[max(0, pos-50):min(len(c), pos+100)].replace('\n', ' ')
        if 'footer-emergency-box' not in snippet2 and 'footer' not in snippet2:
            print(f"Non-footer occurrence of Emergency Helpline in {f}: {snippet2}")
