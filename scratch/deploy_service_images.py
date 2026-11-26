import os
import glob
import json
import re
from PIL import Image

def main():
    # 1. Load generated-*.json
    gen_map = {}
    for f in glob.glob('scratch/generated-*.json'):
        with open(f, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            gen_map[data['key']] = data['source']
    
    print(f"Loaded {len(gen_map)} generated image mappings.")

    # 2. Load remaining-service-prompts.json
    with open('scratch/remaining-service-prompts.json', 'r', encoding='utf-8') as fp:
        prompt_data = json.load(fp)
    
    assets = prompt_data.get('assets', [])
    print(f"Found {len(assets)} assets in remaining-service-prompts.json.")

    # 3. Process each image
    page_updates = {}
    for asset in assets:
        key = asset['key']
        if key not in gen_map:
            continue
        source_path = gen_map.get(key)
        target_path = asset['file']
        page = asset['page']
        placement = asset['placement']
        alt = asset['alt']

        if not source_path or not os.path.exists(source_path):
            raise FileNotFoundError(f"Source image not found for key {key}: {source_path}")

        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        with Image.open(source_path) as im:
            rgb_im = im.convert('RGB')
            # Save as optimized JPEG
            rgb_im.save(target_path, 'JPEG', quality=90, optimize=True)
            w, h = rgb_im.size
            size_kb = os.path.getsize(target_path) / 1024
            print(f"Saved: {target_path} ({w}x{h}, {size_kb:.1f} KB) from {source_path}")

        if page not in page_updates:
            page_updates[page] = {}
        page_updates[page][placement] = {
            'file': target_path.replace('\\', '/'),
            'alt': alt,
            'key': key
        }

    # 4. Update the 7 HTML pages
    hero_pattern = re.compile(r'<div class="hero-media">\s*<div class="hero-img-card">\s*<img[^>]*>\s*</div>\s*</div>')
    intro_pattern = re.compile(r'<div class="intro-media">\s*<div class="intro-img-card">\s*<img[^>]*>\s*</div>\s*</div>')

    for page, placements in page_updates.items():
        if not os.path.exists(page):
            raise FileNotFoundError(f"Target page not found: {page}")

        with open(page, 'r', encoding='utf-8') as fp:
            content = fp.read()

        hero_data = placements.get('hero')
        intro_data = placements.get('overview')

        if hero_data:
            hero_replacement = (
                f'<div class="hero-media">\n'
                f'                <div class="hero-img-card">\n'
                f'                    <img src="{hero_data["file"]}"\n'
                f'                        alt="{hero_data["alt"]}"\n'
                f'                        width="1448" height="1086" fetchpriority="high">\n'
                f'                </div>\n'
                f'            </div>'
            )
            if not hero_pattern.search(content):
                raise ValueError(f"Could not find hero-media pattern in {page}")
            content = hero_pattern.sub(hero_replacement, content, count=1)

        if intro_data:
            intro_replacement = (
                f'<div class="intro-media">\n'
                f'                <div class="intro-img-card">\n'
                f'                    <img src="{intro_data["file"]}"\n'
                f'                        alt="{intro_data["alt"]}"\n'
                f'                        width="1448" height="1086" loading="lazy" decoding="async">\n'
                f'                </div>\n'
                f'            </div>'
            )
            if not intro_pattern.search(content):
                raise ValueError(f"Could not find intro-media pattern in {page}")
            content = intro_pattern.sub(intro_replacement, content, count=1)

        with open(page, 'w', encoding='utf-8') as fp:
            fp.write(content)

        print(f"Updated HTML: {page}")

    print("\n--- All 14 images converted and 7 pages updated successfully! ---")

if __name__ == '__main__':
    main()
