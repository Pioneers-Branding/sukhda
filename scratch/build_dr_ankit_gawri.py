import re

with open('dr-manaswi-gupta.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Title & Meta
title = "Dr. Ankit Gawri — Consultant — Orthopaedics &amp; Robotic Joint Replacement | Sukhda Healthcare Hisar"
desc = "Dr. Ankit Gawri, MBBS, MS (Orthopaedics), FNB (Arthroplasty). Consultant — Orthopaedics &amp; Robotic Joint Replacement at Sukhda Multispeciality Hospital, Hisar. Robotic Knee Specialist, TKR, THR, and sports injury surgery. Book OPD or call +91 8168394634."

html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html, count=1)
html = re.sub(r'<meta name="description"[\s\S]*?>', f'<meta name="description"\n        content="{desc}">', html, count=1)

# Canonical and Schema injection
html = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://sukhdahospitals.com/dr-ankit-gawri.html">', html, count=1)

schema_json = '''<script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Physician",
      "name": "Dr. Ankit Gawri",
      "url": "https://sukhdahospitals.com/dr-ankit-gawri.html",
      "image": "https://sukhdahospitals.com/assets/images/doctors/latest/dr-ankit-gawri.webp",
      "description": "Dr. Ankit Gawri, MBBS, MS (Orthopaedics), FNB (Arthroplasty). Consultant — Orthopaedics & Robotic Joint Replacement at Sukhda Multispeciality Hospital, Hisar.",
      "medicalSpecialty": [
        "Orthopedic",
        "Arthroplasty",
        "Joint Replacement Surgery",
        "Robotic Surgery"
      ],
      "knowsAbout": [
        "Robotic Knee Specialist",
        "Total Knee Replacement (TKR)",
        "Total Hip Replacement (THR)",
        "Sports Injury Management",
        "ACL & PCL Reconstruction",
        "Trauma Surgery",
        "Revision TKR",
        "Primary & Revision Arthroplasty"
      ],
      "alumniOf": [
        {
          "@type": "EducationalOrganization",
          "name": "SDM Medical College, Dharwad"
        },
        {
          "@type": "EducationalOrganization",
          "name": "Government Medical College, Aurangabad"
        },
        {
          "@type": "EducationalOrganization",
          "name": "Aadhar Hospital Hisar"
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
        }
      ]
    }
    </script>'''

html = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>', schema_json, html, count=1)

# 2. Breadcrumb
html = re.sub(
    r'<div class="crumb">[\s\S]*?<span>Dr\. Manaswi Gupta</span>\s*</div>',
    '''<div class="crumb">
                <a href="index.html">Home</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <a href="doctor.html">Doctors</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <span>Dr. Ankit Gawri</span>
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
                    <img src="assets/images/doctors/latest/dr-ankit-gawri.webp" alt="Dr. Ankit Gawri — Consultant, Orthopaedics &amp; Robotic Joint Replacement, Sukhda Hospital Hisar">
                </div>

                <div class="doc-hero-info">
                    <div class="doc-top-tags">
                        <span class="pill-verified"><i data-lucide="shield-check" style="width:14px;height:14px"></i>
                            Consultant</span>
                        <a href="orthopaedic-and-robotic-joint-replacement.html" class="pill-dept-link"><i data-lucide="bone"
                                style="width:14px;height:14px"></i> Orthopaedics &amp; Robotic Joint Replacement</a>
                        <a href="sukhda-multispecialty-hospital.html" class="pill-hosp-link"><i data-lucide="building-2"
                                style="width:14px;height:14px;color:#278132"></i> Sukhda Multispeciality Hospital</a>
                    </div>

                    <h1>Dr. Ankit Gawri</h1>
                    <div class="doc-degrees">MBBS, MS (Orthopaedics), FNB (Arthroplasty)</div>
                    <div class="doc-role">Consultant — Orthopaedics &amp; Robotic Joint Replacement</div>

                    <div class="doc-hero-stats">
                        <div class="stat-item">
                            <b>Robotic Knee Specialist</b>
                            <small>Primary &amp; Revision Arthroplasty</small>
                        </div>
                        <div class="stat-item">
                            <b>FNB Fellow</b>
                            <small>Joint Replacement &amp; Arthroplasty</small>
                        </div>
                    </div>

                    <div class="doc-hero-actions">
                        <a href="#appointment" class="btn green"><i data-lucide="calendar-check"></i> Book OPD
                            Consultation</a>
                        <a href="https://wa.me/918168394634?text=Hello%20Dr.+Ankit+Gawri,%20I%20would%20like%20to%20inquire%20about%20orthopaedic%20consultation"
                            target="_blank" rel="noopener" class="btn whatsapp"><svg class="wa-icon-svg"
                                xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"
                                style="vertical-align:middle;flex-shrink:0;margin-right:6px" aria-hidden="true">
                                <path fill="#ffffff"
                                    d="M12.004 2C6.486 2 2 6.486 2 12.004c0 1.956.564 3.784 1.543 5.334L2.2 21.8l4.634-1.306A9.948 9.948 0 0012.004 22c5.518 0 10.004-4.486 10.004-9.996C22.008 6.486 17.522 2 12.004 2z" />
                                <path fill="#25D366" fill-rule="evenodd" clip-rule="evenodd"
                                    d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z" />
                            </svg> WhatsApp Query</a>
                        <a href="tel:918168394634" class="btn outline"
                            style="color:#fff;border-color:rgba(255,255,255,0.35);background:rgba(255,255,255,0.08)"><i
                                data-lucide="phone"></i> +91 81683-94634</a>
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
                            <p>Dr. Ankit Gawri is a highly trained Orthopaedic Surgeon specializing in Joint Replacement, Arthroplasty, and Robotic-Assisted Joint Replacement Surgery. He has extensive clinical experience in managing complex orthopaedic conditions, trauma cases, fractures, and joint-related disorders.</p>
                            <p>He has specialized training in Primary and Revision Arthroplasty, with expertise in advanced surgical techniques, joint preservation, and comprehensive patient management. His professional interests also include clinical research, cadaveric surgical training, and academic teaching.</p>
                            <p>He is committed to delivering advanced, evidence-based orthopaedic care, with a focus on surgical precision, patient safety, faster recovery, and improved quality of life.</p>
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
                                    <span class="hours">09:00 AM – 05:00 PM</span>
                                    <span class="room">Orthopaedics &amp; Robotic Joint Replacement OPD</span>
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
                                <span>Robotic Knee Specialist</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Total Knee Replacement (TKR)</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Total Hip Replacement (THR)</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Sports Injury Management</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>ACL &amp; PCL Reconstruction</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Trauma Surgery</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Revision TKR</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Joint Preservation Techniques</span>
                            </div>
                            <div class="spec-chip">
                                <i data-lucide="check-circle-2"></i>
                                <span>Complex Fractures Management</span>
                            </div>
                        </div>
                    </article>

                    <!-- D. EDUCATION & QUALIFICATIONS -->
                    <article class="content-card">
                        <h3><i data-lucide="graduation-cap"></i> Educational Qualification</h3>
                        <div class="timeline">
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>FNB Arthroplasty (2024–2026) (From Aadhar Hospital Hisar)</h4>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>MS Orthopaedics – Government Medical College, Aurangabad (2019–2022)</h4>
                            </div>
                            <div class="timeline-item">
                                <div class="timeline-dot"></div>
                                <h4>MBBS – SDM Medical College, Dharwad (2017)</h4>
                            </div>
                        </div>
                    </article>

                    <!-- E. PROFESSIONAL EXPERIENCE -->
                    <article class="content-card">
                        <h3><i data-lucide="briefcase"></i> Professional Experience</h3>
                        <ul class="pub-list">
                            <li>FNB Arthroplasty &amp; Robotic Joint Replacement Surgeon – July 2024–2026</li>
                            <li>Senior Resident, LBS Hospital, Delhi – March 2024–2026</li>
                            <li>Senior Resident, Government Medical College, Jalgaon – October 2022–October 2023</li>
                            <li>Resident, Government Medical College, Aurangabad – June 2019–June 2022</li>
                        </ul>
                    </article>

                    <!-- F. ACHIEVEMENTS & ACADEMIC CONTRIBUTIONS -->
                    <article class="content-card">
                        <h3><i data-lucide="trophy"></i> Achievements &amp; Academic Contributions</h3>
                        <ul class="pub-list">
                            <li>Poster Presentation at IOACON 2021 on Clinical Outcomes of Minimally Invasive Internal Fixation in Ankle Fracture Dislocation.</li>
                            <li>Attended IOACON 2021 Workshop.</li>
                            <li>Presented research and thesis at various national conferences.</li>
                            <li>Involved in postgraduate and undergraduate teaching.</li>
                        </ul>
                    </article>

                    <!-- G. PATIENT CARE PHILOSOPHY -->
                    <article class="content-card">
                        <h3><i data-lucide="heart-handshake"></i> Patient Care Philosophy</h3>
                        <div class="bio-text">
                            <p style="font-size:15px;line-height:1.8;color:#243a53;font-style:italic;background:#f3f9f4;border-left:4px solid var(--green);padding:18px 22px;border-radius:0 10px 10px 0;margin:0">
                                &ldquo;Dr. Ankit Gawri is dedicated to delivering comprehensive, patient-centred orthopaedic care through advanced surgical techniques, evidence-based treatment approaches, and personalized treatment planning. He believes in combining clinical expertise with precision-driven procedures to achieve optimal surgical outcomes.&rdquo;
                            </p>
                        </div>
                    </article>

                    <!-- H. IMMEDIATE ASSISTANCE -->
                    <div class="sidebar-direct-card" style="margin-top: 8px;">
                        <h4><i data-lucide="headphones" style="width:18px;height:18px;vertical-align:middle;margin-right:6px"></i> Need Immediate Assistance?</h4>
                        <p>Our hospital reception and orthopaedic coordinators are available 24 hours a day to assist you.</p>
                        <div style="display:flex;gap:14px;flex-wrap:wrap;">
                            <a href="tel:01662249473" class="direct-phone-btn" style="flex:1;min-width:180px">
                                <span><i data-lucide="phone-call" style="vertical-align:middle;margin-right:6px"></i> 01662-249473</span>
                                <small>24*7 Hospital Desk</small>
                            </a>
                            <a href="tel:918168394634" class="direct-phone-btn" style="flex:1;min-width:180px">
                                <span><i data-lucide="phone" style="vertical-align:middle;margin-right:6px"></i> +91 81683-94634</span>
                                <small>Doctor Direct Helpline</small>
                            </a>
                            <a href="https://wa.me/918168394634?text=Hello%20Dr.+Ankit+Gawri,%20I%20would%20like%20to%20inquire%20about%20orthopaedic%20consultation" target="_blank" rel="noopener" class="direct-phone-btn" style="flex:1;min-width:180px;background:#25D366;border-color:#25D366">
                                <span><svg class="wa-icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" style="vertical-align:middle;flex-shrink:0;margin-right:6px" aria-hidden="true"><path fill="#ffffff" d="M12.004 2C6.486 2 2 6.486 2 12.004c0 1.956.564 3.784 1.543 5.334L2.2 21.8l4.634-1.306A9.948 9.948 0 0012.004 22c5.518 0 10.004-4.486 10.004-9.996C22.008 6.486 17.522 2 12.004 2z"/><path fill="#25D366" fill-rule="evenodd" clip-rule="evenodd" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/></svg>WhatsApp Desk</span>
                                <small>+91 81683-94634</small>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- RIGHT SIDEBAR'''

html = html.replace(old_main_match.group(0), new_main)

# 5. Sidebar Booking Widget Updates
html = html.replace('Direct consultation with Dr. Manaswi Gupta', 'Direct consultation with Dr. Ankit Gawri')
html = html.replace('value="dr-manaswi-gupta"', 'value="dr-ankit-gawri"')
html = html.replace('value="Dr. Manaswi Gupta (Medicine &amp; Critical Care)"', 'value="Dr. Ankit Gawri (Orthopaedics &amp; Robotic Joint Replacement)"')

# 6. Colleague section
old_colleagues_match = re.search(r'<div class="other-docs-grid">[\s\S]*?</div>\s*</div>\s*</section>', html)
if not old_colleagues_match:
    raise Exception("Could not find colleagues section")

new_colleagues = '''<div class="other-docs-grid">
                <article class="colleague-card">
                    <img class="colleague-img" src="assets/images/doctors/latest/dr-pankaj-sharma1.webp" alt="Dr. Pankaj Sharma">
                    <div class="colleague-body">
                        <h4>Dr. Pankaj Sharma</h4>
                        <div class="col-deg">MS (Ortho), Fellowship (Arthroplasty &amp; Arthroscopy)</div>
                        <div class="col-spec">Joint Replacement, Arthroscopy &amp; Sports Injury Surgeon</div>
                        <a href="dr-pankaj-sharma.html" class="btn-profile">View Profile →</a>
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

with open('dr-ankit-gawri.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Generated dr-ankit-gawri.html")
