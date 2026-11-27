# update_sumit_links.py
import re

# 1. doctor.html
with open('doctor.html', 'r', encoding='utf-8') as f:
    doc_html = f.read()

old_doc_card = '''                <article class="doc-card" data-name="dr. sumit grover" data-speciality="Critical Care"
                    data-hospital="multispeciality"
                    data-tags="anaesthesia &amp; pain management consultant — anaesthesia &amp; pain management da (anaesthesiology)">
                    <div class="doc-card-top">
                        <img src="assets/images/doctors/latest/dr-sumit-grover.webp"
                            alt="Dr. Sumit Grover - Consultant — Anaesthesia &amp; Pain Management, Sukhda Hospital">
                    </div>
                    <div class="doc-card-body">
                        <span class="doc-location-pill pill-multi"><i data-lucide="map-pin"></i> Sukhda
                            Multispeciality</span>
                        <h3 class="doc-card-name">Dr. Sumit Grover</h3>
                        <div class="doc-card-desig">Consultant — Anaesthesia &amp; Pain Management</div>
                        <div class="doc-card-qual">DA (Anaesthesiology)</div>
                        <div class="doc-card-tags">
                            <span class="doc-tag">Anaesthesia &amp; Pain Management</span>
                        </div>
                        <div class="doc-card-actions">
                            <a href="opd-schedule.html" class="doc-btn-profile">View OPD Timings</a>
                        </div>
                    </div>
                </article>'''

new_doc_card = '''                <article class="doc-card" data-name="dr. sumit grover" data-speciality="Critical Care"
                    data-hospital="multispeciality"
                    data-tags="anaesthesia &amp; pain management consultant — anaesthesia &amp; pain management mbbs, d.a. (anaesthesiology)">
                    <div class="doc-card-top">
                        <img src="assets/images/doctors/latest/dr-sumit-grover.webp"
                            alt="Dr. Sumit Grover - Consultant — Anaesthesia &amp; Pain Management, Sukhda Hospital">
                    </div>
                    <div class="doc-card-body">
                        <span class="doc-location-pill pill-multi"><i data-lucide="map-pin"></i> Sukhda
                            Multispeciality</span>
                        <h3 class="doc-card-name"><a href="dr-sumit-grover.html">Dr. Sumit Grover</a></h3>
                        <div class="doc-card-desig">Consultant — Anaesthesia &amp; Pain Management</div>
                        <div class="doc-card-qual">MBBS, D.A. (Anaesthesiology)</div>
                        <div class="doc-card-tags">
                            <span class="doc-tag">Anaesthesia &amp; Pain Management</span>
                        </div>
                        <div class="doc-card-actions">
                            <a href="dr-sumit-grover.html" class="doc-btn-profile">View Profile</a>
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
                            <img src="assets/images/doctors/latest/dr-sumit-grover.webp" alt="Dr. Sumit Grover" loading="lazy">
                        </div>
                        <div class="doctor-body">
                            <h3>Dr. Sumit Grover</h3>
                            <div class="doc-spec">Consultant – Anaesthesia &amp; Pain Management</div>
                            <div class="doc-hosp">Sukhda Multispeciality Hospital</div>
                        </div>
                    </a>'''

new_idx_card = '''                    <a href="dr-sumit-grover.html" class="doctor-card">
                        <div class="doctor-photo">
                            <img src="assets/images/doctors/latest/dr-sumit-grover.webp" alt="Dr. Sumit Grover" loading="lazy">
                        </div>
                        <div class="doctor-body">
                            <h3>Dr. Sumit Grover</h3>
                            <div class="doc-spec">Consultant – Anaesthesia &amp; Pain Management</div>
                            <div class="doc-hosp">Sukhda Multispeciality Hospital</div>
                        </div>
                    </a>'''

if old_idx_card in index_html:
    index_html = index_html.replace(old_idx_card, new_idx_card)
    print("Updated doctor slider card in index.html")
else:
    print("WARNING: old_idx_card not found in index.html")

old_searchable = "{ name: 'Dr. Sumit Grover', sub: 'DA (Anaesthesiology) • Consultant — Anaesthesia & Pain Management', cat: 'Doctor', badge: 'doc', url: 'opd-schedule.html' },"
new_searchable = "{ name: 'Dr. Sumit Grover', sub: 'MBBS, D.A. (Anaesthesiology) • Consultant — Anaesthesia & Pain Management', cat: 'Doctor', badge: 'doc', url: 'dr-sumit-grover.html' },"

if old_searchable in index_html:
    index_html = index_html.replace(old_searchable, new_searchable)
    print("Updated searchableData in index.html")
else:
    print("WARNING: old_searchable not found in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)


# 3. anaesthesia-and-pain-management.html
with open('anaesthesia-and-pain-management.html', 'r', encoding='utf-8') as f:
    anaes_html = f.read()

old_anaes_card = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-sumit-grover.webp"
                            alt="Dr. Sumit Grover - Consultant — Anaesthesia &amp; Pain Management" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Sumit Grover</a></h3>
                        <div class="hd-desig">Consultant — Anaesthesia &amp; Pain Management</div>
                        <div class="hd-qual">DA (Anaesthesiology)</div>
                        <div class="hd-actions">
                            <a href="opd-schedule.html" class="hd-btn-profile">View OPD</a>
                            <a href="contact.html" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

new_anaes_card = '''                <article class="hd-card">
                    <a href="dr-sumit-grover.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-sumit-grover.webp"
                            alt="Dr. Sumit Grover - Consultant — Anaesthesia &amp; Pain Management" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-sumit-grover.html">Dr. Sumit Grover</a></h3>
                        <div class="hd-desig">Consultant — Anaesthesia &amp; Pain Management</div>
                        <div class="hd-qual">MBBS, D.A. (Anaesthesiology)</div>
                        <div class="hd-actions">
                            <a href="dr-sumit-grover.html" class="hd-btn-profile">View Profile</a>
                            <a href="contact.html?doctor=dr-sumit-grover" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

if old_anaes_card in anaes_html:
    anaes_html = anaes_html.replace(old_anaes_card, new_anaes_card)
    with open('anaesthesia-and-pain-management.html', 'w', encoding='utf-8') as f:
        f.write(anaes_html)
    print("Updated anaesthesia-and-pain-management.html")
else:
    print("WARNING: old_anaes_card not found in anaesthesia-and-pain-management.html")


# 4. critical-care.html
with open('critical-care.html', 'r', encoding='utf-8') as f:
    cc_html = f.read()

old_cc_card = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-sumit-grover.webp"
                            alt="Dr. Sumit Grover - Consultant — Critical Care &amp; Anaesthesia" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Sumit Grover</a></h3>
                        <div class="hd-desig">Consultant — Critical Care &amp; Anaesthesia</div>
                        <div class="hd-qual">DA (Anaesthesiology)</div>
                        <div class="hd-actions">
                            <a href="opd-schedule.html" class="hd-btn-profile">View OPD</a>
                            <a href="contact.html" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

new_cc_card = '''                <article class="hd-card">
                    <a href="dr-sumit-grover.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-sumit-grover.webp"
                            alt="Dr. Sumit Grover - Consultant — Critical Care &amp; Anaesthesia" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-sumit-grover.html">Dr. Sumit Grover</a></h3>
                        <div class="hd-desig">Consultant — Critical Care &amp; Anaesthesia</div>
                        <div class="hd-qual">MBBS, D.A. (Anaesthesiology)</div>
                        <div class="hd-actions">
                            <a href="dr-sumit-grover.html" class="hd-btn-profile">View Profile</a>
                            <a href="contact.html?doctor=dr-sumit-grover" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

if old_cc_card in cc_html:
    cc_html = cc_html.replace(old_cc_card, new_cc_card)
    with open('critical-care.html', 'w', encoding='utf-8') as f:
        f.write(cc_html)
    print("Updated critical-care.html")
else:
    print("WARNING: old_cc_card not found in critical-care.html")


# 5. sukhda-multispecialty-hospital.html
with open('sukhda-multispecialty-hospital.html', 'r', encoding='utf-8') as f:
    multi_html = f.read()

old_multi_card = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-sumit-grover.webp"
                            alt="Dr. Sumit Grover - Consultant — Anaesthesia &amp; Pain Management" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Sumit Grover</a></h3>
                        <div class="hd-desig">Consultant — Anaesthesia &amp; Pain Management</div>
                        <div class="hd-qual">DA (Anaesthesiology)</div>
                        <div class="hd-actions">
                            <a href="opd-schedule.html" class="hd-btn-profile">View OPD</a>
                            <a href="contact.html" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

new_multi_card = '''                <article class="hd-card">
                    <a href="dr-sumit-grover.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-sumit-grover.webp"
                            alt="Dr. Sumit Grover - Consultant — Anaesthesia &amp; Pain Management" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-sumit-grover.html">Dr. Sumit Grover</a></h3>
                        <div class="hd-desig">Consultant — Anaesthesia &amp; Pain Management</div>
                        <div class="hd-qual">MBBS, D.A. (Anaesthesiology)</div>
                        <div class="hd-actions">
                            <a href="dr-sumit-grover.html" class="hd-btn-profile">View Profile</a>
                            <a href="contact.html?doctor=dr-sumit-grover" class="hd-btn-book">Book OPD</a>
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


# 6. assets/js/site-search.js
with open('assets/js/site-search.js', 'r', encoding='utf-8') as f:
    search_js = f.read()

target_doc = "{ n: 'Dr. Devilal Saharan', s: 'Anaesthesiology & Pain Management', u: 'dr-devilal.html', h: MULTI },"
new_entry = target_doc + "\n        { n: 'Dr. Sumit Grover', s: 'Consultant — Anaesthesia & Pain Management', u: 'dr-sumit-grover.html', h: BOTH },"

if target_doc in search_js:
    if 'Dr. Sumit Grover' not in search_js:
        search_js = search_js.replace(target_doc, new_entry)
        with open('assets/js/site-search.js', 'w', encoding='utf-8') as f:
            f.write(search_js)
        print("Updated assets/js/site-search.js")
    else:
        print("assets/js/site-search.js already contains Dr. Sumit Grover")
else:
    print("WARNING: target_doc not found in assets/js/site-search.js")


# 7. opd-schedule.html
with open('opd-schedule.html', 'r', encoding='utf-8') as f:
    opd_html = f.read()

old_opd_row = '''                        <tr class="opd-row" data-doctor="dr-sumit-grover" data-category="others"
                            data-days="Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
                            data-search="dr. sumit grover da (anaesthesiology) anaesthesia &amp; pain management monday tuesday wednesday thursday friday saturday">
                            <td style="color:var(--muted);font-weight:700;">19</td>
                            <td>
                                <div class="doc-cell">
                                    <span class="opd-doc-name">Dr. Sumit Grover</span>
                                    <span class="opd-doc-qual">DA (Anaesthesiology)</span>
                                </div>
                            </td>
                            <td>
                                <div class="dept-cell">
                                    <a href="anaesthesia-and-pain-management.html" class="opd-dept-link">Anaesthesia &amp; Pain
                                        Management</a>
                                    <a href="sukhda-multispecialty-hospital.html" class="hospital-tag"><i
                                            data-lucide="building" style="width:11px;height:11px"></i> Sukhda
                                        Multispeciality Hospital</a>
                                </div>
                            </td>
                            <td>
                                <span class="days-badge">Mon – Sat</span>
                            </td>
                            <td>
                                <div class="time-slots">
                                    <span class="time-pill morning"><i data-lucide="phone-call"
                                            style="width:12px;height:12px"></i> Timings: please call the OPD desk</span>
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

new_opd_row = '''                        <tr class="opd-row" data-doctor="dr-sumit-grover" data-category="others"
                            data-days="Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
                            data-search="dr. sumit grover mbbs, d.a. (anaesthesiology) anaesthesia &amp; pain management critical care monday tuesday wednesday thursday friday saturday">
                            <td style="color:var(--muted);font-weight:700;">19</td>
                            <td>
                                <div class="doc-cell">
                                    <a href="dr-sumit-grover.html" class="opd-doc-name" style="color:var(--blue);text-decoration:none;font-weight:700;">Dr. Sumit Grover</a>
                                    <span class="opd-doc-qual">MBBS, D.A. (Anaesthesiology) · Consultant – Anaesthesia &amp; Pain Management</span>
                                </div>
                            </td>
                            <td>
                                <div class="dept-cell">
                                    <a href="anaesthesia-and-pain-management.html" class="opd-dept-link">Anaesthesia &amp; Pain
                                        Management</a>
                                    <a href="sukhda-multispecialty-hospital.html" class="hospital-tag"><i
                                            data-lucide="building" style="width:11px;height:11px"></i> Sukhda
                                        Multispeciality Hospital</a>
                                </div>
                            </td>
                            <td>
                                <span class="days-badge">Mon – Sat</span>
                            </td>
                            <td>
                                <div class="time-slots">
                                    <span class="time-pill morning"><i data-lucide="phone-call"
                                            style="width:12px;height:12px"></i> Timings: please call the OPD desk</span>
                                </div>
                            </td>
                            <td>
                                <span class="status-badge available" data-status-badge><i data-lucide="check-circle"
                                        style="width:11px;height:11px"></i> Doctor Available</span>
                            </td>
                            <td style="text-align: right;">
                                <div class="action-btns" style="justify-content: flex-end;">
                                    <a href="dr-sumit-grover.html" class="btn-book-opd" style="background:#eaf1f8;color:var(--blue);margin-right:6px;"><i data-lucide="user"></i> Profile</a>
                                    <a href="contact.html?doctor=dr-sumit-grover" class="btn-book-opd"><i data-lucide="calendar"></i> Book</a>
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
