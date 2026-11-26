import re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

# Extract searchableData array
m = re.search(r'const searchableData = (\[[\s\S]*?\]);\s*let selectedIndex', html)
if not m:
    print("FAILED to find searchableData in index.html")
    exit(1)

js_array = m.group(1)

# Quick json conversion
import json
# Replace single quotes with double quotes roughly or evaluate using node or python
import subprocess
result = subprocess.run(['node', '-e', f'''
    const searchableData = {js_array};
    const testQueries = [
        "cardiology", "gastro", "ortho", "spine", "mri", "oncology", 
        "ent", "dermatology", "gynaecology", "dialysis", "physiotherapy",
        "psychiatry", "dr amit", "dr ankur", "dr bharath", "dr pankaj",
        "dr deepam", "dr deepti", "dr devilal", "dr bansal", "dr trivikrama",
        "dr nidhi", "dr shubham", "dr sanjeet", "dr manisha"
    ];
    for (const q of testQueries) {{
        const words = q.trim().toLowerCase().split(/\\s+/);
        const matches = searchableData.filter(item => {{
            const haystack = (item.name + ' ' + item.sub + ' ' + item.cat).toLowerCase();
            return words.every(w => haystack.includes(w));
        }}).slice(0, 3);
        console.log(`Q: "${{q}}" -> Matches: ${{matches.map(m => m.name + " (" + m.sub.split("•")[0].trim() + ")").join(" | ")}}`);
    }}
'''], capture_output=True, text=True)

print(result.stdout)
if result.stderr:
    print("ERR:", result.stderr)
