with open('dr-hemant-dahiya.html', encoding='utf-8') as f:
    text = f.read()

head_style = text[text.find('<style>'):text.find('</style>')+8]
print(f"Style length: {len(head_style)}")
header = text[text.find('<header'):text.find('</header>')+9]
print(f"Header length: {len(header)}")
footer = text[text.find('<footer'):text.find('</footer>')+9]
print(f"Footer length: {len(footer)}")
scripts = text[text.find('<!-- STICKY BOTTOM FLOATING PILL CTA -->'):]
print(f"Scripts length: {len(scripts)}")
