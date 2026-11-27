# update_ankit_links.py
import re

# 1. doctor.html
with open('doctor.html', 'r', encoding='utf-8') as f:
    doc_html = f.read()

old_doc_card = '''                <article class="doc-card" data-name="dr. ankit gawri" data-speciality="Orthopaedics"
                    data-hospital="multispeciality"
                    data-tags="robotic joint replacement consultant — orthopaedics &amp; robotic joint replacement mbbs, ms (orthopaedics), fnb (arthroplasty)">
                    <div class="doc-card-top">
                        <img src="assets/images/doctors/latest/dr-ankit-gawri.webp"
                            alt="Dr. Ankit Gawri - Consultant — Orthopaedics &amp; Robotic Joint Replacement, Sukhda Hospital">
                    </div>
                    <div class="doc-card-body">
                        <span class="doc-location-pill pill-multi"><i data-lucide="map-pin"></i> Sukhda
                            Multispeciality</span>
                        <h3 class="doc-card-name">Dr. Ankit Gawri</h3>
                        <div class="doc-card-desig">Consultant — Orthopaedics &amp; Robotic Joint Replacement</div>
                        <div class="doc-card-qual">MBBS, MS (Orthopaedics), FNB (Arthroplasty)</div>
                        <div class="doc-card-tags">
                            <span class="doc-tag">Robotic Joint Replacement</span>
                        </div>
                        <div class="doc-card-actions">
                            <a href="opd-schedule.html" class="doc-btn-profile">View OPD Timings</a>
                        </div>
                    </div>
                </article>'''

new_doc_card = '''                <article class="doc-card" data-name="dr. ankit gawri" data-speciality="Orthopaedics"
                    data-hospital="multispeciality"
                    data-tags="robotic joint replacement consultant — orthopaedics &amp; robotic joint replacement mbbs, ms (orthopaedics), fnb (arthroplasty)">
                    <div class="doc-card-top">
                        <img src="assets/images/doctors/latest/dr-ankit-gawri.webp"
                            alt="Dr. Ankit Gawri - Consultant — Orthopaedics &amp; Robotic Joint Replacement, Sukhda Hospital">
                    </div>
                    <div class="doc-card-body">
                        <span class="doc-location-pill pill-multi"><i data-lucide="map-pin"></i> Sukhda
                            Multispeciality</span>
                        <h3 class="doc-card-name"><a href="dr-ankit-gawri.html">Dr. Ankit Gawri</a></h3>
                        <div class="doc-card-desig">Consultant — Orthopaedics &amp; Robotic Joint Replacement</div>
                        <div class="doc-card-qual">MBBS, MS (Orthopaedics), FNB (Arthroplasty)</div>
                        <div class="doc-card-tags">
                            <span class="doc-tag">Robotic Joint Replacement</span>
                        </div>
                        <div class="doc-card-actions">
                            <a href="dr-ankit-gawri.html" class="doc-btn-profile">View Profile</a>
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
                            <img src="assets/images/doctors/latest/dr-ankit-gawri.webp" alt="Dr. Ankit Gawri" loading="lazy">
                        </div>
                        <div class="doctor-body">
                            <h3>Dr. Ankit Gawri</h3>
                            <div class="doc-spec">Consultant – Orthopaedics &amp; Joint Replacement</div>
                            <div class="doc-hosp">Sukhda Multispeciality Hospital</div>
                        </div>
                    </a>'''

new_idx_card = '''                    <a href="dr-ankit-gawri.html" class="doctor-card">
                        <div class="doctor-photo">
                            <img src="assets/images/doctors/latest/dr-ankit-gawri.webp" alt="Dr. Ankit Gawri" loading="lazy">
                        </div>
                        <div class="doctor-body">
                            <h3>Dr. Ankit Gawri</h3>
                            <div class="doc-spec">Consultant – Orthopaedics &amp; Joint Replacement</div>
                            <div class="doc-hosp">Sukhda Multispeciality Hospital</div>
                        </div>
                    </a>'''

if old_idx_card in index_html:
    index_html = index_html.replace(old_idx_card, new_idx_card)
    print("Updated doctor slider card in index.html")
else:
    print("WARNING: old_idx_card not found in index.html")

old_searchable = "{ name: 'Dr. Ankit Gawri', sub: 'MS (Orthopaedics), FNB (Arthroplasty) • Robotic Joint Replacement', cat: 'Doctor', badge: 'doc', url: 'opd-schedule.html' },"
new_searchable = "{ name: 'Dr. Ankit Gawri', sub: 'MS (Orthopaedics), FNB (Arthroplasty) • Robotic Joint Replacement', cat: 'Doctor', badge: 'doc', url: 'dr-ankit-gawri.html' },"

if old_searchable in index_html:
    index_html = index_html.replace(old_searchable, new_searchable)
    print("Updated searchableData in index.html")
else:
    print("WARNING: old_searchable not found in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)


# 3. orthopaedic-and-robotic-joint-replacement.html
with open('orthopaedic-and-robotic-joint-replacement.html', 'r', encoding='utf-8') as f:
    ortho_html = f.read()

old_ortho_card = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-ankit-gawri.webp"
                            alt="Dr. Ankit Gawri - Consultant — Orthopaedics &amp; Robotic Joint Replacement" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Ankit Gawri</a></h3>
                        <div class="hd-desig">Consultant — Orthopaedics &amp; Robotic Joint Replacement</div>
                        <div class="hd-qual">MBBS, MS (Orthopaedics), FNB (Arthroplasty)</div>
                        <div class="hd-actions">
                            <a href="opd-schedule.html" class="hd-btn-profile">View OPD</a>
                            <a href="contact.html" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

new_ortho_card = '''                <article class="hd-card">
                    <a href="dr-ankit-gawri.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-ankit-gawri.webp"
                            alt="Dr. Ankit Gawri - Consultant — Orthopaedics &amp; Robotic Joint Replacement" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-ankit-gawri.html">Dr. Ankit Gawri</a></h3>
                        <div class="hd-desig">Consultant — Orthopaedics &amp; Robotic Joint Replacement</div>
                        <div class="hd-qual">MBBS, MS (Orthopaedics), FNB (Arthroplasty)</div>
                        <div class="hd-actions">
                            <a href="dr-ankit-gawri.html" class="hd-btn-profile">View Profile</a>
                            <a href="contact.html?doctor=dr-ankit-gawri" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

if old_ortho_card in ortho_html:
    ortho_html = ortho_html.replace(old_ortho_card, new_ortho_card)
    with open('orthopaedic-and-robotic-joint-replacement.html', 'w', encoding='utf-8') as f:
        f.write(ortho_html)
    print("Updated orthopaedic-and-robotic-joint-replacement.html")
else:
    print("WARNING: old_ortho_card not found in orthopaedic-and-robotic-joint-replacement.html")


# 4. sukhda-multispecialty-hospital.html
with open('sukhda-multispecialty-hospital.html', 'r', encoding='utf-8') as f:
    multi_html = f.read()

old_multi_card = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-ankit-gawri.webp"
                            alt="Dr. Ankit Gawri - Consultant — Orthopaedics &amp; Robotic Joint Replacement"
                            loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Ankit Gawri</a></h3>
                        <div class="hd-desig">Consultant — Orthopaedics &amp; Robotic Joint Replacement</div>
                        <div class="hd-qual">MBBS, MS (Orthopaedics), FNB (Arthroplasty)</div>
                        <div class="hd-actions">
                            <a href="opd-schedule.html" class="hd-btn-profile">View OPD</a>
                            <a href="contact.html" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

new_multi_card = '''                <article class="hd-card">
                    <a href="dr-ankit-gawri.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-ankit-gawri.webp"
                            alt="Dr. Ankit Gawri - Consultant — Orthopaedics &amp; Robotic Joint Replacement"
                            loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-ankit-gawri.html">Dr. Ankit Gawri</a></h3>
                        <div class="hd-desig">Consultant — Orthopaedics &amp; Robotic Joint Replacement</div>
                        <div class="hd-qual">MBBS, MS (Orthopaedics), FNB (Arthroplasty)</div>
                        <div class="hd-actions">
                            <a href="dr-ankit-gawri.html" class="hd-btn-profile">View Profile</a>
                            <a href="contact.html?doctor=dr-ankit-gawri" class="hd-btn-book">Book OPD</a>
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


# 5. assets/js/site-search.js
with open('assets/js/site-search.js', 'r', encoding='utf-8') as f:
    search_js = f.read()

target_doc = "{ n: 'Dr. Pankaj Sharma', s: 'Joint Replacement, Arthroscopy & Sports Injury', u: 'dr-pankaj-sharma.html', h: MULTI },"
new_entry = target_doc + "\n        { n: 'Dr. Ankit Gawri', s: 'Consultant — Orthopaedics & Robotic Joint Replacement', u: 'dr-ankit-gawri.html', h: MULTI },"

if target_doc in search_js:
    if 'Dr. Ankit Gawri' not in search_js:
        search_js = search_js.replace(target_doc, new_entry)
        with open('assets/js/site-search.js', 'w', encoding='utf-8') as f:
            f.write(search_js)
        print("Updated assets/js/site-search.js")
    else:
        print("assets/js/site-search.js already contains Dr. Ankit Gawri")
else:
    print("WARNING: target_doc not found in assets/js/site-search.js")


# 6. opd-schedule.html
with open('opd-schedule.html', 'r', encoding='utf-8') as f:
    opd_html = f.read()

old_opd_row = '''                        <tr class="opd-row" data-doctor="dr-ankit-gawri" data-category="ortho"
                            data-days="Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
                            data-search="dr. ankit gawri mbbs, ms (orthopaedics), fnb (arthroplasty) – nbe certified orthopaedics &amp; joint replacement monday tuesday wednesday thursday friday saturday 09:00 am – 05:00 pm">
                            <td style="color:var(--muted);font-weight:700;">13</td>
                            <td>
                                <div class="doc-cell">
                                    <span class="opd-doc-name">Dr. Ankit Gawri</span>
                                    <span class="opd-doc-qual">MBBS, MS (Orthopaedics), FNB (Arthroplasty) – NBE
                                        Certified</span>
                                </div>
                            </td>
                            <td>
                                <div class="dept-cell">
                                    <a href="orthopaedic-and-robotic-joint-replacement.html" class="opd-dept-link">Orthopaedics &amp; Robotic Joint
                                        Replacement</a>
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

new_opd_row = '''                        <tr class="opd-row" data-doctor="dr-ankit-gawri" data-category="ortho"
                            data-days="Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
                            data-search="dr. ankit gawri mbbs, ms (orthopaedics), fnb (arthroplasty) – nbe certified orthopaedics &amp; joint replacement monday tuesday wednesday thursday friday saturday 09:00 am – 05:00 pm">
                            <td style="color:var(--muted);font-weight:700;">13</td>
                            <td>
                                <div class="doc-cell">
                                    <a href="dr-ankit-gawri.html" class="opd-doc-name" style="color:var(--blue);text-decoration:none;font-weight:700;">Dr. Ankit Gawri</a>
                                    <span class="opd-doc-qual">MBBS, MS (Orthopaedics), FNB (Arthroplasty) – NBE
                                        Certified</span>
                                </div>
                            </td>
                            <td>
                                <div class="dept-cell">
                                    <a href="orthopaedic-and-robotic-joint-replacement.html" class="opd-dept-link">Orthopaedics &amp; Robotic Joint
                                        Replacement</a>
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
                                    <a href="dr-ankit-gawri.html" class="btn-book-opd" style="background:#eaf1f8;color:var(--blue);margin-right:6px;"><i data-lucide="user"></i> Profile</a>
                                    <a href="contact.html?doctor=dr-ankit-gawri" class="btn-book-opd"><i data-lucide="calendar"></i> Book</a>
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
