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

header_html = raw_header.replace('href="index.html#cases"', 'href="patient-stories.html" class="on"')
header_html = header_html.replace('href="index.html#patients"', 'href="patient-stories.html"')
header_html = header_html.replace('href="doctor.html" class="on"', 'href="doctor.html"')

from generate_all_pages import common_styles

page_styles = """
        /* STORIES SPECIFIC STYLES */
        .sec-stories {
            padding: 60px 0 80px;
            background: #fafcff
        }

        .stories-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px
        }

        .story-card {
            background: #fff;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 8px 24px rgba(5,33,89,0.06);
            border: 1px solid var(--line);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column
        }

        .story-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 16px 36px rgba(5,33,89,0.12);
            border-color: #b0cde6
        }

        .story-header {
            background: linear-gradient(135deg, #052159 0%, #0d3880 100%);
            color: #fff;
            padding: 22px 24px;
            position: relative
        }

        .story-header.oncology {
            background: linear-gradient(135deg, #02163d 0%, #1e3a8a 100%);
        }

        .story-header.cardio {
            background: linear-gradient(135deg, #781010 0%, #a81c1c 100%);
        }

        .story-header.ortho {
            background: linear-gradient(135deg, #064e3b 0%, #047857 100%);
        }

        .story-header.gynae {
            background: linear-gradient(135deg, #6b21a8 0%, #8b5cf6 100%);
        }

        .story-header.nephro {
            background: linear-gradient(135deg, #0f766e 0%, #0284c7 100%);
        }

        .story-badge-top {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(255,255,255,0.18);
            border: 1px solid rgba(255,255,255,0.3);
            font-size: 12px;
            padding: 3px 10px;
            border-radius: 20px;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 12px
        }

        .story-title {
            font-size: 18px;
            font-weight: 800;
            line-height: 1.35;
            margin: 0;
            color: #fff
        }

        .story-body {
            padding: 24px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
            gap: 16px
        }

        .story-patient-meta {
            display: flex;
            align-items: center;
            gap: 14px;
            padding-bottom: 14px;
            border-bottom: 1px solid #edf2f7
        }

        .patient-avatar {
            width: 52px;
            height: 52px;
            border-radius: 50%;
            background: #eaf5ec;
            color: var(--green);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: 800;
            flex-shrink: 0;
            border: 2px solid #278132
        }

        .patient-info b {
            display: block;
            font-size: 16px;
            color: var(--blue);
            font-family: 'Montserrat', sans-serif
        }

        .patient-info span {
            font-size: 13.5px;
            color: var(--muted)
        }

        .story-quote-box {
            background: var(--pale);
            border-left: 4px solid var(--green);
            padding: 14px 16px;
            border-radius: 0 8px 8px 0;
            font-size: 14.5px;
            font-style: italic;
            color: #274060;
            line-height: 1.55;
            position: relative
        }

        .story-clinical-specs {
            display: flex;
            flex-direction: column;
            gap: 8px;
            font-size: 13.5px
        }

        .spec-row {
            display: flex;
            gap: 8px;
            line-height: 1.4
        }

        .spec-row span.label {
            font-weight: 700;
            color: var(--blue);
            min-width: 95px;
            flex-shrink: 0
        }

        .spec-row span.val {
            color: #334155
        }

        .story-footer {
            margin-top: auto;
            padding-top: 14px;
            border-top: 1px solid #edf2f7;
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 13px;
            color: var(--muted)
        }

        .doctor-tag {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-weight: 700;
            color: var(--green)
        }

        /* VIDEO TESTIMONIALS */
        .sec-video-stories {
            padding: 70px 0;
            background: #fff;
            border-top: 1px solid var(--line);
            border-bottom: 1px solid var(--line)
        }

        .video-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 28px
        }

        .video-card {
            background: var(--pale);
            border-radius: 14px;
            overflow: hidden;
            border: 1px solid var(--line);
            box-shadow: 0 6px 18px rgba(0,0,0,0.04);
            display: flex;
            flex-direction: column
        }

        .video-thumb-wrap {
            position: relative;
            background: #02163d;
            aspect-ratio: 16/9;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            overflow: hidden
        }

        .video-thumb-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.8;
            transition: transform 0.3s ease, opacity 0.3s ease
        }

        .video-thumb-wrap:hover img {
            transform: scale(1.05);
            opacity: 0.95
        }

        .play-btn-circle {
            position: absolute;
            width: 54px;
            height: 54px;
            border-radius: 50%;
            background: var(--green);
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            transition: transform 0.2s ease, background 0.2s ease
        }

        .video-thumb-wrap:hover .play-btn-circle {
            transform: scale(1.12);
            background: #1f6b28
        }

        .video-card-body {
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            flex-grow: 1
        }

        .video-card-body h4 {
            margin: 0;
            font-size: 16px;
            color: var(--blue);
            font-weight: 700;
            line-height: 1.3
        }

        .video-card-body p {
            margin: 0;
            font-size: 13.5px;
            color: var(--muted)
        }

        /* REVIEWS */
        .sec-reviews {
            padding: 60px 0;
            background: #fff
        }

        .reviews-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 36px
        }

        .review-card {
            background: var(--pale);
            border: 1px solid var(--line);
            border-radius: 12px;
            padding: 22px;
            display: flex;
            flex-direction: column;
            gap: 12px
        }

        .stars {
            display: flex;
            gap: 3px;
            color: #f59e0b
        }

        .review-card p {
            margin: 0;
            font-size: 14px;
            color: #334155;
            line-height: 1.5;
            font-style: italic
        }

        .review-meta {
            margin-top: auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 12.5px;
            color: var(--muted);
            font-weight: 600
        }

        /* SHARE STORY FORM SECTION */
        .sec-share-form {
            padding: 80px 0;
            background: linear-gradient(135deg, #f2f7fb 0%, #eaf5ec 100%);
            position: relative
        }

        .share-box {
            max-width: 860px;
            margin: 0 auto;
            background: #fff;
            border-radius: 20px;
            padding: 44px;
            box-shadow: 0 16px 40px rgba(5,33,89,0.08);
            border: 1px solid var(--line)
        }

        @media (max-width: 1080px) {
            .stories-grid {
                grid-template-columns: repeat(2, 1fr)
            }
            .reviews-grid {
                grid-template-columns: repeat(2, 1fr)
            }
            .video-grid {
                grid-template-columns: repeat(2, 1fr)
            }
        }

        @media (max-width: 640px) {
            .stories-grid,
            .reviews-grid,
            .video-grid {
                grid-template-columns: 1fr
            }
            .share-box {
                padding: 24px 18px
            }
        }
"""

html_content = f"""<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Patient Stories &amp; Recovery Journeys | Sukhda Hospital Hisar</title>
    <meta name="description" content="Read real, inspiring patient recovery stories and clinical case triumphs from Sukhda Multispeciality Hospital and Sukhda MedPark in Hisar. Discover patient experiences across Cardiology, Oncology, Orthopaedics, High-Risk Gynaecology, and Critical Care.">
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
                <span><i data-lucide="award"></i> NABH Accredited Multi-Speciality</span>
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
                <div class="badge"><i data-lucide="heart-handshake"></i> Patient Stories &amp; Clinical Triumphs</div>
                <h1>Real Stories of <span>Healing &amp; Hope</span></h1>
                <p>Every recovery is a testament to human courage, clinical mastery, and compassionate care. Read how our doctors, nurses, and medical technology helped patients overcome critical health battles at Sukhda Healthcare.</p>
                <div class="hero-actions">
                    <a href="#stories-grid" class="btn primary"><i data-lucide="book-open"></i> Read Case Stories</a>
                    <a href="#share-story" class="btn white"><i data-lucide="message-square-plus"></i> Share Your Story</a>
                </div>
            </div>
            <div>
                <div class="hero-stats-card">
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">50,000+</div>
                        <div class="hero-stat-label">Patients Healed &amp; Recovered</div>
                    </div>
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">99.4%</div>
                        <div class="hero-stat-label">Positive Patient Experience</div>
                    </div>
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">&lt; 40 min</div>
                        <div class="hero-stat-label">Average Door-to-Balloon (PAMI)</div>
                    </div>
                    <div class="hero-stat-item">
                        <div class="hero-stat-num">4.9 ★</div>
                        <div class="hero-stat-label">Google Community Trust Rating</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FILTER TABS -->
    <section class="filter-section">
        <div class="wrap">
            <div class="tab-bar">
                <button type="button" class="tab-btn active" data-filter="all"><i data-lucide="grid"></i> All Stories</button>
                <button type="button" class="tab-btn" data-filter="cardiology"><i data-lucide="heart-pulse"></i> Cardiology &amp; Cath Lab</button>
                <button type="button" class="tab-btn" data-filter="oncology"><i data-lucide="ribbon"></i> Oncology (MedPark)</button>
                <button type="button" class="tab-btn" data-filter="ortho"><i data-lucide="bone"></i> Orthopaedics &amp; 3D Knee</button>
                <button type="button" class="tab-btn" data-filter="gynae"><i data-lucide="baby"></i> High-Risk Gynaecology</button>
                <button type="button" class="tab-btn" data-filter="nephro"><i data-lucide="droplets"></i> Nephrology &amp; Dialysis</button>
                <button type="button" class="tab-btn" data-filter="critical"><i data-lucide="activity"></i> Trauma &amp; Critical Care</button>
            </div>
        </div>
    </section>

    <!-- FEATURED STORIES GRID -->
    <section class="sec-stories" id="stories-grid">
        <div class="wrap">
            <div class="sec-header">
                <span class="kicker">Clinical Case Records</span>
                <h2 class="sec-title">Inspiring Patient Journeys</h2>
                <p class="sec-desc">Explore verified case histories and heartfelt testimonials from patients across Haryana and neighbouring regions treated at Sukhda Hospital &amp; MedPark.</p>
            </div>

            <div class="stories-grid">
                <!-- STORY 1: CARDIOLOGY -->
                <div class="story-card" data-category="cardiology">
                    <div class="story-header cardio">
                        <span class="story-badge-top"><i data-lucide="heart-pulse"></i> Cardiology &bull; PAMI</span>
                        <h3 class="story-title">Golden Hour Angioplasty Saves 68-Year-Old Heart Attack Patient</h3>
                    </div>
                    <div class="story-body">
                        <div class="story-patient-meta">
                            <div class="patient-avatar">RD</div>
                            <div class="patient-info">
                                <b>Rameshwar Dass (68 Yrs)</b>
                                <span>Hansi, Haryana &bull; Emergency PAMI</span>
                            </div>
                        </div>
                        <div class="story-quote-box">
                            "I collapsed at home with crushing chest pain at 1 AM. The Sukhda Emergency and Cath Lab team acted within minutes. By 2:30 AM, Dr. Kamra had opened my 99% blocked artery with a stent. I got a second life!"
                        </div>
                        <div class="story-clinical-specs">
                            <div class="spec-row"><span class="label">Diagnosis:</span><span class="val">Acute Anterior Wall STEMI</span></div>
                            <div class="spec-row"><span class="label">Procedure:</span><span class="val">Primary Angioplasty (PAMI) with DES</span></div>
                            <div class="spec-row"><span class="label">Cath Lab Time:</span><span class="val">Door-to-Balloon: 38 Minutes</span></div>
                            <div class="spec-row"><span class="label">Recovery:</span><span class="val">Walking on Day 2, Discharged Day 3</span></div>
                        </div>
                        <div class="story-footer">
                            <span class="doctor-tag"><i data-lucide="stethoscope"></i> Dr. Ankur Kamra</span>
                            <span>Sukhda Multispeciality</span>
                        </div>
                    </div>
                </div>

                <!-- STORY 2: ONCOLOGY -->
                <div class="story-card" data-category="oncology">
                    <div class="story-header oncology">
                        <span class="story-badge-top"><i data-lucide="ribbon"></i> Oncology &bull; MedPark</span>
                        <h3 class="story-title">Triumph Over Stage-III Breast Cancer Through Multidisciplinary Care</h3>
                    </div>
                    <div class="story-body">
                        <div class="story-patient-meta">
                            <div class="patient-avatar">SD</div>
                            <div class="patient-info">
                                <b>Sunita Devi (52 Yrs)</b>
                                <span>Hisar &bull; Complete Remission</span>
                            </div>
                        </div>
                        <div class="story-quote-box">
                            "When diagnosed with Stage 3 cancer, our family was devastated. The Tumour Board at Sukhda MedPark gave us clarity and hope. The chemotherapy suite, surgery, and LINAC radiation care were all available under one roof with extreme empathy."
                        </div>
                        <div class="story-clinical-specs">
                            <div class="spec-row"><span class="label">Diagnosis:</span><span class="val">Invasive Ductal Carcinoma (Stage III)</span></div>
                            <div class="spec-row"><span class="label">Treatment:</span><span class="val">Neoadjuvant Chemo + Onco-Surgery + LINAC</span></div>
                            <div class="spec-row"><span class="label">Facility:</span><span class="val">Sukhda MedPark Daycare &amp; RT Unit</span></div>
                            <div class="spec-row"><span class="label">Status:</span><span class="val">3 Years Disease-Free Remission</span></div>
                        </div>
                        <div class="story-footer">
                            <span class="doctor-tag"><i data-lucide="stethoscope"></i> Dr. Amit Mehta &amp; Team</span>
                            <span>Sukhda MedPark</span>
                        </div>
                    </div>
                </div>

                <!-- STORY 3: ORTHOPAEDICS -->
                <div class="story-card" data-category="ortho">
                    <div class="story-header ortho">
                        <span class="story-badge-top"><i data-lucide="bone"></i> Orthopaedics &bull; 3D Knee</span>
                        <h3 class="story-title">From Bedridden to Active Farming with 3D Knee Resurfacing</h3>
                    </div>
                    <div class="story-body">
                        <div class="story-patient-meta">
                            <div class="patient-avatar">BS</div>
                            <div class="patient-info">
                                <b>Balwant Singh (71 Yrs)</b>
                                <span>Fatehabad &bull; Bilateral Knee Recovery</span>
                            </div>
                        </div>
                        <div class="story-quote-box">
                            "For 5 years I could not take 10 steps without severe knee pain. After bilateral 3D custom knee resurfacing at Sukhda, I stood on my feet the very next morning without unbearable pain. Today, I am back in my fields."
                        </div>
                        <div class="story-clinical-specs">
                            <div class="spec-row"><span class="label">Diagnosis:</span><span class="val">Grade-4 Bilateral Osteoarthritis</span></div>
                            <div class="spec-row"><span class="label">Technique:</span><span class="val">Custom 3D Muscle-Sparing Resurfacing</span></div>
                            <div class="spec-row"><span class="label">Blood Loss:</span><span class="val">Minimal (&lt;50ml, Zero Transfusion)</span></div>
                            <div class="spec-row"><span class="label">Milestone:</span><span class="val">Climbed Stairs in 1 Week</span></div>
                        </div>
                        <div class="story-footer">
                            <span class="doctor-tag"><i data-lucide="stethoscope"></i> Joint Replacement Unit</span>
                            <span>Sukhda Hospital</span>
                        </div>
                    </div>
                </div>

                <!-- STORY 4: GYNAECOLOGY & NICU -->
                <div class="story-card" data-category="gynae">
                    <div class="story-header gynae">
                        <span class="story-badge-top"><i data-lucide="baby"></i> High-Risk Gynaecology</span>
                        <h3 class="story-title">Miracle Preterm Twin Delivery at 31 Weeks with Level-3 NICU Care</h3>
                    </div>
                    <div class="story-body">
                        <div class="story-patient-meta">
                            <div class="patient-avatar">PS</div>
                            <div class="patient-info">
                                <b>Pooja Sharma (29 Yrs)</b>
                                <span>Jind &bull; High-Risk Twin Gestation</span>
                            </div>
                        </div>
                        <div class="story-quote-box">
                            "My blood pressure spiked dangerously at 31 weeks. Dr. Manisha Mehta expertly performed an emergency caesarean, and the Sukhda NICU team cared for our 1.2kg twin babies like family for 22 days until they were thriving."
                        </div>
                        <div class="story-clinical-specs">
                            <div class="spec-row"><span class="label">Condition:</span><span class="val">Severe Preeclampsia &amp; Preterm Twins</span></div>
                            <div class="spec-row"><span class="label">Management:</span><span class="val">Emergency LSCS + Level-3 NICU CPAP</span></div>
                            <div class="spec-row"><span class="label">Birth Weights:</span><span class="val">1.2 kg &amp; 1.4 kg</span></div>
                            <div class="spec-row"><span class="label">Discharge:</span><span class="val">Both babies healthy at 2.1 kg</span></div>
                        </div>
                        <div class="story-footer">
                            <span class="doctor-tag"><i data-lucide="stethoscope"></i> Dr. Manisha Mehta</span>
                            <span>Sukhda Hospital</span>
                        </div>
                    </div>
                </div>

                <!-- STORY 5: NEPHROLOGY -->
                <div class="story-card" data-category="nephro">
                    <div class="story-header nephro">
                        <span class="story-badge-top"><i data-lucide="droplets"></i> Nephrology &bull; Dialysis</span>
                        <h3 class="story-title">Renal Crisis Managed: Quality Life Restored with Cashless Dialysis</h3>
                    </div>
                    <div class="story-body">
                        <div class="story-patient-meta">
                            <div class="patient-avatar">SK</div>
                            <div class="patient-info">
                                <b>Satish Kumar (58 Yrs)</b>
                                <span>Barwala &bull; ESRD Maintenance</span>
                            </div>
                        </div>
                        <div class="story-quote-box">
                            "I came in breathless with severe fluid in my lungs due to kidney failure. Sukhda's nephrology team stabilized me overnight. With Ayushman PM-JAY cashless support, I receive hygienic, painless dialysis twice a week."
                        </div>
                        <div class="story-clinical-specs">
                            <div class="spec-row"><span class="label">Condition:</span><span class="val">End-Stage Renal Disease (ESRD)</span></div>
                            <div class="spec-row"><span class="label">Procedure:</span><span class="val">Urgent Bedside Dialysis &amp; AV Fistula</span></div>
                            <div class="spec-row"><span class="label">Coverage:</span><span class="val">100% Cashless via PM-JAY / TPA</span></div>
                            <div class="spec-row"><span class="label">Quality:</span><span class="val">German Fresenius RO Dialysis Machines</span></div>
                        </div>
                        <div class="story-footer">
                            <span class="doctor-tag"><i data-lucide="stethoscope"></i> Nephrology Unit</span>
                            <span>Sukhda Hospital</span>
                        </div>
                    </div>
                </div>

                <!-- STORY 6: TRAUMA & CRITICAL CARE -->
                <div class="story-card" data-category="critical">
                    <div class="story-header">
                        <span class="story-badge-top"><i data-lucide="activity"></i> Polytrauma &bull; ICU</span>
                        <h3 class="story-title">Road Accident Polytrauma Survivor Returns to Full Mobility</h3>
                    </div>
                    <div class="story-body">
                        <div class="story-patient-meta">
                            <div class="patient-avatar">VY</div>
                            <div class="patient-info">
                                <b>Vikas Yadav (34 Yrs)</b>
                                <span>Sirsa &bull; Major Trauma Recovery</span>
                            </div>
                        </div>
                        <div class="story-quote-box">
                            "Following a severe highway crash, I was brought to Sukhda in shock with internal bleeding and fractured limbs. The trauma surgeons and 24/7 ICU team worked tirelessly. Today, I am walking independently and working again."
                        </div>
                        <div class="story-clinical-specs">
                            <div class="spec-row"><span class="label">Injuries:</span><span class="val">Splenic Rupture + Compound Femur Fracture</span></div>
                            <div class="spec-row"><span class="label">Surgeries:</span><span class="val">Emergency Laparotomy + Ortho IM Nailing</span></div>
                            <div class="spec-row"><span class="label">ICU Stay:</span><span class="val">5 Days Multidisciplinary Critical Care</span></div>
                            <div class="spec-row"><span class="label">Outcome:</span><span class="val">100% Limb Function &amp; Independence</span></div>
                        </div>
                        <div class="story-footer">
                            <span class="doctor-tag"><i data-lucide="stethoscope"></i> Trauma &amp; ICU Team</span>
                            <span>Sukhda Hospital</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- VIDEO RECOVERY HIGHLIGHTS -->
    <section class="sec-video-stories">
        <div class="wrap">
            <div class="sec-header">
                <span class="kicker">Video Chronicles</span>
                <h2 class="sec-title">In Their Own Words</h2>
                <p class="sec-desc">Listen to patients and their loved ones recount their experiences with our medical specialists, nursing staff, and hospital facilities.</p>
            </div>

            <div class="video-grid">
                <div class="video-card">
                    <div class="video-thumb-wrap" onclick="alert('Playing patient video testimonial...')">
                        <img src="assets/images/service-img-1.jpg" alt="Cardiac Angioplasty Recovery Video" onerror="this.src='assets/images/about-img-1.jpg'">
                        <div class="play-btn-circle"><i data-lucide="play" style="fill:#fff;margin-left:3px"></i></div>
                    </div>
                    <div class="video-card-body">
                        <h4>"How Fast Action in Cath Lab Saved My Life"</h4>
                        <p>Mr. Jagdish Chander shares his emergency heart attack recovery under Dr. Ankur Kamra at Sukhda Cath Lab.</p>
                    </div>
                </div>

                <div class="video-card">
                    <div class="video-thumb-wrap" onclick="alert('Playing patient video testimonial...')">
                        <img src="assets/images/service-img-2.jpg" alt="Cancer Warrior Story Video" onerror="this.src='assets/images/about-img-2.jpg'">
                        <div class="play-btn-circle"><i data-lucide="play" style="fill:#fff;margin-left:3px"></i></div>
                    </div>
                    <div class="video-card-body">
                        <h4>"My Battle with Lymphoma at Sukhda MedPark"</h4>
                        <p>Cancer warrior Anita shares her chemotherapy journey, comfortable daycare suite experience, and compassionate support.</p>
                    </div>
                </div>

                <div class="video-card">
                    <div class="video-thumb-wrap" onclick="alert('Playing patient video testimonial...')">
                        <img src="assets/images/service-img-3.jpg" alt="3D Knee Replacement Testimonial Video" onerror="this.src='assets/images/facility-img-1.jpg'">
                        <div class="play-btn-circle"><i data-lucide="play" style="fill:#fff;margin-left:3px"></i></div>
                    </div>
                    <div class="video-card-body">
                        <h4>"Walking Without Pain After 10 Years"</h4>
                        <p>Mrs. Prem Lata demonstrates her knee flexibility and fast recovery following minimally invasive joint surgery.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- GOOGLE COMMUNITY REVIEWS -->
    <section class="sec-reviews">
        <div class="wrap">
            <div class="sec-header">
                <span class="kicker">Community Trust</span>
                <h2 class="sec-title">What Patients Say Across Hisar</h2>
                <p class="sec-desc">Verified feedback from patients and families who trust Sukhda Healthcare for their medical needs.</p>
            </div>

            <div class="reviews-grid">
                <div class="review-card">
                    <div class="stars">
                        <i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i>
                    </div>
                    <p>"Dr. Amit Mehta is one of the most knowledgeable and humble physicians in Haryana. His diagnosis was spot-on when other clinics were guessing. The staff is extremely polite."</p>
                    <div class="review-meta">
                        <span>Kuldeep Beniwal</span>
                        <span>Google Review &bull; Hisar</span>
                    </div>
                </div>

                <div class="review-card">
                    <div class="stars">
                        <i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i>
                    </div>
                    <p>"Dr. Manisha Mehta made my high-risk delivery seamless. The labour room and post-op nursing care were world class. We cannot thank the Sukhda maternity team enough!"</p>
                    <div class="review-meta">
                        <span>Priyanka Saini</span>
                        <span>Google Review &bull; Hansi</span>
                    </div>
                </div>

                <div class="review-card">
                    <div class="stars">
                        <i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i>
                    </div>
                    <p>"The 24/7 Cath Lab and emergency team saved my father in the middle of the night. Transparent billing, cashless insurance desk helped us get full claim without any hassle."</p>
                    <div class="review-meta">
                        <span>Amit Goyal</span>
                        <span>Google Review &bull; Sirsa</span>
                    </div>
                </div>

                <div class="review-card">
                    <div class="stars">
                        <i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i><i data-lucide="star" style="fill:#f59e0b"></i>
                    </div>
                    <p>"Sukhda MedPark is a blessing for cancer patients in Hisar. No need to travel to Delhi for chemotherapy or radiation. Clean, modern, and compassionate doctors."</p>
                    <div class="review-meta">
                        <span>Ritu Aggarwal</span>
                        <span>Google Review &bull; Fatehabad</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SHARE YOUR STORY FORM -->
    <section class="sec-share-form" id="share-story">
        <div class="wrap">
            <div class="share-box">
                <div style="text-align:center;max-width:650px;margin:0 auto">
                    <span class="kicker">We Want to Hear From You</span>
                    <h2 class="sec-title" style="margin-bottom:10px">Share Your Healing Story</h2>
                    <p class="sec-desc">Your journey can inspire, comfort, and give hope to thousands of other patients facing similar health challenges.</p>
                </div>

                <form onsubmit="event.preventDefault(); alert('Thank you for sharing your inspiring journey! Our patient relations team will review and feature your story.'); this.reset();">
                    <div class="form-grid">
                        <div class="form-group">
                            <label>Patient's Full Name *</label>
                            <input type="text" class="form-control" placeholder="e.g. Rameshwar Dass" required>
                        </div>
                        <div class="form-group">
                            <label>Phone / WhatsApp Number *</label>
                            <input type="tel" class="form-control" placeholder="e.g. +91 98765 43210" required>
                        </div>
                        <div class="form-group">
                            <label>City / Town *</label>
                            <input type="text" class="form-control" placeholder="e.g. Hisar, Hansi, Fatehabad" required>
                        </div>
                        <div class="form-group">
                            <label>Department / Treated By</label>
                            <select class="form-control">
                                <option value="">Select Speciality / Doctor</option>
                                <option value="Cardiology">Interventional Cardiology (Dr. Ankur Kamra)</option>
                                <option value="Internal Medicine">Internal Medicine (Dr. Amit Mehta)</option>
                                <option value="Gynaecology">Gynaecology &amp; Obstetrics (Dr. Manisha Mehta)</option>
                                <option value="Oncology">Oncology &amp; Cancer Care (Sukhda MedPark)</option>
                                <option value="Orthopaedics">Orthopaedics &amp; Joint Replacement</option>
                                <option value="Nephrology">Nephrology &amp; Dialysis Unit</option>
                                <option value="General Surgery">General &amp; Laparoscopic Surgery</option>
                                <option value="Emergency & ICU">Emergency Trauma &amp; ICU</option>
                            </select>
                        </div>
                        <div class="form-group form-full">
                            <label>Your Recovery Story &amp; Experience *</label>
                            <textarea class="form-control" placeholder="Please describe how you felt when you arrived at Sukhda, the care you received from our doctors and nurses, and how you are doing today..." required></textarea>
                        </div>
                        <div class="form-group form-full">
                            <label>Would you like to attach a photo or discharge note? (Optional)</label>
                            <input type="file" class="form-control" accept="image/*,.pdf">
                        </div>
                        <div class="form-group form-full" style="display:flex;align-items:center;gap:10px">
                            <input type="checkbox" id="consent" required style="width:18px;height:18px">
                            <label for="consent" style="font-size:13px;font-weight:500;color:var(--muted)">I give consent to Sukhda Healthcare to feature my healing story to inspire other patients on the website and social media.</label>
                        </div>
                    </div>
                    <div style="text-align:center;margin-top:24px">
                        <button type="submit" class="btn primary" style="padding:14px 36px;font-size:16px"><i data-lucide="send"></i> Submit My Story</button>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <!-- CALL TO ACTION BANNER -->
    <section class="sec-cta">
        <div class="wrap cta-box">
            <div>
                <h2>Need Expert Medical Care or Second Opinion?</h2>
                <p>Consult with our senior medical specialists or visit our 24/7 emergency care department in Hisar.</p>
            </div>
            <div class="cta-actions">
                <a href="doctor.html" class="btn white"><i data-lucide="users"></i> Find a Doctor</a>
                <a href="contact.html" class="btn primary"><i data-lucide="calendar-days"></i> Book Consultation</a>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    {footer_html}

    <!-- TAB FILTER SCRIPT -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const buttons = document.querySelectorAll('.tab-btn');
            const cards = document.querySelectorAll('.story-card');

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

# Replace double footer / body / html tags if necessary
# In our case footer_html contains </html> so let's adjust:
if '</html>' in footer_html:
    idx = footer_html.find('</body>')
    if idx != -1:
        clean_footer = footer_html[:idx]
    else:
        clean_footer = footer_html
else:
    clean_footer = footer_html

full_page = html_content.replace(f"<!-- FOOTER -->\n    {footer_html}", f"<!-- FOOTER -->\n    {clean_footer}")

with open('patient-stories.html', 'w', encoding='utf-8') as f:
    f.write(full_page)

print("patient-stories.html generated successfully!")
