import os
import re

with open('temp_header.html', 'r', encoding='utf-8') as f:
    raw_header = f.read()

with open('temp_footer.html', 'r', encoding='utf-8') as f:
    raw_footer = f.read()

# Update Quick Links in Footer
new_footer_nav = """                <ul class="footer-nav">
                    <li><a href="index.html"><span>›</span> Home</a></li>
                    <li><a href="about.html"><span>›</span> About Sukhda</a></li>
                    <li><a href="doctor.html"><span>›</span> Find Doctors</a></li>
                    <li><a href="patient-stories.html"><span>›</span> Patient Stories</a></li>
                    <li><a href="careers.html"><span>›</span> Careers</a></li>
                    <li><a href="csr.html"><span>›</span> CSR &amp; Community</a></li>
                    <li><a href="media-centre.html"><span>›</span> Media Centre</a></li>
                    <li><a href="contact.html"><span>›</span> Contact Us</a></li>
                </ul>"""

footer_html = re.sub(r'<ul class="footer-nav">[\s\S]*?</ul>', new_footer_nav, raw_footer)

header_html = raw_header.replace('href="index.html#cases"', 'href="patient-stories.html"')
header_html = header_html.replace('href="index.html#patients"', 'href="patient-stories.html"')
header_html = header_html.replace('href="doctor.html" class="on"', 'href="doctor.html"')

from generate_all_pages import common_styles

page_styles = """
        /* CSR SPECIFIC STYLES */
        .sec-usaid-spotlight {
            padding: 70px 0;
            background: linear-gradient(135deg, #02163d 0%, #052159 100%);
            color: #fff
        }

        .usaid-grid {
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 40px;
            align-items: center
        }

        .usaid-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(39, 129, 50, 0.35);
            border: 1px solid #8ce09e;
            color: #8ce09e;
            padding: 5px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 14px
        }

        .usaid-grid h2 {
            font-size: clamp(26px, 3.2vw, 36px);
            margin: 0 0 16px;
            color: #fff;
            line-height: 1.25
        }

        .usaid-grid p {
            font-size: 16px;
            color: #cbd5e1;
            line-height: 1.65;
            margin: 0 0 20px
        }

        .usaid-stats-box {
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 16px;
            padding: 28px;
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px
        }

        .usaid-stat-num {
            font-size: 28px;
            font-weight: 800;
            color: #8ce09e;
            font-family: 'Montserrat', sans-serif
        }

        .usaid-stat-label {
            font-size: 13px;
            color: #cbd5e1;
            margin-top: 4px
        }

        /* CSR PILLARS SECTION */
        .sec-csr-pillars {
            padding: 80px 0;
            background: #fafcff
        }

        .csr-pillars-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin-top: 40px
        }

        .csr-card {
            background: #fff;
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 30px 26px;
            display: flex;
            flex-direction: column;
            gap: 16px;
            box-shadow: 0 6px 22px rgba(5,33,89,0.04);
            transition: all 0.3s ease;
            position: relative
        }

        .csr-card:hover {
            transform: translateY(-6px);
            border-color: #a3c4e0;
            box-shadow: 0 16px 36px rgba(5,33,89,0.1)
        }

        .csr-icon-wrap {
            width: 54px;
            height: 54px;
            border-radius: 14px;
            background: #eaf5ec;
            color: var(--green);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0
        }

        .csr-icon-wrap.red {
            background: #fef2f2;
            color: #dc2626
        }

        .csr-icon-wrap.blue {
            background: #eff6ff;
            color: #2563eb
        }

        .csr-icon-wrap.purple {
            background: #faf5ff;
            color: #9333ea
        }

        .csr-icon-wrap.teal {
            background: #f0fdfa;
            color: #0d9488
        }

        .csr-card-title {
            margin: 0;
            font-size: 19px;
            font-weight: 800;
            color: var(--blue);
            line-height: 1.3
        }

        .csr-card p {
            margin: 0;
            color: var(--muted);
            font-size: 14.5px;
            line-height: 1.6
        }

        .csr-stat-tag {
            margin-top: auto;
            background: var(--pale);
            border-radius: 8px;
            padding: 10px 14px;
            font-size: 13px;
            font-weight: 700;
            color: var(--blue);
            display: inline-flex;
            align-items: center;
            gap: 8px
        }

        /* IMPACT STORIES HIGHLIGHT */
        .sec-impact-stories {
            padding: 70px 0;
            background: #fff
        }

        .impact-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 28px;
            margin-top: 36px
        }

        .impact-card {
            background: var(--pale);
            border: 1px solid var(--line);
            border-radius: 14px;
            padding: 26px;
            display: flex;
            flex-direction: column;
            gap: 14px
        }

        .impact-card-header {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 13px;
            font-weight: 700;
            color: var(--green)
        }

        .impact-card h4 {
            margin: 0;
            font-size: 17px;
            color: var(--blue);
            font-weight: 800;
            line-height: 1.35
        }

        .impact-card p {
            margin: 0;
            font-size: 14px;
            color: #475569;
            line-height: 1.55
        }

        /* CAMP REQUEST FORM */
        .sec-camp-form {
            padding: 80px 0;
            background: linear-gradient(135deg, #f2f7fb 0%, #eaf5ec 100%)
        }

        .camp-box {
            max-width: 880px;
            margin: 0 auto;
            background: #fff;
            border-radius: 20px;
            padding: 44px;
            box-shadow: 0 16px 40px rgba(5,33,89,0.08);
            border: 1px solid var(--line)
        }

        @media (max-width: 1080px) {
            .csr-pillars-grid {
                grid-template-columns: repeat(2, 1fr)
            }
            .impact-grid {
                grid-template-columns: repeat(2, 1fr)
            }
        }

        @media (max-width: 900px) {
            .usaid-grid {
                grid-template-columns: 1fr;
                gap: 30px
            }
        }

        @media (max-width: 640px) {
            .csr-pillars-grid,
            .impact-grid,
            .usaid-stats-box {
                grid-template-columns: 1fr
            }
            .camp-box {
                padding: 24px 18px
            }
        }
"""

html_content = f"""<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Corporate Social Responsibility (CSR) &amp; Community Health | Sukhda Hospital Hisar</title>
    <meta name="description" content="Discover Sukhda Healthcare's CSR initiatives, USAID SAMRIDH &amp; Pahel partnership, rural health screening camps, subsidized dialysis support, free cancer screening, and public health programmes across Haryana.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,300;0,400;0,700;0,900;1,400;1,700&family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,600;1,700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js"></script>
    <style>
        {common_styles}
        {page_styles}
    </style>
</head>

<body>
    <!-- TOP BAR -->
    <div class="top">
        <div class="wrap">
            <div class="links">
                <span><i data-lucide="map-pin"></i> Delhi Road, Model Town, Hisar</span>
                <span><i data-lucide="heart"></i> Sukhda Seva &bull; Community Health Outreach</span>
            </div>
            <div class="links">
                <a href="tel:01662249473" class="top-emergency"><i data-lucide="phone-call"></i> 24/7 Emergency: 01662-249473</a>
                <a href="https://wa.me/919996544005" target="_blank" class="top-wa"><i data-lucide="message-circle"></i> WhatsApp</a>
            </div>
        </div>
    </div>

    <!-- HEADER / NAVIGATION -->
    {header_html}

    <!-- HERO SECTION -->
    <section class="hero-banner">
        <div class="wrap hero-grid">
            <div>
                <div class="badge"><i data-lucide="heart-handshake"></i> Sukhda Seva &bull; Community Health</div>
                <h1>Healthcare Beyond <span>Hospital Walls</span></h1>
                <p>We believe every individual deserves access to quality, compassionate medical care regardless of socioeconomic boundaries. Discover how our community outreach, rural health camps, and subsidized treatments touch lives every day.</p>
                <div class="hero-actions">
                    <a href="#initiatives" class="btn primary"><i data-lucide="heart"></i> Our CSR Initiatives</a>
                    <a href="#request-camp" class="btn white"><i data-lucide="calendar-plus"></i> Request a Free Health Camp</a>
                </div>
            </div>
            <div>
                <div class="hero-stats-card">
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">65,000+</div>
                        <div class="hero-stat-label">Rural Beneficiaries Reached</div>
                    </div>
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">120+</div>
                        <div class="hero-stat-label">Free Camps Annually</div>
                    </div>
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">5,000+</div>
                        <div class="hero-stat-label">Subsidized Dialysis Sessions</div>
                    </div>
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">8 Blocks</div>
                        <div class="hero-stat-label">Adopted Under USAID Pahel</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- USAID SAMRIDH & PAHEL SPOTLIGHT -->
    <section class="sec-usaid-spotlight">
        <div class="wrap usaid-grid">
            <div>
                <div class="usaid-badge"><i data-lucide="globe"></i> Strategic CSR Alliance</div>
                <h2>Partnering with USAID SAMRIDH &amp; Pahel for Rural Health Resilience</h2>
                <p>Sukhda Healthcare partnered with the <b>USAID SAMRIDH Healthcare Blended Finance Facility</b> and <b>Pahel</b> to strengthen primary and secondary healthcare infrastructure across 8 underserved rural blocks in Western Haryana. Through mobile diagnostic units, village-level telemedicine screening hubs, and maternal-child health follow-ups, we have brought super-specialist consultations directly to rural doorsteps.</p>
                <div style="display:flex;gap:14px;flex-wrap:wrap">
                    <a href="#request-camp" class="btn primary"><i data-lucide="users"></i> Partner With Us for Rural Outreach</a>
                </div>
            </div>
            <div>
                <div class="usaid-stats-box">
                    <div>
                        <div class="usaid-stat-num">8 Blocks</div>
                        <div class="usaid-stat-label">Covered in Hisar, Hansi &amp; Fatehabad</div>
                    </div>
                    <div>
                        <div class="usaid-stat-num">65,000+</div>
                        <div class="usaid-stat-label">Primary Care Screenings Completed</div>
                    </div>
                    <div>
                        <div class="usaid-stat-num">100%</div>
                        <div class="usaid-stat-label">Free Essential Drugs &amp; Point-of-Care Diagnostics</div>
                    </div>
                    <div>
                        <div class="usaid-stat-num">24/7</div>
                        <div class="usaid-stat-label">Telemedicine Referral Linkage to Hospital</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CSR PILLARS SECTION -->
    <section class="sec-csr-pillars" id="initiatives">
        <div class="wrap">
            <div class="sec-header">
                <span class="kicker">Core Pillars of Action</span>
                <h2 class="sec-title">Our Community Initiatives</h2>
                <p class="sec-desc">Targeted healthcare programmes designed to bridge the urban-rural healthcare divide, promote early detection, and provide safety nets for underprivileged families.</p>
            </div>

            <div class="csr-pillars-grid">
                <!-- PILLAR 1: RURAL CAMPS -->
                <div class="csr-card">
                    <div class="csr-icon-wrap"><i data-lucide="map-pin"></i></div>
                    <h3 class="csr-card-title">Free Rural Multi-Speciality Camps</h3>
                    <p>Regular on-ground medical camps in remote villages across Hisar, Hansi, Narnaund, and Barwala. Senior physicians, gynaecologists, and paediatricians provide free consultations, ECGs, blood glucose tests, and free prescription medicines.</p>
                    <div class="csr-stat-tag"><i data-lucide="check-circle"></i> 120+ Village Camps Completed Annually</div>
                </div>

                <!-- PILLAR 2: CANCER SCREENING -->
                <div class="csr-card">
                    <div class="csr-icon-wrap red"><i data-lucide="ribbon"></i></div>
                    <h3 class="csr-card-title">Community Cancer Screening Clinics</h3>
                    <p>In association with Sukhda MedPark oncology specialists, we conduct free oral, breast, and cervical cancer awareness and screening clinics to identify malignancies at Stage 0/1 when cure rates exceed 90%.</p>
                    <div class="csr-stat-tag"><i data-lucide="check-circle"></i> 12,000+ Screenings Conducted</div>
                </div>

                <!-- PILLAR 3: SUBSIDIZED DIALYSIS -->
                <div class="csr-card">
                    <div class="csr-icon-wrap teal"><i data-lucide="droplets"></i></div>
                    <h3 class="csr-card-title">Subsidized &amp; BPL Dialysis Support</h3>
                    <p>Ensuring no chronic kidney disease (CKD) patient goes without life-saving haemodialysis due to poverty. We provide highly subsidized and trust-funded dialysis slots using world-class Fresenius RO systems.</p>
                    <div class="csr-stat-tag"><i data-lucide="check-circle"></i> 5,000+ Subsidized Sessions Delivered</div>
                </div>

                <!-- PILLAR 4: AYUSHMAN HELP DESK -->
                <div class="csr-card">
                    <div class="csr-icon-wrap blue"><i data-lucide="shield-check"></i></div>
                    <h3 class="csr-card-title">Ayushman PM-JAY &amp; Chirayu Facilitation</h3>
                    <p>Dedicated on-campus helpdesks and village facilitation camps to assist eligible BPL families in creating Ayushman Golden Cards and receiving 100% cashless treatment across medical and surgical super-specialities.</p>
                    <div class="csr-stat-tag"><i data-lucide="check-circle"></i> 100% Cashless Patient Navigation</div>
                </div>

                <!-- PILLAR 5: BLOOD DONATION -->
                <div class="csr-card">
                    <div class="csr-icon-wrap red"><i data-lucide="heart"></i></div>
                    <h3 class="csr-card-title">Voluntary Blood Donation Drives</h3>
                    <p>Quarterly mega voluntary blood donation camps organized in partnership with Red Cross Society, Rotary Club, and educational institutions, maintaining an active emergency rare-blood donor registry.</p>
                    <div class="csr-stat-tag"><i data-lucide="check-circle"></i> 2,500+ Units Donated Annually</div>
                </div>

                <!-- PILLAR 6: SCHOOL HEALTH & CPR -->
                <div class="csr-card">
                    <div class="csr-icon-wrap purple"><i data-lucide="graduation-cap"></i></div>
                    <h3 class="csr-card-title">School Health, Nutrition &amp; CPR Training</h3>
                    <p>Adolescent anaemia screening drives for schoolgirls, nutritional counselling in rural schools, and hands-on CPR / Basic Life Support (BLS) training for college students, police, and auto-drivers.</p>
                    <div class="csr-stat-tag"><i data-lucide="check-circle"></i> 15,000+ Students &amp; Youths Trained</div>
                </div>
            </div>
        </div>
    </section>

    <!-- IMPACT STORIES -->
    <section class="sec-impact-stories">
        <div class="wrap">
            <div class="sec-header">
                <span class="kicker">Real World Impact</span>
                <h2 class="sec-title">Stories from the Field</h2>
                <p class="sec-desc">How our community healthcare drives are making a tangible difference in rural Haryana.</p>
            </div>

            <div class="impact-grid">
                <div class="impact-card">
                    <div class="impact-card-header"><i data-lucide="map-pin"></i> Village Rawalwas Khurd, Hisar</div>
                    <h4>Early Cervical Cancer Detection in 45-Year-Old Homemaker</h4>
                    <p>During a Sukhda MedPark rural screening camp, Smt. Kamlesh was diagnosed with early-stage cervical dysplasia. She was promptly treated at MedPark with full financial assistance and is now healthy.</p>
                </div>

                <div class="impact-card">
                    <div class="impact-card-header"><i data-lucide="map-pin"></i> Village Sisai, Hansi Block</div>
                    <h4>180+ Farmers Screened for Silent Hypertension &amp; Diabetes</h4>
                    <p>Our mobile medical van conducted point-of-care HbA1c and ECG checks, identifying 42 previously undiagnosed hypertensive patients who were provided free essential medications and dietary counselling.</p>
                </div>

                <div class="impact-card">
                    <div class="impact-card-header"><i data-lucide="map-pin"></i> Government Senior Secondary School, Hisar</div>
                    <h4>Hands-Only CPR Training for 350 College Students</h4>
                    <p>Sukhda emergency medicine faculty conducted practical mannequin simulation sessions, training young citizens as first responders in out-of-hospital cardiac arrest emergencies.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- REQUEST A HEALTH CAMP FORM -->
    <section class="sec-camp-form" id="request-camp">
        <div class="wrap">
            <div class="camp-box">
                <div style="text-align:center;max-width:680px;margin:0 auto">
                    <span class="kicker">Collaborate for Community Welfare</span>
                    <h2 class="sec-title" style="margin-bottom:10px">Request a Free Health Camp</h2>
                    <p class="sec-desc">Gram Panchayats, NGOs, schools, colleges, and corporate organizations can request a free screening and diagnostic camp in their locality.</p>
                </div>

                <form onsubmit="event.preventDefault(); alert('Thank you for your camp request! Our CSR & Community Outreach coordinator will contact you within 24 hours to coordinate dates and logistics.'); this.reset();">
                    <div class="form-grid">
                        <div class="form-group">
                            <label>Organization / Gram Panchayat / Institution Name *</label>
                            <input type="text" class="form-control" placeholder="e.g. Gram Panchayat Sisai / Rotary Club Hisar" required>
                        </div>
                        <div class="form-group">
                            <label>Contact Person Name *</label>
                            <input type="text" class="form-control" placeholder="e.g. Sarpanch / Secretary Name" required>
                        </div>
                        <div class="form-group">
                            <label>Phone / WhatsApp Number *</label>
                            <input type="tel" class="form-control" placeholder="e.g. +91 98765 43210" required>
                        </div>
                        <div class="form-group">
                            <label>Email Address</label>
                            <input type="email" class="form-control" placeholder="e.g. contact@organization.org">
                        </div>
                        <div class="form-group">
                            <label>Village / Town / Location *</label>
                            <input type="text" class="form-control" placeholder="e.g. Village Narnaund, Dist. Hisar" required>
                        </div>
                        <div class="form-group">
                            <label>Expected Number of Beneficiaries *</label>
                            <select class="form-control" required>
                                <option value="">Select Expected Turnout</option>
                                <option value="50-100">50 - 100 People</option>
                                <option value="100-300">100 - 300 People</option>
                                <option value="300-500">300 - 500 People</option>
                                <option value="500+">500+ Mega Camp</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label>Type of Camp Requested *</label>
                            <select class="form-control" required>
                                <option value="">Select Camp Type</option>
                                <option value="Multi-Speciality General Health & ECG">General Health, ECG &amp; Sugar Checkup</option>
                                <option value="Cancer Awareness & Screening">Cancer Awareness &amp; Early Screening</option>
                                <option value="Cardiac & Hypertension Checkup">Cardiac &amp; Blood Pressure Screening</option>
                                <option value="Women & Child Nutrition Camp">Women, Gynaecology &amp; Child Health</option>
                                <option value="Blood Donation Drive">Voluntary Blood Donation Drive</option>
                                <option value="School CPR & First Aid Workshop">School CPR &amp; First Aid Training</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label>Proposed Date / Month</label>
                            <input type="text" class="form-control" placeholder="e.g. Next Sunday / Mid Next Month">
                        </div>
                        <div class="form-group form-full">
                            <label>Additional Notes / Logistics Support Available</label>
                            <textarea class="form-control" placeholder="Mention venue details (Panchayat Bhawan / School campus), specific health concerns in the village, or special requirements..."></textarea>
                        </div>
                    </div>
                    <div style="text-align:center;margin-top:24px">
                        <button type="submit" class="btn primary" style="padding:14px 40px;font-size:16px"><i data-lucide="send"></i> Submit Camp Request</button>
                    </div>
                    <p style="text-align:center;font-size:13px;color:var(--muted);margin-top:14px">For urgent CSR coordinator inquiries, email <a href="mailto:csr@sukhdahospitalhisar.com" style="color:var(--green);font-weight:700">csr@sukhdahospitalhisar.com</a></p>
                </form>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    {footer_html}
</body>
</html>
"""

if '</html>' in footer_html:
    idx = footer_html.find('</body>')
    clean_footer = footer_html[:idx] if idx != -1 else footer_html
else:
    clean_footer = footer_html

full_page = html_content.replace(f"<!-- FOOTER -->\n    {footer_html}", f"<!-- FOOTER -->\n    {clean_footer}")

with open('csr.html', 'w', encoding='utf-8') as f:
    f.write(full_page)

print("csr.html generated successfully!")
