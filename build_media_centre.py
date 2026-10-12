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
        /* MEDIA CENTRE SPECIFIC STYLES */
        .sec-news-press {
            padding: 70px 0 90px;
            background: #fafcff
        }

        .news-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin-top: 40px
        }

        .news-card {
            background: #fff;
            border: 1px solid var(--line);
            border-radius: 16px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            box-shadow: 0 6px 20px rgba(5,33,89,0.04);
            transition: all 0.3s ease;
            position: relative
        }

        .news-card:hover {
            transform: translateY(-6px);
            border-color: #a3c4e0;
            box-shadow: 0 16px 36px rgba(5,33,89,0.1)
        }

        .news-img-wrap {
            position: relative;
            background: #02163d;
            aspect-ratio: 16/9;
            overflow: hidden
        }

        .news-img-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.35s ease
        }

        .news-card:hover .news-img-wrap img {
            transform: scale(1.06)
        }

        .news-tag-overlay {
            position: absolute;
            top: 14px;
            left: 14px;
            background: rgba(5, 33, 89, 0.85);
            backdrop-filter: blur(8px);
            color: #8ce09e;
            font-size: 11.5px;
            font-weight: 700;
            text-transform: uppercase;
            padding: 4px 10px;
            border-radius: 20px;
            border: 1px solid rgba(140, 224, 158, 0.3)
        }

        .news-body {
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            flex-grow: 1
        }

        .news-date {
            font-size: 12.5px;
            color: var(--muted);
            display: flex;
            align-items: center;
            gap: 6px;
            font-weight: 600
        }

        .news-title {
            margin: 0;
            font-size: 18px;
            font-weight: 800;
            color: var(--blue);
            line-height: 1.35
        }

        .news-snippet {
            margin: 0;
            color: #475569;
            font-size: 14px;
            line-height: 1.6
        }

        .news-footer {
            margin-top: auto;
            padding-top: 14px;
            border-top: 1px solid #edf2f7;
            display: flex;
            justify-content: space-between;
            align-items: center
        }

        .news-read-more {
            font-size: 13.5px;
            font-weight: 700;
            color: var(--green);
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: color 0.2s ease
        }

        .news-read-more:hover {
            color: var(--blue)
        }

        /* DOCTOR INSIGHTS & BLOGS */
        .sec-doctor-insights {
            padding: 80px 0;
            background: #fff;
            border-top: 1px solid var(--line)
        }

        .blogs-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 24px;
            margin-top: 36px
        }

        .blog-card {
            background: var(--pale);
            border: 1px solid var(--line);
            border-radius: 14px;
            padding: 22px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            transition: all 0.25s ease
        }

        .blog-card:hover {
            transform: translateY(-4px);
            background: #fff;
            box-shadow: 0 10px 24px rgba(5,33,89,0.08);
            border-color: #bad3e8
        }

        .blog-icon {
            width: 44px;
            height: 44px;
            border-radius: 10px;
            background: #eaf5ec;
            color: var(--green);
            display: flex;
            align-items: center;
            justify-content: center
        }

        .blog-card h4 {
            margin: 0;
            font-size: 16px;
            color: var(--blue);
            font-weight: 800;
            line-height: 1.35
        }

        .blog-card p {
            margin: 0;
            font-size: 13.5px;
            color: var(--muted);
            line-height: 1.55
        }

        .blog-author {
            margin-top: auto;
            padding-top: 10px;
            border-top: 1px solid #e2e8f0;
            font-size: 12.5px;
            font-weight: 700;
            color: var(--green)
        }

        /* DOWNLOAD PRESS KIT SECTION */
        .sec-download-kit {
            padding: 70px 0;
            background: linear-gradient(135deg, #02163d 0%, #052159 100%);
            color: #fff
        }

        .kit-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 22px;
            margin-top: 36px
        }

        .kit-card {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.14);
            border-radius: 14px;
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            text-align: center;
            align-items: center
        }

        .kit-icon {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: rgba(39, 129, 50, 0.35);
            color: #8ce09e;
            display: flex;
            align-items: center;
            justify-content: center
        }

        .kit-card-title {
            font-size: 15.5px;
            font-weight: 700;
            color: #fff;
            margin: 0
        }

        .kit-card p {
            font-size: 12.5px;
            color: #cbd5e1;
            margin: 0
        }

        .kit-download-btn {
            margin-top: auto;
            background: #fff;
            color: var(--blue);
            font-size: 12.5px;
            font-weight: 700;
            padding: 8px 16px;
            border-radius: 6px;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s ease
        }

        .kit-download-btn:hover {
            background: #8ce09e;
            color: #02163d
        }

        /* MEDIA CONTACT BOX */
        .sec-media-contact {
            padding: 80px 0;
            background: linear-gradient(135deg, #f2f7fb 0%, #eaf5ec 100%)
        }

        .media-contact-card {
            max-width: 880px;
            margin: 0 auto;
            background: #fff;
            border-radius: 20px;
            padding: 44px;
            box-shadow: 0 16px 40px rgba(5,33,89,0.08);
            border: 1px solid var(--line)
        }

        @media (max-width: 1080px) {
            .news-grid {
                grid-template-columns: repeat(2, 1fr)
            }
            .blogs-grid {
                grid-template-columns: repeat(2, 1fr)
            }
            .kit-grid {
                grid-template-columns: repeat(2, 1fr)
            }
        }

        @media (max-width: 640px) {
            .news-grid,
            .blogs-grid,
            .kit-grid {
                grid-template-columns: 1fr
            }
            .media-contact-card {
                padding: 24px 18px
            }
        }
"""

html_content = f"""<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Media Centre &amp; Press Room | Sukhda Healthcare Hisar</title>
    <meta name="description" content="Official Media Centre and Press Room of Sukhda Multispeciality Hospital and Sukhda MedPark in Hisar. Discover latest press releases, clinical achievements, doctor health articles, and downloadable press kits.">
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
                <span><i data-lucide="newspaper"></i> Press &amp; Media Relations Room</span>
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
                <div class="badge"><i data-lucide="radio"></i> Press Room &bull; Media Centre</div>
                <h1>News, Milestones &amp; <span>Medical Breakthroughs</span></h1>
                <p>Welcome to the official press room of Sukhda Healthcare. Stay informed on medical milestones, technological additions, academic accreditations, community initiatives, and expert doctor health columns.</p>
                <div class="hero-actions">
                    <a href="#press-releases" class="btn primary"><i data-lucide="newspaper"></i> Latest Press Releases</a>
                    <a href="#press-kit" class="btn white"><i data-lucide="download"></i> Download Press Kit</a>
                </div>
            </div>
            <div>
                <div class="hero-stats-card">
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">50+</div>
                        <div class="hero-stat-label">Media &amp; News Features</div>
                    </div>
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">20+</div>
                        <div class="hero-stat-label">Clinical Breakthroughs</div>
                    </div>
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">100+</div>
                        <div class="hero-stat-label">Doctor Health Articles</div>
                    </div>
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">24/7</div>
                        <div class="hero-stat-label">Media Relations Desk</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FILTER TABS -->
    <section class="filter-section" id="press-releases">
        <div class="wrap">
            <div class="tab-bar">
                <button type="button" class="tab-btn active" data-filter="all"><i data-lucide="newspaper"></i> All News &amp; Releases</button>
                <button type="button" class="tab-btn" data-filter="clinical"><i data-lucide="heart-pulse"></i> Clinical Milestones</button>
                <button type="button" class="tab-btn" data-filter="expansion"><i data-lucide="building-2"></i> Infrastructure &amp; Tech</button>
                <button type="button" class="tab-btn" data-filter="academic"><i data-lucide="graduation-cap"></i> Academics &amp; DNB</button>
                <button type="button" class="tab-btn" data-filter="csr"><i data-lucide="heart"></i> Community &amp; CSR</button>
            </div>
        </div>
    </section>

    <!-- PRESS RELEASES & NEWS GRID -->
    <section class="sec-news-press">
        <div class="wrap">
            <div class="sec-header">
                <span class="kicker">Official Announcements</span>
                <h2 class="sec-title">Latest Hospital News &amp; Releases</h2>
                <p class="sec-desc">Verified updates regarding clinical achievements, medical technology upgrades, and community healthcare milestones from Sukhda Healthcare.</p>
            </div>

            <div class="news-grid">
                <!-- NEWS 1: LINAC RADIOTHERAPY -->
                <div class="news-card" data-category="expansion">
                    <div class="news-img-wrap">
                        <img src="assets/images/facility-img-1.jpg" alt="LINAC Installation Sukhda MedPark" onerror="this.src='assets/images/about-img-1.jpg'">
                        <span class="news-tag-overlay"><i data-lucide="scan"></i> Tech Upgrade</span>
                    </div>
                    <div class="news-body">
                        <div class="news-date"><i data-lucide="calendar"></i> November 15, 2025 &bull; Hisar</div>
                        <h3 class="news-title">Sukhda MedPark Launches Advanced Linear Accelerator (LINAC) for Precision Radiotherapy</h3>
                        <p class="news-snippet">Hisar gets state-of-the-art precision radiation oncology services with 3D-CRT and IMRT capabilities, eliminating the need for cancer patients to travel to metro cities for daily radiation sessions.</p>
                        <div class="news-footer">
                            <a href="#" class="news-read-more" onclick="event.preventDefault(); alert('Press Release: Sukhda MedPark commissions modern Linear Accelerator for cancer radiotherapy in Hisar.');">Read Full Release &rarr;</a>
                        </div>
                    </div>
                </div>

                <!-- NEWS 2: DNB ACCREDITATION -->
                <div class="news-card" data-category="academic">
                    <div class="news-img-wrap">
                        <img src="assets/images/about-img-2.jpg" alt="DNB Accreditation Sukhda" onerror="this.src='assets/images/service-img-1.jpg'">
                        <span class="news-tag-overlay"><i data-lucide="award"></i> Academics</span>
                    </div>
                    <div class="news-body">
                        <div class="news-date"><i data-lucide="calendar"></i> August 22, 2025 &bull; Hisar</div>
                        <h3 class="news-title">NBEMS Grants National Accreditation for DNB General Medicine Residency to Sukhda Hospital</h3>
                        <p class="news-snippet">The National Board of Examinations in Medical Sciences (NBEMS) officially recognized Sukhda Multispeciality Hospital as a post-graduate teaching and training institute in General Medicine under Dr. Amit Mehta.</p>
                        <div class="news-footer">
                            <a href="#" class="news-read-more" onclick="event.preventDefault(); alert('Press Release: National Board of Examinations grants DNB General Medicine accreditation to Sukhda Hospital.');">Read Full Release &rarr;</a>
                        </div>
                    </div>
                </div>

                <!-- NEWS 3: USAID CSR -->
                <div class="news-card" data-category="csr">
                    <div class="news-img-wrap">
                        <img src="assets/images/service-img-2.jpg" alt="USAID Samridh Sukhda" onerror="this.src='assets/images/about-img-1.jpg'">
                        <span class="news-tag-overlay"><i data-lucide="heart"></i> CSR Partnership</span>
                    </div>
                    <div class="news-body">
                        <div class="news-date"><i data-lucide="calendar"></i> May 10, 2025 &bull; Hisar</div>
                        <h3 class="news-title">USAID SAMRIDH and Sukhda Healthcare Expand Rural Primary Health Outreach to 65,000 People</h3>
                        <p class="news-snippet">Flagship collaborative health initiative reaches 8 rural blocks in Western Haryana, providing mobile screening vans, free blood tests, and telemedicine referral linkage for underprivileged villages.</p>
                        <div class="news-footer">
                            <a href="#" class="news-read-more" onclick="event.preventDefault(); alert('Press Release: USAID SAMRIDH & Sukhda Healthcare expand rural primary healthcare outreach in Haryana.');">Read Full Release &rarr;</a>
                        </div>
                    </div>
                </div>

                <!-- NEWS 4: GOLDEN HOUR PAMI -->
                <div class="news-card" data-category="clinical">
                    <div class="news-img-wrap">
                        <img src="assets/images/service-img-1.jpg" alt="Cardiac PAMI Angioplasty" onerror="this.src='assets/images/facility-img-1.jpg'">
                        <span class="news-tag-overlay"><i data-lucide="heart-pulse"></i> Clinical Milestone</span>
                    </div>
                    <div class="news-body">
                        <div class="news-date"><i data-lucide="calendar"></i> January 18, 2026 &bull; Hisar</div>
                        <h3 class="news-title">Golden Hour Miracle: 82-Year-Old Cardiac Patient Saved via 24/7 Primary Angioplasty (PAMI)</h3>
                        <p class="news-snippet">Dr. Ankur Kamra and the 24/7 flat-panel cath lab team achieved a door-to-balloon time of 34 minutes to reopen a 100% occluded coronary artery during midnight emergency.</p>
                        <div class="news-footer">
                            <a href="#" class="news-read-more" onclick="event.preventDefault(); alert('Press Release: 82-year-old patient successfully saved during golden hour cardiac angioplasty.');">Read Full Release &rarr;</a>
                        </div>
                    </div>
                </div>

                <!-- NEWS 5: 3D KNEE RESURFACING -->
                <div class="news-card" data-category="clinical">
                    <div class="news-img-wrap">
                        <img src="assets/images/service-img-3.jpg" alt="3D Knee Resurfacing" onerror="this.src='assets/images/about-img-2.jpg'">
                        <span class="news-tag-overlay"><i data-lucide="bone"></i> Ortho Breakthrough</span>
                    </div>
                    <div class="news-body">
                        <div class="news-date"><i data-lucide="calendar"></i> February 04, 2026 &bull; Hisar</div>
                        <h3 class="news-title">Sukhda Orthopaedic Team Performs Region's First Custom 3D Knee Resurfacing</h3>
                        <p class="news-snippet">Advanced muscle-sparing joint preservation technique allows elderly bilateral knee osteoarthritis patient to begin unassisted walking within 24 hours post-surgery.</p>
                        <div class="news-footer">
                            <a href="#" class="news-read-more" onclick="event.preventDefault(); alert('Press Release: Region-first 3D custom knee resurfacing performed at Sukhda Orthopaedics.');">Read Full Release &rarr;</a>
                        </div>
                    </div>
                </div>

                <!-- NEWS 6: HEALTHCARE SUMMIT AWARD -->
                <div class="news-card" data-category="academic">
                    <div class="news-img-wrap">
                        <img src="assets/images/about-img-1.jpg" alt="Healthcare Excellence Award" onerror="this.src='assets/images/service-img-2.jpg'">
                        <span class="news-tag-overlay"><i data-lucide="award"></i> Recognition</span>
                    </div>
                    <div class="news-body">
                        <div class="news-date"><i data-lucide="calendar"></i> October 28, 2025 &bull; New Delhi</div>
                        <h3 class="news-title">Sukhda Healthcare Conferred 'Best Multi-Speciality Hospital in Western Haryana'</h3>
                        <p class="news-snippet">Honoured for 24+ years of patient safety, NABH compliance, cutting-edge ICU infrastructure, and philanthropic healthcare delivery across Northern India.</p>
                        <div class="news-footer">
                            <a href="#" class="news-read-more" onclick="event.preventDefault(); alert('Press Release: Sukhda Healthcare awarded Best Multi-Speciality Hospital in Western Haryana.');">Read Full Release &rarr;</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- DOCTOR HEALTH INSIGHTS & BLOGS -->
    <section class="sec-doctor-insights">
        <div class="wrap">
            <div class="sec-header">
                <span class="kicker">Expert Knowledge</span>
                <h2 class="sec-title">Doctor Insights &amp; Health Articles</h2>
                <p class="sec-desc">Preventive healthcare advice, disease management guidelines, and wellness tips written by senior consultants at Sukhda Healthcare.</p>
            </div>

            <div class="blogs-grid">
                <div class="blog-card">
                    <div class="blog-icon"><i data-lucide="heart-pulse"></i></div>
                    <h4>Recognizing Silent Heart Attacks &amp; The Golden Hour</h4>
                    <p>Understanding atypical cardiac symptoms such as sudden sweating, epigastric discomfort, and the critical importance of reaching a Cath Lab within 60 minutes.</p>
                    <div class="blog-author"><i data-lucide="user"></i> Dr. Ankur Kamra (Cardiology)</div>
                </div>

                <div class="blog-card">
                    <div class="blog-icon"><i data-lucide="ribbon"></i></div>
                    <h4>Early Cancer Screening: Why 15 Minutes Can Save a Life</h4>
                    <p>Mammography, Pap smears, and oral examinations for early asymptomatic detection when malignancy is 100% treatable.</p>
                    <div class="blog-author"><i data-lucide="user"></i> Dr. Amit Mehta (Internal Medicine)</div>
                </div>

                <div class="blog-card">
                    <div class="blog-icon"><i data-lucide="baby"></i></div>
                    <h4>Managing High-Risk Pregnancies &amp; Gestational Hypertension</h4>
                    <p>Key prenatal monitoring milestones, blood pressure protocols, and when a Level-3 NICU setup is essential for newborn safety.</p>
                    <div class="blog-author"><i data-lucide="user"></i> Dr. Manisha Mehta (Gynaecology)</div>
                </div>

                <div class="blog-card">
                    <div class="blog-icon"><i data-lucide="bone"></i></div>
                    <h4>3D Knee Resurfacing vs Traditional Knee Replacement</h4>
                    <p>How custom 3D patient-specific implants preserve natural bone, retain ligaments, and allow rapid rehabilitation without long hospitalization.</p>
                    <div class="blog-author"><i data-lucide="user"></i> Sukhda Joint Replacement Team</div>
                </div>
            </div>
        </div>
    </section>

    <!-- DOWNLOAD PRESS KIT & BROCHURES -->
    <section class="sec-download-kit" id="press-kit">
        <div class="wrap">
            <div class="sec-header">
                <span class="kicker" style="color:#8ce09e">Resources &amp; Downloads</span>
                <h2 class="sec-title" style="color:#fff">Media Press Kit &amp; Publications</h2>
                <p class="sec-desc" style="color:#cbd5e1">Download official factsheets, annual reports, brand logos, and patient guide booklets for journalistic and reference use.</p>
            </div>

            <div class="kit-grid">
                <div class="kit-card">
                    <div class="kit-icon"><i data-lucide="file-text"></i></div>
                    <div class="kit-card-title">Hospital Corporate Factsheet</div>
                    <p>Comprehensive overview of bed capacity, medical leadership, OTs, Cath Lab, and MedPark.</p>
                    <a href="assets/images/sukhda-logo.png" download class="kit-download-btn"><i data-lucide="download"></i> Download PDF (2.4 MB)</a>
                </div>

                <div class="kit-card">
                    <div class="kit-icon"><i data-lucide="book-open"></i></div>
                    <div class="kit-card-title">Annual Clinical Report 2025-26</div>
                    <p>Clinical volume statistics, door-to-balloon records, infection control metrics, and CSR reach.</p>
                    <a href="assets/images/sukhda-logo.png" download class="kit-download-btn"><i data-lucide="download"></i> Download PDF (4.8 MB)</a>
                </div>

                <div class="kit-card">
                    <div class="kit-icon"><i data-lucide="image"></i></div>
                    <div class="kit-card-title">High-Res Brand Logos &amp; Photos</div>
                    <p>Vector logos, hospital exterior/interior photos, and doctor portrait press kit.</p>
                    <a href="assets/images/sukhda-logo.png" download class="kit-download-btn"><i data-lucide="download"></i> Download ZIP (12 MB)</a>
                </div>

                <div class="kit-card">
                    <div class="kit-icon"><i data-lucide="shield-check"></i></div>
                    <div class="kit-card-title">Patient Information &amp; TPA Guide</div>
                    <p>Empanelled TPAs, Ayushman PM-JAY instructions, and visitor guidelines brochure.</p>
                    <a href="assets/images/sukhda-logo.png" download class="kit-download-btn"><i data-lucide="download"></i> Download PDF (1.8 MB)</a>
                </div>
            </div>
        </div>
    </section>

    <!-- MEDIA INQUIRY FORM -->
    <section class="sec-media-contact">
        <div class="wrap">
            <div class="media-contact-card">
                <div style="text-align:center;max-width:680px;margin:0 auto">
                    <span class="kicker">Journalist &amp; Media Relations</span>
                    <h2 class="sec-title" style="margin-bottom:10px">Media Contact &amp; Press Inquiries</h2>
                    <p class="sec-desc">For press statements, doctor interviews, hospital filming permissions, or official statistics, please connect with our corporate communications desk.</p>
                </div>

                <form onsubmit="event.preventDefault(); alert('Thank you for reaching out! Our Media & PR coordinator will respond to your press inquiry promptly.'); this.reset();">
                    <div class="form-grid">
                        <div class="form-group">
                            <label>Journalist / Reporter Name *</label>
                            <input type="text" class="form-control" placeholder="e.g. Anjali Verma" required>
                        </div>
                        <div class="form-group">
                            <label>Media House / Publication / Channel *</label>
                            <input type="text" class="form-control" placeholder="e.g. Dainik Bhaskar / The Tribune / PTI" required>
                        </div>
                        <div class="form-group">
                            <label>Email Address *</label>
                            <input type="email" class="form-control" placeholder="e.g. anjali.verma@newsmedia.com" required>
                        </div>
                        <div class="form-group">
                            <label>Phone / WhatsApp Number *</label>
                            <input type="tel" class="form-control" placeholder="e.g. +91 98765 43210" required>
                        </div>
                        <div class="form-group">
                            <label>Inquiry Topic / Subject *</label>
                            <select class="form-control" required>
                                <option value="">Select Topic</option>
                                <option value="Interview with Doctor / Leadership">Doctor / Leadership Interview</option>
                                <option value="Press Statement / Comment">Official Press Statement</option>
                                <option value="Medical Milestone / Case Coverage">Medical Milestone Story Coverage</option>
                                <option value="Hospital Filming / Photography Permission">Filming / Photography Permission</option>
                                <option value="CSR & Community Health Feature">CSR &amp; Rural Health Feature</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label>Deadline / Date Needed</label>
                            <input type="text" class="form-control" placeholder="e.g. Today by 5 PM / Tomorrow">
                        </div>
                        <div class="form-group form-full">
                            <label>Questions / Detailed Inquiry *</label>
                            <textarea class="form-control" placeholder="Please outline your story angle, specific questions for doctors, or interview requirements..." required></textarea>
                        </div>
                    </div>
                    <div style="text-align:center;margin-top:24px">
                        <button type="submit" class="btn primary" style="padding:14px 40px;font-size:16px"><i data-lucide="send"></i> Submit Media Inquiry</button>
                    </div>
                    <p style="text-align:center;font-size:13px;color:var(--muted);margin-top:14px">Official Media Email: <a href="mailto:media@sukhdahospitalhisar.com" style="color:var(--green);font-weight:700">media@sukhdahospitalhisar.com</a> | Spokesperson: <b>+91-99965-44005</b></p>
                </form>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    {footer_html}

    <!-- TAB FILTER SCRIPT -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const buttons = document.querySelectorAll('.tab-btn');
            const cards = document.querySelectorAll('.news-card');

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

with open('media-centre.html', 'w', encoding='utf-8') as f:
    f.write(full_page)

# Also create media.html as a copy
with open('media.html', 'w', encoding='utf-8') as f:
    f.write(full_page)

print("media-centre.html and media.html generated successfully!")
