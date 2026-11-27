import re

with open('dr-mohan-lal.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Title & Meta
title = "Dr. Priyanka Chhabra — Senior Consultant Radiologist &amp; Director — Radiodiagnosis &amp; Imaging | Sukhda Healthcare Hisar"
desc = "Dr. Priyanka Chhabra, MBBS, DMRD, EDiR, DICRI. Senior Consultant Radiologist & Director, Department of Radiodiagnosis & Imaging at Sukhda MedPark Hospital, Hisar. 20+ years of post-PG experience in CT, MRI, onco-imaging, and cross-sectional imaging. Book consultation or call +91 94666 38426."

html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html, count=1)
html = re.sub(r'<meta name="description"[\s\S]*?>', f'<meta name="description"\n        content="{desc}">', html, count=1)

# Canonical and Schema injection
html = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://sukhdahospitals.com/dr-priyanka-chhabra.html">', html, count=1)

schema_json = '''<script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Physician",
      "name": "Dr. Priyanka Chhabra",
      "url": "https://sukhdahospitals.com/dr-priyanka-chhabra.html",
      "image": "https://sukhdahospitals.com/assets/images/doctors/latest/dr-priyanka-chabra.webp",
      "description": "Dr. Priyanka Chhabra, MBBS, DMRD, EDiR, DICRI. Senior Consultant Radiologist & Director, Department of Radiodiagnosis & Imaging at Sukhda MedPark Hospital, Hisar.",
      "medicalSpecialty": [
        "Radiology",
        "Diagnostic Radiology",
        "Cross-sectional Imaging",
        "Onco-imaging",
        "Neuro-Radiology"
      ],
      "knowsAbout": [
        "Onco-imaging",
        "Head & Neck Imaging",
        "Neuro-Radiology",
        "Chest & Abdominal Imaging",
        "Doppler Studies",
        "Obstetric Ultrasound & Follicular Monitoring",
        "Advanced Cross-sectional Imaging",
        "1.5T MRI Examination & Reporting",
        "64-Slice CT Reporting"
      ],
      "alumniOf": [
        {
          "@type": "EducationalOrganization",
          "name": "JLN Medical College, Ajmer"
        },
        {
          "@type": "EducationalOrganization",
          "name": "PGIMS, Rohtak"
        },
        {
          "@type": "EducationalOrganization",
          "name": "European Society of Radiology (ESR)"
        },
        {
          "@type": "EducationalOrganization",
          "name": "Indian College of Radiology & Imaging (ICRI)"
        },
        {
          "@type": "EducationalOrganization",
          "name": "DY Patil, Pune"
        }
      ],
      "hospitalAffiliation": [
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
        },
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
        }
      ]
    }
    </script>'''

html = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>', schema_json, html, count=1)

# 2. Breadcrumb
html = re.sub(
    r'<div class="crumb">[\s\S]*?<span>Dr\. Mohan Lal</span>\s*</div>',
    '''<div class="crumb">
                <a href="index.html">Home</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <a href="doctor.html">Doctors</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <span>Dr. Priyanka Chhabra</span>
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
                    <img src="assets/images/doctors/latest/dr-priyanka-chabra.webp" alt="Dr. Priyanka Chhabra — Senior Consultant Radiologist &amp; Director, Radiodiagnosis &amp; Imaging, Sukhda Hospital Hisar">
                </div>

                <div class="doc-hero-info">
                    <div class="doc-top-tags">
                        <span class="pill-verified"><i data-lucide="shield-check" style="width:14px;height:14px"></i>
                            Director &amp; Senior Consultant</span>
                        <a href="radiodiagnosis-and-imaging.html" class="pill-dept-link"><i data-lucide="scan"
                                style="width:14px;height:14px"></i> Radiodiagnosis &amp; Imaging</a>
                        <a href="sukhda-medpark-hospital.html" class="pill-hosp-link"><i data-lucide="building-2"
                                style="width:14px;height:14px;color:#278132"></i> Both Locations</a>
                    </div>

                    <h1>Dr. Priyanka Chhabra</h1>
                    <div class="doc-degrees">MBBS, DMRD, EDiR, DICRI</div>
                    <div class="doc-role">Senior Consultant Radiologist &amp; Director, Department of Radiodiagnosis &amp; Imaging</div>

                    <div class="doc-hero-stats">
                        <div class="stat-item">
                            <b>20+ Years</b>
                            <small>Post-PG Diagnostic Radiology Experience</small>
                        </div>
                        <div class="stat-item">
                            <b>EDiR &amp; DICRI</b>
                            <small>European &amp; National Radiology Diplomate</small>
                        </div>
                    </div>

                    <div class="doc-hero-actions">
                        <a href="#appointment" class="btn green"><i data-lucide="calendar-check"></i> Book Imaging /
                            Consultation</a>
                        <a href="https://wa.me/919466638426?text=Hello%20Dr.+Priyanka+Chhabra,%20I%20would%20like%20to%20inquire%20about%20radiology%20consultation"
                            target="_blank" rel="noopener" class="btn whatsapp"><svg class="wa-icon-svg"
                                xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"
                                style="vertical-align:middle;flex-shrink:0;margin-right:6px" aria-hidden="true">
                                <path fill="#ffffff"
                                    d="M12.004 2C6.486 2 2 6.486 2 12.004c0 1.956.564 3.784 1.543 5.334L2.2 21.8l4.634-1.306A9.948 9.948 0 0012.004 22c5.518 0 10.004-4.486 10.004-9.996C22.008 6.486 17.522 2 12.004 2z" />
                                <path fill="#25D366" fill-rule="evenodd" clip-rule="evenodd"
                                    d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z" />
                            </svg> WhatsApp Query</a>
                        <a href="tel:919466638426" class="btn outline"
                            style="color:#fff;border-color:rgba(255,255,255,0.35);background:rgba(255,255,255,0.08)"><i
                                data-lucide="phone"></i> +91 94666-38426</a>
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
                            <p>Dr. Priyanka Chhabra is a Senior Consultant Radiologist with over 20+ years of post-PG experience in Diagnostic Radiology and Advanced Cross-sectional Imaging. She has expertise in reporting complex CT and MRI examinations, with special interests in Head &amp; Neck Imaging, Women's Imaging, Onco-imaging, and Body Imaging.</p>
                        </div>
                    </article>

                    <!-- B. OPD TIMINGS & CONSULTATION LOCATION -->
                    <article class="content-card">
                        <h3><i data-lucide="clock"></i> Reporting Schedule &amp; Hospital Locations</h3>
                        <div class="opd-grid">
                            <div class="opd-item">
                                <div class="opd-loc">
                                    <b>Sukhda MedPark Hospital</b>
                                    <small><i data-lucide="map-pin"
                                            style="width:14px;height:14px;color:var(--green)"></i> NH 1P-4P, Sector-5, Hisar - 125005</small>
                                </div>
                                <div class="opd-time">
                                    <span class="days">Mon – Sat</span>
                                    <span class="hours">09:00 AM – 05:00 PM</span>
                                    <span class="room">Advanced MRI, CT &amp; Cross-sectional Imaging</span>
                                </div>
                                <div>
                                    <a href="#appointment" class="btn primary"
                                        style="padding:8px 16px;font-size:13px"><i data-lucide="calendar"></i> Book
                                        Slot</a>
                                </div>
                            </div>
                            <div class="opd-item">
                                <div class="opd-loc">
                                    <b>Sukhda Multispeciality Hospital</b>
                                    <small><i data-lucide="map-pin"
                                            style="width:14px;height:14px;color:var(--green)"></i> Opposite Green Belt, Delhi Road, Hisar - 125001</small>
                                </div>
                                <div class="opd-time">
                                    <span class="days">Mon – Sat</span>
                                    <span class="hours">09:00 AM – 05:00 PM (24/7 Emergency Coverage)</span>
                                    <span class="room">Ultrasound, Doppler &amp; Diagnostic Radiology</span>
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
                                <span>Onco-imaging</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Head &amp; Neck Imaging</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Neuro-Radiology</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Chest &amp; Abdominal Imaging</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Doppler Studies</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Obstetric Ultrasound &amp; Follicular Monitoring</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Advanced Cross-sectional Imaging</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>1.5T MRI Examination &amp; Reporting</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>64-Slice CT Reporting</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Women's Imaging &amp; Mammography</span>
                            </div>
                        </div>
                    </article>

                    <!-- D. EDUCATION & QUALIFICATIONS -->
                    <article class="content-card">
                        <h3><i data-lucide="graduation-cap"></i> Educational Qualification</h3>
                        <div class="timeline">
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>MBA (Hospital Administration &amp; Healthcare Management) – DY Patil, Pune (2022)</h4>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>EDiR (European Diploma in Radiology) – ESR (2020)</h4>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>DICRI – IRIA (2020)</h4>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>DMRD – PGIMS, Rohtak (2005)</h4>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>MBBS – JLN Medical College, Ajmer (2002)</h4>
                            </div>
                        </div>
                    </article>

                    <!-- E. PROFESSIONAL EXPERIENCE -->
                    <article class="content-card">
                        <h3><i data-lucide="briefcase"></i> Professional Experience</h3>
                        <div class="bio-text" style="margin-bottom:14px">
                            <p>Medical Superintendent &amp; HOD Jindal Institute of Medical Sciences, Hisar (Formerly). Clinical reporting of Ultrasound, CT &amp; MRI. Departmental administration and management. Quality assurance and supervision of radiology services. Teaching and mentoring DNB residents. Multidisciplinary and Tumour Board participation.</p>
                        </div>
                        <ul class="pub-list">
                            <li>Director, Department of Radiodiagnosis &amp; Imaging – Sukhda Healthcare (MedPark &amp; Multispeciality)</li>
                            <li>Former Medical Superintendent &amp; HOD – Jindal Institute of Medical Sciences, Hisar</li>
                            <li>Clinical reporting of Ultrasound, multislice CT &amp; 1.5T MRI examinations</li>
                            <li>Departmental administration, quality assurance, and supervision of radiology services</li>
                            <li>Teaching and mentoring DNB Radiology residents</li>
                            <li>Active participation in Multidisciplinary and Tumour Board clinical decision-making</li>
                        </ul>
                    </article>

                    <!-- F. ACHIEVEMENTS & ACADEMIC CONTRIBUTIONS -->
                    <article class="content-card">
                        <h3><i data-lucide="trophy"></i> Achievements &amp; Academic Contributions</h3>
                        <ul class="pub-list">
                            <li>Presented at IRIA Haryana State Conferences.</li>
                            <li>Multiple scientific posters at ECR 2020 (European Congress of Radiology).</li>
                            <li>Poster presentation at IRIA National Conference 2026.</li>
                            <li>Delivered academic lectures on Women's Imaging, PCOD, MRI Fistulogram and Thoracic Emergencies.</li>
                            <li>Awarded European Diploma in Radiology (EDiR) by the European Society of Radiology (ESR) in 2020.</li>
                            <li>Awarded Diplomate of ICRI (DICRI) by the Indian College of Radiology &amp; Imaging in 2020.</li>
                        </ul>
                    </article>

                    <!-- G. PATIENT CARE PHILOSOPHY -->
                    <article class="content-card">
                        <h3><i data-lucide="heart-handshake"></i> Patient Care Philosophy</h3>
                        <div class="bio-text">
                            <p style="font-size:15px;line-height:1.8;color:#243a53;font-style:italic;background:#f3f9f4;border-left:4px solid var(--green);padding:18px 22px;border-radius:0 10px 10px 0;margin:0">
                                &ldquo;Committed to delivering accurate, timely, and patient-centred diagnostic imaging services through clinical expertise, advanced imaging techniques, multidisciplinary collaboration, and continuous quality improvement.&rdquo;
                            </p>
                        </div>
                    </article>

                    <!-- H. IMMEDIATE ASSISTANCE -->
                    <div class="sidebar-direct-card" style="margin-top: 8px;">
                        <h4><i data-lucide="headphones" style="width:18px;height:18px;vertical-align:middle;margin-right:6px"></i> Need Immediate Assistance?</h4>
                        <p>Our imaging coordinators and hospital reception are available 24 hours a day to assist with diagnostic scans and reports.</p>
                        <div style="display:flex;gap:14px;flex-wrap:wrap;">
                            <a href="tel:01662249473" class="direct-phone-btn" style="flex:1;min-width:180px">
                                <span><i data-lucide="phone-call" style="vertical-align:middle;margin-right:6px"></i> 01662-249473</span>
                                <small>24/7 Hospital Desk</small>
                            </a>
                            <a href="tel:919466638426" class="direct-phone-btn" style="flex:1;min-width:180px">
                                <span><i data-lucide="phone" style="vertical-align:middle;margin-right:6px"></i> +91 94666-38426</span>
                                <small>Doctor Direct Line</small>
                            </a>
                            <a href="https://wa.me/919466638426?text=Hello%20Dr.+Priyanka+Chhabra,%20I%20would%20like%20to%20inquire%20about%20radiology%20consultation" target="_blank" rel="noopener" class="direct-phone-btn" style="flex:1;min-width:180px;background:#25D366;border-color:#25D366">
                                <span><svg class="wa-icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" style="vertical-align:middle;flex-shrink:0;margin-right:6px" aria-hidden="true"><path fill="#ffffff" d="M12.004 2C6.486 2 2 6.486 2 12.004c0 1.956.564 3.784 1.543 5.334L2.2 21.8l4.634-1.306A9.948 9.948 0 0012.004 22c5.518 0 10.004-4.486 10.004-9.996C22.008 6.486 17.522 2 12.004 2z"/><path fill="#25D366" fill-rule="evenodd" clip-rule="evenodd" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg>WhatsApp Desk</span>
                                <small>+91 94666-38426</small>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- RIGHT SIDEBAR'''

html = html.replace(old_main_match.group(0), new_main)

# 5. Sidebar Booking Widget Updates
html = html.replace('Direct consultation with Dr. Mohan Lal', 'Direct consultation with Dr. Priyanka Chhabra')
html = html.replace('value="dr-mohan-lal"', 'value="dr-priyanka-chhabra"')
html = html.replace('value="Dr. Mohan Lal (Radiation Oncology)"', 'value="Dr. Priyanka Chhabra (Radiodiagnosis &amp; Imaging)"')

# 6. Colleague section
old_colleagues_match = re.search(r'<div class="other-docs-grid">[\s\S]*?</div>\s*</div>\s*</section>', html)
if not old_colleagues_match:
    raise Exception("Could not find colleagues section")

new_colleagues = '''<div class="other-docs-grid">
                <article class="colleague-card">
                    <img class="colleague-img" src="assets/images/doctors/latest/dr-anil-bansal1.webp" alt="Dr. Anil Bansal">
                    <div class="colleague-body">
                        <h4>Dr. Anil Bansal</h4>
                        <div class="col-deg">MBBS, MD (Radiology)</div>
                        <div class="col-spec">HOD &amp; Senior Consultant — Radiodiagnosis</div>
                        <a href="dr-anil-bansal.html" class="btn-profile">View Profile →</a>
                    </div>
                </article>
                <article class="colleague-card">
                    <img class="colleague-img" src="assets/images/doctors/latest/dr-mohanlal.webp" alt="Dr. Mohan Lal">
                    <div class="colleague-body">
                        <h4>Dr. Mohan Lal</h4>
                        <div class="col-deg">MBBS, MD (Radiation Oncology), Fellow (Medanta)</div>
                        <div class="col-spec">Senior Consultant &amp; HOD — Radiation Oncology</div>
                        <a href="dr-mohan-lal.html" class="btn-profile">View Profile →</a>
                    </div>
                </article>
                <article class="colleague-card">
                    <img class="colleague-img" src="assets/images/doctors/latest/dr-trivikrama-rao1.webp" alt="Dr. Trivikrama Rao">
                    <div class="colleague-body">
                        <h4>Dr. Trivikrama Rao</h4>
                        <div class="col-deg">MBBS, DNB, DrNB (Medical Oncology), ECMO</div>
                        <div class="col-spec">Sr. Consultant Medical Oncologist</div>
                        <a href="dr-trivikrama-rao.html" class="btn-profile">View Profile →</a>
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
            </div>
        </div>
    </section>'''

html = html.replace(old_colleagues_match.group(0), new_colleagues)

with open('dr-priyanka-chhabra.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Generated dr-priyanka-chhabra.html")
