for p in ['dr-amit-kumar-garg.html', 'dr-hemant-dahiya.html', 'dr-amit-mehta.html']:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    import re
    m = re.search(r'<article class="content-card">[\s\S]*?Educational Qualification[\s\S]*?</article>', c)
    if m:
        print(f'=== {p} ===')
        print(m.group(0))
