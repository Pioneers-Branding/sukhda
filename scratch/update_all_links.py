# update_all_links.py
import re

# 1. doctor.html
with open('doctor.html', 'r', encoding='utf-8') as f:
    doc_html = f.read()

old_doc_card = '''                <article class="doc-card" data-name="dr. manaswi gupta" data-speciality="Internal Medicine"
                    data-hospital="both"
                    data-tags="medicine &amp; critical care consultant physician — medicine &amp; critical care mbbs, md (general medicine), fice">
                    <div class="doc-card-top">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Consultant Physician — Medicine &amp; Critical Care, Sukhda Hospital">
                    </div>
                    <div class="doc-card-body">
                        <span class="doc-location-pill pill-both"><i data-lucide="map-pin"></i> Both Locations</span>
                        <h3 class="doc-card-name">Dr. Manaswi Gupta</h3>
                        <div class="doc-card-desig">Consultant Physician — Medicine &amp; Critical Care</div>
                        <div class="doc-card-qual">MBBS, MD (General Medicine), FICE</div>
                        <div class="doc-card-tags">
                            <span class="doc-tag">Medicine &amp; Critical Care</span>
                        </div>
                        <div class="doc-card-actions">
                            <a href="opd-schedule.html" class="doc-btn-profile">View OPD Timings</a>
                        </div>
                    </div>
                </article>'''

new_doc_card = '''                <article class="doc-card" data-name="dr. manaswi gupta" data-speciality="Internal Medicine"
                    data-hospital="both"
                    data-tags="medicine &amp; critical care consultant physician — medicine &amp; critical care mbbs, md (general medicine), fice">
                    <div class="doc-card-top">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Consultant Physician — Medicine &amp; Critical Care, Sukhda Hospital">
                    </div>
                    <div class="doc-card-body">
                        <span class="doc-location-pill pill-both"><i data-lucide="map-pin"></i> Both Locations</span>
                        <h3 class="doc-card-name"><a href="dr-manaswi-gupta.html">Dr. Manaswi Gupta</a></h3>
                        <div class="doc-card-desig">Consultant Physician — Medicine &amp; Critical Care</div>
                        <div class="doc-card-qual">MBBS, MD (General Medicine), FICE</div>
                        <div class="doc-card-tags">
                            <span class="doc-tag">Medicine &amp; Critical Care</span>
                        </div>
                        <div class="doc-card-actions">
                            <a href="dr-manaswi-gupta.html" class="doc-btn-profile">View Profile</a>
                        </div>
                    </div>
                </article>'''

if old_doc_card in doc_html:
    doc_html = doc_html.replace(old_doc_card, new_doc_card)
    with open('doctor.html', 'w', encoding='utf-8') as f:
        f.write(doc_html)
    print("Updated doctor.html")
else:
    print("WARNING: old_doc_card not found in doctor.html")


# 2. index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Update doctor slider card
old_idx_card = '''                    <a href="doctor.html" class="doctor-card">
                        <div class="doctor-photo">
                            <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp" alt="Dr. Manaswi Gupta" loading="lazy">
                        </div>
                        <div class="doctor-body">
                            <h3>Dr. Manaswi Gupta</h3>
                            <div class="doc-spec">Consultant Physician – Medicine &amp; Critical Care</div>
                            <div class="doc-hosp">Sukhda Multispeciality Hospital</div>
                        </div>
                    </a>'''

new_idx_card = '''                    <a href="dr-manaswi-gupta.html" class="doctor-card">
                        <div class="doctor-photo">
                            <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp" alt="Dr. Manaswi Gupta" loading="lazy">
                        </div>
                        <div class="doctor-body">
                            <h3>Dr. Manaswi Gupta</h3>
                            <div class="doc-spec">Consultant Physician – Medicine &amp; Critical Care</div>
                            <div class="doc-hosp">Sukhda Multispeciality Hospital</div>
                        </div>
                    </a>'''

if old_idx_card in index_html:
    index_html = index_html.replace(old_idx_card, new_idx_card)
    print("Updated doctor slider card in index.html")
else:
    print("WARNING: old_idx_card not found in index.html")

# Update searchableData in index.html
old_searchable = "{ name: 'Dr. Manaswi Gupta', sub: 'MD (General Medicine), FICE • Medicine & Critical Care', cat: 'Doctor', badge: 'doc', url: 'opd-schedule.html' },"
new_searchable = "{ name: 'Dr. Manaswi Gupta', sub: 'MD (General Medicine), FICE • Medicine & Critical Care', cat: 'Doctor', badge: 'doc', url: 'dr-manaswi-gupta.html' },"

if old_searchable in index_html:
    index_html = index_html.replace(old_searchable, new_searchable)
    print("Updated searchableData in index.html")
else:
    print("WARNING: old_searchable not found in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)


# 3. medicine-and-critical-care.html
with open('medicine-and-critical-care.html', 'r', encoding='utf-8') as f:
    med_html = f.read()

old_med_card = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Consultant Physician — Medicine &amp; Critical Care"
                            loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Manaswi Gupta</a></h3>
                        <div class="hd-desig">Consultant Physician — Medicine &amp; Critical Care</div>
                        <div class="hd-qual">MBBS, DNB (General Medicine)</div>
                        <div class="hd-meta">
                            <span><i data-lucide="map-pin"></i> Both Locations</span>
                            <span><i data-lucide="clock"></i> Mon–Sat (Regular OPD)</span>
                        </div>
                    </div>
                </article>'''

new_med_card = '''                <article class="hd-card">
                    <a href="dr-manaswi-gupta.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Consultant Physician — Medicine &amp; Critical Care"
                            loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-manaswi-gupta.html">Dr. Manaswi Gupta</a></h3>
                        <div class="hd-desig">Consultant Physician — Medicine &amp; Critical Care</div>
                        <div class="hd-qual">MBBS, MD (General Medicine), FICE</div>
                        <div class="hd-meta">
                            <span><i data-lucide="map-pin"></i> Both Locations</span>
                            <span><i data-lucide="clock"></i> Mon–Sat (Regular OPD)</span>
                        </div>
                    </div>
                </article>'''

if old_med_card in med_html:
    med_html = med_html.replace(old_med_card, new_med_card)
    with open('medicine-and-critical-care.html', 'w', encoding='utf-8') as f:
        f.write(med_html)
    print("Updated medicine-and-critical-care.html")
else:
    print("WARNING: old_med_card not found in medicine-and-critical-care.html")


# 4. sukhda-multispecialty-hospital.html
with open('sukhda-multispecialty-hospital.html', 'r', encoding='utf-8') as f:
    multi_html = f.read()

old_multi_card = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Associate Consultant — Internal Medicine" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Manaswi Gupta</a></h3>
                        <div class="hd-desig">Associate Consultant — Internal Medicine</div>
                        <div class="hd-qual">MBBS, DNB (General Medicine)</div>
                        <div class="hd-meta">
                            <span><i data-lucide="map-pin"></i> Both Hospitals</span>
                            <span><i data-lucide="clock"></i> Mon–Sat (Regular OPD)</span>
                        </div>
                    </div>
                </article>'''

new_multi_card = '''                <article class="hd-card">
                    <a href="dr-manaswi-gupta.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Consultant Physician — Medicine &amp; Critical Care" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-manaswi-gupta.html">Dr. Manaswi Gupta</a></h3>
                        <div class="hd-desig">Consultant Physician — Medicine &amp; Critical Care</div>
                        <div class="hd-qual">MBBS, MD (General Medicine), FICE</div>
                        <div class="hd-meta">
                            <span><i data-lucide="map-pin"></i> Both Locations</span>
                            <span><i data-lucide="clock"></i> Mon–Sat (Regular OPD)</span>
                        </div>
                    </div>
                </article>'''

if old_multi_card in multi_html:
    multi_html = multi_html.replace(old_multi_card, new_multi_card)
    with open('sukhda-multispecialty-hospital.html', 'w', encoding='utf-8') as f:
        f.write(multi_html)
    print("Updated sukhda-multispecialty-hospital.html")
else:
    print("WARNING: old_multi_card not found in sukhda-multispecialty-hospital.html")


# 5. sukhda-medpark-hospital.html
with open('sukhda-medpark-hospital.html', 'r', encoding='utf-8') as f:
    medpark_html = f.read()

old_medpark_card = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Associate Consultant — Internal Medicine" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Manaswi Gupta</a></h3>
                        <div class="hd-desig">Associate Consultant — Internal Medicine</div>
                        <div class="hd-qual">MBBS, DNB (General Medicine)</div>
                        <div class="hd-meta">
                            <span><i data-lucide="map-pin"></i> Both Hospitals</span>
                            <span><i data-lucide="clock"></i> Mon–Sat (Regular OPD)</span>
                        </div>
                    </div>
                </article>'''

new_medpark_card = '''                <article class="hd-card">
                    <a href="dr-manaswi-gupta.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Consultant Physician — Medicine &amp; Critical Care" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-manaswi-gupta.html">Dr. Manaswi Gupta</a></h3>
                        <div class="hd-desig">Consultant Physician — Medicine &amp; Critical Care</div>
                        <div class="hd-qual">MBBS, MD (General Medicine), FICE</div>
                        <div class="hd-meta">
                            <span><i data-lucide="map-pin"></i> Both Locations</span>
                            <span><i data-lucide="clock"></i> Mon–Sat (Regular OPD)</span>
                        </div>
                    </div>
                </article>'''

if old_medpark_card in medpark_html:
    medpark_html = medpark_html.replace(old_medpark_card, new_medpark_card)
    with open('sukhda-medpark-hospital.html', 'w', encoding='utf-8') as f:
        f.write(medpark_html)
    print("Updated sukhda-medpark-hospital.html")
else:
    print("WARNING: old_medpark_card not found in sukhda-medpark-hospital.html")


# 6. assets/js/site-search.js
with open('assets/js/site-search.js', 'r', encoding='utf-8') as f:
    search_js = f.read()

target_doc = "{ n: 'Dr. Hemant Dahiya', s: 'Consultant Physician - Internal Medicine', u: 'dr-hemant-dahiya.html', h: MULTI },"
new_entry = target_doc + "\n        { n: 'Dr. Manaswi Gupta', s: 'Consultant Physician — Medicine & Critical Care', u: 'dr-manaswi-gupta.html', h: BOTH },"

if target_doc in search_js:
    if 'Dr. Manaswi Gupta' not in search_js:
        search_js = search_js.replace(target_doc, new_entry)
        with open('assets/js/site-search.js', 'w', encoding='utf-8') as f:
            f.write(search_js)
        print("Updated assets/js/site-search.js")
    else:
        print("assets/js/site-search.js already contains Dr. Manaswi Gupta")
else:
    print("WARNING: target_doc not found in assets/js/site-search.js")


# 7. opd-schedule.html
with open('opd-schedule.html', 'r', encoding='utf-8') as f:
    opd_html = f.read()

old_opd_btn = '''                        <tr class="opd-row" data-doctor="dr-manaswi-gupta" data-category="medicine"
                            data-days="Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
                            data-search="dr. manaswi gupta mbbs, md (general medicine), fice · consultant – physician internal medicine monday tuesday wednesday thursday friday saturday 09:00 am – 04:00 pm 05:30 pm – 07:00 pm">
                            <td style="color:var(--muted);font-weight:700;">3</td>
                            <td>
                                <div class="doc-cell">
                                    <span class="opd-doc-name">Dr. Manaswi Gupta</span>
                                    <span class="opd-doc-qual">MBBS, MD (General Medicine), FICE · Consultant –
                                        Physician</span>
                                </div>
                            </td>
                            <td>
                                <div class="dept-cell">
                                    <a href="medicine-and-critical-care.html" class="opd-dept-link">Medicine &amp; Critical
                                        Care</a>
                                    <a href="sukhda-multispecialty-hospital.html" class="hospital-tag"><i
                                            data-lucide="building" style="width:11px;height:11px"></i> Sukhda
                                        Multispeciality Hospital</a>
                                    <a href="sukhda-medpark-hospital.html" class="hospital-tag"><i
                                            data-lucide="building" style="width:11px;height:11px"></i> Sukhda
                                        MedPark</a>
                                </div>
                            </td>
                            <td>
                                <span class="days-badge">Mon – Sat</span>
                            </td>
                            <td>
                                <div class="time-slots">
                                    <span class="time-pill morning"><i data-lucide="sun"
                                            style="width:12px;height:12px"></i> 09:00 AM – 04:00 PM</span>
                                    <span class="time-pill evening"><i data-lucide="moon"
                                            style="width:12px;height:12px"></i> 05:30 PM – 07:00 PM</span>
                                </div>
                            </td>
                            <td>
                                <span class="status-badge available" data-status-badge><i data-lucide="check-circle"
                                        style="width:11px;height:11px"></i> Doctor Available</span>
                            </td>
                            <td style="text-align: right;">
                                <div class="action-btns" style="justify-content: flex-end;">
                                    <a href="contact.html" class="btn-book-opd"><i data-lucide="calendar"></i> Book</a>
                                </div>
                            </td>
                        </tr>'''

new_opd_btn = '''                        <tr class="opd-row" data-doctor="dr-manaswi-gupta" data-category="medicine"
                            data-days="Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
                            data-search="dr. manaswi gupta mbbs, md (general medicine), fice · consultant – physician internal medicine monday tuesday wednesday thursday friday saturday 09:00 am – 04:00 pm 05:30 pm – 07:00 pm">
                            <td style="color:var(--muted);font-weight:700;">3</td>
                            <td>
                                <div class="doc-cell">
                                    <a href="dr-manaswi-gupta.html" class="opd-doc-name" style="color:var(--blue);text-decoration:none;font-weight:700;">Dr. Manaswi Gupta</a>
                                    <span class="opd-doc-qual">MBBS, MD (General Medicine), FICE · Consultant –
                                        Physician</span>
                                </div>
                            </td>
                            <td>
                                <div class="dept-cell">
                                    <a href="medicine-and-critical-care.html" class="opd-dept-link">Medicine &amp; Critical
                                        Care</a>
                                    <a href="sukhda-multispecialty-hospital.html" class="hospital-tag"><i
                                            data-lucide="building" style="width:11px;height:11px"></i> Sukhda
                                        Multispeciality Hospital</a>
                                    <a href="sukhda-medpark-hospital.html" class="hospital-tag"><i
                                            data-lucide="building" style="width:11px;height:11px"></i> Sukhda
                                        MedPark</a>
                                </div>
                            </td>
                            <td>
                                <span class="days-badge">Mon – Sat</span>
                            </td>
                            <td>
                                <div class="time-slots">
                                    <span class="time-pill morning"><i data-lucide="sun"
                                            style="width:12px;height:12px"></i> 09:00 AM – 04:00 PM</span>
                                    <span class="time-pill evening"><i data-lucide="moon"
                                            style="width:12px;height:12px"></i> 05:30 PM – 07:00 PM</span>
                                </div>
                            </td>
                            <td>
                                <span class="status-badge available" data-status-badge><i data-lucide="check-circle"
                                        style="width:11px;height:11px"></i> Doctor Available</span>
                            </td>
                            <td style="text-align: right;">
                                <div class="action-btns" style="justify-content: flex-end;">
                                    <a href="dr-manaswi-gupta.html" class="btn-book-opd" style="background:#eaf1f8;color:var(--blue);margin-right:6px;"><i data-lucide="user"></i> Profile</a>
                                    <a href="contact.html?doctor=dr-manaswi-gupta" class="btn-book-opd"><i data-lucide="calendar"></i> Book</a>
                                </div>
                            </td>
                        </tr>'''

if old_opd_btn in opd_html:
    opd_html = opd_html.replace(old_opd_btn, new_opd_btn)
    with open('opd-schedule.html', 'w', encoding='utf-8') as f:
        f.write(opd_html)
    print("Updated opd-schedule.html")
else:
    print("WARNING: old_opd_btn not found in opd-schedule.html")
