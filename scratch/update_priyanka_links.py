# update_priyanka_links.py
import re

# 1. doctor.html
with open('doctor.html', 'r', encoding='utf-8') as f:
    doc_html = f.read()

old_doc_card = '''                <article class="doc-card" data-name="dr. priyanka chhabra" data-speciality="Radiology"
                    data-hospital="medpark"
                    data-tags="radiodiagnosis &amp; imaging consultant — radiodiagnosis &amp; imaging dmrd (radiology)">
                    <div class="doc-card-top">
                        <img src="assets/images/doctors/latest/dr-priyanka-chabra.webp"
                            alt="Dr. Priyanka Chhabra - Consultant — Radiodiagnosis &amp; Imaging, Sukhda Hospital">
                    </div>
                    <div class="doc-card-body">
                        <span class="doc-location-pill pill-medpark"><i data-lucide="map-pin"></i> Sukhda MedPark</span>
                        <h3 class="doc-card-name">Dr. Priyanka Chhabra</h3>
                        <div class="doc-card-desig">Consultant — Radiodiagnosis &amp; Imaging</div>
                        <div class="doc-card-qual">DMRD (Radiology)</div>
                        <div class="doc-card-tags">
                            <span class="doc-tag">Radiodiagnosis &amp; Imaging</span>
                        </div>
                        <div class="doc-card-actions">
                            <a href="opd-schedule.html" class="doc-btn-profile">View OPD Timings</a>
                        </div>
                    </div>
                </article>'''

new_doc_card = '''                <article class="doc-card" data-name="dr. priyanka chhabra" data-speciality="Radiology"
                    data-hospital="medpark"
                    data-tags="radiodiagnosis &amp; imaging senior consultant radiologist director mbbs, dmrd, edir, dicri">
                    <div class="doc-card-top">
                        <img src="assets/images/doctors/latest/dr-priyanka-chabra.webp"
                            alt="Dr. Priyanka Chhabra - Senior Consultant Radiologist &amp; Director, Sukhda Hospital">
                    </div>
                    <div class="doc-card-body">
                        <span class="doc-location-pill pill-medpark"><i data-lucide="map-pin"></i> Sukhda MedPark</span>
                        <h3 class="doc-card-name"><a href="dr-priyanka-chhabra.html">Dr. Priyanka Chhabra</a></h3>
                        <div class="doc-card-desig">Senior Consultant Radiologist &amp; Director</div>
                        <div class="doc-card-qual">MBBS, DMRD, EDiR, DICRI</div>
                        <div class="doc-card-tags">
                            <span class="doc-tag">Radiodiagnosis &amp; Imaging</span>
                        </div>
                        <div class="doc-card-actions">
                            <a href="dr-priyanka-chhabra.html" class="doc-btn-profile">View Profile</a>
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

old_idx_card = '''                    <a href="doctor.html" class="doctor-card">
                        <div class="doctor-photo">
                            <img src="assets/images/doctors/latest/dr-priyanka-chabra.webp" alt="Dr. Priyanka Chhabra" loading="lazy">
                        </div>
                        <div class="doctor-body">
                            <h3>Dr. Priyanka Chhabra</h3>
                            <div class="doc-spec">Consultant – Radiodiagnosis &amp; Imaging</div>
                            <div class="doc-hosp">Sukhda Multispeciality Hospital</div>
                        </div>
                    </a>'''

new_idx_card = '''                    <a href="dr-priyanka-chhabra.html" class="doctor-card">
                        <div class="doctor-photo">
                            <img src="assets/images/doctors/latest/dr-priyanka-chabra.webp" alt="Dr. Priyanka Chhabra" loading="lazy">
                        </div>
                        <div class="doctor-body">
                            <h3>Dr. Priyanka Chhabra</h3>
                            <div class="doc-spec">Senior Consultant Radiologist &amp; Director</div>
                            <div class="doc-hosp">Sukhda MedPark &amp; Multispeciality</div>
                        </div>
                    </a>'''

if old_idx_card in index_html:
    index_html = index_html.replace(old_idx_card, new_idx_card)
    print("Updated doctor slider card in index.html")
else:
    print("WARNING: old_idx_card not found in index.html")

old_searchable = "{ name: 'Dr. Priyanka Chhabra', sub: 'DMRD (Radiology) • Consultant — Radiodiagnosis & Imaging', cat: 'Doctor', badge: 'doc', url: 'opd-schedule.html' },"
new_searchable = "{ name: 'Dr. Priyanka Chhabra', sub: 'MBBS, DMRD, EDiR, DICRI • Senior Consultant Radiologist & Director', cat: 'Doctor', badge: 'doc', url: 'dr-priyanka-chhabra.html' },"

if old_searchable in index_html:
    index_html = index_html.replace(old_searchable, new_searchable)
    print("Updated searchableData in index.html")
else:
    print("WARNING: old_searchable not found in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)


# 3. radiodiagnosis-and-imaging.html
with open('radiodiagnosis-and-imaging.html', 'r', encoding='utf-8') as f:
    rad_html = f.read()

old_rad_card = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-priyanka-chabra.webp"
                            alt="Dr. Priyanka Chhabra - Consultant — Radiodiagnosis &amp; Imaging" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Priyanka Chhabra</a></h3>
                        <div class="hd-desig">Consultant — Radiodiagnosis &amp; Imaging</div>
                        <div class="hd-qual">DMRD (Radiology)</div>
                        <div class="hd-actions">
                            <a href="opd-schedule.html" class="hd-btn-profile">View OPD</a>
                            <a href="contact.html" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

new_rad_card = '''                <article class="hd-card">
                    <a href="dr-priyanka-chhabra.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-priyanka-chabra.webp"
                            alt="Dr. Priyanka Chhabra - Senior Consultant Radiologist &amp; Director" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-priyanka-chhabra.html">Dr. Priyanka Chhabra</a></h3>
                        <div class="hd-desig">Senior Consultant Radiologist &amp; Director</div>
                        <div class="hd-qual">MBBS, DMRD, EDiR, DICRI</div>
                        <div class="hd-actions">
                            <a href="dr-priyanka-chhabra.html" class="hd-btn-profile">View Profile</a>
                            <a href="contact.html?doctor=dr-priyanka-chhabra" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

if old_rad_card in rad_html:
    rad_html = rad_html.replace(old_rad_card, new_rad_card)
    with open('radiodiagnosis-and-imaging.html', 'w', encoding='utf-8') as f:
        f.write(rad_html)
    print("Updated radiodiagnosis-and-imaging.html")
else:
    print("WARNING: old_rad_card not found in radiodiagnosis-and-imaging.html")


# 4. sukhda-medpark-hospital.html
with open('sukhda-medpark-hospital.html', 'r', encoding='utf-8') as f:
    medpark_html = f.read()

old_medpark_card = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-priyanka-chabra.webp"
                            alt="Dr. Priyanka Chhabra - Consultant — Radiodiagnosis &amp; Imaging" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Priyanka Chhabra</a></h3>
                        <div class="hd-desig">Consultant — Radiodiagnosis &amp; Imaging</div>
                        <div class="hd-qual">DMRD (Radiology)</div>
                        <div class="hd-actions">
                            <a href="opd-schedule.html" class="hd-btn-profile">View OPD</a>
                            <a href="contact.html" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

new_medpark_card = '''                <article class="hd-card">
                    <a href="dr-priyanka-chhabra.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-priyanka-chabra.webp"
                            alt="Dr. Priyanka Chhabra - Senior Consultant Radiologist &amp; Director" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-priyanka-chhabra.html">Dr. Priyanka Chhabra</a></h3>
                        <div class="hd-desig">Senior Consultant Radiologist &amp; Director</div>
                        <div class="hd-qual">MBBS, DMRD, EDiR, DICRI</div>
                        <div class="hd-actions">
                            <a href="dr-priyanka-chhabra.html" class="hd-btn-profile">View Profile</a>
                            <a href="contact.html?doctor=dr-priyanka-chhabra" class="hd-btn-book">Book OPD</a>
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


# 5. assets/js/site-search.js
with open('assets/js/site-search.js', 'r', encoding='utf-8') as f:
    search_js = f.read()

target_doc = "{ n: 'Dr. Anil Bansal', s: 'HOD - Radiology', u: 'dr-anil-bansal.html', h: MULTI },"
new_entry = target_doc + "\n        { n: 'Dr. Priyanka Chhabra', s: 'Senior Consultant Radiologist & Director', u: 'dr-priyanka-chhabra.html', h: BOTH },"

if target_doc in search_js:
    if 'Dr. Priyanka Chhabra' not in search_js:
        search_js = search_js.replace(target_doc, new_entry)
        with open('assets/js/site-search.js', 'w', encoding='utf-8') as f:
            f.write(search_js)
        print("Updated assets/js/site-search.js")
    else:
        print("assets/js/site-search.js already contains Dr. Priyanka Chhabra")
else:
    print("WARNING: target_doc not found in assets/js/site-search.js")


# 6. opd-schedule.html
with open('opd-schedule.html', 'r', encoding='utf-8') as f:
    opd_html = f.read()

old_opd_row = '''                        <tr class="opd-row" data-doctor="dr-priyanka-chhabra" data-category="others"
                            data-days="Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
                            data-search="dr. priyanka chhabra mbbs, dmrd (radiology) · consultant – radiology radiodiagnosis &amp; imaging sukhda medpark monday tuesday wednesday thursday friday saturday">
                            <td style="color:var(--muted);font-weight:700;">17</td>
                            <td>
                                <div class="doc-cell">
                                    <span class="opd-doc-name">Dr. Priyanka Chhabra</span>
                                    <span class="opd-doc-qual">DMRD (Radiology) · Consultant – Radiology</span>
                                </div>
                            </td>
                            <td>
                                <div class="dept-cell">
                                    <a href="radiodiagnosis-and-imaging.html" class="opd-dept-link">Radiodiagnosis &amp; Imaging</a>
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
                                            style="width:12px;height:12px"></i> 09:00 AM – 05:00 PM</span>
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

new_opd_row = '''                        <tr class="opd-row" data-doctor="dr-priyanka-chhabra" data-category="others"
                            data-days="Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
                            data-search="dr. priyanka chhabra mbbs, dmrd, edir, dicri · senior consultant radiologist &amp; director radiodiagnosis &amp; imaging sukhda medpark monday tuesday wednesday thursday friday saturday">
                            <td style="color:var(--muted);font-weight:700;">17</td>
                            <td>
                                <div class="doc-cell">
                                    <a href="dr-priyanka-chhabra.html" class="opd-doc-name" style="color:var(--blue);text-decoration:none;font-weight:700;">Dr. Priyanka Chhabra</a>
                                    <span class="opd-doc-qual">MBBS, DMRD, EDiR, DICRI · Senior Consultant Radiologist &amp; Director</span>
                                </div>
                            </td>
                            <td>
                                <div class="dept-cell">
                                    <a href="radiodiagnosis-and-imaging.html" class="opd-dept-link">Radiodiagnosis &amp; Imaging</a>
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
                                            style="width:12px;height:12px"></i> 09:00 AM – 05:00 PM</span>
                                </div>
                            </td>
                            <td>
                                <span class="status-badge available" data-status-badge><i data-lucide="check-circle"
                                        style="width:11px;height:11px"></i> Doctor Available</span>
                            </td>
                            <td style="text-align: right;">
                                <div class="action-btns" style="justify-content: flex-end;">
                                    <a href="dr-priyanka-chhabra.html" class="btn-book-opd" style="background:#eaf1f8;color:var(--blue);margin-right:6px;"><i data-lucide="user"></i> Profile</a>
                                    <a href="contact.html?doctor=dr-priyanka-chhabra" class="btn-book-opd"><i data-lucide="calendar"></i> Book</a>
                                </div>
                            </td>
                        </tr>'''

if old_opd_row in opd_html:
    opd_html = opd_html.replace(old_opd_row, new_opd_row)
    with open('opd-schedule.html', 'w', encoding='utf-8') as f:
        f.write(opd_html)
    print("Updated opd-schedule.html")
else:
    print("WARNING: old_opd_row not found in opd-schedule.html")
