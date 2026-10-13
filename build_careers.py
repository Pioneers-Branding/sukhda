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
        /* CAREERS SPECIFIC STYLES */
        .sec-why-join {
            padding: 70px 0;
            background: #fff
        }

        .why-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 28px;
            margin-top: 40px
        }

        .why-card {
            background: var(--pale);
            border: 1px solid var(--line);
            border-radius: 14px;
            padding: 30px 26px;
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column;
            gap: 14px
        }

        .why-card:hover {
            transform: translateY(-5px);
            background: #fff;
            box-shadow: 0 12px 30px rgba(5,33,89,0.08);
            border-color: #bad3e8
        }

        .why-icon {
            width: 52px;
            height: 52px;
            border-radius: 12px;
            background: #eaf5ec;
            color: var(--green);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0
        }

        .why-card h3 {
            margin: 0;
            font-size: 19px;
            color: var(--blue);
            font-weight: 800
        }

        .why-card p {
            margin: 0;
            color: var(--muted);
            font-size: 14.5px;
            line-height: 1.6
        }

        /* DNB SPOTLIGHT CARD */
        .sec-dnb-banner {
            padding: 60px 0;
            background: linear-gradient(135deg, #02163d 0%, #052159 100%);
            color: #fff
        }

        .dnb-box {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 18px;
            padding: 36px;
            display: grid;
            grid-template-columns: 1.3fr 0.7fr;
            gap: 36px;
            align-items: center
        }

        .dnb-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(39, 129, 50, 0.35);
            border: 1px solid #278132;
            color: #278132;
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 12.5px;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 12px
        }

        .dnb-box h2 {
            font-size: 26px;
            margin: 0 0 12px;
            color: #fff
        }

        .dnb-box p {
            margin: 0 0 20px;
            color: #cbd5e1;
            font-size: 15px;
            line-height: 1.6
        }

        .dnb-features {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px
        }

        .dnb-feat-item {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 13.5px;
            color: #e2e8f0;
            font-weight: 600
        }

        .dnb-feat-item i {
            color: #278132;
            width: 18px;
            height: 18px;
            flex-shrink: 0
        }

        .dnb-side-card {
            background: #fff;
            color: var(--blue);
            border-radius: 14px;
            padding: 26px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 12px
        }

        .dnb-side-card b {
            font-size: 17px;
            color: var(--blue)
        }

        .dnb-side-card p {
            font-size: 13px;
            color: var(--muted);
            margin: 0
        }

        /* OPENINGS SECTION */
        .sec-openings {
            padding: 70px 0 90px;
            background: #fafcff
        }

        .jobs-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 26px;
            margin-top: 36px
        }

        .job-card {
            background: #fff;
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 28px;
            display: flex;
            flex-direction: column;
            gap: 16px;
            box-shadow: 0 6px 20px rgba(5,33,89,0.04);
            transition: all 0.25s ease;
            position: relative
        }

        .job-card:hover {
            transform: translateY(-4px);
            border-color: #a3c4e0;
            box-shadow: 0 14px 30px rgba(5,33,89,0.1)
        }

        .job-card-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 14px
        }

        .job-dept-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #eaf5ec;
            color: var(--green);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase
        }

        .job-card-title {
            margin: 8px 0 0;
            font-size: 20px;
            font-weight: 800;
            color: var(--blue);
            line-height: 1.3
        }

        .job-location-tag {
            font-size: 13px;
            color: var(--muted);
            display: inline-flex;
            align-items: center;
            gap: 5px;
            margin-top: 4px
        }

        .job-meta-pills {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            padding: 12px 0;
            border-top: 1px solid #edf2f7;
            border-bottom: 1px solid #edf2f7
        }

        .meta-pill {
            background: var(--pale);
            color: #274060;
            font-size: 13px;
            font-weight: 600;
            padding: 5px 12px;
            border-radius: 6px;
            display: inline-flex;
            align-items: center;
            gap: 6px
        }

        .job-desc-summary {
            color: #475569;
            font-size: 14.5px;
            line-height: 1.55;
            margin: 0
        }

        .job-card-footer {
            margin-top: auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
            padding-top: 6px
        }

        .job-salary-note {
            font-size: 13px;
            font-weight: 700;
            color: var(--green)
        }

        /* LIFE AT SUKHDA & BENEFITS */
        .sec-life {
            padding: 70px 0;
            background: #fff
        }

        .perks-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 36px
        }

        .perk-card {
            background: var(--pale);
            border: 1px solid var(--line);
            border-radius: 12px;
            padding: 24px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px
        }

        .perk-icon {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: #fff;
            color: var(--green);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05)
        }

        .perk-card b {
            font-size: 15px;
            color: var(--blue)
        }

        .perk-card p {
            margin: 0;
            font-size: 13px;
            color: var(--muted);
            line-height: 1.45
        }

        /* APPLICATION FORM SECTION */
        .sec-apply-form {
            padding: 80px 0;
            background: linear-gradient(135deg, #f2f7fb 0%, #eaf5ec 100%)
        }

        .apply-box {
            max-width: 900px;
            margin: 0 auto;
            background: #fff;
            border-radius: 20px;
            padding: 44px;
            box-shadow: 0 16px 40px rgba(5,33,89,0.08);
            border: 1px solid var(--line)
        }

        @media (max-width: 1080px) {
            .why-grid {
                grid-template-columns: repeat(2, 1fr)
            }
            .perks-grid {
                grid-template-columns: repeat(2, 1fr)
            }
        }

        @media (max-width: 900px) {
            .dnb-box {
                grid-template-columns: 1fr;
                gap: 24px
            }
            .jobs-grid {
                grid-template-columns: 1fr
            }
        }

        @media (max-width: 640px) {
            .why-grid,
            .perks-grid,
            .dnb-features {
                grid-template-columns: 1fr
            }
            .apply-box {
                padding: 24px 18px
            }
            .job-card-footer {
                flex-direction: column;
                align-items: stretch;
                gap: 10px
            }
            .job-card-footer .btn {
                width: 100%
            }
        }
"""

html_content = f"""<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Careers &amp; Job Openings | Sukhda Healthcare Hisar</title>
    <meta name="description" content="Explore exciting medical, nursing, paramedical, and administrative career opportunities at Sukhda Multispeciality Hospital and Sukhda MedPark in Hisar. Join our NBEMS DNB residency teaching hospital.">
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
                <span><i data-lucide="award"></i> NABH Accredited &amp; DNB Residency Centre</span>
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
                <div class="badge"><i data-lucide="briefcase"></i> Work With Purpose &bull; Careers at Sukhda</div>
                <h1>Build Your Career with <span>Haryana's Healthcare Leader</span></h1>
                <p>Join a progressive multidisciplinary team committed to academic rigor, cutting-edge medical technology, and compassionate patient care. Grow your clinical acumen in a supportive, NABH-accredited ecosystem.</p>
                <div class="hero-actions">
                    <a href="#openings" class="btn primary"><i data-lucide="search"></i> View Current Openings</a>
                    <a href="#apply-direct" class="btn white"><i data-lucide="upload-cloud"></i> Apply Direct (Upload CV)</a>
                </div>
            </div>
            <div>
                <div class="hero-stats-card">
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">450+</div>
                        <div class="hero-stat-label">Healthcare Professionals</div>
                    </div>
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">NBEMS</div>
                        <div class="hero-stat-label">DNB General Medicine Centre</div>
                    </div>
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">2 Campuses</div>
                        <div class="hero-stat-label">Multispeciality &amp; MedPark Cancer</div>
                    </div>
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">20+ Depts</div>
                        <div class="hero-stat-label">Super Specialities &amp; Critical Care</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- WHY JOIN SUKHDA -->
    <section class="sec-why-join">
        <div class="wrap">
            <div class="sec-header">
                <span class="kicker">Why Choose Sukhda?</span>
                <h2 class="sec-title">Empowering Your Medical &amp; Professional Growth</h2>
                <p class="sec-desc">We foster a culture of clinical excellence, innovation, and continuous learning where doctors, nurses, and allied professionals thrive.</p>
            </div>

            <div class="why-grid">
                <div class="why-card">
                    <div class="why-icon"><i data-lucide="activity"></i></div>
                    <h3>Advanced Medical Technology</h3>
                    <p>Work with state-of-the-art infrastructure including Philips Flat-Panel Cath Lab, Varian Linear Accelerator (LINAC), Modular Laminar OTs, 3D Arthroscopy, and advanced ICU ventilators.</p>
                </div>

                <div class="why-card">
                    <div class="why-icon"><i data-lucide="graduation-cap"></i></div>
                    <h3>DNB Academics &amp; Research</h3>
                    <p>Accredited by NBEMS for Post-Graduate DNB in General Medicine. Learn and practice alongside AIIMS-trained faculty Dr. Amit Mehta with active clinical audits, mortality rounds, and journal clubs.</p>
                </div>

                <div class="why-card">
                    <div class="why-icon"><i data-lucide="shield-check"></i></div>
                    <h3>NABH Quality &amp; Safety Culture</h3>
                    <p>Rigorous clinical governance led by Dr. Manisha Mehta (Certified NABH Assessor). Practice in an environment that puts patient safety, transparent protocols, and infection control first.</p>
                </div>

                <div class="why-card">
                    <div class="why-icon"><i data-lucide="award"></i></div>
                    <h3>Competitive Rewards &amp; Benefits</h3>
                    <p>Attractive remuneration packages commensurate with qualifications and merit, Provident Fund (PF), ESI, gratuity, medical coverage for family, and performance-linked bonuses.</p>
                </div>

                <div class="why-card">
                    <div class="why-icon"><i data-lucide="heart-handshake"></i></div>
                    <h3>Nursing &amp; Paramedical Empowerment</h3>
                    <p>Structured onboarding, BLS/ACLS certifications, simulation-based workshops, infection control up-skilling, and clear clinical leadership progression pathways.</p>
                </div>

                <div class="why-card">
                    <div class="why-icon"><i data-lucide="users"></i></div>
                    <h3>Inclusive, Supportive Community</h3>
                    <p>Collaborative multidisciplinary teamwork across departments, on-campus accommodation assistance for outstation candidates, and active welfare committees.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- DNB RESIDENCY BANNER -->
    <section class="sec-dnb-banner">
        <div class="wrap">
            <div class="dnb-box">
                <div>
                    <div class="dnb-badge"><i data-lucide="award"></i> Academic Excellence</div>
                    <h2>NBEMS Accredited DNB Residency Program</h2>
                    <p>Sukhda Multispeciality Hospital is accredited by the National Board of Examinations in Medical Sciences (NBEMS) for Post-Graduate DNB (General Medicine) residency training. Our academic curriculum blends intensive bedside clinical exposure, ICU rotations, research, and thesis guidance under AIIMS New Delhi alumni.</p>
                    <div class="dnb-features">
                        <div class="dnb-feat-item"><i data-lucide="check-circle-2"></i> Daily Clinical Case Discussions</div>
                        <div class="dnb-feat-item"><i data-lucide="check-circle-2"></i> Comprehensive ICU &amp; Cath Lab Rotations</div>
                        <div class="dnb-feat-item"><i data-lucide="check-circle-2"></i> Dedicated Central Medical Library</div>
                        <div class="dnb-feat-item"><i data-lucide="check-circle-2"></i> National Conference Sponsorships</div>
                    </div>
                </div>
                <div class="dnb-side-card">
                    <i data-lucide="book-open" style="width:40px;height:40px;color:var(--green)"></i>
                    <b>DNB Residency Inquiries</b>
                    <p>For DNB counselling and academic coordinator queries:</p>
                    <a href="mailto:dnb@sukhdahospitalhisar.com" class="btn primary" style="padding:10px 20px;font-size:14px"><i data-lucide="mail"></i> Email Academic Office</a>
                </div>
            </div>
        </div>
    </section>

    <!-- JOB FILTER TABS -->
    <section class="filter-section" id="openings">
        <div class="wrap">
            <div class="tab-bar">
                <button type="button" class="tab-btn active" data-filter="all"><i data-lucide="briefcase"></i> All Openings (12)</button>
                <button type="button" class="tab-btn" data-filter="medical"><i data-lucide="stethoscope"></i> Doctors &amp; Consultants</button>
                <button type="button" class="tab-btn" data-filter="nursing"><i data-lucide="heart"></i> Nursing Staff</button>
                <button type="button" class="tab-btn" data-filter="paramedical"><i data-lucide="activity"></i> Paramedical &amp; Allied</button>
                <button type="button" class="tab-btn" data-filter="admin"><i data-lucide="building-2"></i> Administration &amp; Ops</button>
            </div>
        </div>
    </section>

    <!-- CURRENT OPENINGS SECTION -->
    <section class="sec-openings">
        <div class="wrap">
            <div class="sec-header">
                <span class="kicker">Opportunities</span>
                <h2 class="sec-title">Current Open Positions</h2>
                <p class="sec-desc">Explore active vacancies across our clinical, nursing, diagnostic, and hospital management departments in Hisar.</p>
            </div>

            <div class="jobs-grid">
                <!-- JOB 1: CARDIOLOGIST -->
                <div class="job-card" data-category="medical">
                    <div class="job-card-top">
                        <div>
                            <span class="job-dept-badge"><i data-lucide="heart-pulse"></i> Cardiology</span>
                            <h3 class="job-card-title">Consultant Interventional Cardiologist</h3>
                            <div class="job-location-tag"><i data-lucide="map-pin"></i> Sukhda Multispeciality Hospital, Hisar</div>
                        </div>
                    </div>
                    <div class="job-meta-pills">
                        <span class="meta-pill"><i data-lucide="graduation-cap"></i> DM / DrNB Cardiology</span>
                        <span class="meta-pill"><i data-lucide="clock"></i> 2+ Years Post-DM</span>
                        <span class="meta-pill"><i data-lucide="briefcase"></i> Full Time</span>
                    </div>
                    <p class="job-desc-summary">Manage flat-panel cath lab procedures including primary angioplasties (PAMI), elective PCI, pacemaker implantations, and lead the 24/7 cardiac emergency response team.</p>
                    <div class="job-card-footer">
                        <span class="job-salary-note">Competitive + Incentive Structure</span>
                        <a href="#apply-direct" class="btn primary apply-btn" data-role="Consultant Interventional Cardiologist"><i data-lucide="send"></i> Apply Now</a>
                    </div>
                </div>

                <!-- JOB 2: MEDICAL ONCOLOGIST -->
                <div class="job-card" data-category="medical">
                    <div class="job-card-top">
                        <div>
                            <span class="job-dept-badge"><i data-lucide="ribbon"></i> Oncology (MedPark)</span>
                            <h3 class="job-card-title">Consultant Medical Oncologist</h3>
                            <div class="job-location-tag"><i data-lucide="map-pin"></i> Sukhda MedPark, Hisar</div>
                        </div>
                    </div>
                    <div class="job-meta-pills">
                        <span class="meta-pill"><i data-lucide="graduation-cap"></i> DM / DrNB Medical Oncology</span>
                        <span class="meta-pill"><i data-lucide="clock"></i> 1-3 Years Experience</span>
                        <span class="meta-pill"><i data-lucide="briefcase"></i> Full Time</span>
                    </div>
                    <p class="job-desc-summary">Lead the daycare chemotherapy infusion suite, targeted immunotherapy protocols, active participation in multidisciplinary tumour boards, and inpatient oncology care.</p>
                    <div class="job-card-footer">
                        <span class="job-salary-note">Best in Healthcare Industry</span>
                        <a href="#apply-direct" class="btn primary apply-btn" data-role="Consultant Medical Oncologist"><i data-lucide="send"></i> Apply Now</a>
                    </div>
                </div>

                <!-- JOB 3: SENIOR RESIDENT MEDICINE -->
                <div class="job-card" data-category="medical">
                    <div class="job-card-top">
                        <div>
                            <span class="job-dept-badge"><i data-lucide="stethoscope"></i> Internal Medicine</span>
                            <h3 class="job-card-title">Senior Resident - Internal Medicine</h3>
                            <div class="job-location-tag"><i data-lucide="map-pin"></i> Sukhda Hospital (DNB Centre)</div>
                        </div>
                    </div>
                    <div class="job-meta-pills">
                        <span class="meta-pill"><i data-lucide="graduation-cap"></i> MD / DNB General Medicine</span>
                        <span class="meta-pill"><i data-lucide="clock"></i> 0-2 Years Post MD</span>
                        <span class="meta-pill"><i data-lucide="briefcase"></i> Full Time</span>
                    </div>
                    <p class="job-desc-summary">Manage medical wards, Medical ICU cases, assist senior consultants in daily rounds, and mentor junior residents under AIIMS-faculty academic guidelines.</p>
                    <div class="job-card-footer">
                        <span class="job-salary-note">Standard Resident Scale + Allowances</span>
                        <a href="#apply-direct" class="btn primary apply-btn" data-role="Senior Resident - Internal Medicine"><i data-lucide="send"></i> Apply Now</a>
                    </div>
                </div>

                <!-- JOB 4: EMERGENCY PHYSICIAN / CMO -->
                <div class="job-card" data-category="medical">
                    <div class="job-card-top">
                        <div>
                            <span class="job-dept-badge"><i data-lucide="zap"></i> Emergency Medicine</span>
                            <h3 class="job-card-title">Casualty Medical Officer (CMO)</h3>
                            <div class="job-location-tag"><i data-lucide="map-pin"></i> 24/7 Emergency Department</div>
                        </div>
                    </div>
                    <div class="job-meta-pills">
                        <span class="meta-pill"><i data-lucide="graduation-cap"></i> MBBS (FEM / MEM Preferred)</span>
                        <span class="meta-pill"><i data-lucide="clock"></i> 1-4 Years in ER</span>
                        <span class="meta-pill"><i data-lucide="briefcase"></i> Rotational Shifts</span>
                    </div>
                    <p class="job-desc-summary">Initial stabilization of acute trauma, cardiac emergencies, stroke protocols, poisoning, and coordination with on-call super specialists.</p>
                    <div class="job-card-footer">
                        <span class="job-salary-note">Commensurate with Experience</span>
                        <a href="#apply-direct" class="btn primary apply-btn" data-role="Casualty Medical Officer"><i data-lucide="send"></i> Apply Now</a>
                    </div>
                </div>

                <!-- JOB 5: ICU STAFF NURSE -->
                <div class="job-card" data-category="nursing">
                    <div class="job-card-top">
                        <div>
                            <span class="job-dept-badge"><i data-lucide="heart"></i> Critical Care Nursing</span>
                            <h3 class="job-card-title">Critical Care / ICU Staff Nurse</h3>
                            <div class="job-location-tag"><i data-lucide="map-pin"></i> Medical / Surgical ICU</div>
                        </div>
                    </div>
                    <div class="job-meta-pills">
                        <span class="meta-pill"><i data-lucide="graduation-cap"></i> B.Sc / GNM Nursing (HNRC Reg.)</span>
                        <span class="meta-pill"><i data-lucide="clock"></i> 1-5 Years ICU Exp</span>
                        <span class="meta-pill"><i data-lucide="briefcase"></i> Rotational Shifts</span>
                    </div>
                    <p class="job-desc-summary">Ventilator management, inotropic infusion monitoring, arterial line &amp; CVP care, adherence to NABH nursing and infection control bundles.</p>
                    <div class="job-card-footer">
                        <span class="job-salary-note">Attractive Salary + PF + ESI + Hostel</span>
                        <a href="#apply-direct" class="btn primary apply-btn" data-role="Critical Care ICU Staff Nurse"><i data-lucide="send"></i> Apply Now</a>
                    </div>
                </div>

                <!-- JOB 6: OT & CATH LAB NURSE -->
                <div class="job-card" data-category="nursing">
                    <div class="job-card-top">
                        <div>
                            <span class="job-dept-badge"><i data-lucide="shield-check"></i> Surgical Nursing</span>
                            <h3 class="job-card-title">OT &amp; Cath Lab Scrub Nurse</h3>
                            <div class="job-location-tag"><i data-lucide="map-pin"></i> Modular OTs / Cath Lab Unit</div>
                        </div>
                    </div>
                    <div class="job-meta-pills">
                        <span class="meta-pill"><i data-lucide="graduation-cap"></i> B.Sc / GNM Nursing</span>
                        <span class="meta-pill"><i data-lucide="clock"></i> 2+ Years OT Experience</span>
                        <span class="meta-pill"><i data-lucide="briefcase"></i> Full Time</span>
                    </div>
                    <p class="job-desc-summary">Assist surgical oncologists, laparoscopy, orthopaedic joint replacement, and cath lab angioplasty cases maintaining strict sterile field standards.</p>
                    <div class="job-card-footer">
                        <span class="job-salary-note">Competitive Pay + Overtime</span>
                        <a href="#apply-direct" class="btn primary apply-btn" data-role="OT & Cath Lab Scrub Nurse"><i data-lucide="send"></i> Apply Now</a>
                    </div>
                </div>

                <!-- JOB 7: DIALYSIS TECHNICIAN -->
                <div class="job-card" data-category="paramedical">
                    <div class="job-card-top">
                        <div>
                            <span class="job-dept-badge"><i data-lucide="droplets"></i> Nephrology</span>
                            <h3 class="job-card-title">Senior Dialysis Technician</h3>
                            <div class="job-location-tag"><i data-lucide="map-pin"></i> Nephrology &amp; Dialysis Centre</div>
                        </div>
                    </div>
                    <div class="job-meta-pills">
                        <span class="meta-pill"><i data-lucide="graduation-cap"></i> Diploma / B.Sc Dialysis Tech</span>
                        <span class="meta-pill"><i data-lucide="clock"></i> 2-4 Years Exp</span>
                        <span class="meta-pill"><i data-lucide="briefcase"></i> Full Time</span>
                    </div>
                    <p class="job-desc-summary">Perform haemodialysis sessions, machine calibration, priming, RO water treatment quality checks, and emergency bedside dialysis in ICU.</p>
                    <div class="job-card-footer">
                        <span class="job-salary-note">Good Compensation Package</span>
                        <a href="#apply-direct" class="btn primary apply-btn" data-role="Senior Dialysis Technician"><i data-lucide="send"></i> Apply Now</a>
                    </div>
                </div>

                <!-- JOB 8: TPA & CASHLESS EXECUTIVE -->
                <div class="job-card" data-category="admin">
                    <div class="job-card-top">
                        <div>
                            <span class="job-dept-badge"><i data-lucide="building-2"></i> Insurance Desk</span>
                            <h3 class="job-card-title">TPA &amp; Cashless Insurance Executive</h3>
                            <div class="job-location-tag"><i data-lucide="map-pin"></i> Sukhda Billing &amp; TPA Desk</div>
                        </div>
                    </div>
                    <div class="job-meta-pills">
                        <span class="meta-pill"><i data-lucide="graduation-cap"></i> Graduate / MBA Healthcare</span>
                        <span class="meta-pill"><i data-lucide="clock"></i> 2+ Years in Hospital TPA</span>
                        <span class="meta-pill"><i data-lucide="briefcase"></i> Full Time</span>
                    </div>
                    <p class="job-desc-summary">Manage pre-authorizations, query resolutions, final cashless approvals with TPAs and private health insurers, and assist Ayushman PM-JAY claims.</p>
                    <div class="job-card-footer">
                        <span class="job-salary-note">Competitive + Performance Bonus</span>
                        <a href="#apply-direct" class="btn primary apply-btn" data-role="TPA & Cashless Insurance Executive"><i data-lucide="send"></i> Apply Now</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- LIFE AT SUKHDA & BENEFITS -->
    <section class="sec-life">
        <div class="wrap">
            <div class="sec-header">
                <span class="kicker">Employee Well-being</span>
                <h2 class="sec-title">Life &amp; Benefits at Sukhda</h2>
                <p class="sec-desc">We take care of the people who care for our patients. Enjoy comprehensive benefits and a healthy work environment.</p>
            </div>

            <div class="perks-grid">
                <div class="perk-card">
                    <div class="perk-icon"><i data-lucide="shield-plus"></i></div>
                    <b>Family Health Insurance</b>
                    <p>Subsidized medical care and health insurance coverage for employees and direct family members.</p>
                </div>

                <div class="perk-card">
                    <div class="perk-icon"><i data-lucide="home"></i></div>
                    <b>Accommodation Assistance</b>
                    <p>Hostel and residential support for outstation doctors, nursing staff, and medical residents in Hisar.</p>
                </div>

                <div class="perk-card">
                    <div class="perk-icon"><i data-lucide="book-open"></i></div>
                    <b>CME &amp; Training Allowances</b>
                    <p>Financial support and on-duty leave to attend national medical conferences and skill workshops.</p>
                </div>

                <div class="perk-card">
                    <div class="perk-icon"><i data-lucide="smile"></i></div>
                    <b>Cultural &amp; Sports Fests</b>
                    <p>Annual Doctors' Day, Nurses' Week celebrations, sports tournaments, and festival gatherings.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- APPLICATION FORM SECTION -->
    <section class="sec-apply-form" id="apply-direct">
        <div class="wrap">
            <div class="apply-box">
                <div style="text-align:center;max-width:650px;margin:0 auto">
                    <span class="kicker">Take the Next Step</span>
                    <h2 class="sec-title" style="margin-bottom:10px">Submit Your Application</h2>
                    <p class="sec-desc">Fill out the form below and attach your CV. Our Human Resources team will review your application and reach out for suitable openings.</p>
                </div>

                <form onsubmit="event.preventDefault(); alert('Thank you for applying to Sukhda Healthcare! Our HR team will review your profile and contact you shortly.'); this.reset();">
                    <div class="form-grid">
                        <div class="form-group">
                            <label>Full Name *</label>
                            <input type="text" class="form-control" placeholder="e.g. Dr. Rajesh Kumar" required>
                        </div>
                        <div class="form-group">
                            <label>Email Address *</label>
                            <input type="email" class="form-control" placeholder="e.g. rajesh.kumar@email.com" required>
                        </div>
                        <div class="form-group">
                            <label>Phone / WhatsApp Number *</label>
                            <input type="tel" class="form-control" placeholder="e.g. +91 98765 43210" required>
                        </div>
                        <div class="form-group">
                            <label>Position Applied For *</label>
                            <select class="form-control" id="position-select" required>
                                <option value="">Select Open Position</option>
                                <option value="Consultant Interventional Cardiologist">Consultant Interventional Cardiologist</option>
                                <option value="Consultant Medical Oncologist">Consultant Medical Oncologist</option>
                                <option value="Senior Resident - Internal Medicine">Senior Resident - Internal Medicine</option>
                                <option value="Casualty Medical Officer">Casualty Medical Officer (CMO)</option>
                                <option value="Critical Care ICU Staff Nurse">Critical Care / ICU Staff Nurse</option>
                                <option value="OT & Cath Lab Scrub Nurse">OT &amp; Cath Lab Scrub Nurse</option>
                                <option value="Senior Dialysis Technician">Senior Dialysis Technician</option>
                                <option value="CT Scan & MRI Radiology Technician">CT Scan &amp; MRI Radiology Technician</option>
                                <option value="TPA & Cashless Insurance Executive">TPA &amp; Cashless Insurance Executive</option>
                                <option value="Patient Care Coordinator">Patient Care Coordinator / Front Desk</option>
                                <option value="General Medical Application">Other / General Speculative Application</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label>Highest Qualification *</label>
                            <input type="text" class="form-control" placeholder="e.g. MD Medicine / B.Sc Nursing" required>
                        </div>
                        <div class="form-group">
                            <label>Total Experience (Years) *</label>
                            <input type="text" class="form-control" placeholder="e.g. 3 Years" required>
                        </div>
                        <div class="form-group">
                            <label>Current Location / City</label>
                            <input type="text" class="form-control" placeholder="e.g. Hisar, Rohtak, Delhi">
                        </div>
                        <div class="form-group">
                            <label>Notice Period / Availability</label>
                            <input type="text" class="form-control" placeholder="e.g. Immediate / 15 Days / 1 Month">
                        </div>
                        <div class="form-group form-full">
                            <label>Upload Resume / CV (PDF or DOCX format, Max 5MB) *</label>
                            <input type="file" class="form-control" accept=".pdf,.doc,.docx" required>
                        </div>
                        <div class="form-group form-full">
                            <label>Cover Note / Professional Summary (Optional)</label>
                            <textarea class="form-control" placeholder="Briefly highlight your clinical strengths, procedural skills, or career goals..."></textarea>
                        </div>
                    </div>
                    <div style="text-align:center;margin-top:24px">
                        <button type="submit" class="btn primary" style="padding:14px 40px;font-size:16px"><i data-lucide="send"></i> Submit Job Application</button>
                    </div>
                    <p style="text-align:center;font-size:13px;color:var(--muted);margin-top:14px">Or email your CV directly to <a href="mailto:careers@sukhdahospitalhisar.com" style="color:var(--green);font-weight:700">careers@sukhdahospitalhisar.com</a></p>
                </form>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    {footer_html}

    <!-- TAB FILTER & APPLY BUTTON SCRIPT -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const buttons = document.querySelectorAll('.tab-btn');
            const cards = document.querySelectorAll('.job-card');
            const posSelect = document.getElementById('position-select');

            buttons.forEach(btn => {{
                btn.addEventListener('click', () => {{
                    buttons.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');

                    const filter = btn.getAttribute('data-filter');
                    cards.forEach(card => {{
                        if (filter === 'all' || card.getAttribute('data-category') === filter) {{
                            card.style.display = 'flex';
                        }} else {{
                            card.style.display = 'none';
                        }}
                    }});
                }});
            }});

            document.querySelectorAll('.apply-btn').forEach(btn => {{
                btn.addEventListener('click', () => {{
                    const role = btn.getAttribute('data-role');
                    if (posSelect && role) {{
                        for (let i = 0; i < posSelect.options.length; i++) {{
                            if (posSelect.options[i].text.toLowerCase().includes(role.toLowerCase())) {{
                                posSelect.selectedIndex = i;
                                break;
                            }}
                        }}
                    }}
                }});
            }});
        }});
    </script>
</body>
</html>
"""

if '</html>' in footer_html:
    idx = footer_html.find('</body>')
    clean_footer = footer_html[:idx] if idx != -1 else footer_html
else:
    clean_footer = footer_html

full_page = html_content.replace(f"<!-- FOOTER -->\n    {footer_html}", f"<!-- FOOTER -->\n    {clean_footer}")

with open('careers.html', 'w', encoding='utf-8') as f:
    f.write(full_page)

print("careers.html generated successfully!")
