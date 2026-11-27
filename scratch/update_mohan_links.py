# update_mohan_links.py
import re

# 1. doctor.html
with open('doctor.html', 'r', encoding='utf-8') as f:
    doc_html = f.read()

old_doc_card = '''                <article class="doc-card" data-name="dr. mohan lal" data-speciality="Radiation Oncology"
                    data-hospital="medpark"
                    data-tags="radiation oncology senior consultant &amp; hod — radiation oncology mbbs, md (radiation oncology)">
                    <div class="doc-card-top">
                        <img src="assets/images/doctors/latest/dr-mohanlal.webp"
                            alt="Dr. Mohan Lal - Senior Consultant &amp; HOD — Radiation Oncology, Sukhda Hospital">
                    </div>
                    <div class="doc-card-body">
                        <span class="doc-location-pill pill-medpark"><i data-lucide="map-pin"></i> Sukhda MedPark</span>
                        <h3 class="doc-card-name">Dr. Mohan Lal</h3>
                        <div class="doc-card-desig">Senior Consultant &amp; HOD — Radiation Oncology</div>
                        <div class="doc-card-qual">MBBS, MD (Radiation Oncology)</div>
                        <div class="doc-card-tags">
                            <span class="doc-tag">Radiation Oncology</span>
                        </div>
                        <div class="doc-card-actions">
                            <a href="opd-schedule.html" class="doc-btn-profile">View OPD Timings</a>
                        </div>
                    </div>
                </article>'''

new_doc_card = '''                <article class="doc-card" data-name="dr. mohan lal" data-speciality="Radiation Oncology"
                    data-hospital="medpark"
                    data-tags="radiation oncology senior consultant &amp; hod — radiation oncology mbbs, md (radiation oncology)">
                    <div class="doc-card-top">
                        <img src="assets/images/doctors/latest/dr-mohanlal.webp"
                            alt="Dr. Mohan Lal - Senior Consultant &amp; HOD — Radiation Oncology, Sukhda Hospital">
                    </div>
                    <div class="doc-card-body">
                        <span class="doc-location-pill pill-medpark"><i data-lucide="map-pin"></i> Sukhda MedPark</span>
                        <h3 class="doc-card-name"><a href="dr-mohan-lal.html">Dr. Mohan Lal</a></h3>
                        <div class="doc-card-desig">Senior Consultant &amp; HOD — Radiation Oncology</div>
                        <div class="doc-card-qual">MBBS, MD (Radiation Oncology), Fellow (Medanta)</div>
                        <div class="doc-card-tags">
                            <span class="doc-tag">Radiation Oncology</span>
                        </div>
                        <div class="doc-card-actions">
                            <a href="dr-mohan-lal.html" class="doc-btn-profile">View Profile</a>
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
                            <img src="assets/images/doctors/latest/dr-mohanlal.webp" alt="Dr. Mohan Lal" loading="lazy">
                        </div>
                        <div class="doctor-body">
                            <h3>Dr. Mohan Lal</h3>
                            <div class="doc-spec">Senior Consultant &amp; HOD – Radiation Oncology</div>
                            <div class="doc-hosp">Sukhda MedPark</div>
                        </div>
                    </a>'''

new_idx_card = '''                    <a href="dr-mohan-lal.html" class="doctor-card">
                        <div class="doctor-photo">
                            <img src="assets/images/doctors/latest/dr-mohanlal.webp" alt="Dr. Mohan Lal" loading="lazy">
                        </div>
                        <div class="doctor-body">
                            <h3>Dr. Mohan Lal</h3>
                            <div class="doc-spec">Senior Consultant &amp; HOD – Radiation Oncology</div>
                            <div class="doc-hosp">Sukhda MedPark</div>
                        </div>
                    </a>'''

if old_idx_card in index_html:
    index_html = index_html.replace(old_idx_card, new_idx_card)
    print("Updated doctor slider card in index.html")
else:
    print("WARNING: old_idx_card not found in index.html")

old_searchable = "{ name: 'Dr. Mohan Lal', sub: 'MD (Radiation Oncology) • Senior Consultant & HOD — Radiation Oncology', cat: 'Doctor', badge: 'doc', url: 'opd-schedule.html' },"
new_searchable = "{ name: 'Dr. Mohan Lal', sub: 'MD (Radiation Oncology) • Senior Consultant & HOD — Radiation Oncology', cat: 'Doctor', badge: 'doc', url: 'dr-mohan-lal.html' },"

if old_searchable in index_html:
    index_html = index_html.replace(old_searchable, new_searchable)
    print("Updated searchableData in index.html")
else:
    print("WARNING: old_searchable not found in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)


# 3. radiation-oncology.html
with open('radiation-oncology.html', 'r', encoding='utf-8') as f:
    rad_html = f.read()

old_rad_card = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-mohanlal.webp"
                            alt="Dr. Mohan Lal - Senior Consultant &amp; HOD — Radiation Oncology" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Mohan Lal</a></h3>
                        <div class="hd-desig">Senior Consultant &amp; HOD — Radiation Oncology</div>
                        <div class="hd-qual">MBBS, MD (Radiation Oncology)</div>
                        <div class="hd-actions">
                            <a href="opd-schedule.html" class="hd-btn-profile">View OPD</a>
                            <a href="contact.html" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

new_rad_card = '''                <article class="hd-card">
                    <a href="dr-mohan-lal.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-mohanlal.webp"
                            alt="Dr. Mohan Lal - Senior Consultant &amp; HOD — Radiation Oncology" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-mohan-lal.html">Dr. Mohan Lal</a></h3>
                        <div class="hd-desig">Senior Consultant &amp; HOD — Radiation Oncology</div>
                        <div class="hd-qual">MBBS, MD (Radiation Oncology), Fellow (Medanta)</div>
                        <div class="hd-actions">
                            <a href="dr-mohan-lal.html" class="hd-btn-profile">View Profile</a>
                            <a href="contact.html?doctor=dr-mohan-lal" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

if old_rad_card in rad_html:
    rad_html = rad_html.replace(old_rad_card, new_rad_card)
    with open('radiation-oncology.html', 'w', encoding='utf-8') as f:
        f.write(rad_html)
    print("Updated radiation-oncology.html")
else:
    print("WARNING: old_rad_card not found in radiation-oncology.html")


# 4. sukhda-medpark-hospital.html
with open('sukhda-medpark-hospital.html', 'r', encoding='utf-8') as f:
    medpark_html = f.read()

old_medpark_card = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-mohanlal.webp"
                            alt="Dr. Mohan Lal - Senior Consultant &amp; HOD — Radiation Oncology" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Mohan Lal</a></h3>
                        <div class="hd-desig">Senior Consultant &amp; HOD — Radiation Oncology</div>
                        <div class="hd-qual">MBBS, MD (Radiation Oncology)</div>
                        <div class="hd-actions">
                            <a href="opd-schedule.html" class="hd-btn-profile">View OPD</a>
                            <a href="contact.html" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

new_medpark_card = '''                <article class="hd-card">
                    <a href="dr-mohan-lal.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-mohanlal.webp"
                            alt="Dr. Mohan Lal - Senior Consultant &amp; HOD — Radiation Oncology" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-mohan-lal.html">Dr. Mohan Lal</a></h3>
                        <div class="hd-desig">Senior Consultant &amp; HOD — Radiation Oncology</div>
                        <div class="hd-qual">MBBS, MD (Radiation Oncology), Fellow (Medanta)</div>
                        <div class="hd-actions">
                            <a href="dr-mohan-lal.html" class="hd-btn-profile">View Profile</a>
                            <a href="contact.html?doctor=dr-mohan-lal" class="hd-btn-book">Book OPD</a>
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

target_doc = "{ n: 'Dr. Trivikrama Rao', s: 'Consultant - Medical Oncology', u: 'dr-trivikrama-rao.html', h: BOTH },"
new_entry = target_doc + "\n        { n: 'Dr. Mohan Lal', s: 'Senior Consultant & HOD — Radiation Oncology', u: 'dr-mohan-lal.html', h: MEDPARK },"

if target_doc in search_js:
    if 'Dr. Mohan Lal' not in search_js:
        search_js = search_js.replace(target_doc, new_entry)
        with open('assets/js/site-search.js', 'w', encoding='utf-8') as f:
            f.write(search_js)
        print("Updated assets/js/site-search.js")
    else:
        print("assets/js/site-search.js already contains Dr. Mohan Lal")
else:
    print("WARNING: target_doc not found in assets/js/site-search.js")


# 6. opd-schedule.html
with open('opd-schedule.html', 'r', encoding='utf-8') as f:
    opd_html = f.read()

old_opd_row = '''                        <tr class="opd-row" data-doctor="dr-mohan-lal" data-category="oncology"
                            data-days="Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
                            data-search="dr. mohan lal mbbs, md (radiation oncology) · senior consultant &amp; hod – radiation oncology radiation oncology monday tuesday wednesday thursday friday saturday 10:00 am – 05:00 pm">
                            <td style="color:var(--muted);font-weight:700;">6</td>
                            <td>
                                <div class="doc-cell">
                                    <span class="opd-doc-name">Dr. Mohan Lal</span>
                                    <span class="opd-doc-qual">MBBS, MD (Radiation Oncology) · Senior Consultant &amp;
                                        HOD – Radiation Oncology</span>
                                </div>
                            </td>
                            <td>
                                <div class="dept-cell">
                                    <a href="radiation-oncology.html" class="opd-dept-link">Radiation Oncology</a>
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
                                            style="width:12px;height:12px"></i> 10:00 AM – 05:00 PM</span>
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

new_opd_row = '''                        <tr class="opd-row" data-doctor="dr-mohan-lal" data-category="oncology"
                            data-days="Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
                            data-search="dr. mohan lal mbbs, md (radiation oncology) · senior consultant &amp; hod – radiation oncology radiation oncology monday tuesday wednesday thursday friday saturday 10:00 am – 05:00 pm">
                            <td style="color:var(--muted);font-weight:700;">6</td>
                            <td>
                                <div class="doc-cell">
                                    <a href="dr-mohan-lal.html" class="opd-doc-name" style="color:var(--blue);text-decoration:none;font-weight:700;">Dr. Mohan Lal</a>
                                    <span class="opd-doc-qual">MBBS, MD (Radiation Oncology), Fellow (Medanta) · Senior Consultant &amp;
                                        HOD – Radiation Oncology</span>
                                </div>
                            </td>
                            <td>
                                <div class="dept-cell">
                                    <a href="radiation-oncology.html" class="opd-dept-link">Radiation Oncology</a>
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
                                            style="width:12px;height:12px"></i> 10:00 AM – 05:00 PM</span>
                                </div>
                            </td>
                            <td>
                                <span class="status-badge available" data-status-badge><i data-lucide="check-circle"
                                        style="width:11px;height:11px"></i> Doctor Available</span>
                            </td>
                            <td style="text-align: right;">
                                <div class="action-btns" style="justify-content: flex-end;">
                                    <a href="dr-mohan-lal.html" class="btn-book-opd" style="background:#eaf1f8;color:var(--blue);margin-right:6px;"><i data-lucide="user"></i> Profile</a>
                                    <a href="contact.html?doctor=dr-mohan-lal" class="btn-book-opd"><i data-lucide="calendar"></i> Book</a>
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
