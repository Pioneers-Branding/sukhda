import re

with open('dr-priyanka-chhabra.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Title & Meta
title = "Dr. Sumit Grover — Consultant — Anaesthesia &amp; Pain Management | Sukhda Healthcare Hisar"
desc = "Dr. Sumit Grover, MBBS, D.A. (Anaesthesiology). Consultant — Anaesthesia, Critical Care & Pain Management at Sukhda Multispeciality Hospital, Hisar. Experienced in Neuro-Anaesthesia, Cardiac ICU, and OT/Cath Lab anaesthesia. Book OPD or call +91 7015380751."

html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html, count=1)
html = re.sub(r'<meta name="description"[\s\S]*?>', f'<meta name="description"\n        content="{desc}">', html, count=1)

# Canonical and Schema injection
html = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://sukhdahospitals.com/dr-sumit-grover.html">', html, count=1)

schema_json = '''<script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Physician",
      "name": "Dr. Sumit Grover",
      "url": "https://sukhdahospitals.com/dr-sumit-grover.html",
      "image": "https://sukhdahospitals.com/assets/images/doctors/latest/dr-sumit-grover.webp",
      "description": "Dr. Sumit Grover, MBBS, D.A. (Anaesthesiology). Consultant — Anaesthesia, Critical Care & Pain Management at Sukhda Multispeciality Hospital, Hisar.",
      "medicalSpecialty": [
        "Anesthesia",
        "Critical Care",
        "Pain Management",
        "Neuro-Anesthesia"
      ],
      "knowsAbout": [
        "General Anaesthesia & Regional Anaesthesia",
        "Neuro-Anaesthesia & Neurocritical Care",
        "Cardiac Anaesthesia & Cardiac ICU Management",
        "Critical Care & Intensive Care Management",
        "OT Anaesthesia Services",
        "Cath Lab Anaesthesia",
        "Perioperative Patient Monitoring",
        "Pain Management & Patient Safety"
      ],
      "alumniOf": [
        {
          "@type": "EducationalOrganization",
          "name": "Tribhuvan University"
        },
        {
          "@type": "EducationalOrganization",
          "name": "Himalayan Institute of Medical Sciences, Dehradun"
        }
      ],
      "hospitalAffiliation": [
        {
          "@type": "Hospital",
          "name": "Sukhda Multispeciality Hospital",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "Opposite Green Belt, Delhi Road",
            "addressLocality": "Hisar",
            "addressRegion": "Haryana",
            "postalCode": "125001",
            "addressCountry": "IN"
          },
          "telephone": "+91-1662-249473"
        },
        {
          "@type": "Hospital",
          "name": "Sukhda MedPark Hospital",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "NH 1P-4P, Sector-5",
            "addressLocality": "Hisar",
            "addressRegion": "Haryana",
            "postalCode": "125005",
            "addressCountry": "IN"
          },
          "telephone": "+91-1662-249473"
        }
      ]
    }
    </script>'''

html = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>', schema_json, html, count=1)

# 2. Breadcrumb
html = re.sub(
    r'<div class="crumb">[\s\S]*?<span>Dr\. Priyanka Chhabra</span>\s*</div>',
    '''<div class="crumb">
                <a href="index.html">Home</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <a href="doctor.html">Doctors</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <span>Dr. Sumit Grover</span>
            </div>''',
    html,
    count=1
)

# 3. Hero Section
old_hero_match = re.search(r'<div class="doc-hero-grid">[\s\S]*?</div>\s*</div>\s*</section>', html)
if not old_hero_match:
    raise Exception("Could not find hero section")

new_hero = '''<div class="doc-hero-grid">
                <div class="doc-photo-box">
                    <img src="assets/images/doctors/latest/dr-sumit-grover.webp" alt="Dr. Sumit Grover — Consultant, Anaesthesia &amp; Pain Management, Sukhda Hospital Hisar">
                </div>

                <div class="doc-hero-info">
                    <div class="doc-top-tags">
                        <span class="pill-verified"><i data-lucide="shield-check" style="width:14px;height:14px"></i>
                            Consultant</span>
                        <a href="anaesthesia-and-pain-management.html" class="pill-dept-link"><i data-lucide="syringe"
                                style="width:14px;height:14px"></i> Anaesthesia &amp; Pain Management</a>
                        <a href="sukhda-multispecialty-hospital.html" class="pill-hosp-link"><i data-lucide="building-2"
                                style="width:14px;height:14px;color:#278132"></i> Both Locations</a>
                    </div>

                    <h1>Dr. Sumit Grover</h1>
                    <div class="doc-degrees">MBBS, D.A. (Anaesthesiology)</div>
                    <div class="doc-role">Consultant — Anaesthesia &amp; Pain Management</div>

                    <div class="doc-hero-stats">
                        <div class="stat-item">
                            <b>Anaesthesia &amp; Critical Care</b>
                            <small>OT, ICU &amp; Cath Lab Specialist</small>
                        </div>
                        <div class="stat-item">
                            <b>Neuro &amp; Cardiac Care</b>
                            <small>Intensive Perioperative Care</small>
                        </div>
                    </div>

                    <div class="doc-hero-actions">
                        <a href="#appointment" class="btn green"><i data-lucide="calendar-check"></i> Book OPD
                            Consultation</a>
                        <a href="https://wa.me/917015380751?text=Hello%20Dr.+Sumit+Grover,%20I%20would%20like%20to%20inquire%20about%20anaesthesia%20consultation"
                            target="_blank" rel="noopener" class="btn whatsapp"><svg class="wa-icon-svg"
                                xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"
                                style="vertical-align:middle;flex-shrink:0;margin-right:6px" aria-hidden="true">
                                <path fill="#ffffff"
                                    d="M12.004 2C6.486 2 2 6.486 2 12.004c0 1.956.564 3.784 1.543 5.334L2.2 21.8l4.634-1.306A9.948 9.948 0 0012.004 22c5.518 0 10.004-4.486 10.004-9.996C22.008 6.486 17.522 2 12.004 2z" />
                                <path fill="#25D366" fill-rule="evenodd" clip-rule="evenodd"
                                    d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z" />
                            </svg> WhatsApp Query</a>
                        <a href="tel:917015380751" class="btn outline"
                            style="color:#fff;border-color:rgba(255,255,255,0.35);background:rgba(255,255,255,0.08)"><i
                                data-lucide="phone"></i> +91 70153-80751</a>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

html = html.replace(old_hero_match.group(0), new_hero)

# 4. Main Left Column
old_main_match = re.search(r'<div class="doc-main-col">[\s\S]*?</div>\s*<!-- RIGHT SIDEBAR', html)
if not old_main_match:
    raise Exception("Could not find doc-main-col")

new_main = '''<div class="doc-main-col">

                    <!-- A. ABOUT THE DOCTOR -->
                    <article class="content-card">
                        <h3><i data-lucide="user-check"></i> Introduction</h3>
                        <div class="bio-text">
                            <p>Dr. Sumit Grover is an experienced Anaesthesiologist with expertise in Anaesthesia, Critical Care, Neuro-Anaesthesia, and Cardiac ICU Management. He holds an MBBS and Diploma in Anaesthesia, with experience in reputed hospitals. He specializes in OT, ICU, and Cath Lab anaesthesia services, focusing on patient safety and quality care. Experienced in managing complex clinical cases and providing comprehensive perioperative care with a patient-centred approach.</p>
                        </div>
                    </article>

                    <!-- B. OPD TIMINGS & CONSULTATION LOCATION -->
                    <article class="content-card">
                        <h3><i data-lucide="clock"></i> Clinical Schedule &amp; Hospital Locations</h3>
                        <div class="opd-grid">
                            <div class="opd-item">
                                <div class="opd-loc">
                                    <b>Sukhda Multispeciality Hospital</b>
                                    <small><i data-lucide="map-pin"
                                            style="width:14px;height:14px;color:var(--green)"></i> Opposite Green Belt, Delhi Road, Hisar - 125001</small>
                                </div>
                                <div class="opd-time">
                                    <span class="days">Mon – Sat</span>
                                    <span class="hours">09:00 AM – 05:00 PM (24*7 Emergency OT &amp; ICU Coverage)</span>
                                    <span class="room">OT, ICU &amp; Anaesthesia Consultation</span>
                                </div>
                                <div>
                                    <a href="#appointment" class="btn primary"
                                        style="padding:8px 16px;font-size:13px"><i data-lucide="calendar"></i> Book
                                        Slot</a>
                                </div>
                            </div>
                            <div class="opd-item">
                                <div class="opd-loc">
                                    <b>Sukhda MedPark Hospital</b>
                                    <small><i data-lucide="map-pin"
                                            style="width:14px;height:14px;color:var(--green)"></i> NH 1P-4P, Sector-5, Hisar - 125005</small>
                                </div>
                                <div class="opd-time">
                                    <span class="days">Mon – Sat</span>
                                    <span class="hours">Consultation by Prior Appointment</span>
                                    <span class="room">Surgical &amp; Oncology Perioperative Services</span>
                                </div>
                                <div>
                                    <a href="#appointment" class="btn primary"
                                        style="padding:8px 16px;font-size:13px"><i data-lucide="calendar"></i> Book
                                        Slot</a>
                                </div>
                            </div>
                        </div>
                    </article>

                    <!-- C. AREAS OF CLINICAL EXPERTISE -->
                    <article class="content-card">
                        <h3><i data-lucide="stethoscope"></i> Areas of Expertise</h3>
                        <div class="speciality-chips">
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>General Anaesthesia &amp; Regional Anaesthesia</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Neuro-Anaesthesia &amp; Neurocritical Care</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Cardiac Anaesthesia &amp; Cardiac ICU Management</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Critical Care &amp; Intensive Care Management</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>OT Anaesthesia Services</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Cath Lab Anaesthesia</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Perioperative Patient Monitoring</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Pain Management &amp; Patient Safety</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Airway Management &amp; Resuscitation</span>
                            </div>
                        </div>
                    </article>

                    <!-- D. EDUCATION & QUALIFICATIONS -->
                    <article class="content-card">
                        <h3><i data-lucide="graduation-cap"></i> Educational Qualification</h3>
                        <div class="timeline">
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>Diploma in Anaesthesia – Himalayan Institute of Medical Sciences, Swami Rama Himalayan University, Dehradun (2017)</h4>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>MBBS – Tribhuvan University (2010)</h4>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>Senior Secondary (CBSE) – Hisar, Haryana (2001)</h4>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>Secondary (CBSE) – Hisar, Haryana (1999)</h4>
                            </div>
                        </div>
                    </article>

                    <!-- E. PROFESSIONAL EXPERIENCE -->
                    <article class="content-card">
                        <h3><i data-lucide="briefcase"></i> Professional Experience</h3>
                        <ul class="pub-list">
                            <li>Junior Resident – Surgery, BSA Hospital, New Delhi (2012)</li>
                            <li>Junior Resident – CTVS &amp; Cardiology, Safdarjung Hospital, New Delhi (2012–2013)</li>
                            <li>Medical Officer – Cardiac ICU, Jindal Institute of Medical Sciences, Hisar (2013–2015)</li>
                            <li>Resident – Anaesthesia, Himalayan Institute of Medical Sciences, Dehradun (2015–2017)</li>
                            <li>Senior Resident – Neuro-Anaesthesia &amp; Neurocritical Care, Max Super Speciality Hospital, Dehradun (2017–2018)</li>
                            <li>Consultant Anaesthesiologist – Sarvodaya Hospital, Hisar (2018–2021)</li>
                            <li>Freelance Consultant – Akarsh Hospital, Sonakshi IVF Centre, Sukhda Hospital &amp; Sapra Hospital (2021–2026)</li>
                            <li>Consultant Anaesthesiologist – Sarvodaya Hospital, Hisar (May 2026–October)</li>
                            <li>Consultant — Anaesthesia &amp; Pain Management, Sukhda Healthcare</li>
                        </ul>
                    </article>

                    <!-- F. ACHIEVEMENTS & ACADEMIC CONTRIBUTIONS -->
                    <article class="content-card">
                        <h3><i data-lucide="trophy"></i> Achievements &amp; Academic Contributions</h3>
                        <ul class="pub-list">
                            <li>Clinical experience in Anaesthesia and Critical Care.</li>
                            <li>Experience in Neuro-Anaesthesia and Cardiac ICU Management.</li>
                            <li>Expertise in OT, ICU, and Cath Lab Anaesthesia Services.</li>
                            <li>Extensive clinical practice across leading tertiary multi-speciality hospitals.</li>
                        </ul>
                    </article>

                    <!-- G. PATIENT CARE PHILOSOPHY -->
                    <article class="content-card">
                        <h3><i data-lucide="heart-handshake"></i> Patient Care Philosophy</h3>
                        <div class="bio-text">
                            <p style="font-size:15px;line-height:1.8;color:#243a53;font-style:italic;background:#f3f9f4;border-left:4px solid var(--green);padding:18px 22px;border-radius:0 10px 10px 0;margin:0">
                                &ldquo;Committed to providing safe, compassionate, and patient-centred anaesthesia care. Focuses on patient safety, effective pain management, and continuous monitoring to ensure optimal outcomes throughout surgical and critical care procedures.&rdquo;
                            </p>
                        </div>
                    </article>

                    <!-- H. IMMEDIATE ASSISTANCE -->
                    <div class="sidebar-direct-card" style="margin-top: 8px;">
                        <h4><i data-lucide="headphones" style="width:18px;height:18px;vertical-align:middle;margin-right:6px"></i> Need Immediate Assistance?</h4>
                        <p>Our anaesthesia and critical care coordinators are available 24 hours a day to assist you.</p>
                        <div style="display:flex;gap:14px;flex-wrap:wrap;">
                            <a href="tel:01662249473" class="direct-phone-btn" style="flex:1;min-width:180px">
                                <span><i data-lucide="phone-call" style="vertical-align:middle;margin-right:6px"></i> 01662-249473</span>
                                <small>24*7 Hospital Desk</small>
                            </a>
                            <a href="tel:917015380751" class="direct-phone-btn" style="flex:1;min-width:180px">
                                <span><i data-lucide="phone" style="vertical-align:middle;margin-right:6px"></i> +91 70153-80751</span>
                                <small>Doctor Direct Line</small>
                            </a>
                            <a href="https://wa.me/917015380751?text=Hello%20Dr.+Sumit+Grover,%20I%20would%20like%20to%20inquire%20about%20anaesthesia%20consultation" target="_blank" rel="noopener" class="direct-phone-btn" style="flex:1;min-width:180px;background:#25D366;border-color:#25D366">
                                <span><svg class="wa-icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" style="vertical-align:middle;flex-shrink:0;margin-right:6px" aria-hidden="true"><path fill="#ffffff" d="M12.004 2C6.486 2 2 6.486 2 12.004c0 1.956.564 3.784 1.543 5.334L2.2 21.8l4.634-1.306A9.948 9.948 0 0012.004 22c5.518 0 10.004-4.486 10.004-9.996C22.008 6.486 17.522 2 12.004 2z"/><path fill="#25D366" fill-rule="evenodd" clip-rule="evenodd" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg>WhatsApp Desk</span>
                                <small>+91 70153-80751</small>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- RIGHT SIDEBAR'''

html = html.replace(old_main_match.group(0), new_main)

# 5. Sidebar Booking Widget Updates
html = html.replace('Direct consultation with Dr. Priyanka Chhabra', 'Direct consultation with Dr. Sumit Grover')
html = html.replace('value="dr-priyanka-chhabra"', 'value="dr-sumit-grover"')
html = html.replace('value="Dr. Priyanka Chhabra (Radiodiagnosis &amp; Imaging)"', 'value="Dr. Sumit Grover (Anaesthesia &amp; Pain Management)"')

# 6. Colleague section
old_colleagues_match = re.search(r'<div class="other-docs-grid">[\s\S]*?</div>\s*</div>\s*</section>', html)
if not old_colleagues_match:
    raise Exception("Could not find colleagues section")

new_colleagues = '''<div class="other-docs-grid">
                <article class="colleague-card">
                    <img class="colleague-img" src="assets/images/doctors/latest/dr-devilal1.webp" alt="Dr. Devilal Saharan">
                    <div class="colleague-body">
                        <h4>Dr. Devilal Saharan</h4>
                        <div class="col-deg">D.A. (Anaesthesiology)</div>
                        <div class="col-spec">Consultant Anaesthesiologist &amp; Pain Specialist</div>
                        <a href="dr-devilal.html" class="btn-profile">View Profile →</a>
                    </div>
                </article>
                <article class="colleague-card">
                    <img class="colleague-img" src="assets/images/doctors/latest/dr-amit-mehta1.webp" alt="Dr. Amit Mehta">
                    <div class="colleague-body">
                        <h4>Dr. Amit Mehta</h4>
                        <div class="col-deg">MBBS, MD (Medicine) · AIIMS, New Delhi</div>
                        <div class="col-spec">Director &amp; Head — Internal Medicine &amp; Critical Care</div>
                        <a href="dr-amit-mehta.html" class="btn-profile">View Profile →</a>
                    </div>
                </article>
                <article class="colleague-card">
                    <img class="colleague-img" src="assets/images/doctors/latest/dr-deepam-das1.webp" alt="Dr. Deepam Das">
                    <div class="colleague-body">
                        <h4>Dr. Deepam Das</h4>
                        <div class="col-deg">MBBS, MS (General Surgery), FIAGES, FMAS</div>
                        <div class="col-spec">HOD — Laparoscopic &amp; Bariatric Surgery</div>
                        <a href="dr-deepam-das.html" class="btn-profile">View Profile →</a>
                    </div>
                </article>
                <article class="colleague-card">
                    <img class="colleague-img" src="assets/images/doctors/latest/dr-anil-khyalia1.webp" alt="Dr. Anil Khyalia">
                    <div class="colleague-body">
                        <h4>Dr. Anil Khyalia</h4>
                        <div class="col-deg">MBBS, MS, MCh (Neurosurgery)</div>
                        <div class="col-spec">Brain and Spine Surgeon</div>
                        <a href="dr-anil-khyalia.html" class="btn-profile">View Profile →</a>
                    </div>
                </article>
            </div>
        </div>
    </section>'''

html = html.replace(old_colleagues_match.group(0), new_colleagues)

with open('dr-sumit-grover.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Generated dr-sumit-grover.html")
