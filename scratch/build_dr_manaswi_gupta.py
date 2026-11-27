import re

with open('dr-hemant-dahiya.html', 'r', encoding='utf-8') as f:
    template = f.read()

# 1. Update Head: Title, Meta description, Canonical, Schema JSON-LD
title = "Dr. Manaswi Gupta — Consultant Physician — Medicine &amp; Critical Care | Sukhda Healthcare Hisar"
description = "Dr. Manaswi Gupta, MBBS, MD (General Medicine), FICE. Consultant Physician — Medicine &amp; Critical Care at Sukhda Multispeciality Hospital, Hisar. Expertise in critical care, multi-organ failure, diabetes, poisoning, and respiratory diseases."

# Replace Title and Meta
page = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', template, count=1)
page = re.sub(r'<meta name="description"\s+content=".*?">', f'<meta name="description"\n        content="{description}">', page, count=1)

# Canonical URL if present
page = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://sukhdahospitals.com/dr-manaswi-gupta.html">', page)

# Update Breadcrumb
page = re.sub(
    r'<div class="crumb">[\s\S]*?<span>Dr\. Hemant Dahiya</span>\s*</div>',
    '''<div class="crumb">
                <a href="index.html">Home</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <a href="doctor.html">Doctors</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <span>Dr. Manaswi Gupta</span>
            </div>''',
    page,
    count=1
)

# Update Hero Section
old_hero = re.search(r'<div class="doc-hero-grid">[\s\S]*?</div>\s*</div>\s*</section>', page).group(0)

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

page = page.replace(old_hero, new_hero)

# Update Main Left Content (doc-main-col)
old_main_col = re.search(r'<div class="doc-main-col">[\s\S]*?</div>\s*<!-- SIDEBAR / APPOINTMENT BOOKING COLUMN -->', page).group(0)

new_main_col = '''<div class="doc-main-col">

                    <!-- A. INTRODUCTION -->
                    <article class="content-card">
                        <h3><i data-lucide="user-check"></i> Introduction</h3>
                        <div class="bio-text">
                            <p>Dr. Manaswi Gupta is an experienced medical professional specializing in General Medicine, with a strong academic background and extensive clinical experience.</p>
                            <p>He completed his MBBS from GMCH, Udaipur, in 2015, followed by an MD in General Medicine from SRMC Medical College, Chennai, in 2019. He subsequently obtained a Fellowship in Echocardiography (FICE) from JROP, New Delhi, in 2019.</p>
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

                    <!-- C. AREAS OF EXPERTISE -->
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
                                <span>Treatment of Poisoning &amp; Snake Bite</span>
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

                    <!-- D. EDUCATIONAL QUALIFICATION -->
                    <article class="content-card">
                        <h3><i data-lucide="graduation-cap"></i> Educational Qualification</h3>
                        <div class="timeline">
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>FICE (2019)</h4>
                                <span class="inst">Fellowship in Echocardiography · JROP Institute of Echocardiography, New Delhi</span>
                                <p class="desc">Specialized fellowship training in advanced 2D and Doppler transthoracic echocardiography, bedside cardiac assessment, and hemodynamic monitoring.</p>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>MD (General Medicine) (2016 – 2019)</h4>
                                <span class="inst">SRMC Medical College, Chennai</span>
                                <p class="desc">Postgraduate specialty training in General Medicine, acute inpatient care, multi-organ intensive care management, and internal medicine diagnostics.</p>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>MBBS (2009 – 2015)</h4>
                                <span class="inst">Geetanjali Medical College &amp; Hospital (GMCH), Udaipur</span>
                                <p class="desc">Foundational medical education and comprehensive clinical internship across core clinical disciplines, emergency care, and public health.</p>
                            </div>
                        </div>
                    </article>

                    <!-- E. PROFESSIONAL EXPERIENCE -->
                    <article class="content-card">
                        <h3><i data-lucide="briefcase"></i> Professional Experience</h3>
                        <div class="experience-list">
                            <div class="exp-item">
                                <div class="exp-badge"><i data-lucide="shield-check"></i></div>
                                <div>
                                    <h4>Consultant Physician — Medicine &amp; Critical Care</h4>
                                    <span class="inst">Sukhda Multispeciality Hospital &amp; Sukhda MedPark Hospital, Hisar</span>
                                    <p class="desc">Delivering advanced inpatient, intensive care, and outpatient care for patients with multi-organ diseases, infectious disorders, diabetes, and acute medical emergencies.</p>
                                </div>
                            </div>
                            <div class="exp-item">
                                <div class="exp-badge"><i data-lucide="activity"></i></div>
                                <div>
                                    <h4>Medical Superintendent and Consultant</h4>
                                    <span class="inst">Ravindra Hospital and Heart Centre</span>
                                    <p class="desc">Served in hospital leadership supervising medical services, clinical audits, quality healthcare administration, and delivering dedicated internal medicine care.</p>
                                </div>
                            </div>
                            <div class="exp-item">
                                <div class="exp-badge"><i data-lucide="heart-pulse"></i></div>
                                <div>
                                    <h4>Clinical Consultations &amp; Patient Management</h4>
                                    <span class="inst">Extensive Clinical Practice</span>
                                    <p class="desc">Experienced in comprehensive clinical evaluations, individualized pharmacotherapy, toxicological emergencies (poisoning, snake bite), and life-saving critical care protocols.</p>
                                </div>
                            </div>
                        </div>
                    </article>

                    <!-- F. ACHIEVEMENTS & ACADEMIC CONTRIBUTIONS -->
                    <article class="content-card">
                        <h3><i data-lucide="award"></i> Achievements &amp; Academic Contributions</h3>
                        <div class="achieve-grid">
                            <div class="achieve-item">
                                <div class="achieve-icon"><i data-lucide="award"></i></div>
                                <div>
                                    <b>Fellowship in Echocardiography (FICE)</b>
                                    <p>Successfully cleared the prestigious FICE examination in 2019 from JROP New Delhi.</p>
                                </div>
                            </div>
                            <div class="achieve-item">
                                <div class="achieve-icon"><i data-lucide="check-circle-2"></i></div>
                                <div>
                                    <b>Postgraduate Degree (MD) in General Medicine</b>
                                    <p>Earned Master of Medicine (MD) in General Medicine from SRMC Medical College, Chennai.</p>
                                </div>
                            </div>
                            <div class="achieve-item">
                                <div class="achieve-icon"><i data-lucide="users"></i></div>
                                <div>
                                    <b>Clinical &amp; Healthcare Leadership</b>
                                    <p>Demonstrated strong professional leadership while serving as Medical Superintendent and Consultant at Ravindra Hospital and Heart Centre.</p>
                                </div>
                            </div>
                            <div class="achieve-item">
                                <div class="achieve-icon"><i data-lucide="heart"></i></div>
                                <div>
                                    <b>Compassionate Care Excellence</b>
                                    <p>Committed to delivering high-quality healthcare, patient safety, ethical standards, and compassionate patient care.</p>
                                </div>
                            </div>
                        </div>
                    </article>

                    <!-- G. PATIENT CARE PHILOSOPHY -->
                    <article class="content-card">
                        <h3><i data-lucide="heart-handshake"></i> Patient Care Philosophy</h3>
                        <div class="bio-text">
                            <p style="font-size:16px;line-height:1.8;color:#243a53;font-style:italic;background:#f3f9f4;border-left:4px solid var(--green);padding:20px 24px;border-radius:0 12px 12px 0;margin:0">
                                &ldquo;Dr. Manaswi Gupta believes in providing patient-centric healthcare built on compassion, trust, and ethical medical practices. His approach focuses on understanding each patient's individual needs, offering accurate diagnosis, and providing evidence-based treatment. He emphasizes clear communication, patient education, and personalized attention to ensure that every patient feels comfortable, respected, and well cared for.&rdquo;
                            </p>
                        </div>
                    </article>

                </div>
                <!-- SIDEBAR / APPOINTMENT BOOKING COLUMN -->'''

page = page.replace(old_main_col, new_main_col)

# Update appointment form doctor name
page = re.sub(
    r'<input type="text" id="docSelected" class="form-control"\s+value=".*?" readonly>',
    '<input type="text" id="docSelected" class="form-control"\n                                    value="Dr. Manaswi Gupta (Medicine &amp; Critical Care)" readonly>',
    page
)

# Update Schema.org JSON-LD
schema_json = '''<script type="application/ld+json">
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
        "Treatment of Poisoning and Snake Bite",
        "Diabetes Management",
        "Hypertension Management",
        "Thyroid Disorders",
        "Fever & Infectious Diseases",
        "Respiratory Diseases (Asthma, COPD, Pneumonia, TB)",
        "Echocardiography (FICE)"
      ],
      "alumniOf": [
        {
          "@type": "EducationalOrganization",
          "name": "Geetanjali Medical College & Hospital (GMCH), Udaipur"
        },
        {
          "@type": "EducationalOrganization",
          "name": "SRMC Medical College, Chennai"
        },
        {
          "@type": "EducationalOrganization",
          "name": "JROP Institute of Echocardiography, New Delhi"
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

# Replace schema
page = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>', schema_json, page, count=1)

# Update Colleague card for Dr. Hemant Dahiya in the colleague section so Dr. Hemant is in other docs list!
old_colleagues = re.search(r'<div class="other-docs-grid">[\s\S]*?</div>\s*</div>\s*</section>', page).group(0)

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
                        <div class="col-deg">MBBS, M.D. (Internal Medicine)</div>
                        <div class="col-spec">Consultant Physician — Internal Medicine</div>
                        <a href="dr-hemant-dahiya.html" class="btn-profile">View Profile →</a>
                    </div>
                </article>
                <article class="colleague-card">
                    <img class="colleague-img" src="assets/images/doctors/latest/dr-ankur-kamra1.webp" alt="Dr. Ankur Kamra">
                    <div class="colleague-body">
                        <h4>Dr. Ankur Kamra</h4>
                        <div class="col-deg">MBBS, MD (Medicine), DM (Cardiology)</div>
                        <div class="col-spec">HOD &amp; Senior Consultant — Interventional Cardiology</div>
                        <a href="dr-ankur-kamra.html" class="btn-profile">View Profile →</a>
                    </div>
                </article>
                <article class="colleague-card">
                    <img class="colleague-img" src="assets/images/doctors/latest/dr-bharath1.webp" alt="Dr. Bharath">
                    <div class="colleague-body">
                        <h4>Dr. Bharath</h4>
                        <div class="col-deg">MBBS, MD (Medicine), DM (Gastroenterology)</div>
                        <div class="col-spec">Consultant Gastroenterologist &amp; Hepatologist</div>
                        <a href="dr-bharath.html" class="btn-profile">View Profile →</a>
                    </div>
                </article>
            </div>
        </div>
    </section>'''

page = page.replace(old_colleagues, new_colleagues)

with open('dr-manaswi-gupta.html', 'w', encoding='utf-8') as f:
    f.write(page)

print("Created dr-manaswi-gupta.html successfully!")
