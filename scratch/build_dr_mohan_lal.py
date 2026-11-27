import re

with open('dr-ankit-gawri.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Title & Meta
title = "Dr. Mohan Lal — Senior Consultant &amp; HOD — Radiation Oncology | Sukhda Healthcare Hisar"
desc = "Dr. Mohan Lal, MBBS, MD (Radiation Oncology), Fellow Medanta. Senior Consultant &amp; HOD — Radiation Oncology at Sukhda MedPark Hospital, Hisar. 21+ years experience in IMRT, IGRT, SBRT, SRS, VMAT, and HDR Brachytherapy. Book OPD or call +91 9268421705."

html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html, count=1)
html = re.sub(r'<meta name="description"[\s\S]*?>', f'<meta name="description"\n        content="{desc}">', html, count=1)

# Canonical and Schema injection
html = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://sukhdahospitals.com/dr-mohan-lal.html">', html, count=1)

schema_json = '''<script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Physician",
      "name": "Dr. Mohan Lal",
      "url": "https://sukhdahospitals.com/dr-mohan-lal.html",
      "image": "https://sukhdahospitals.com/assets/images/doctors/latest/dr-mohanlal.webp",
      "description": "Dr. Mohan Lal, MBBS, MD (Radiation Oncology), Fellow Medanta. Senior Consultant & HOD — Radiation Oncology at Sukhda MedPark Hospital, Hisar. Over 21 years of experience in advanced radiation oncology and cancer care.",
      "medicalSpecialty": [
        "Radiation Oncology",
        "Oncology",
        "Cancer Care",
        "Clinical Oncology"
      ],
      "knowsAbout": [
        "Advanced Radiation Therapy (IMRT, IGRT, SBRT, SRS & SRT)",
        "DIBH (Deep Inspiration Breath Hold)",
        "VMAT (RapidArc)",
        "3D Conformal Radiotherapy",
        "HDR Brachytherapy",
        "Radiation Treatment Planning & Contouring",
        "Palliative Care & Pain Management",
        "Chemotherapy, Immunotherapy & Targeted Therapy"
      ],
      "alumniOf": [
        {
          "@type": "EducationalOrganization",
          "name": "Pt. B. D. Sharma University of Medical Sciences, Rohtak"
        },
        {
          "@type": "EducationalOrganization",
          "name": "Medanta Cancer Institute, Gurugram"
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
    r'<div class="crumb">[\s\S]*?<span>Dr\. Ankit Gawri</span>\s*</div>',
    '''<div class="crumb">
                <a href="index.html">Home</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <a href="doctor.html">Doctors</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <span>Dr. Mohan Lal</span>
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
                    <img src="assets/images/doctors/latest/dr-mohanlal.webp" alt="Dr. Mohan Lal — Senior Consultant &amp; HOD, Radiation Oncology, Sukhda Hospital Hisar">
                </div>

                <div class="doc-hero-info">
                    <div class="doc-top-tags">
                        <span class="pill-verified"><i data-lucide="shield-check" style="width:14px;height:14px"></i>
                            Senior Consultant &amp; HOD</span>
                        <a href="radiation-oncology.html" class="pill-dept-link"><i data-lucide="shield"
                                style="width:14px;height:14px"></i> Radiation Oncology</a>
                        <a href="sukhda-medpark-hospital.html" class="pill-hosp-link"><i data-lucide="building-2"
                                style="width:14px;height:14px;color:#278132"></i> Sukhda MedPark</a>
                    </div>

                    <h1>Dr. Mohan Lal</h1>
                    <div class="doc-degrees">MBBS, MD (Radiation Oncology), Fellow Precision Beam RT (Medanta)</div>
                    <div class="doc-role">Senior Consultant &amp; HOD — Radiation Oncology</div>

                    <div class="doc-hero-stats">
                        <div class="stat-item">
                            <b>21+ Years</b>
                            <small>Clinical Oncology Experience</small>
                        </div>
                        <div class="stat-item">
                            <b>Precision RT Specialist</b>
                            <small>LINAC, VMAT, SBRT, SRS &amp; HDR Brachytherapy</small>
                        </div>
                    </div>

                    <div class="doc-hero-actions">
                        <a href="#appointment" class="btn green"><i data-lucide="calendar-check"></i> Book OPD
                            Consultation</a>
                        <a href="https://wa.me/919268421705?text=Hello%20Dr.+Mohan+Lal,%20I%20would%20like%20to%20inquire%20about%20radiation%20oncology%20consultation"
                            target="_blank" rel="noopener" class="btn whatsapp"><svg class="wa-icon-svg"
                                xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"
                                style="vertical-align:middle;flex-shrink:0;margin-right:6px" aria-hidden="true">
                                <path fill="#ffffff"
                                    d="M12.004 2C6.486 2 2 6.486 2 12.004c0 1.956.564 3.784 1.543 5.334L2.2 21.8l4.634-1.306A9.948 9.948 0 0012.004 22c5.518 0 10.004-4.486 10.004-9.996C22.008 6.486 17.522 2 12.004 2z" />
                                <path fill="#25D366" fill-rule="evenodd" clip-rule="evenodd"
                                    d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z" />
                            </svg> WhatsApp Query</a>
                        <a href="tel:919268421705" class="btn outline"
                            style="color:#fff;border-color:rgba(255,255,255,0.35);background:rgba(255,255,255,0.08)"><i
                                data-lucide="phone"></i> +91 92684-21705</a>
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
                            <p>Dr. Mohan Lal has over 21 years of clinical experience in treating various types of cancer. He specializes in advanced radiation therapy techniques, including IMRT, IGRT, SBRT, SRS, SRT, DIBH, RapidArc/VMAT, 3D Conformal Radiotherapy, and HDR Brachytherapy.</p>
                            <p>He also has extensive experience in administering chemotherapy, immunotherapy, hormonal therapy, and targeted therapy. He is highly skilled in managing complex cancer cases, radiation treatment planning, and palliative care. Additionally, he has contributed to national and international medical research publications.</p>
                        </div>
                    </article>

                    <!-- B. OPD TIMINGS & CONSULTATION LOCATION -->
                    <article class="content-card">
                        <h3><i data-lucide="clock"></i> OPD Schedule &amp; Hospital Location</h3>
                        <div class="opd-grid">
                            <div class="opd-item">
                                <div class="opd-loc">
                                    <b>Sukhda MedPark Hospital</b>
                                    <small><i data-lucide="map-pin"
                                            style="width:14px;height:14px;color:var(--green)"></i> NH 1P-4P, Sector-5, Hisar - 125005</small>
                                </div>
                                <div class="opd-time">
                                    <span class="days">Mon – Sat</span>
                                    <span class="hours">10:00 AM – 05:00 PM</span>
                                    <span class="room">Radiation Oncology &amp; LINAC Centre</span>
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
                                    <span class="hours">Consultation by Prior Appointment</span>
                                    <span class="room">Comprehensive Cancer Care Clinic</span>
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
                                <span>Advanced Radiation Therapy (IMRT, IGRT, SBRT, SRS &amp; SRT), DIBH</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>VMAT (RapidArc) &amp; 3D Conformal Radiotherapy</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>HDR Brachytherapy</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Radiation Treatment Planning &amp; Contouring</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Palliative Care &amp; Pain Management</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Comprehensive Cancer Management</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Chemotherapy, Immunotherapy &amp; Targeted Therapy</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Head &amp; Neck, Breast, Cervical, Lung &amp; Brain Malignancies</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Prostate, Rectal, Bladder Cancers &amp; Bone Sarcomas</span>
                            </div>
                        </div>
                    </article>

                    <!-- D. EDUCATION & QUALIFICATIONS -->
                    <article class="content-card">
                        <h3><i data-lucide="graduation-cap"></i> Educational Qualification</h3>
                        <div class="timeline">
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>Fellowship in Precision External Beam Radiation Therapy – Medanta Cancer Institute, Gurugram (2012–2013)</h4>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>MD in Radiation Oncology (Clinical Oncology) – Pt. B. D. Sharma University of Medical Sciences, Rohtak (2005–2008)</h4>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>MBBS – Pt. B. D. Sharma University of Medical Sciences, Rohtak (1997–2002)</h4>
                            </div>
                        </div>
                    </article>

                    <!-- E. PROFESSIONAL EXPERIENCE -->
                    <article class="content-card">
                        <h3><i data-lucide="briefcase"></i> Professional Experience</h3>
                        <div class="bio-text" style="margin-bottom:14px">
                            <p>Dr. Mohan Lal has worked at several prestigious institutions, including Safdarjung Hospital, New Delhi; Medanta Hospital, Gurugram; Asian Hospital, Faridabad; Kainos Hospital, Rohtak; and American Oncology Institute, Hisar (Sarvodaya and Sarvesh Hospitals).</p>
                            <p>He has extensive experience in the radiation treatment of various types of cancer, including head and neck, breast, cervical, endometrial, lung, oesophageal, brain, prostate, rectal, and urinary bladder cancers, as well as bone tumours and sarcomas.</p>
                        </div>
                        <ul class="pub-list">
                            <li>Safdarjung Hospital, New Delhi</li>
                            <li>Medanta Hospital, Gurugram</li>
                            <li>Asian Hospital, Faridabad</li>
                            <li>Kainos Hospital, Rohtak</li>
                            <li>American Oncology Institute, Hisar (Sarvodaya and Sarvesh Hospitals)</li>
                            <li>Senior Consultant &amp; Head, Department of Radiation Oncology – Sukhda Healthcare (MedPark &amp; Multispeciality)</li>
                        </ul>
                    </article>

                    <!-- F. ACHIEVEMENTS & ACADEMIC CONTRIBUTIONS -->
                    <article class="content-card">
                        <h3><i data-lucide="trophy"></i> Achievements &amp; Academic Contributions</h3>
                        <p style="font-weight:700;color:var(--blue);margin-bottom:10px;">Publications in Various National and International Journals:</p>
                        <ul class="pub-list">
                            <li>Smart Study Series: Radiology (2010)</li>
                            <li>Indian Journal of Cancer (2012)</li>
                            <li>Asian Journal of Radiation Oncology (2013)</li>
                            <li>Indian Journal of Surgical Oncology (2015)</li>
                            <li>Archives of Surgical Oncology (2018)</li>
                            <li>Brachytherapy (2025)</li>
                            <li>Oncology (2026)</li>
                            <li>Frontiers in Oncology (2026)</li>
                        </ul>
                    </article>

                    <!-- G. PATIENT CARE PHILOSOPHY -->
                    <article class="content-card">
                        <h3><i data-lucide="heart-handshake"></i> Patient Care Philosophy</h3>
                        <div class="bio-text">
                            <p style="font-size:15px;line-height:1.8;color:#243a53;font-style:italic;background:#f3f9f4;border-left:4px solid var(--green);padding:18px 22px;border-radius:0 10px 10px 0;margin:0">
                                &ldquo;Dr. Mohan Lal believes in providing compassionate, personalised and evidence-based cancer care, focusing on each patient's individual needs. He is committed to delivering advanced cancer treatments while prioritising patient comfort, quality of life, pain management and overall well-being.&rdquo;
                            </p>
                        </div>
                    </article>

                    <!-- H. IMMEDIATE ASSISTANCE -->
                    <div class="sidebar-direct-card" style="margin-top: 8px;">
                        <h4><i data-lucide="headphones" style="width:18px;height:18px;vertical-align:middle;margin-right:6px"></i> Need Immediate Assistance?</h4>
                        <p>Our radiation oncology coordinators and hospital reception are available to guide and assist you with appointments.</p>
                        <div style="display:flex;gap:14px;flex-wrap:wrap;">
                            <a href="tel:01662249473" class="direct-phone-btn" style="flex:1;min-width:180px">
                                <span><i data-lucide="phone-call" style="vertical-align:middle;margin-right:6px"></i> 01662-249473</span>
                                <small>24*7 Hospital Desk</small>
                            </a>
                            <a href="tel:919268421705" class="direct-phone-btn" style="flex:1;min-width:180px">
                                <span><i data-lucide="phone" style="vertical-align:middle;margin-right:6px"></i> +91 92684-21705</span>
                                <small>Doctor Direct Line</small>
                            </a>
                            <a href="https://wa.me/919268421705?text=Hello%20Dr.+Mohan+Lal,%20I%20would%20like%20to%20inquire%20about%20radiation%20oncology%20consultation" target="_blank" rel="noopener" class="direct-phone-btn" style="flex:1;min-width:180px;background:#25D366;border-color:#25D366">
                                <span><svg class="wa-icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" style="vertical-align:middle;flex-shrink:0;margin-right:6px" aria-hidden="true"><path fill="#ffffff" d="M12.004 2C6.486 2 2 6.486 2 12.004c0 1.956.564 3.784 1.543 5.334L2.2 21.8l4.634-1.306A9.948 9.948 0 0012.004 22c5.518 0 10.004-4.486 10.004-9.996C22.008 6.486 17.522 2 12.004 2z"/><path fill="#25D366" fill-rule="evenodd" clip-rule="evenodd" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg>WhatsApp Desk</span>
                                <small>+91 92684-21705</small>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- RIGHT SIDEBAR'''

html = html.replace(old_main_match.group(0), new_main)

# 5. Sidebar Booking Widget Updates
html = html.replace('Direct consultation with Dr. Ankit Gawri', 'Direct consultation with Dr. Mohan Lal')
html = html.replace('value="dr-ankit-gawri"', 'value="dr-mohan-lal"')
html = html.replace('value="Dr. Ankit Gawri (Orthopaedics &amp; Robotic Joint Replacement)"', 'value="Dr. Mohan Lal (Radiation Oncology)"')

# 6. Colleague section
old_colleagues_match = re.search(r'<div class="other-docs-grid">[\s\S]*?</div>\s*</div>\s*</section>', html)
if not old_colleagues_match:
    raise Exception("Could not find colleagues section")

new_colleagues = '''<div class="other-docs-grid">
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
                    <img class="colleague-img" src="assets/images/doctors/latest/dr-amit-kumar-garg1.webp" alt="Dr. Amit Kumar Garg">
                    <div class="colleague-body">
                        <h4>Dr. Amit Kumar Garg</h4>
                        <div class="col-deg">MBBS, MS, DNB, MCh (Surgical Oncology)</div>
                        <div class="col-spec">Consultant Surgical Oncologist</div>
                        <a href="dr-amit-kumar-garg.html" class="btn-profile">View Profile →</a>
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

with open('dr-mohan-lal.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Generated dr-mohan-lal.html")
