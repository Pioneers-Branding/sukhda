import re

with open('dr-hemant-dahiya.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Title & Meta
title = "Dr. Manaswi Gupta — Consultant Physician — Medicine &amp; Critical Care | Sukhda Healthcare Hisar"
desc = "Dr. Manaswi Gupta, MBBS, MD (General Medicine), FICE. Consultant Physician — Medicine &amp; Critical Care at Sukhda Multispeciality Hospital, Hisar. Expertise in critical care, multi-organ failure, diabetes, poisoning, and respiratory diseases. Book OPD or call 01662-249473."

html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html, count=1)
html = re.sub(r'<meta name="description"[\s\S]*?>', f'<meta name="description"\n        content="{desc}">', html, count=1)

# Canonical and Schema injection before </head>
schema_and_canonical = '''    <link rel="canonical" href="https://sukhdahospitals.com/dr-manaswi-gupta.html">
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Physician",
      "name": "Dr. Manaswi Gupta",
      "url": "https://sukhdahospitals.com/dr-manaswi-gupta.html",
      "image": "https://sukhdahospitals.com/assets/images/doctors/latest/dr-manaswi-gupta.webp",
      "description": "Dr. Manaswi Gupta, MBBS, MD (General Medicine), FICE. Consultant Physician — Medicine & Critical Care at Sukhda Multispeciality Hospital, Hisar.",
      "medicalSpecialty": [
        "Internal Medicine",
        "Critical Care Medicine",
        "General Medicine"
      ],
      "knowsAbout": [
        "Critical Care Medicine",
        "Management of Multiple Organ Failure",
        "Treatment of Poisoning, Snake bite",
        "Diabetes Management",
        "Hypertension Management",
        "Thyroid Disorders",
        "Fever & Infectious Diseases",
        "Respiratory Diseases (Asthma, COPD, Pneumonia, TB)",
        "Lifestyle Disease Management",
        "Chronic Pain-Related Issues",
        "Anxiety-Related Disorders",
        "Echocardiography (FICE)"
      ],
      "alumniOf": [
        {
          "@type": "EducationalOrganization",
          "name": "GMCH, Udaipur"
        },
        {
          "@type": "EducationalOrganization",
          "name": "SRMC Medical College, Chennai"
        },
        {
          "@type": "EducationalOrganization",
          "name": "JROP, New Delhi"
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
    </script>
</head>'''

html = html.replace('</head>', schema_and_canonical, 1)

# 2. Breadcrumb
html = re.sub(
    r'<div class="crumb">[\s\S]*?<span>Dr\. Hemant Dahiya</span>\s*</div>',
    '''<div class="crumb">
                <a href="index.html">Home</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <a href="doctor.html">Doctors</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <span>Dr. Manaswi Gupta</span>
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
                    <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp" alt="Dr. Manaswi Gupta — Consultant Physician, Medicine &amp; Critical Care, Sukhda Hospital Hisar">
                </div>

                <div class="doc-hero-info">
                    <div class="doc-top-tags">
                        <span class="pill-verified"><i data-lucide="shield-check" style="width:14px;height:14px"></i>
                            Consultant</span>
                        <a href="medicine-and-critical-care.html" class="pill-dept-link"><i data-lucide="stethoscope"
                                style="width:14px;height:14px"></i> Medicine &amp; Critical Care</a>
                        <a href="index.html#hospitals" class="pill-hosp-link"><i data-lucide="building-2"
                                style="width:14px;height:14px;color:#278132"></i> Both Locations</a>
                    </div>

                    <h1>Dr. Manaswi Gupta</h1>
                    <div class="doc-degrees">MBBS, MD (General Medicine), FICE</div>
                    <div class="doc-role">Consultant Physician — Medicine &amp; Critical Care</div>

                    <div class="doc-hero-stats">
                        <div class="stat-item">
                            <b>10+ Years</b>
                            <small>Clinical &amp; Administrative Experience</small>
                        </div>
                        <div class="stat-item">
                            <b>FICE Fellow</b>
                            <small>Echocardiography (JROP New Delhi)</small>
                        </div>
                    </div>

                    <div class="doc-hero-actions">
                        <a href="#appointment" class="btn green"><i data-lucide="calendar-check"></i> Book OPD
                            Consultation</a>
                        <a href="https://wa.me/919996544005?text=Hello%20Dr.+Manaswi+Gupta,%20I%20would%20like%20to%20inquire%20about%20OPD%20consultation"
                            target="_blank" rel="noopener" class="btn whatsapp"><svg class="wa-icon-svg"
                                xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"
                                style="vertical-align:middle;flex-shrink:0;margin-right:6px" aria-hidden="true">
                                <path fill="#ffffff"
                                    d="M12.004 2C6.486 2 2 6.486 2 12.004c0 1.956.564 3.784 1.543 5.334L2.2 21.8l4.634-1.306A9.948 9.948 0 0012.004 22c5.518 0 10.004-4.486 10.004-9.996C22.008 6.486 17.522 2 12.004 2z" />
                                <path fill="#25D366" fill-rule="evenodd" clip-rule="evenodd"
                                    d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z" />
                            </svg> WhatsApp Query</a>
                        <a href="tel:01662249473" class="btn outline"
                            style="color:#fff;border-color:rgba(255,255,255,0.35);background:rgba(255,255,255,0.08)"><i
                                data-lucide="phone"></i> 01662-249473</a>
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
                            <p>Dr. Manaswi Gupta is an experienced medical professional specializing in General Medicine, with a strong academic background and extensive clinical experience.</p>
                            <p>He completed his MBBS from GMCH, Udaipur, in 2015, followed by an MD in General Medicine from SRMC Medical College, Chennai, in 2019. He subsequently obtained a Fellowship in Echocardiography from JROP, New Delhi, in 2019.</p>
                            <p>He has served as a Medical Superintendent and Consultant at Ravindra Hospital and Heart Centre, bringing valuable expertise in clinical practice, hospital administration, and patient care.</p>
                        </div>
                    </article>

                    <!-- B. OPD TIMINGS & CONSULTATION LOCATION -->
                    <article class="content-card">
                        <h3><i data-lucide="clock"></i> OPD Schedule &amp; Hospital Location</h3>
                        <div class="opd-grid">
                            <div class="opd-item">
                                <div class="opd-loc">
                                    <b>Sukhda Multispeciality Hospital</b>
                                    <small><i data-lucide="map-pin"
                                            style="width:14px;height:14px;color:var(--green)"></i> Opposite Green Belt, Delhi Road, Hisar - 125001</small>
                                </div>
                                <div class="opd-time">
                                    <span class="days">Mon – Sat</span>
                                    <span class="hours">09:00 AM – 04:00 PM &amp; 05:30 PM – 07:00 PM</span>
                                    <span class="room">Medicine &amp; Critical Care OPD</span>
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
                                    <span class="room">Internal Medicine &amp; Inpatient Care</span>
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
                                <span>Critical Care Medicine</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Management of Multiple Organ Failure</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Treatment of Poisoning, Snake bite</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Diabetes Management</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Hypertension Management</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Thyroid Disorders</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Fever &amp; Infectious Diseases</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Respiratory Diseases (Asthma, COPD, Pneumonia, TB)</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Lifestyle Disease Management</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Chronic Pain-Related Issues</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Anxiety-Related Disorders</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Echocardiography (FICE)</span>
                            </div>
                        </div>
                    </article>

                    <!-- D. EDUCATION & QUALIFICATIONS -->
                    <article class="content-card">
                        <h3><i data-lucide="graduation-cap"></i> Educational Qualification</h3>
                        <div class="timeline">
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>FICE (2019)</h4>
                                <span class="inst">Fellowship in Echocardiography · JROP, New Delhi</span>
                                <p class="desc">Specialized training in 2D and Doppler transthoracic echocardiography, bedside cardiac assessment, and hemodynamic monitoring.</p>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>MD (General Medicine) (2016)</h4>
                                <span class="inst">SRMC Medical College, Chennai</span>
                                <p class="desc">Postgraduate specialty training in General Medicine, intensive care, multi-organ failure management, and acute clinical emergencies.</p>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>MBBS (2009)</h4>
                                <span class="inst">GMCH, Udaipur</span>
                                <p class="desc">Graduated with comprehensive clinical internship across core inpatient medical departments and healthcare services.</p>
                            </div>
                        </div>
                    </article>

                    <!-- E. PROFESSIONAL EXPERIENCE -->
                    <article class="content-card">
                        <h3><i data-lucide="briefcase"></i> Professional Experience</h3>
                        <ul class="pub-list">
                            <li>Served as Medical Superintendent and Consultant at Ravindra Hospital and Heart Centre.</li>
                            <li>Experienced in clinical consultations and patient management.</li>
                            <li>Involved in hospital administration and supervision of medical services.</li>
                            <li>Committed to delivering quality healthcare and providing compassionate patient care.</li>
                        </ul>
                    </article>

                    <!-- F. ACHIEVEMENTS & ACADEMIC CONTRIBUTIONS -->
                    <article class="content-card">
                        <h3><i data-lucide="trophy"></i> Achievements &amp; Academic Contributions</h3>
                        <ul class="pub-list">
                            <li>Successfully cleared the FICE examination in 2019.</li>
                            <li>Earned a postgraduate degree (MD) in General Medicine from SRMC Medical College, Chennai.</li>
                            <li>Demonstrated strong professional leadership while serving as Medical Superintendent and Consultant at Ravindra Hospital and Heart Centre.</li>
                        </ul>
                    </article>

                    <!-- G. PATIENT CARE PHILOSOPHY -->
                    <article class="content-card">
                        <h3><i data-lucide="heart-handshake"></i> Patient Care Philosophy</h3>
                        <div class="bio-text">
                            <p style="font-size:15px;line-height:1.8;color:#243a53;font-style:italic;background:#f3f9f4;border-left:4px solid var(--green);padding:18px 22px;border-radius:0 10px 10px 0;margin:0">
                                &ldquo;Dr. Manaswi Gupta believes in providing patient-centric healthcare built on compassion, trust, and ethical medical practices. His approach focuses on understanding each patient's individual needs, offering accurate diagnosis, and providing evidence-based treatment. He emphasizes clear communication, patient education, and personalized attention to ensure that every patient feels comfortable, respected, and well cared for.&rdquo;
                            </p>
                        </div>
                    </article>

                    <!-- H. IMMEDIATE ASSISTANCE -->
                    <div class="sidebar-direct-card" style="margin-top: 8px;">
                        <h4><i data-lucide="headphones" style="width:18px;height:18px;vertical-align:middle;margin-right:6px"></i> Need Immediate Assistance?</h4>
                        <p>Our hospital reception and emergency care coordinators are available 24 hours a day to assist you.</p>
                        <div style="display:flex;gap:14px;flex-wrap:wrap;">
                            <a href="tel:01662249473" class="direct-phone-btn" style="flex:1;min-width:180px">
                                <span><i data-lucide="phone-call" style="vertical-align:middle;margin-right:6px"></i> 01662-249473</span>
                                <small>24*7 Hospital Desk</small>
                            </a>
                            <a href="tel:919996544005" class="direct-phone-btn" style="flex:1;min-width:180px">
                                <span><i data-lucide="phone" style="vertical-align:middle;margin-right:6px"></i> +91 99965-44005</span>
                                <small>OPD Helpline</small>
                            </a>
                            <a href="https://wa.me/919996544005?text=Hello%20Dr.+Manaswi+Gupta,%20I%20would%20like%20to%20inquire%20about%20OPD%20consultation" target="_blank" rel="noopener" class="direct-phone-btn" style="flex:1;min-width:180px;background:#25D366;border-color:#25D366">
                                <span><svg class="wa-icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" style="vertical-align:middle;flex-shrink:0;margin-right:6px" aria-hidden="true"><path fill="#ffffff" d="M12.004 2C6.486 2 2 6.486 2 12.004c0 1.956.564 3.784 1.543 5.334L2.2 21.8l4.634-1.306A9.948 9.948 0 0012.004 22c5.518 0 10.004-4.486 10.004-9.996C22.008 6.486 17.522 2 12.004 2z"/><path fill="#25D366" fill-rule="evenodd" clip-rule="evenodd" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg>WhatsApp Desk</span>
                                <small>+91 99965-44005</small>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- RIGHT SIDEBAR'''

html = html.replace(old_main_match.group(0), new_main)

# 5. Sidebar Booking Widget Updates
html = html.replace('Direct consultation with Dr. Hemant Dahiya', 'Direct consultation with Dr. Manaswi Gupta')
html = html.replace('value="dr-hemant-dahiya"', 'value="dr-manaswi-gupta"')
html = html.replace('value="Dr. Hemant Dahiya (Internal Medicine)"', 'value="Dr. Manaswi Gupta (Medicine &amp; Critical Care)"')

# 6. Colleague section
old_colleagues_match = re.search(r'<div class="other-docs-grid">[\s\S]*?</div>\s*</div>\s*</section>', html)
if not old_colleagues_match:
    raise Exception("Could not find colleagues section")

new_colleagues = '''<div class="other-docs-grid">
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
                    <img class="colleague-img" src="assets/images/doctors/latest/dr-hemant-dahiya1.webp" alt="Dr. Hemant Dahiya">
                    <div class="colleague-body">
                        <h4>Dr. Hemant Dahiya</h4>
                        <div class="col-deg">MBBS, M.D. (Internal Medicine), FICP</div>
                        <div class="col-spec">Consultant Physician — Internal Medicine</div>
                        <a href="dr-hemant-dahiya.html" class="btn-profile">View Profile →</a>
                    </div>
                </article>
                <article class="colleague-card">
                    <img class="colleague-img" src="assets/images/doctors/latest/dr-trivikrama-rao1.webp" alt="Dr. Trivikrama Rao">
                    <div class="colleague-body">
                        <h4>Dr. Trivikrama Rao</h4>
                        <div class="col-deg">MBBS (Gold Medalist), DNB, DrNB (Medical Oncology)</div>
                        <div class="col-spec">Sr. Consultant Medical Oncologist</div>
                        <a href="dr-trivikrama-rao.html" class="btn-profile">View Profile →</a>
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

with open('dr-manaswi-gupta.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Generated dr-manaswi-gupta.html")
