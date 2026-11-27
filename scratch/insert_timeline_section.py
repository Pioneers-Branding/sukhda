import re

with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update timeline CSS slightly to handle icons in badges and timeline-list
css_target = """        .timeline-year-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--green-light);
            color: var(--green);
            font-weight: 800;
            font-size: 13px;
            padding: 4px 12px;
            border-radius: 20px;
            margin-bottom: 10px;
        }"""

css_replacement = """        .timeline-year-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: var(--green-light);
            color: var(--green);
            font-weight: 800;
            font-size: 13px;
            padding: 4px 12px;
            border-radius: 20px;
            margin-bottom: 10px;
        }

        .timeline-year-badge svg {
            width: 14px;
            height: 14px;
        }

        .timeline-list {
            margin: 8px 0 14px 20px;
            padding: 0;
            color: var(--muted);
            font-size: 14.5px;
            line-height: 1.65;
        }

        .timeline-list li {
            margin-bottom: 6px;
        }

        .timeline-list li:last-child {
            margin-bottom: 0;
        }

        .timeline-list strong {
            color: var(--blue);
        }"""

if css_target in content:
    content = content.replace(css_target, css_replacement, 1)
    print("Updated timeline CSS in about.html")
else:
    print("CSS target not matched directly, checking if already updated...")

# 2. Add Timeline to About Us dropdowns in about.html
nav_target = """                            <a href="about.html">About Sukhda</a>
                            <a href="about.html#leadership">Leadership</a>
                            <a href="about.html#vision">Vision &amp; Mission</a>"""

nav_replacement = """                            <a href="about.html">About Sukhda</a>
                            <a href="about.html#leadership">Leadership</a>
                            <a href="about.html#vision">Vision &amp; Mission</a>
                            <a href="about.html#timeline">Our Journey / Timeline</a>"""

if nav_target in content:
    content = content.replace(nav_target, nav_replacement)
    print("Updated About Us dropdown in about.html")
else:
    print("Nav target not matched directly")

# 3. Create the Timeline Section HTML
timeline_html = """
    <!-- SECTION: OUR JOURNEY & TIMELINE -->
    <section class="section" id="timeline" style="background:#ffffff;">
        <div class="wrap">
            <div class="kicker">TWO DECADES OF HEALTHCARE EXCELLENCE</div>
            <h2 class="title">Our Journey &amp; Milestones</h2>
            <p class="sub">From a 20-bedded clinic in 2002 to a 125-bedded NABH-accredited tertiary multispeciality hospital &amp; comprehensive cancer centre.</p>

            <div class="timeline-container">
                <!-- 2002 -->
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <div class="timeline-year-badge"><i data-lucide="calendar"></i> 2002</div>
                        <h3 class="timeline-title">2002 – The Beginning</h3>
                        <p class="timeline-text">Sukhda Hospital was established as a 20-bedded hospital with two in-house specialists in the Departments of General Medicine and Radiology, with a vision to develop a comprehensive multispecialty healthcare facility.</p>
                        <div class="timeline-tags">
                            <span class="timeline-tag">20 Beds Foundation</span>
                            <span class="timeline-tag">General Medicine</span>
                            <span class="timeline-tag">Radiology</span>
                            <span class="timeline-tag">Visionary Healthcare</span>
                        </div>
                    </div>
                </div>

                <!-- 2006 -->
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <div class="timeline-year-badge"><i data-lucide="calendar"></i> 2006</div>
                        <h3 class="timeline-title">2006 – Expansion of Clinical Services</h3>
                        <p class="timeline-text">The Departments of General &amp; Laparoscopic Surgery and Obstetrics &amp; Gynaecology were introduced with full-time specialists, increasing the hospital capacity to 45 beds.</p>
                        <div class="timeline-tags">
                            <span class="timeline-tag">45 Beds Capacity</span>
                            <span class="timeline-tag">General &amp; Laparoscopic Surgery</span>
                            <span class="timeline-tag">Obstetrics &amp; Gynaecology</span>
                            <span class="timeline-tag">Full-Time Specialists</span>
                        </div>
                    </div>
                </div>

                <!-- 2007 -->
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <div class="timeline-year-badge"><i data-lucide="calendar"></i> 2007</div>
                        <h3 class="timeline-title">2007 – Critical Care Services</h3>
                        <p class="timeline-text">The Critical Care Department was established with a 6-bedded Intensive Care Unit (ICU), and the hospital's total bed capacity was expanded to 60 beds.</p>
                        <div class="timeline-tags">
                            <span class="timeline-tag">60 Beds Total</span>
                            <span class="timeline-tag">6-Bedded ICU</span>
                            <span class="timeline-tag">Critical Care Department</span>
                            <span class="timeline-tag">24*7 Emergency Support</span>
                        </div>
                    </div>
                </div>

                <!-- 2012 -->
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <div class="timeline-year-badge"><i data-lucide="calendar"></i> 2012</div>
                        <h3 class="timeline-title">2012 – Infrastructure Expansion</h3>
                        <p class="timeline-text">Hospital infrastructure was significantly enhanced, increasing the total bed capacity to 100 beds to meet the growing healthcare needs of the region.</p>
                        <div class="timeline-tags">
                            <span class="timeline-tag">100 Beds Milestone</span>
                            <span class="timeline-tag">Advanced Infrastructure</span>
                            <span class="timeline-tag">Regional Healthcare Hub</span>
                        </div>
                    </div>
                </div>

                <!-- 2015 -->
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <div class="timeline-year-badge"><i data-lucide="calendar"></i> 2015</div>
                        <h3 class="timeline-title">2015 – New Specialties &amp; ECHS Empanelment</h3>
                        <p class="timeline-text">Sukhda Hospital received ECHS Empanelment, enabling healthcare services for Ex-Servicemen and their dependents. The Departments of Urology, Neurosurgery, and Orthopaedics were also introduced.</p>
                        <div class="timeline-tags">
                            <span class="timeline-tag">ECHS Empanelment</span>
                            <span class="timeline-tag">Urology</span>
                            <span class="timeline-tag">Neurosurgery</span>
                            <span class="timeline-tag">Orthopaedics</span>
                        </div>
                    </div>
                </div>

                <!-- 2016 -->
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <div class="timeline-year-badge"><i data-lucide="calendar"></i> 2016</div>
                        <h3 class="timeline-title">2016 – Comprehensive Multispecialty Growth</h3>
                        <p class="timeline-text">The hospital expanded its sanctioned capacity to 125 beds and added new specialties, including Dermatology, ENT, Psychiatry, further strengthening its multidisciplinary healthcare services.</p>
                        <div class="timeline-tags">
                            <span class="timeline-tag">125 Beds Sanctioned</span>
                            <span class="timeline-tag">Dermatology</span>
                            <span class="timeline-tag">ENT</span>
                            <span class="timeline-tag">Psychiatry</span>
                        </div>
                    </div>
                </div>

                <!-- 2020 -->
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <div class="timeline-year-badge" style="background:#eaf7ee;color:#1e7e34;"><i data-lucide="award"></i> 2020</div>
                        <h3 class="timeline-title">2020 – National Recognition for Quality</h3>
                        <p class="timeline-text">Sukhda Hospital achieved Full NABH Accreditation and was awarded the AB PM-JAY Gold Quality Certification, reflecting its commitment to quality healthcare, patient safety, and clinical excellence.</p>
                        <div class="timeline-tags">
                            <span class="timeline-tag" style="background:#eaf7ee;color:#1e7e34;border-color:#bce5cb;">Full NABH Accreditation</span>
                            <span class="timeline-tag" style="background:#fff8e6;color:#b26a00;border-color:#ffe299;">AB PM-JAY Gold Quality Certification</span>
                            <span class="timeline-tag">Patient Safety &amp; Clinical Excellence</span>
                        </div>
                    </div>
                </div>

                <!-- 2022 -->
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <div class="timeline-year-badge"><i data-lucide="graduation-cap"></i> 2022</div>
                        <h3 class="timeline-title">2022 – Clinical Excellence &amp; Academic Milestones</h3>
                        <p class="timeline-text">The hospital continued its growth by:</p>
                        <ul class="timeline-list">
                            <li><strong>Gastroenterology &amp; Endoscopy:</strong> Launching the Gastroenterology Department with advanced Endoscopy, ERCP, and related diagnostic services.</li>
                            <li><strong>Academic Accreditation:</strong> Got Accredited with National Board of Examinations – Medical Sciences (NBEMS) New Delhi for DNB – General Medicine with two seats.</li>
                            <li><strong>Rural Health Outreach:</strong> Partnering with the USAID Samridh &amp; Pahel Initiative to extend primary and secondary healthcare services to eight rural areas, benefiting approximately 65,000 people.</li>
                            <li><strong>Laboratory Advancement:</strong> Introducing a Hormone Analyser in the Pathology Laboratory.</li>
                            <li><strong>Orthopaedic Innovation:</strong> Launching 3D Technology Knee Resurfacing in the Department of Orthopaedics.</li>
                        </ul>
                        <div class="timeline-tags">
                            <span class="timeline-tag">Gastroenterology &amp; ERCP</span>
                            <span class="timeline-tag">DNB General Medicine</span>
                            <span class="timeline-tag">USAID Samridh &amp; Pahel</span>
                            <span class="timeline-tag">Hormone Analyser</span>
                            <span class="timeline-tag">3D Knee Resurfacing</span>
                        </div>
                    </div>
                </div>

                <!-- 2025 -->
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-content">
                        <div class="timeline-year-badge" style="background:#eef4fb;color:#0b3a75;"><i data-lucide="ribbon"></i> 2025</div>
                        <h3 class="timeline-title">2025 – Comprehensive Cancer Care</h3>
                        <p class="timeline-text">The hospital established its Medical &amp; Surgical Oncology Department and launched a fully equipped Chemotherapy Ward featuring a Bio-Safety Cabinet and advanced life-support equipment, expanding its comprehensive cancer care services.</p>
                        <div class="timeline-tags">
                            <span class="timeline-tag" style="background:#fcedf2;color:#9b1c48;border-color:#f6c4d7;">Medical &amp; Surgical Oncology</span>
                            <span class="timeline-tag">Bio-Safety Cabinet Chemotherapy</span>
                            <span class="timeline-tag">Advanced Life-Support</span>
                            <span class="timeline-tag">Comprehensive Cancer Care</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# 4. Insert after section #vision
vision_end_target = """                <div class="val-card">
                    <i data-lucide="wallet"></i>
                    <h4>Affordability for Every Patient</h4>
                    <p>Deliver world-class quality healthcare while ensuring genuine affordability, accessible health
                        schemes, and cashless TPA partnerships.</p>
                </div>
            </div>
        </div>
    </section>"""

if vision_end_target in content:
    replacement = vision_end_target + "\n" + timeline_html
    content = content.replace(vision_end_target, replacement, 1)
    print("Successfully inserted timeline section into about.html after #vision section!")
else:
    print("Could not find vision_end_target in about.html")

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Finished updating about.html")
