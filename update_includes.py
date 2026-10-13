import os
import glob
import re

HEADER_FILE = os.path.join("include", "header.html")
FOOTER_FILE = os.path.join("include", "footer.html")
CSS_LINK = '<link rel="stylesheet" href="include/header-footer.css">'
JS_SCRIPT = '<script src="include/include.js"></script>'

with open(HEADER_FILE, "r", encoding="utf-8") as f:
    raw_header = f.read().strip()

with open(FOOTER_FILE, "r", encoding="utf-8") as f:
    raw_footer = f.read().strip()

def get_page_header(filename):
    """Return header HTML with no active link highlighting."""
    h = raw_header
    # Reset any existing 'on' class in header
    h = re.sub(r'\s+class="on"', '', h)
    return h

def update_file(filepath, dry_run=False):
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content

    # 1. Ensure CSS Link in <head>
    if "include/header-footer.css" not in content:
        if "</head>" in content:
            content = content.replace("</head>", f"    {CSS_LINK}\n</head>", 1)

    # 2. Extract and preserve any page-specific scripts that follow </footer>
    custom_scripts = []
    # Known page-specific script snippets to preserve:
    f_idx = content.find("</footer>")
    if f_idx != -1:
        after_footer = content[f_idx + len("</footer>"):]
        
        # Doctor filter logic in doctor.html
        if "doctorSearchInput" in after_footer and filename == "doctor.html":
            m = re.search(r'(<script>[\s\S]*?filterDoctors[\s\S]*?</script>)', after_footer)
            if m: custom_scripts.append(m.group(1))
            
        # Careers modal logic in careers.html
        if "apply-btn" in after_footer or "jobModal" in after_footer:
            m = re.search(r'(<script>[\s\S]*?apply-btn[\s\S]*?</script>)', after_footer)
            if m: custom_scripts.append(m.group(1))
            
        # Corporate filter logic in empanelled-corporate.html
        if "corpSearch" in after_footer or "corp-card" in after_footer:
            m = re.search(r'(<script>[\s\S]*?corpSearch[\s\S]*?</script>)', after_footer)
            if m: custom_scripts.append(m.group(1))

        # Media centre tabs in media-centre.html / media.html
        if "tab-btn" in after_footer and ("media-centre" in filename or "media.html" in filename):
            m = re.search(r'(<script>[\s\S]*?tab-btn[\s\S]*?</script>)', after_footer)
            if m: custom_scripts.append(m.group(1))

        # OPD Schedule filter in opd-schedule.html
        if "opdSearch" in after_footer or "schedule-table" in after_footer:
            m = re.search(r'(<script>[\s\S]*?opdSearch[\s\S]*?</script>)', after_footer)
            if m: custom_scripts.append(m.group(1))

        # Patient stories tabs in patient-stories.html
        if "story-card" in after_footer or "filterStories" in after_footer:
            m = re.search(r'(<script>[\s\S]*?story[\s\S]*?</script>)', after_footer)
            if m: custom_scripts.append(m.group(1))

    # 3. Replace Header Section
    page_header = get_page_header(filename)
    header_block = page_header

    # Detect header range
    # Check if already has INCLUDE: header comment
    if "<!-- INCLUDE: header -->" in content and "<!-- /INCLUDE: header -->" in content:
        content = re.sub(
            r'<!-- INCLUDE: header -->[\s\S]*?<!-- /INCLUDE: header -->',
            lambda m: header_block,
            content
        )
    else:
        # Match from <!-- TOP BAR or <div class="top"> to </header> and optional nav-overlay
        h_pattern = r'(?:<!--\s*TOP BAR[\s\S]*?-->\s*)?<div class=["\']top["\'][\s\S]*?</header>(?:\s*<div class=["\']nav-overlay["\']></div>)?'
        if re.search(h_pattern, content):
            content = re.sub(h_pattern, lambda m: header_block, content, count=1)
        else:
            # Fallback
            h_start = content.find('<div class="top">')
            if h_start == -1: h_start = content.find("<div class='top'>")
            h_end = content.find('</header>')
            if h_start != -1 and h_end != -1:
                h_end += len('</header>')
                after = content[h_end:h_end+60]
                if 'nav-overlay' in after:
                    h_end = content.find('</div>', h_end) + len('</div>')
                content = content[:h_start] + header_block + content[h_end:]

    # 4. Replace Footer Section
    custom_scripts_html = "\n\n    ".join(custom_scripts)
    if custom_scripts_html:
        custom_scripts_html = f"\n    <!-- Page Specific Script -->\n    {custom_scripts_html}\n"

    footer_block = f"""    <!-- INCLUDE: footer -->
    <div id="site-footer" data-include="footer">
{raw_footer}
    </div>
    <!-- /INCLUDE: footer -->{custom_scripts_html}
    {JS_SCRIPT}"""

    # Check if already has INCLUDE: footer
    if "<!-- INCLUDE: footer -->" in content and "<!-- /INCLUDE: footer -->" in content:
        # replace between INCLUDE: footer and </body>
        content = re.sub(
            r'<!-- INCLUDE: footer -->[\s\S]*?(?=</body>)',
            lambda m: footer_block + "\n",
            content
        )
    else:
        # Match from <!-- FOOTER or <footer class="footer" to </body>
        f_start_match = re.search(r'(?:<!--\s*FOOTER[\s\S]*?-->\s*)?<footer class=["\']footer["\']', content)
        if f_start_match:
            f_start = f_start_match.start()
            b_end = content.rfind('</body>')
            if b_end != -1:
                content = content[:f_start] + footer_block + "\n" + content[b_end:]

    if not dry_run and content != orig_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return content != orig_content

if __name__ == "__main__":
    html_files = [f for f in sorted(glob.glob("*.html")) if not f.startswith("temp_")]
    print(f"Scanning {len(html_files)} files for update...")
    updated = 0
    for f in html_files:
        changed = update_file(f, dry_run=False)
        if changed:
            updated += 1
            print(f"  [UPDATED] {f}")
        else:
            print(f"  [NO CHANGE] {f}")
    print(f"\nDone! Successfully updated header and footer in {updated}/{len(html_files)} files.")
