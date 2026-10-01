<?php
$year = date('Y');

// Doctor Directory Data
$allDoctors = [
    'dr-amit-mehta' => [
        'slug'         => 'dr-amit-mehta',
        'name'         => 'Dr. Amit Mehta',
        'photo'        => 'assets/images/doctors/dr-amit-mehta.jpg',
        'degrees'      => 'MD (Internal Medicine, AIIMS New Delhi) · MBBS',
        'role'         => 'Founder & Director — Head of Internal Medicine & Critical Care',
        'department'   => 'Internal Medicine & Critical Care',
        'experience'   => '25+ Years',
        'patients'     => '1,20,000+',
        'rating'       => '4.95',
        'reviews_count'=> '1,840+',
        'hospitals'    => 'Available at Both Locations (Multispeciality & MedPark)',
        'location_tag' => 'Both Locations',
        'languages'    => 'English, Hindi, Punjabi',
        'summary'      => 'Alumnus of AIIMS New Delhi with 25+ years of clinical excellence in complex multi-system diseases, acute critical care, diabetes reversal, and preventive adult healthcare.',
        'about'        => 'Dr. Amit Mehta is the Founder and Director of Sukhda Healthcare, heading the Department of Internal Medicine & Critical Care across both Sukhda Multispeciality Hospital and Sukhda MedPark. An esteemed alumnus of the All India Institute of Medical Sciences (AIIMS, New Delhi), Dr. Mehta headed Internal Medicine & Critical Care at Jindal Hospital for 9 years before establishing Sukhda Hospital in 2002.<br><br>Over two and a half decades, Dr. Mehta has pioneered ethical clinical governance, protocolized Level-3 intensive care management, and comprehensive multisystem diagnosis in Western Haryana. Known for his methodical diagnostic precision and compassionate patient bedside manner, he has successfully managed over 1,20,000 adult cases and emergency ICU admissions.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda Multispeciality Hospital',
                'address'  => 'Delhi Road, Model Town, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '10:00 AM – 02:00 PM',
                'type'     => 'Morning OPD & Inpatient Rounds',
                'room'     => 'OPD Chamber 101, 1st Floor'
            ],
            [
                'hospital' => 'Sukhda MedPark (Super Speciality)',
                'address'  => 'Delhi Road, Hisar (Opp. Green Belt)',
                'days'     => 'Monday to Saturday',
                'timings'  => '03:00 PM – 05:00 PM',
                'type'     => 'Evening OPD & Onco-Medical Consults',
                'room'     => 'Consultation Suite 02'
            ],
            [
                'hospital' => '24/7 Critical Care & Emergency',
                'address'  => 'Level-3 ICU / Emergency Response',
                'days'     => 'Sunday & 24×7',
                'timings'  => '24 Hours Emergency On-Call',
                'type'     => 'Emergency & ICU Triage',
                'room'     => 'Emergency Care Unit'
            ]
        ],
        'specializations' => [
            'Multisystem & Undiagnosed Clinical Disorders',
            'Type-2 Diabetes & Diabetic Complication Management',
            'Hypertension, Dyslipidemia & Cardiovascular Risk',
            'Critical Care, Sepsis & Multi-Organ Dysfunction',
            'Severe Respiratory Illnesses & ARDS Management',
            'Infectious Diseases & Tropical Pyrexia (Fevers)',
            'Geriatric Medicine & Polypharmacy Optimization',
            'Autoimmune & Rheumatological Disorders',
            'Preventive Health Checkups & Lifestyle Medicine',
            'Thyroid & Endocrine Metabolic Disorders'
        ],
        'education' => [
            [
                'degree'      => 'MD — Internal Medicine',
                'institution' => 'All India Institute of Medical Sciences (AIIMS), New Delhi',
                'year'        => '1997',
                'desc'        => 'Premier post-graduate clinical training in complex systemic diseases, intensive care, and diagnostic protocols.'
            ],
            [
                'degree'      => 'MBBS',
                'institution' => 'Premier Medical College / PGIMER Rohtak-Chandigarh Network',
                'year'        => '1993',
                'desc'        => 'Graduated with high honours and academic excellence across clinical rotatory internships.'
            ],
            [
                'degree'      => 'Senior Residency & ICU Fellowship',
                'institution' => 'Apex Healthcare & Critical Care Centres',
                'year'        => '1997 – 1999',
                'desc'        => 'Extensive hands-on training in mechanical ventilation, hemodynamic monitoring, and central line interventions.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Founder, Director & Head of Internal Medicine',
                'org'    => 'Sukhda Multispeciality Hospital & Sukhda MedPark',
                'period' => '2002 – Present',
                'desc'   => 'Leading clinical strategy, ICU protocol implementation, and daily outpatient care across both hospital campuses.'
            ],
            [
                'role'   => 'Head of Department — Internal Medicine & Critical Care',
                'org'    => 'Jindal Hospital, Hisar',
                'period' => '1993 – 2002',
                'desc'   => 'Supervised tertiary medical wards, coronary care unit, and adult emergency medicine division for 9 years.'
            ]
        ],
        'memberships' => [
            'Life Member — Association of Physicians of India (API)',
            'Member — Indian Society of Critical Care Medicine (ISCCM)',
            'Fellow — Research Society for the Study of Diabetes in India (RSSDI)',
            'Active Member — Indian Medical Association (IMA), Hisar Chapter'
        ],
        'awards' => [
            [
                'title' => 'Vikas Ratan Gold Award',
                'body'  => 'Conferred for exemplary medical leadership, critical care excellence, and social healthcare contribution across Haryana.'
            ],
            [
                'title' => 'Healthcare Pioneer in Adult Medicine',
                'body'  => 'Recognized for establishing Hisar’s first multi-disciplinary Level-3 critical care and multi-system medical protocol.'
            ],
            [
                'title' => 'NABH Quality Champion',
                'body'  => 'Honoured for institutional commitment towards zero-infection protocols and evidence-based patient safety standards.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Rameshwar Sharma',
                'place'   => 'Hisar, Haryana',
                'service' => 'Severe Sepsis & Multi-System Illness',
                'quote'   => 'My father had severe chest infection with sudden kidney complications. Dr. Amit Mehta diagnosed the root issue immediately and his ICU care brought my father back to health safely. We are eternally grateful to Dr. Mehta and Sukhda Hospital.'
            ],
            [
                'name'    => 'Sunita Chawla',
                'place'   => 'Fatehabad',
                'service' => 'Diabetes & Hypertension Clinic',
                'quote'   => 'I was struggling with uncontrolled HbA1c and fluctuating blood pressure for 7 years. Dr. Amit Mehta streamlined my medications, prescribed the right diet plan, and today my sugar is completely in control without side effects.'
            ],
            [
                'name'    => 'Vikas Bishnoi',
                'place'   => 'Sirsa',
                'service' => 'Pyrexia of Unknown Origin',
                'quote'   => 'After visiting three hospitals for 3 weeks of unexplained high fever, Dr. Amit Mehta identified the exact tropical infection within 24 hours of admission. Within 4 days, I was completely discharged and healthy.'
            ]
        ]
    ],
    'dr-nidhi-mehta' => [
        'slug'         => 'dr-nidhi-mehta',
        'name'         => 'Dr. Nidhi Mehta',
        'photo'        => 'assets/images/doctors/dr-nidhi-mehta.jpg',
        'degrees'      => 'M.B.B.S, D.G.O, D.N.B (Obstetrics & Gynaecology)',
        'role'         => 'Senior Consultant — Obstetrics, Gynaecology & Laparoscopic Surgery',
        'department'   => 'Gynaecology & Obstetrics',
        'experience'   => '22+ Years',
        'patients'     => '45,000+',
        'rating'       => '4.94',
        'reviews_count'=> '1,120+',
        'hospitals'    => 'Sukhda Multispeciality Hospital',
        'location_tag' => 'Multispeciality',
        'languages'    => 'English, Hindi',
        'summary'      => 'Renowned Senior Obstetrician & Gynaecological Laparoscopic Surgeon specializing in painless deliveries, high-risk pregnancies, fibroid removal, and fertility management.',
        'about'        => 'Dr. Nidhi Mehta is a distinguished Obstetrician and Gynaecologist with over two decades of clinical experience in women’s reproductive health. She leads the Department of Gynaecology & Maternity at Sukhda Multispeciality Hospital, having delivered thousands of safe and happy childbirths.<br><br>Her expertise spans normal and painless deliveries (LDR), complex high-risk obstetric cases, minimally invasive laparoscopic myomectomies, Total Laparoscopic Hysterectomies (TLH), PCOD management, and fertility interventions.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda Multispeciality Hospital',
                'address'  => 'Delhi Road, Model Town, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '10:30 AM – 02:30 PM & 05:00 PM – 07:00 PM',
                'type'     => 'OPD & Antenatal Consultations',
                'room'     => 'Gynae Suite 104, 1st Floor'
            ]
        ],
        'specializations' => [
            'Normal & Painless Childbirth (Epidural LDR)',
            'High-Risk Pregnancy (Preeclampsia, Gestational Diabetes)',
            'Laparoscopic Hysterectomy & Myomectomy',
            'Ovarian Cystectomy & Endometriosis Surgeries',
            'PCOS & Adolescent Hormone Health',
            'Infertility Workup & IUI Procedures'
        ],
        'education' => [
            [
                'degree'      => 'DNB (Obstetrics & Gynaecology)',
                'institution' => 'National Board of Examinations (NBE), New Delhi',
                'year'        => '2004',
                'desc'        => 'Advanced clinical accreditation in maternal-fetal medicine and operative gynaecology.'
            ],
            [
                'degree'      => 'DGO & MBBS',
                'institution' => 'Premier Medical Institution',
                'year'        => '1998',
                'desc'        => 'Graduated with distinction in surgical obstetrics and maternal care.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Senior Consultant Gynaecologist',
                'org'    => 'Sukhda Multispeciality Hospital',
                'period' => '2003 – Present',
                'desc'   => 'Spearheading women’s health, high-risk deliveries, and advanced keyhole laparoscopic surgery.'
            ]
        ],
        'memberships' => [
            'Federation of Obstetric and Gynaecological Societies of India (FOGSI)',
            'Indian Menopause Society (IMS)',
            'Indian Medical Association (IMA)'
        ],
        'awards' => [
            [
                'title' => 'Excellence in Women’s Health Award',
                'body'  => 'Recognized for pioneering compassionate, patient-first maternal care and high-risk pregnancy management.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Pooja Agarwal',
                'place'   => 'Hisar',
                'service' => 'Normal Painless Delivery',
                'quote'   => 'Dr. Nidhi Mehta made my first delivery completely fearless and comfortable. Her guidance throughout the 9 months gave us immense confidence.'
            ]
        ]
    ],
    'dr-ankur-kamra' => [
        'slug'         => 'dr-ankur-kamra',
        'name'         => 'Dr. Ankur Kamra',
        'photo'        => 'assets/images/doctors/dr-ankur-kamra.jpg',
        'degrees'      => 'DM (Cardiology), MD (Medicine), MBBS',
        'role'         => 'Senior Consultant — Interventional Cardiology',
        'department'   => 'Interventional Cardiology',
        'experience'   => '15+ Years',
        'patients'     => '30,000+',
        'rating'       => '4.96',
        'reviews_count'=> '980+',
        'hospitals'    => 'Sukhda Multispeciality Hospital',
        'location_tag' => 'Multispeciality',
        'languages'    => 'English, Hindi, Punjabi',
        'summary'      => 'Experienced Interventional Cardiologist specializing in primary coronary angioplasty, complex stenting, pacemaker implantation, and heart failure management.',
        'about'        => 'Dr. Ankur Kamra is a senior interventional cardiologist at Sukhda Multispeciality Hospital with advanced fellowship training in coronary angiographies, complex angioplasties, and cardiac device implantations.<br><br>He has performed thousands of emergency cardiac interventions with exceptional success rates, supported by Sukhda’s 24/7 dedicated Cath Lab and Coronary Intensive Care Unit.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda Multispeciality Hospital',
                'address'  => 'Delhi Road, Model Town, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '11:00 AM – 03:00 PM',
                'type'     => 'Cardiac OPD & Echo Clinics',
                'room'     => 'Cath Lab & Cardiac Clinic'
            ]
        ],
        'specializations' => [
            'Coronary Angiography & Radial Angioplasty (PTCA)',
            'Primary Angioplasty in Acute Myocardial Infarction',
            'Permanent Pacemaker & ICD Implantation',
            'Heart Failure & Cardiomyopathy Management',
            'Echocardiography, TMT & Holter Monitoring',
            'Preventive Cardiovascular Risk Profiling'
        ],
        'education' => [
            [
                'degree'      => 'DM — Cardiology',
                'institution' => 'Premier Apex Institute of Cardiology',
                'year'        => '2012',
                'desc'        => 'Specialized super-speciality training in catheterization interventions.'
            ],
            [
                'degree'      => 'MD (Medicine) & MBBS',
                'institution' => 'Top Medical University',
                'year'        => '2008',
                'desc'        => 'Graduated with academic distinctions in internal medicine.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Senior Consultant Cardiologist',
                'org'    => 'Sukhda Multispeciality Hospital',
                'period' => '2016 – Present',
                'desc'   => 'Leading the 24/7 primary angioplasty programme and cardiac intensive care unit.'
            ]
        ],
        'memberships' => [
            'Cardiological Society of India (CSI)',
            'Indian Medical Association (IMA)'
        ],
        'awards' => [
            [
                'title' => 'Best Interventional Cardiologist (Regional)',
                'body'  => 'Honoured for rapid door-to-balloon times in emergency acute heart attack interventions.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Harish Kumar',
                'place'   => 'Hisar',
                'service' => 'Emergency Radial Angioplasty',
                'quote'   => 'Dr. Ankur Kamra performed my emergency stent within 40 minutes of reaching the hospital. His team saved my life!'
            ]
        ]
    ],
    'dr-trivikrama-rao' => [
        'slug'         => 'dr-trivikrama-rao',
        'name'         => 'Dr. Trivikrama Rao',
        'photo'        => 'assets/images/doctors/dr-trivikrama-rao.jpg',
        'degrees'      => 'DrNB (Medical Oncology), MD (Medicine), MBBS',
        'role'         => 'Lead Consultant & Head — Medical Oncology',
        'department'   => 'Medical Oncology (Cancer Care)',
        'experience'   => '16+ Years',
        'patients'     => '22,000+',
        'rating'       => '4.98',
        'reviews_count'=> '860+',
        'hospitals'    => 'Sukhda MedPark (Cancer & Super Speciality Hospital)',
        'location_tag' => 'MedPark',
        'languages'    => 'English, Hindi, Telugu',
        'summary'      => 'Renowned Medical Oncologist specializing in precision chemotherapy, targeted therapy, immunotherapy, and multidisciplinary solid tumour management.',
        'about'        => 'Dr. Trivikrama Rao heads the Department of Medical Oncology at Sukhda MedPark. He brings extensive expertise in managing solid malignancies and haematological cancers with evidence-based chemotherapy, immunotherapy, and biologic protocols.<br><br>Under his leadership, Sukhda MedPark runs weekly Tumour Board meetings and a dedicated modern daycare chemotherapy lounge ensuring zero-delay, compassionate oncological support.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda MedPark (Cancer Hospital)',
                'address'  => 'Delhi Road, Hisar (Opp. Green Belt)',
                'days'     => 'Monday to Saturday',
                'timings'  => '10:00 AM – 04:00 PM',
                'type'     => 'Cancer OPD & Daycare Chemo Rounds',
                'room'     => 'Oncology Suite 01'
            ]
        ],
        'specializations' => [
            'Systemic & Daycare Chemotherapy',
            'Targeted Therapy & Precision Oncology',
            'Immunotherapy & Biological Cancer Therapies',
            'Breast, Lung, GI & Gynaecological Cancers',
            'Lymphomas, Leukemias & Multiple Myeloma',
            'Multidisciplinary Tumour Board Planning'
        ],
        'education' => [
            [
                'degree'      => 'DrNB — Medical Oncology',
                'institution' => 'Premier National Apex Cancer Institute',
                'year'        => '2014',
                'desc'        => 'Super-speciality doctorate in systemic cancer therapeutics and clinical trials.'
            ],
            [
                'degree'      => 'MD (Internal Medicine) & MBBS',
                'institution' => 'Top Medical University',
                'year'        => '2010',
                'desc'        => 'Post-graduate distinction in systemic diagnosis and clinical care.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Lead Medical Oncologist',
                'org'    => 'Sukhda MedPark Hospital',
                'period' => '2018 – Present',
                'desc'   => 'Heading comprehensive medical oncology and daycare chemotherapy operations.'
            ]
        ],
        'memberships' => [
            'Indian Society of Medical and Paediatric Oncology (ISMPO)',
            'European Society for Medical Oncology (ESMO)',
            'American Society of Clinical Oncology (ASCO)'
        ],
        'awards' => [
            [
                'title' => 'Excellence in Oncology Care',
                'body'  => 'Awarded for delivering protocolized, affordable cancer care and patient-centric chemotherapy protocols in Western Haryana.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Baljeet Singh',
                'place'   => 'Sirsa',
                'service' => 'Daycare Chemotherapy',
                'quote'   => 'Dr. Trivikrama Rao gave us hope when my wife was diagnosed with stage-3 breast cancer. His gentle demeanor and precise treatment plan helped her recover fully.'
            ]
        ]
    ],
    'dr-amit-kumar-garg' => [
        'slug'         => 'dr-amit-kumar-garg',
        'name'         => 'Dr. Amit Kumar Garg',
        'photo'        => 'assets/images/doctors/dr-amit-kumar-garg.jpg',
        'degrees'      => 'M.S. (Surgery), M.Ch / DNB (Surgical Oncology), MBBS',
        'role'         => 'Senior Consultant — Surgical Oncology',
        'department'   => 'Surgical Oncology',
        'experience'   => '14+ Years',
        'patients'     => '18,000+',
        'rating'       => '4.93',
        'reviews_count'=> '740+',
        'hospitals'    => 'Sukhda MedPark (Cancer & Super Speciality Hospital)',
        'location_tag' => 'MedPark',
        'languages'    => 'English, Hindi',
        'summary'      => 'Expert Surgical Oncologist specializing in organ-preserving cancer resections, gastrointestinal cancer surgeries, breast oncoplasty, and head & neck oncosurgery.',
        'about'        => 'Dr. Amit Kumar Garg is a senior surgical oncologist at Sukhda MedPark with advanced fellowship training in complex oncological resections. He specializes in radical cancer surgeries, minimally invasive thoraco-laparoscopic cancer operations, and reconstructive oncosurgery.<br><br>He has performed hundreds of complex tumor resections supported by Sukhda’s ultra-clean modular operation theatres and multi-bed surgical ICUs.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda MedPark (Cancer Hospital)',
                'address'  => 'Delhi Road, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '11:00 AM – 03:00 PM',
                'type'     => 'Surgical Onco OPD & OT Consults',
                'room'     => 'Surgical Suite 03'
            ]
        ],
        'specializations' => [
            'Breast Cancer Surgery & Sentinel Node Biopsy',
            'Gastrointestinal (GI) & Colorectal Oncosurgery',
            'Head & Neck Tumor Resection & Reconstruction',
            'Gynaecological Malignancy Surgeries',
            'Thoracic & Esophageal Cancer Excision',
            'Skin & Soft Tissue Sarcoma Resection'
        ],
        'education' => [
            [
                'degree'      => 'DNB / M.Ch — Surgical Oncology',
                'institution' => 'Apex Cancer Centre & Research Institute',
                'year'        => '2015',
                'desc'        => 'Specialized surgical fellowship in advanced oncological procedures.'
            ],
            [
                'degree'      => 'M.S. (General Surgery) & MBBS',
                'institution' => 'Premier Medical College',
                'year'        => '2011',
                'desc'        => 'Honours in operative surgery and clinical trauma management.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Senior Consultant Surgical Oncologist',
                'org'    => 'Sukhda MedPark Hospital',
                'period' => '2019 – Present',
                'desc'   => 'Spearheading operative cancer surgeries and onco-reconstructive procedures.'
            ]
        ],
        'memberships' => [
            'Indian Association of Surgical Oncology (IASO)',
            'Association of Surgeons of India (ASI)'
        ],
        'awards' => [
            [
                'title' => 'Distinguished Cancer Surgeon',
                'body'  => 'Recognized for high success rates and organ-sparing surgical oncology interventions.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Geeta Rani',
                'place'   => 'Jind, Haryana',
                'service' => 'Oncological Excision',
                'quote'   => 'Dr. Amit Kumar Garg performed my tumor removal surgery with great care and precision. I am completely tumor-free today!'
            ]
        ]
    ],
    'dr-arun-dua' => [
        'slug'         => 'dr-arun-dua',
        'name'         => 'Dr. Arun Dua',
        'photo'        => 'assets/images/doctors/dr-arun-dua.jpg',
        'degrees'      => 'DrNB (Nephrology), MD (Medicine), MBBS',
        'role'         => 'Senior Consultant & Head — Nephrology & Dialysis',
        'department'   => 'Nephrology & Dialysis',
        'experience'   => '17+ Years',
        'patients'     => '35,000+',
        'rating'       => '4.95',
        'reviews_count'=> '890+',
        'hospitals'    => 'Sukhda Multispeciality Hospital',
        'location_tag' => 'Multispeciality',
        'languages'    => 'English, Hindi, Punjabi',
        'summary'      => 'Senior Nephrologist with vast clinical acumen in acute kidney injury, chronic kidney disease (CKD), hemodialysis management, and renal hypertension.',
        'about'        => 'Dr. Arun Dua leads the Department of Nephrology and Dialysis at Sukhda Multispeciality Hospital. He brings over 17 years of clinical experience in preserving kidney function and managing complex renal disorders.<br><br>He supervises Sukhda’s 7-bed high-flux dialysis unit, ensuring strict infection control, biocompatible dialyzers, and continuous nephrology oversight.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda Multispeciality Hospital',
                'address'  => 'Delhi Road, Model Town, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '10:00 AM – 02:00 PM',
                'type'     => 'Nephrology OPD & Dialysis Unit Rounds',
                'room'     => 'Room 105, 1st Floor'
            ]
        ],
        'specializations' => [
            'Chronic Kidney Disease (CKD) Management',
            'Acute Kidney Injury & ICU Renal Support',
            'Hemodialysis & Volumetric Hemodiafiltration',
            'Diabetic Nephropathy & Renal Hypertension',
            'Glomerulonephritis & Nephrotic Syndrome',
            'Kidney Transplant Pre & Post Evaluation'
        ],
        'education' => [
            [
                'degree'      => 'DrNB — Nephrology',
                'institution' => 'Premier Institute of Kidney Diseases',
                'year'        => '2012',
                'desc'        => 'Super-speciality doctorate in advanced nephrology and dialysis management.'
            ],
            [
                'degree'      => 'MD (Internal Medicine) & MBBS',
                'institution' => 'Top Medical University',
                'year'        => '2007',
                'desc'        => 'Graduated with academic honours in adult medicine.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Head of Nephrology & Dialysis',
                'org'    => 'Sukhda Multispeciality Hospital',
                'period' => '2015 – Present',
                'desc'   => 'Leading clinical nephrology, acute dialysis, and renal failure management.'
            ]
        ],
        'memberships' => [
            'Indian Society of Nephrology (ISN)',
            'International Society of Nephrology (ISN Global)'
        ],
        'awards' => [
            [
                'title' => 'Excellence in Renal Care',
                'body'  => 'Recognized for establishing high-quality, infection-free dialysis services in Hisar.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Karamjit Singh',
                'place'   => 'Hisar',
                'service' => 'Renal Dialysis Care',
                'quote'   => 'Dr. Arun Dua has been managing my kidney treatment for 4 years. His advice and the caring dialysis staff make every session smooth.'
            ]
        ]
    ],
    'dr-bharath' => [
        'slug'         => 'dr-bharath',
        'name'         => 'Dr. Bharath',
        'photo'        => 'assets/images/doctors/dr-bharath.jpg',
        'degrees'      => 'DM (Gastroenterology), MD (Medicine), MBBS',
        'role'         => 'Senior Consultant — Gastroenterology & Hepatology',
        'department'   => 'Gastroenterology & Hepatology',
        'experience'   => '13+ Years',
        'patients'     => '24,000+',
        'rating'       => '4.92',
        'reviews_count'=> '680+',
        'hospitals'    => 'Sukhda MedPark (Super Speciality)',
        'location_tag' => 'MedPark',
        'languages'    => 'English, Hindi, Kannada',
        'summary'      => 'Experienced Gastroenterologist specializing in diagnostic and therapeutic GI endoscopy, colonoscopy, ERCP, liver cirrhosis, pancreatitis, and IBD.',
        'about'        => 'Dr. Bharath is a senior gastroenterologist and hepatologist at Sukhda MedPark. He specializes in advanced therapeutic endoscopic procedures, GI bleeding management, liver care, and digestive tract disorders.<br><br>He operates modern HD endoscopy suites with advanced fluoroscopy for bile duct stone extraction, ERCP stenting, and polypectomies.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda MedPark (Super Speciality)',
                'address'  => 'Delhi Road, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '11:00 AM – 03:00 PM',
                'type'     => 'Gastro OPD & Endoscopy Procedures',
                'room'     => 'Endoscopy Suite 02'
            ]
        ],
        'specializations' => [
            'Upper GI Endoscopy & Colonoscopy',
            'ERCP & Biliary Stenting',
            'Liver Cirrhosis, Hepatitis & Fatty Liver',
            'Pancreatitis & Gallbladder Stone Complications',
            'Inflammatory Bowel Disease (Ulcerative Colitis & Crohn’s)',
            'GERD, Acid Peptic Disease & Dyspepsia'
        ],
        'education' => [
            [
                'degree'      => 'DM — Gastroenterology',
                'institution' => 'Premier Institute of Digestive Diseases',
                'year'        => '2015',
                'desc'        => 'Super-speciality doctorate in advanced endoscopy and luminal gastroenterology.'
            ],
            [
                'degree'      => 'MD (Medicine) & MBBS',
                'institution' => 'Top Medical University',
                'year'        => '2011',
                'desc'        => 'Distinction in internal medicine and gastroenterology rotations.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Senior Consultant Gastroenterologist',
                'org'    => 'Sukhda MedPark',
                'period' => '2019 – Present',
                'desc'   => 'Leading therapeutic GI endoscopy, ERCP, and comprehensive hepatology clinics.'
            ]
        ],
        'memberships' => [
            'Indian Society of Gastroenterology (ISG)',
            'Society of Gastrointestinal Endoscopy of India (SGEI)'
        ],
        'awards' => [
            [
                'title' => 'Pioneer in Therapeutic Endoscopy',
                'body'  => 'Honoured for emergency GI bleed management and painless colonoscopy services.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Mohammed Rafiq',
                'place'   => 'Sirsa',
                'service' => 'Therapeutic ERCP',
                'quote'   => 'Dr. Bharath removed my bile duct stone via endoscopy without any open surgery. I was discharged in 2 days pain-free!'
            ]
        ]
    ],
    'dr-deepam-das' => [
        'slug'         => 'dr-deepam-das',
        'name'         => 'Dr. Deepam Das',
        'photo'        => 'assets/images/doctors/dr-deepam-das.jpg',
        'degrees'      => 'M.S. (General Surgery), FIAGES (Laparoscopic Surgery), MBBS',
        'role'         => 'Consultant — Advanced Laparoscopy & General Surgery',
        'department'   => 'Laparoscopic Surgery',
        'experience'   => '12+ Years',
        'patients'     => '20,000+',
        'rating'       => '4.91',
        'reviews_count'=> '610+',
        'hospitals'    => 'Sukhda Multispeciality Hospital',
        'location_tag' => 'Multispeciality',
        'languages'    => 'English, Hindi, Bengali',
        'summary'      => 'Accomplished keyhole laparoscopic surgeon specializing in gallbladder stones, complex hernia repair (TEP/TAPP), laparoscopic appendectomy, and surgical trauma.',
        'about'        => 'Dr. Deepam Das is a skilled consultant laparoscopic and general surgeon at Sukhda Multispeciality Hospital. He brings over a decade of experience in minimally invasive keyhole operations resulting in faster patient recovery and minimal scars.<br><br>He has performed over 3,500 successful laparoscopic surgeries including advanced hernia repairs, gallbladder removals, and emergency surgical interventions.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda Multispeciality Hospital',
                'address'  => 'Delhi Road, Model Town, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '10:00 AM – 02:00 PM',
                'type'     => 'Surgical OPD & Daycare Procedures',
                'room'     => 'Room 108, 1st Floor'
            ]
        ],
        'specializations' => [
            'Laparoscopic Cholecystectomy (Gallbladder Stones)',
            'Laparoscopic Inguinal & Ventral Hernia Repair (TEP/TAPP)',
            'Laparoscopic Appendectomy & Diagnostic Laparoscopy',
            'Laser Proctology (Piles, Fistula & Fissure)',
            'Emergency Abdominal Trauma Surgeries',
            'Thyroid & Soft Tissue Excision Surgeries'
        ],
        'education' => [
            [
                'degree'      => 'M.S. — General Surgery',
                'institution' => 'Premier Medical College',
                'year'        => '2013',
                'desc'        => 'Post-graduate specialization in operative surgery and trauma care.'
            ],
            [
                'degree'      => 'FIAGES Fellowship & MBBS',
                'institution' => 'Indian Association of Gastrointestinal Endo Surgeons',
                'year'        => '2016',
                'desc'        => 'Advanced fellowship training in minimal access laparoscopic surgery.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Consultant Laparoscopic Surgeon',
                'org'    => 'Sukhda Multispeciality Hospital',
                'period' => '2017 – Present',
                'desc'   => 'Performing routine and emergency laparoscopic keyhole surgeries.'
            ]
        ],
        'memberships' => [
            'Association of Surgeons of India (ASI)',
            'Indian Association of Gastrointestinal Endo Surgeons (IAGES)'
        ],
        'awards' => [
            [
                'title' => 'Excellence in Minimal Access Surgery',
                'body'  => 'Honoured for rapid recovery protocols in daycare laparoscopic procedures.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Naveen Goyal',
                'place'   => 'Hisar',
                'service' => 'Laparoscopic Hernia Surgery',
                'quote'   => 'Dr. Deepam Das explained the keyhole procedure clearly. I was walking the same evening and resumed work in 4 days.'
            ]
        ]
    ],
    'dr-pankaj-sharma' => [
        'slug'         => 'dr-pankaj-sharma',
        'name'         => 'Dr. Pankaj Sharma',
        'photo'        => 'assets/images/doctors/dr-pankaj-sharma.jpg',
        'degrees'      => 'M.S. (Orthopaedics), Fellow in Joint Replacement & Arthroscopy, MBBS',
        'role'         => 'Senior Consultant — Orthopaedics & Joint Replacement',
        'department'   => 'Orthopaedics & Joint Replacement',
        'experience'   => '16+ Years',
        'patients'     => '32,000+',
        'rating'       => '4.96',
        'reviews_count'=> '1,040+',
        'hospitals'    => 'Sukhda Multispeciality Hospital',
        'location_tag' => 'Multispeciality',
        'languages'    => 'English, Hindi',
        'summary'      => 'Premier Orthopaedic Surgeon specializing in Total Knee Replacement (TKR), Total Hip Replacement (THR), arthroscopic ACL reconstruction, and complex trauma surgery.',
        'about'        => 'Dr. Pankaj Sharma leads the Orthopaedics & Joint Replacement wing at Sukhda Multispeciality Hospital. He brings 16+ years of clinical expertise in joint reconstruction, sports injuries, and complex fracture management.<br><br>Equipped with laminar-flow sterile operation theatres, Dr. Sharma uses advanced implant alignment systems to ensure long-lasting joint mobility and painless rehabilitation.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda Multispeciality Hospital',
                'address'  => 'Delhi Road, Model Town, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '10:30 AM – 02:30 PM',
                'type'     => 'Ortho & Joint Clinic OPD',
                'room'     => 'Room 102, Ground Floor'
            ]
        ],
        'specializations' => [
            'Total Knee Replacement (TKR) & Revision Knee Surgeries',
            'Total Hip Replacement (THR) & Hemiarthroplasty',
            'Arthroscopic ACL / PCL Ligament Reconstruction',
            'Complex Pelvic-Acetabular & Polytrauma Fractures',
            'Spine Disc Decompression & Sciatica Care',
            'Osteoarthritis, Osteoporosis & Rheumatoid Arthritis Care'
        ],
        'education' => [
            [
                'degree'      => 'M.S. — Orthopaedics',
                'institution' => 'Premier Apex Orthopaedic Institute',
                'year'        => '2010',
                'desc'        => 'Advanced post-graduate clinical training in trauma, joint replacements, and bone pathology.'
            ],
            [
                'degree'      => 'Fellowship in Arthroscopy & Joint Replacement',
                'institution' => 'Apex Joint Care Foundation',
                'year'        => '2012',
                'desc'        => 'Hands-on fellowship in primary and revision knee-hip arthroplasty.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Senior Consultant Orthopaedic Surgeon',
                'org'    => 'Sukhda Multispeciality Hospital',
                'period' => '2015 – Present',
                'desc'   => 'Leading the joint replacement centre and 24/7 polytrauma orthopaedic team.'
            ]
        ],
        'memberships' => [
            'Indian Orthopaedic Association (IOA)',
            'Indian Arthroscopy Society (IAS)',
            'Haryana Orthopaedic Association (HOA)'
        ],
        'awards' => [
            [
                'title' => 'Best Joint Replacement Surgeon',
                'body'  => 'Conferred for performing over 2,000 successful knee and hip replacements with excellent mobility outcomes.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Vikas Kumar',
                'place'   => 'Fatehabad',
                'service' => 'Total Knee Replacement',
                'quote'   => 'Knee replacement done by Dr. Pankaj Sharma in March. I was walking pain-free within 4 weeks. He gave me back my active mornings.'
            ]
        ]
    ],
    'dr-joginder-silayach' => [
        'slug'         => 'dr-joginder-silayach',
        'name'         => 'Dr. Joginder Silayach',
        'photo'        => 'assets/images/doctors/dr-joginder-silayach.jpg',
        'degrees'      => 'M.D. (Paediatrics & Neonatology), MBBS',
        'role'         => 'Senior Consultant — Paediatrics & Level-3 NICU',
        'department'   => 'Paediatrics & Neonatology',
        'experience'   => '18+ Years',
        'patients'     => '40,000+',
        'rating'       => '4.97',
        'reviews_count'=> '1,250+',
        'hospitals'    => 'Sukhda Multispeciality Hospital',
        'location_tag' => 'Multispeciality',
        'languages'    => 'English, Hindi, Haryanvi',
        'summary'      => 'Leading Paediatrician and Neonatologist leading Sukhda’s 24/7 Level-3 NICU, managing premature infant resuscitation, childhood respiratory illnesses, and immunizations.',
        'about'        => 'Dr. Joginder Silayach is a senior paediatrician and neonatologist at Sukhda Multispeciality Hospital. He brings 18+ years of dedicated experience caring for newborns, infants, children, and adolescents.<br><br>He heads the state-of-the-art Level-3 Neonatal Intensive Care Unit (NICU), saving hundreds of premature, low-birth-weight babies with modern phototherapy, CPAP, and high-frequency ventilation.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda Multispeciality Hospital',
                'address'  => 'Delhi Road, Model Town, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '10:00 AM – 02:00 PM & 05:00 PM – 07:00 PM',
                'type'     => 'Paediatric OPD & Vaccination Clinic',
                'room'     => 'Paediatric Clinic 106'
            ]
        ],
        'specializations' => [
            'Level-3 Neonatal ICU (NICU) & Premature Baby Care',
            'Childhood Asthma & Severe Respiratory Infections',
            'Pediatric Growth, Nutrition & Developmental Monitoring',
            'Universal Vaccination & Immunization Schedules',
            'Neonatal Jaundice & Phototherapy Protocols',
            'Pediatric Infectious Illnesses & Tropical Fevers'
        ],
        'education' => [
            [
                'degree'      => 'M.D. — Paediatrics & Neonatology',
                'institution' => 'Premier Apex Paediatric Institute',
                'year'        => '2008',
                'desc'        => 'Specialized doctorate in neonatology, pediatric critical care, and developmental genetics.'
            ],
            [
                'degree'      => 'MBBS',
                'institution' => 'Top Medical University',
                'year'        => '2004',
                'desc'        => 'Graduated with distinctions in pediatrics and social medicine.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Head of Paediatrics & NICU',
                'org'    => 'Sukhda Multispeciality Hospital',
                'period' => '2012 – Present',
                'desc'   => 'Managing pediatric OPD, 24/7 neonatal intensive care, and child health clinics.'
            ]
        ],
        'memberships' => [
            'Indian Academy of Pediatrics (IAP)',
            'National Neonatology Forum (NNF)',
            'Indian Medical Association (IMA)'
        ],
        'awards' => [
            [
                'title' => 'Excellence in Neonatal Care Award',
                'body'  => 'Recognized for highest survival rates in critically ill and extremely low birth weight neonates in Hisar.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Sunita Devi',
                'place'   => 'Hansi',
                'service' => 'Level-3 NICU Care',
                'quote'   => 'My granddaughter was born premature at 29 weeks. Dr. Joginder Silayach and the NICU staff treated her like their own child. Today she is completely healthy!'
            ]
        ]
    ],
    'dr-devilal' => [
        'slug'         => 'dr-devilal',
        'name'         => 'Dr. Devilal',
        'photo'        => 'assets/images/doctors/dr-devilal.jpg',
        'degrees'      => 'D.A. (Anaesthesiology & Critical Care), MBBS',
        'role'         => 'Consultant — Anaesthesia & Emergency Critical Care',
        'department'   => 'Anaesthesia & Critical Care',
        'experience'   => '15+ Years',
        'patients'     => '25,000+',
        'rating'       => '4.90',
        'reviews_count'=> '520+',
        'hospitals'    => 'Sukhda Multispeciality Hospital',
        'location_tag' => 'Multispeciality',
        'languages'    => 'English, Hindi',
        'summary'      => 'Critical Care & Anaesthesia specialist managing multi-bed surgical ICUs, advanced mechanical ventilation, invasive monitoring, and trauma resuscitation.',
        'about'        => 'Dr. Devilal is a consultant anaesthesiologist and intensivist at Sukhda Multispeciality Hospital. He brings 15+ years of clinical acumen in surgical peri-operative care, trauma resuscitation, and multi-organ intensive care management.<br><br>He oversees surgical anaesthetic safety for high-risk cardiac, neuro, and onco-surgeries in Sukhda’s modular operation theatres.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda Multispeciality Hospital',
                'address'  => 'Delhi Road, Model Town, Hisar',
                'days'     => 'Monday to Saturday (24/7 On-Call)',
                'timings'  => '09:00 AM – 01:00 PM (PAC & ICU)',
                'type'     => 'Pre-Anaesthesia Checkup (PAC) & ICU',
                'room'     => 'PAC Clinic & Level-3 ICU'
            ]
        ],
        'specializations' => [
            'General, Spinal & Epidural Anaesthesia',
            'Level-3 Multi-bed ICU & Mechanical Ventilation',
            'Pre-Anaesthetic Fitness Assessment (PAC)',
            'Emergency Airway & Central Line Interventions',
            'Sepsis, ARDS & Trauma Resuscitation',
            'Post-Operative Hemodynamic Monitoring'
        ],
        'education' => [
            [
                'degree'      => 'D.A. — Anaesthesiology',
                'institution' => 'Premier Medical College',
                'year'        => '2010',
                'desc'        => 'Post-graduate diploma in surgical anaesthesia and intensive care.'
            ],
            [
                'degree'      => 'MBBS',
                'institution' => 'Medical University Network',
                'year'        => '2006',
                'desc'        => 'Graduated with high honours across clinical rotations.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Consultant Anaesthesiologist & Intensivist',
                'org'    => 'Sukhda Multispeciality Hospital',
                'period' => '2014 – Present',
                'desc'   => 'Managing OT surgical anaesthesia and ICU resuscitation protocols.'
            ]
        ],
        'memberships' => [
            'Indian Society of Anaesthesiologists (ISA)',
            'Indian Society of Critical Care Medicine (ISCCM)'
        ],
        'awards' => [
            [
                'title' => 'Clinical Safety Champion',
                'body'  => 'Recognized for achieving exemplary safety standards in high-risk geriatric and pediatric surgical anaesthesia.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Surender Malik',
                'place'   => 'Hisar',
                'service' => 'ICU & Surgical Anaesthesia',
                'quote'   => 'Dr. Devilal managed my father’s anaesthesia and critical care during a major emergency abdominal surgery with utmost confidence and success.'
            ]
        ]
    ],
    'dr-parveen' => [
        'slug'         => 'dr-parveen',
        'name'         => 'Dr. Parveen',
        'photo'        => 'assets/images/doctors/dr-parveen.jpg',
        'degrees'      => 'D.N.B. (Anesthesiology), MBBS',
        'role'         => 'Consultant — Anaesthesiology & Pain Management',
        'department'   => 'Anaesthesiology & Pain Care',
        'experience'   => '11+ Years',
        'patients'     => '18,000+',
        'rating'       => '4.89',
        'reviews_count'=> '430+',
        'hospitals'    => 'Sukhda Multispeciality Hospital',
        'location_tag' => 'Multispeciality',
        'languages'    => 'English, Hindi',
        'summary'      => 'Expert in general, neuro and regional anaesthesia, painless epidural labor analgesia, post-operative multimodal pain relief, and acute critical care.',
        'about'        => 'Dr. Parveen is a consultant anaesthesiologist and pain management specialist at Sukhda Multispeciality Hospital. He brings 11+ years of expertise in nerve block techniques, acute pain relief, and painless delivery analgesia.<br><br>He coordinates pain-free surgical recovery protocols across ortho, gynae, and general surgical procedures.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda Multispeciality Hospital',
                'address'  => 'Delhi Road, Model Town, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '11:00 AM – 03:00 PM',
                'type'     => 'Pain Management & PAC Clinic',
                'room'     => 'Pain Clinic 107'
            ]
        ],
        'specializations' => [
            'Painless Normal Delivery (Labor Epidural Analgesia)',
            'Ultrasound-Guided Regional Nerve Blocks',
            'Multimodal Post-Surgical Pain Management',
            'Chronic Back Pain & Sciatica Nerve Blocks',
            'Neuro & Orthopaedic Surgical Anaesthesia',
            'Daycare Procedural Sedation'
        ],
        'education' => [
            [
                'degree'      => 'DNB — Anesthesiology',
                'institution' => 'National Board of Examinations (NBE), New Delhi',
                'year'        => '2015',
                'desc'        => 'Accredited post-graduate specialization in modern anaesthetic protocols and pain medicine.'
            ],
            [
                'degree'      => 'MBBS',
                'institution' => 'Premier Medical College',
                'year'        => '2011',
                'desc'        => 'Completed MBBS with distinctions in pharmacology and surgery.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Consultant Anaesthesiologist',
                'org'    => 'Sukhda Multispeciality Hospital',
                'period' => '2017 – Present',
                'desc'   => 'Overseeing labor epidural services and acute pain management.'
            ]
        ],
        'memberships' => [
            'Indian Society of Anaesthesiologists (ISA)',
            'Indian Society for Study of Pain (ISSP)'
        ],
        'awards' => [
            [
                'title' => 'Painless Delivery Excellence',
                'body'  => 'Honoured for pioneering comfortable epidural analgesia for mothers in Western Haryana.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Meenakshi Jain',
                'place'   => 'Hisar',
                'service' => 'Labor Epidural Analgesia',
                'quote'   => 'Dr. Parveen’s painless epidural made my childbirth completely stress-free. I felt no labor pain at all!'
            ]
        ]
    ],
    'dr-anil-bansal' => [
        'slug'         => 'dr-anil-bansal',
        'name'         => 'Dr. Anil Bansal',
        'photo'        => 'assets/images/doctors/dr-anil-bansal.jpg',
        'degrees'      => 'M.B.B.S, DMRD (Radiodiagnosis)',
        'role'         => 'Senior Consultant — CT Scan & Digital Radiology',
        'department'   => 'Radiology & Imaging',
        'experience'   => '24+ Years',
        'patients'     => '60,000+',
        'rating'       => '4.94',
        'reviews_count'=> '910+',
        'hospitals'    => 'Sukhda Multispeciality Hospital',
        'location_tag' => 'Multispeciality',
        'languages'    => 'English, Hindi',
        'summary'      => 'Senior Radiologist heading Sukhda’s high-precision 32-slice CT scanning unit, 4D Ultrasonography, Colour Doppler investigations, and image-guided biopsies.',
        'about'        => 'Dr. Anil Bansal is a veteran radiologist with over 24 years of clinical diagnostic experience. He heads the Department of Radiology and Diagnostic Imaging at Sukhda Multispeciality Hospital.<br><br>His diagnostic precision across CT angiography, neuro-imaging, trauma whole-body scans, and antenatal anomaly sonographies provides the clinical backbone for accurate surgical and medical decision-making.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda Multispeciality Hospital',
                'address'  => 'Delhi Road, Model Town, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '09:30 AM – 02:30 PM & 05:00 PM – 07:00 PM',
                'type'     => 'CT Scan & Ultrasound Reporting',
                'room'     => 'Diagnostic Imaging Wing'
            ]
        ],
        'specializations' => [
            '32-Slice CT Angiography & Whole-Body Scans',
            '4D Pregnancy Anomaly Scans & Level-II USG',
            'Colour Doppler Studies (Carotid, Peripheral & Renal)',
            'High-Resolution Chest CT (HRCT) for Lungs',
            'USG & CT-Guided Diagnostic Biopsies / FNAC',
            'Emergency Trauma Neuro-Cranial Imaging'
        ],
        'education' => [
            [
                'degree'      => 'DMRD — Radiodiagnosis',
                'institution' => 'Premier Apex Medical University',
                'year'        => '2001',
                'desc'        => 'Specialized post-graduate training in cross-sectional imaging, Doppler, and CT diagnostics.'
            ],
            [
                'degree'      => 'MBBS',
                'institution' => 'Top Medical College',
                'year'        => '1997',
                'desc'        => 'Graduated with high honours in anatomy and diagnostic pathology.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Head of Radiology & Imaging',
                'org'    => 'Sukhda Multispeciality Hospital',
                'period' => '2004 – Present',
                'desc'   => 'Supervising high-resolution diagnostic imaging, CT scan suite, and digital radiology.'
            ]
        ],
        'memberships' => [
            'Indian Radiological and Imaging Association (IRIA)',
            'Indian Medical Association (IMA)'
        ],
        'awards' => [
            [
                'title' => 'Excellence in Diagnostic Imaging',
                'body'  => 'Recognized for fast turnaround times and high diagnostic accuracy in emergency trauma CT scans.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Ashok Singla',
                'place'   => 'Hisar',
                'service' => 'CT Angiography & HRCT Scan',
                'quote'   => 'Dr. Anil Bansal’s accurate CT report detected my hidden lung issue in time for treatment. Very courteous and thorough doctor.'
            ]
        ]
    ],
    'dr-shubham-mehta' => [
        'slug'         => 'dr-shubham-mehta',
        'name'         => 'Dr. Shubham Mehta',
        'photo'        => 'assets/images/doctors/dr-shubham-mehta.jpg',
        'degrees'      => 'M.D. (Psychiatry), MBBS',
        'role'         => 'Consultant — Psychiatry & Mental Health',
        'department'   => 'Psychiatry & Mental Health',
        'experience'   => '8+ Years',
        'patients'     => '12,000+',
        'rating'       => '4.93',
        'reviews_count'=> '490+',
        'hospitals'    => 'Sukhda Multispeciality Hospital',
        'location_tag' => 'Multispeciality',
        'languages'    => 'English, Hindi, Punjabi',
        'summary'      => 'Compassionate Psychiatrist offering evidence-based psychiatric interventions, clinical depression care, anxiety & panic disorders, de-addiction, and adolescent wellness.',
        'about'        => 'Dr. Shubham Mehta is a consultant psychiatrist heading the Department of Mental Health & De-Addiction at Sukhda Multispeciality Hospital. He is dedicated to destigmatizing mental health and providing confidential, compassionate therapeutic care.<br><br>His practice combines evidence-based pharmacotherapy with cognitive behavioral counseling for stress, mood disorders, insomnia, obsessive-compulsive disorders (OCD), and substance de-addiction.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda Multispeciality Hospital',
                'address'  => 'Delhi Road, Model Town, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '10:00 AM – 02:00 PM',
                'type'     => 'Psychiatric Consultation & Counseling',
                'room'     => 'Mental Wellness Suite 109'
            ]
        ],
        'specializations' => [
            'Clinical Depression, Bipolar & Mood Disorders',
            'Anxiety, Panic Attacks & Phobia Management',
            'Obsessive-Compulsive Disorder (OCD)',
            'Substance De-Addiction (Alcohol, Tobacco, Opioids)',
            'Adolescent Behavioral Health & Exam Stress',
            'Sleep Disorders & Chronic Insomnia Therapy'
        ],
        'education' => [
            [
                'degree'      => 'M.D. — Psychiatry',
                'institution' => 'Premier Apex Psychiatric Institute',
                'year'        => '2018',
                'desc'        => 'Specialized doctorate in adult and adolescent psychiatry, neuropsychiatry, and psychotherapy.'
            ],
            [
                'degree'      => 'MBBS',
                'institution' => 'Top Medical University',
                'year'        => '2014',
                'desc'        => 'Graduated with academic distinctions in psychiatry and forensic medicine.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Consultant Psychiatrist',
                'org'    => 'Sukhda Multispeciality Hospital',
                'period' => '2019 – Present',
                'desc'   => 'Providing daily outpatient psychiatric consultations, counseling, and de-addiction programs.'
            ]
        ],
        'memberships' => [
            'Indian Psychiatric Society (IPS)',
            'Indian Medical Association (IMA)'
        ],
        'awards' => [
            [
                'title' => 'Youth Mental Health Advocate',
                'body'  => 'Awarded for community mental health awareness and youth stress management initiatives across Haryana.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Rohit Verma',
                'place'   => 'Hisar',
                'service' => 'Anxiety & Stress Counseling',
                'quote'   => 'Dr. Shubham Mehta listened to my struggles patiently without any judgment. His guidance helped me overcome crippling anxiety completely.'
            ]
        ]
    ],
    'dr-sanjeet-sahu' => [
        'slug'         => 'dr-sanjeet-sahu',
        'name'         => 'Dr. Sanjeet Sahu',
        'photo'        => 'assets/images/doctors/dr-sanjeet-sahu.jpg',
        'degrees'      => 'B.P.T, M.P.T (Musculoskeletal & Sports Physiotherapy), MIAP',
        'role'         => 'Head — Department of Physiotherapy & Rehabilitation',
        'department'   => 'Physiotherapy & Rehabilitation',
        'experience'   => '14+ Years',
        'patients'     => '28,000+',
        'rating'       => '4.95',
        'reviews_count'=> '780+',
        'hospitals'    => 'Sukhda Multispeciality Hospital',
        'location_tag' => 'Multispeciality',
        'languages'    => 'English, Hindi',
        'summary'      => 'Expert Physiotherapist specializing in post-joint replacement mobility rehabilitation, stroke & neuro-rehab, cervical-lumbar traction, and sports injury recovery.',
        'about'        => 'Dr. Sanjeet Sahu is the Head of the Department of Physiotherapy & Physical Rehabilitation at Sukhda Multispeciality Hospital. He brings 14+ years of expertise in restoring movement and relieving pain for surgical, orthopaedic, and neurological patients.<br><br>The department is equipped with modern electrotherapy, shortwave diathermy (SWD), cervical-lumbar motorized traction, ultrasound therapy, and customized kinetic exercise gyms.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda Multispeciality Hospital',
                'address'  => 'Delhi Road, Model Town, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '09:00 AM – 01:00 PM & 04:00 PM – 07:00 PM',
                'type'     => 'Physical Rehab & Exercise Sessions',
                'room'     => 'Physiotherapy Centre, Ground Floor'
            ]
        ],
        'specializations' => [
            'Post-Knee & Hip Replacement (TKR/THR) Rehabilitation',
            'Cervical Spondylosis, Sciatica & Lumbar Slip Disc',
            'Stroke & Hemiplegia Neuro-Rehabilitation',
            'Sports Injury & Ligament Strain Recovery',
            'Frozen Shoulder & Post-Fracture Stiffness Therapy',
            'Geriatric Balance, Posture & Gait Training'
        ],
        'education' => [
            [
                'degree'      => 'M.P.T. — Musculoskeletal Physiotherapy',
                'institution' => 'Premier Apex Physiotherapy Institute',
                'year'        => '2012',
                'desc'        => 'Post-graduate specialization in sports rehabilitation, orthopaedic manual therapy, and biomechanics.'
            ],
            [
                'degree'      => 'B.P.T. (Bachelor of Physiotherapy)',
                'institution' => 'Top Health Sciences University',
                'year'        => '2008',
                'desc'        => 'Completed 4.5-year clinical degree with honours in kinesiology.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Head of Physiotherapy',
                'org'    => 'Sukhda Multispeciality Hospital',
                'period' => '2014 – Present',
                'desc'   => 'Managing outpatient rehab, inpatient post-op mobilization, and therapeutic exercise clinics.'
            ]
        ],
        'memberships' => [
            'Indian Association of Physiotherapists (MIAP)',
            'Haryana Physiotherapy Council'
        ],
        'awards' => [
            [
                'title' => 'Excellence in Physical Rehabilitation',
                'body'  => 'Conferred for achieving fastest post-operative functional recovery times for joint replacement patients.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Kamlesh Devi',
                'place'   => 'Hisar',
                'service' => 'Post-TKR Knee Rehabilitation',
                'quote'   => 'Dr. Sanjeet Sahu’s physiotherapy sessions made my knee replacement recovery fast and pain-free. I was able to climb stairs without support in 3 weeks!'
            ]
        ]
    ],
    'dr-manisha-mehta' => [
        'slug'         => 'dr-manisha-mehta',
        'name'         => 'Dr. Manisha Mehta',
        'photo'        => 'assets/images/doctors/dr-manisha-mehta.jpg',
        'degrees'      => 'M.S. (Obstetrics & Gynaecology), D.G.O, MBBS',
        'role'         => 'Co-Founder & Director — Gynaecology & Clinical Governance',
        'department'   => 'Gynaecology & Obstetrics',
        'experience'   => '24+ Years',
        'patients'     => '55,000+',
        'rating'       => '4.96',
        'reviews_count'=> '1,420+',
        'hospitals'    => 'Sukhda Multispeciality Hospital',
        'location_tag' => 'Multispeciality',
        'languages'    => 'English, Hindi, Punjabi',
        'summary'      => 'Co-Founder of Sukhda Healthcare with over 24 years of dedicated leadership in women\'s health, maternity excellence, and ethical clinical quality systems.',
        'about'        => 'Dr. Manisha Mehta is the Co-Founder and Director of Sukhda Healthcare, heading clinical governance and women\'s healthcare services across the network. Established in 2002 alongside Dr. Amit Mehta, Dr. Manisha Mehta has guided thousands of safe deliveries and championed compassionate maternity care in Western Haryana.<br><br>Her clinical acumen spans complex obstetric surgeries, high-risk pregnancy monitoring, preventive oncology for women, and patient-first clinical standards that earned Sukhda its NABH accreditation.',
        'opd_schedule' => [
            [
                'hospital' => 'Sukhda Multispeciality Hospital',
                'address'  => 'Delhi Road, Model Town, Hisar',
                'days'     => 'Monday to Saturday',
                'timings'  => '10:00 AM – 02:00 PM',
                'type'     => 'Senior Consultant Maternity & Gynae OPD',
                'room'     => 'Director Suite 102, 1st Floor'
            ]
        ],
        'specializations' => [
            'Comprehensive Maternity & Antenatal Clinical Care',
            'High-Risk Pregnancy & Recurrent Miscarriage Workup',
            'Women’s Preventive Health & Cervical Cancer Screening',
            'Menopausal Health & Hormone Replacement Advice',
            'Adolescent Reproductive Wellness & PCOD Care',
            'Clinical Quality & Patient Safety Governance'
        ],
        'education' => [
            [
                'degree'      => 'M.S. — Obstetrics & Gynaecology',
                'institution' => 'Premier Apex Medical University',
                'year'        => '1998',
                'desc'        => 'Post-graduate specialization in operative obstetrics, maternal health, and fetal wellbeing.'
            ],
            [
                'degree'      => 'D.G.O & MBBS',
                'institution' => 'Top Medical College Network',
                'year'        => '1994',
                'desc'        => 'Graduated with distinctions across clinical rotatory internships.'
            ]
        ],
        'experience_timeline' => [
            [
                'role'   => 'Co-Founder & Director',
                'org'    => 'Sukhda Multispeciality Hospital',
                'period' => '2002 – Present',
                'desc'   => 'Directing maternal health services, patient experience, and NABH healthcare protocols.'
            ]
        ],
        'memberships' => [
            'Federation of Obstetric and Gynaecological Societies of India (FOGSI)',
            'Indian Menopause Society (IMS)',
            'Indian Medical Association (IMA)'
        ],
        'awards' => [
            [
                'title' => 'Women Healthcare Leadership Award',
                'body'  => 'Honoured for two decades of outstanding contribution to safe maternity and patient-first healthcare in Haryana.'
            ]
        ],
        'testimonials' => [
            [
                'name'    => 'Anita Yadav',
                'place'   => 'Bhiwani',
                'service' => 'Maternity & Childbirth',
                'quote'   => 'Dr. Manisha Mehta made my pregnancy journey calm, joyful, and completely safe. The hospital care is exceptional!'
            ]
        ]
    ]
];

// Determine selected doctor
if (!isset($reqDoc) || empty($reqDoc)) {
    $reqDoc = isset($_GET['doc']) ? trim($_GET['doc']) : 'dr-amit-mehta';
}
if (!array_key_exists($reqDoc, $allDoctors)) {
    $reqDoc = 'dr-amit-mehta';
}
$doc = $allDoctors[$reqDoc];

// Empanelled Lists for Cashless Trust Strip
$empanelledGov = [
    'Ayushman Bharat (PM-JAY)',
    'CGHS (Central Govt Health Scheme)',
    'ECHS (Ex-Servicemen Contributory Health Scheme)',
    'Haryana Govt Employees & Pensioners',
    'Northern Railway',
    'BSNL',
    'Food Corporation of India (FCI)'
];

$empanelledTPA = [
    'Star Health Insurance',
    'HDFC ERGO General Insurance',
    'ICICI Lombard',
    'Bajaj Allianz',
    'Care Health Insurance (Religare)',
    'Niva Bupa Health Insurance',
    'Medi Assist TPA',
    'Paramount Health TPA'
];
?>
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title><?= htmlspecialchars($doc['name']) ?> — <?= htmlspecialchars($doc['role']) ?> | Sukhda Hospital Hisar</title>
    <meta name="description" content="Consult <?= htmlspecialchars($doc['name']) ?>, <?= htmlspecialchars($doc['role']) ?> at Sukhda Healthcare Hisar. <?= htmlspecialchars($doc['degrees']) ?>. Experience: <?= htmlspecialchars($doc['experience']) ?>. Book OPD appointment online or call 01662-249473.">
    <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js"></script>
    <style>
        :root {
            --blue: #03205A;
            --blue-dark: #02163d;
            --blue-light: #eaf1f8;
            --green: #2A8238;
            --green-dark: #1b6326;
            --green-light: #eaf5ec;
            --pale: #f4f8fb;
            --muted: #53677f;
            --line: #dce7f0;
            --shadow-sm: 0 4px 12px rgba(3, 32, 90, 0.06);
            --shadow-md: 0 10px 30px rgba(3, 32, 90, 0.09);
            --shadow-lg: 0 18px 45px rgba(3, 32, 90, 0.14);
            --gold: #f59e0b;
        }

        * {
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            margin: 0;
            color: var(--blue);
            font: 15.5px/1.6 'Nunito Sans', sans-serif;
            background: #fff;
            overflow-x: hidden;
        }

        a {
            text-decoration: none;
            color: inherit;
        }

        img {
            display: block;
            width: 100%;
        }

        .wrap {
            width: min(1380px, calc(100% - 64px));
            margin: auto;
        }

        /* TOP NOTIFICATION BAR */
        .top {
            height: 40px;
            background: var(--blue);
            color: #fff;
            font-size: 13px;
        }

        .top .wrap,
        .nav .wrap {
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .links {
            display: flex;
            gap: 20px;
            align-items: center;
        }

        .links a {
            color: #fff;
            transition: color 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .links a:hover {
            color: #2A8238;
        }

        .links a+a,
        .links span+span {
            border-left: 1px solid #ffffff44;
            padding-left: 20px;
        }

        /* NAVIGATION HEADER */
        .nav {
            height: 80px;
            box-shadow: 0 2px 10px rgba(3, 32, 90, 0.08);
            position: sticky;
            top: 0;
            z-index: 100;
            background: #fff;
        }

        .logo {
            width: 230px;
            height: 62px;
            object-fit: contain;
            object-position: left center;
        }

        .menu {
            display: flex;
            gap: 30px;
            align-items: center;
            font-size: 15.5px;
            font-weight: 700;
        }

        .menu a {
            padding: 28px 0;
            position: relative;
            transition: color 0.2s ease;
            color: var(--blue);
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }

        .menu a:hover {
            color: var(--green);
        }

        .menu .on:after {
            content: '';
            height: 3px;
            background: var(--green);
            position: absolute;
            bottom: 14px;
            left: 0;
            right: 0;
        }

        .nav-group {
            position: relative;
            display: inline-flex;
            align-items: center;
        }

        .nav-group>a {
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }

        .nav-chevron {
            width: 14px;
            height: 14px;
            stroke-width: 2.4;
            transition: transform 0.2s ease;
        }

        @media(min-width: 901px) {
            .mobile-menu-head,
            .mobile-menu-footer,
            .nav-overlay {
                display: none !important;
            }

            .mobile-nav-links {
                display: flex !important;
                align-items: center;
                gap: 26px;
            }

            .nav-group:hover .nav-chevron {
                transform: rotate(180deg);
            }

            .nav-drop {
                display: none;
                position: absolute;
                top: 100%;
                left: 0;
                min-width: 250px;
                background: #fff;
                border: 1px solid var(--line);
                border-radius: 8px;
                box-shadow: 0 8px 24px rgba(3, 32, 90, 0.12);
                padding: 8px 0;
                z-index: 1000;
            }

            .nav-drop a {
                display: block;
                padding: 11px 20px !important;
                font-size: 14.5px;
                font-weight: 600;
                color: var(--blue);
                border: 0 !important;
            }

            .nav-drop a:hover {
                background: var(--pale);
                color: var(--green);
            }

            .nav-group:hover .nav-drop {
                display: block;
            }

            .services-drop {
                min-width: 280px;
            }

            /* MEGA MENU FOR OUR SERVICES */
            .nav-group.mega-group {
                position: relative;
            }

            .services-mega {
                display: none;
                position: absolute;
                top: 100%;
                left: 50%;
                transform: translateX(-50%);
                width: 820px;
                max-width: calc(100vw - 32px);
                background: #ffffff;
                border: 1px solid #d8e5f2;
                border-radius: 14px;
                box-shadow: 0 20px 48px rgba(3, 32, 90, 0.18), 0 4px 14px rgba(3, 32, 90, 0.06);
                padding: 0;
                z-index: 1000;
                overflow: hidden;
                animation: megaFadeIn 0.22s cubic-bezier(0.16, 1, 0.3, 1);
            }

            @keyframes megaFadeIn {
                from {
                    opacity: 0;
                    transform: translate(-50%, 8px);
                }
                to {
                    opacity: 1;
                    transform: translate(-50%, 0);
                }
            }

            .nav-group:hover .services-mega {
                display: block;
            }

            .mega-body {
                display: grid;
                grid-template-columns: 1.16fr 0.94fr;
                background: #fff;
            }

            .mega-col {
                padding: 18px 20px 16px;
            }

            .mega-col.medpark-col {
                background: #f7faff;
                border-left: 1px solid #e3edf7;
            }

            .mega-col-header {
                display: flex;
                align-items: center;
                gap: 10px;
                margin-bottom: 12px;
                padding-bottom: 10px;
                border-bottom: 1.5px solid #edf3f8;
            }

            .mega-col.medpark-col .mega-col-header {
                border-bottom-color: #dce7f3;
            }

            .mega-col-icon {
                width: 34px;
                height: 34px;
                border-radius: 8px;
                background: #eaf5ec;
                color: var(--green);
                display: flex;
                align-items: center;
                justify-content: center;
                flex-shrink: 0;
            }

            .mega-col-icon i, .mega-col-icon svg {
                width: 18px;
                height: 18px;
            }

            .mega-col-icon.medpark {
                background: #e8f0fe;
                color: var(--blue);
            }

            .mega-col-title {
                font-size: 13.5px;
                font-weight: 800;
                color: var(--blue);
                line-height: 1.25;
                letter-spacing: -0.2px;
            }

            .mega-col-sub {
                font-size: 11px;
                font-weight: 600;
                color: var(--muted);
                margin-top: 1px;
            }

            .mega-links-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 3px 8px;
            }

            .mega-links-grid.single-col {
                display: flex;
                flex-direction: column;
                gap: 4px;
            }

            .mega-links-grid a {
                display: flex !important;
                align-items: center !important;
                gap: 7px !important;
                padding: 6.5px 8px !important;
                font-size: 12.5px !important;
                font-weight: 600 !important;
                color: #355070 !important;
                border-radius: 6px !important;
                border: 0 !important;
                transition: all 0.16s ease !important;
                text-decoration: none !important;
                line-height: 1.25 !important;
            }

            .mega-links-grid a i, .mega-links-grid a svg {
                width: 14px !important;
                height: 14px !important;
                color: var(--green) !important;
                flex-shrink: 0 !important;
                stroke-width: 2.2 !important;
            }

            .mega-links-grid a:hover {
                background: #eaf5ec !important;
                color: var(--green) !important;
                transform: translateX(2px);
            }

            .mega-col.medpark-col .mega-links-grid a i,
            .mega-col.medpark-col .mega-links-grid a svg {
                color: #0d6efd !important;
            }

            .mega-col.medpark-col .mega-links-grid a:hover {
                background: #eef4ff !important;
                color: var(--blue) !important;
            }

            .mega-links-grid a.featured-service {
                background: #ffffff !important;
                border: 1px solid #c9dcf0 !important;
                border-left: 3.5px solid var(--green) !important;
                padding: 8px 10px !important;
                border-radius: 7px !important;
                box-shadow: 0 2px 6px rgba(3, 32, 90, 0.05) !important;
                margin-bottom: 3px;
            }

            .mega-links-grid a.featured-service i,
            .mega-links-grid a.featured-service svg {
                color: var(--green) !important;
                width: 18px !important;
                height: 18px !important;
            }

            .mega-links-grid a.featured-service b {
                display: block;
                font-size: 12.5px;
                color: var(--blue);
                font-weight: 800;
            }

            .mega-links-grid a.featured-service small {
                display: block;
                font-size: 10px;
                color: var(--muted);
                font-weight: 600;
                margin-top: 1px;
            }

            .mega-links-grid a.featured-service:hover {
                border-color: var(--green) !important;
                border-left-color: var(--green) !important;
                background: #f0faf2 !important;
            }

            .mega-links-grid a.featured-service:hover b {
                color: var(--green) !important;
            }

            .mega-footer {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 9px 20px;
                background: #f1f6fa;
                border-top: 1px solid #e1ecf6;
                font-size: 12px;
            }

            .mega-view-all {
                display: inline-flex !important;
                align-items: center !important;
                gap: 6px !important;
                color: var(--green) !important;
                font-weight: 800 !important;
                font-size: 12px !important;
                padding: 0 !important;
                border: 0 !important;
                background: transparent !important;
            }

            .mega-view-all:hover {
                background: transparent !important;
                text-decoration: underline !important;
            }

            .mega-emergency-tag {
                display: inline-flex;
                align-items: center;
                gap: 6px;
                color: var(--blue);
                font-size: 11.5px;
                font-weight: 600;
            }

            .mega-emergency-tag i, .mega-emergency-tag svg {
                width: 13px;
                height: 13px;
                color: var(--green);
            }
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            border-radius: 8px;
            padding: 11px 22px;
            font-weight: 800;
            font-size: 14px;
            transition: all 0.2s ease;
            cursor: pointer;
            border: 1px solid transparent;
        }

        .btn.primary {
            background: var(--blue);
            color: #fff;
            border-color: var(--blue);
        }

        .btn.primary:hover {
            background: var(--blue-dark);
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(3, 32, 90, 0.2);
        }

        .btn.green {
            background: var(--green);
            color: #fff;
            border-color: var(--green);
        }

        .btn.green:hover {
            background: var(--green-dark);
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(42, 130, 56, 0.25);
        }

        .btn.outline {
            background: #fff;
            border-color: var(--line);
            color: var(--blue);
        }

        .btn.outline:hover {
            border-color: var(--green);
            color: var(--green);
            background: var(--green-light);
        }

        .btn.whatsapp {
            background: #25D366;
            color: #fff;
            border-color: #25D366;
        }

        .btn.whatsapp:hover {
            background: #1eb956;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(37, 211, 102, 0.3);
        }

        .hamb {
            display: none;
            background: none;
            border: none;
            font-size: 26px;
            color: var(--blue);
            cursor: pointer;
        }

        /* HERO PROFILE SECTION */
        .doctor-hero {
            background: linear-gradient(135deg, #03205a 0%, #062f7a 50%, #0a3d99 100%);
            color: #fff;
            padding: 40px 0 55px;
            position: relative;
            overflow: hidden;
        }

        .doctor-hero::after {
            content: '';
            position: absolute;
            right: -120px;
            bottom: -120px;
            width: 480px;
            height: 480px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(104, 212, 147, 0.15) 0%, rgba(3, 32, 90, 0) 70%);
            pointer-events: none;
        }

        .crumb {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 13px;
            color: #bcd4e9;
            margin-bottom: 28px;
        }

        .crumb a {
            color: #bcd4e9;
            transition: color 0.2s;
        }

        .crumb a:hover {
            color: #68d493;
        }

        .crumb span {
            color: #68d493;
        }

        .doc-hero-grid {
            display: grid;
            grid-template-columns: 320px 1fr;
            gap: 48px;
            align-items: center;
        }

        .doc-photo-box {
            position: relative;
            border-radius: 18px;
            overflow: hidden;
            background: #fff;
            box-shadow: var(--shadow-lg);
            border: 4px solid rgba(255, 255, 255, 0.18);
        }

        .doc-photo-box img {
            height: 380px;
            object-fit: cover;
            object-position: top center;
            transition: transform 0.4s ease;
        }

        .doc-photo-box:hover img {
            transform: scale(1.03);
        }

        .doc-photo-badge {
            position: absolute;
            bottom: 14px;
            left: 14px;
            right: 14px;
            background: rgba(3, 32, 90, 0.92);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 9px 14px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            color: #fff;
            font-size: 12.5px;
            font-weight: 700;
        }

        .doc-photo-badge .badge-left {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .doc-photo-badge i {
            color: #68d493;
            width: 16px;
            height: 16px;
        }

        .doc-hero-info {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .doc-top-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            align-items: center;
        }

        .pill-verified {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 5px 12px;
            background: rgba(42, 130, 56, 0.35);
            border: 1px solid rgba(104, 212, 147, 0.5);
            border-radius: 99px;
            color: #8ae6ae;
            font-size: 11.5px;
            font-weight: 800;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }

        .pill-hosp-tag {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 5px 12px;
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.22);
            border-radius: 99px;
            color: #d8e8f8;
            font-size: 12px;
            font-weight: 700;
        }

        .doc-hero-info h1 {
            font-size: 38px;
            line-height: 1.15;
            margin: 0;
            font-weight: 900;
            letter-spacing: -0.5px;
        }

        .doc-degrees {
            font-size: 15.5px;
            color: #68d493;
            font-weight: 800;
            margin-top: -4px;
        }

        .doc-role {
            font-size: 17px;
            color: #e2eef9;
            font-weight: 700;
            line-height: 1.4;
        }

        .doc-summary {
            font-size: 15px;
            line-height: 1.6;
            color: #cfe1f2;
            max-width: 820px;
        }

        .doc-hero-stats {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            margin: 10px 0 16px;
            background: rgba(255, 255, 255, 0.07);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 12px;
            padding: 16px 20px;
            backdrop-filter: blur(6px);
        }

        .stat-item b {
            display: block;
            font-size: 22px;
            font-weight: 900;
            color: #fff;
            line-height: 1.2;
        }

        .stat-item small {
            display: block;
            font-size: 12px;
            color: #b9d3eb;
            font-weight: 600;
            margin-top: 3px;
        }

        .stat-item.rating b {
            color: #fbbf24;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .doc-hero-actions {
            display: flex;
            flex-wrap: wrap;
            gap: 14px;
            align-items: center;
        }

        /* SECTION STYLING */
        .section {
            padding: 68px 0;
        }

        .section.soft {
            background: var(--pale);
        }

        .kicker {
            color: var(--green);
            font-size: 12.5px;
            font-weight: 900;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            margin-bottom: 6px;
        }

        .section-title {
            font-size: 32px;
            line-height: 1.2;
            margin: 0 0 14px;
            color: var(--blue);
            font-weight: 900;
        }

        .section-sub {
            color: var(--muted);
            font-size: 15.5px;
            line-height: 1.6;
            margin: 0 0 34px;
            max-width: 760px;
        }

        /* MAIN CONTENT LAYOUT */
        .doc-page-layout {
            display: grid;
            grid-template-columns: 1fr 390px;
            gap: 44px;
            align-items: start;
        }

        .doc-main-col {
            display: flex;
            flex-direction: column;
            gap: 48px;
        }

        /* CONTENT BLOCK CARD */
        .content-card {
            background: #fff;
            border-radius: 14px;
            border: 1px solid var(--line);
            padding: 34px;
            box-shadow: var(--shadow-sm);
        }

        .content-card h3 {
            font-size: 22px;
            margin: 0 0 18px;
            color: var(--blue);
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 10px;
            padding-bottom: 12px;
            border-bottom: 1.5px solid var(--blue-light);
        }

        .content-card h3 i {
            color: var(--green);
            width: 22px;
            height: 22px;
        }

        .bio-text p {
            margin: 0 0 16px;
            color: #3b5168;
            font-size: 15.5px;
            line-height: 1.7;
        }

        .bio-text p:last-child {
            margin-bottom: 0;
        }

        /* OPD SCHEDULE CARDS */
        .opd-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 16px;
        }

        .opd-item {
            background: var(--pale);
            border: 1px solid var(--line);
            border-radius: 12px;
            padding: 20px 24px;
            display: grid;
            grid-template-columns: 1.3fr 1fr auto;
            gap: 18px;
            align-items: center;
            transition: all 0.2s ease;
        }

        .opd-item:hover {
            border-color: #92d0ab;
            background: #f1f8f3;
            transform: translateY(-2px);
            box-shadow: var(--shadow-sm);
        }

        .opd-loc b {
            font-size: 16px;
            color: var(--blue);
            display: block;
            margin-bottom: 4px;
        }

        .opd-loc small {
            color: var(--muted);
            font-size: 13px;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .opd-time {
            border-left: 2px solid #d0e1ed;
            padding-left: 18px;
        }

        .opd-time .days {
            font-size: 14px;
            font-weight: 800;
            color: var(--green);
            display: block;
        }

        .opd-time .hours {
            font-size: 13px;
            color: var(--blue);
            font-weight: 700;
            margin-top: 2px;
            display: block;
        }

        .opd-time .room {
            font-size: 11.5px;
            color: var(--muted);
            margin-top: 2px;
            display: block;
        }

        /* SPECIALTIES CHIP GRID */
        .speciality-chips {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
        }

        .spec-chip {
            background: #f7fafc;
            border: 1px solid #e2edf6;
            border-radius: 10px;
            padding: 13px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 14px;
            font-weight: 700;
            color: var(--blue);
            transition: all 0.2s;
        }

        .spec-chip:hover {
            background: var(--green-light);
            border-color: #95d3ad;
            color: var(--green-dark);
            transform: translateX(4px);
        }

        .spec-chip i {
            color: var(--green);
            width: 18px;
            height: 18px;
            flex-shrink: 0;
        }

        /* TIMELINE */
        .timeline {
            display: flex;
            flex-direction: column;
            gap: 22px;
            position: relative;
            padding-left: 28px;
        }

        .timeline::before {
            content: '';
            position: absolute;
            left: 7px;
            top: 6px;
            bottom: 6px;
            width: 2px;
            background: #cfe0ee;
        }

        .timeline-item {
            position: relative;
        }

        .timeline-dot {
            position: absolute;
            left: -28px;
            top: 4px;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: #fff;
            border: 3.5px solid var(--green);
            box-shadow: 0 0 0 2px rgba(42, 130, 56, 0.2);
        }

        .timeline-item h4 {
            font-size: 16px;
            margin: 0 0 3px;
            color: var(--blue);
            font-weight: 800;
        }

        .timeline-item .inst {
            font-size: 13.5px;
            color: var(--green);
            font-weight: 700;
            margin-bottom: 4px;
            display: block;
        }

        .timeline-item p {
            margin: 0;
            font-size: 13.5px;
            color: var(--muted);
            line-height: 1.55;
        }

        /* AWARDS LIST */
        .awards-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 14px;
        }

        .award-card {
            background: linear-gradient(135deg, #fdfbf7 0%, #fff 100%);
            border: 1px solid #f1e2c3;
            border-radius: 12px;
            padding: 16px 20px;
            display: flex;
            align-items: flex-start;
            gap: 16px;
        }

        .award-icon {
            width: 42px;
            height: 42px;
            background: #fef3c7;
            color: #d97706;
            border-radius: 10px;
            display: grid;
            place-items: center;
            flex-shrink: 0;
        }

        .award-icon i {
            width: 22px;
            height: 22px;
        }

        .award-card h4 {
            margin: 0 0 4px;
            font-size: 15.5px;
            color: #78350f;
            font-weight: 800;
        }

        .award-card p {
            margin: 0;
            font-size: 13.5px;
            color: #6b7280;
            line-height: 1.5;
        }

        /* SIDEBAR / APPOINTMENT CARD */
        .doc-sidebar {
            position: sticky;
            top: 100px;
            display: flex;
            flex-direction: column;
            gap: 24px;
        }

        .booking-card {
            background: #fff;
            border-radius: 16px;
            border: 1.5px solid #c9dfef;
            padding: 30px;
            box-shadow: var(--shadow-md);
        }

        .booking-header {
            margin-bottom: 22px;
            text-align: center;
            padding-bottom: 18px;
            border-bottom: 1px solid var(--line);
        }

        .booking-header h3 {
            font-size: 20px;
            margin: 0 0 6px;
            color: var(--blue);
            font-weight: 900;
        }

        .booking-header p {
            margin: 0;
            font-size: 13.5px;
            color: var(--muted);
        }

        .form-group {
            margin-bottom: 16px;
        }

        .form-group label {
            display: block;
            font-size: 13px;
            font-weight: 800;
            color: var(--blue);
            margin-bottom: 6px;
        }

        .form-control {
            width: 100%;
            height: 44px;
            border: 1px solid #c4d7e8;
            border-radius: 8px;
            padding: 0 14px;
            font-family: inherit;
            font-size: 14px;
            color: var(--blue);
            background: #fff;
            transition: border-color 0.2s;
        }

        .form-control:focus {
            outline: none;
            border-color: var(--green);
            box-shadow: 0 0 0 3px rgba(42, 130, 56, 0.15);
        }

        .form-group select.form-control {
            cursor: pointer;
        }

        .booking-help-box {
            background: var(--pale);
            border-radius: 10px;
            padding: 14px;
            margin: 18px 0;
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 12.5px;
            color: var(--muted);
        }

        .booking-help-box i {
            color: var(--green);
            width: 20px;
            height: 20px;
            flex-shrink: 0;
        }

        .sidebar-direct-card {
            background: linear-gradient(135deg, var(--blue) 0%, var(--blue-dark) 100%);
            color: #fff;
            border-radius: 14px;
            padding: 24px;
            box-shadow: var(--shadow-sm);
        }

        .sidebar-direct-card h4 {
            margin: 0 0 8px;
            font-size: 16px;
            font-weight: 800;
            color: #fff;
        }

        .sidebar-direct-card p {
            margin: 0 0 16px;
            font-size: 13px;
            color: #bed7ee;
            line-height: 1.5;
        }

        .direct-phone-btn {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 11px 16px;
            border-radius: 8px;
            color: #fff;
            font-weight: 800;
            font-size: 14px;
            transition: all 0.2s;
        }

        .direct-phone-btn:hover {
            background: rgba(255, 255, 255, 0.22);
            color: #68d493;
        }

        /* TESTIMONIALS SECTION */
        .reviews-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 22px;
        }

        .review-card {
            background: #fff;
            border-radius: 14px;
            border: 1px solid var(--line);
            padding: 26px;
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .review-card:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-md);
            border-color: #92d0ab;
        }

        .rev-stars {
            display: flex;
            gap: 4px;
            color: #f59e0b;
            margin-bottom: 14px;
        }

        .rev-quote {
            font-size: 14px;
            line-height: 1.65;
            color: #3f556d;
            margin: 0 0 18px;
            font-style: italic;
        }

        .rev-author {
            display: flex;
            align-items: center;
            gap: 12px;
            border-top: 1px solid var(--line);
            padding-top: 14px;
        }

        .rev-avatar {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: #e2eef7;
            color: var(--blue);
            font-weight: 900;
            font-size: 14px;
            display: grid;
            place-items: center;
        }

        .rev-author b {
            display: block;
            font-size: 14px;
            color: var(--blue);
        }

        .rev-author small {
            display: block;
            font-size: 12px;
            color: var(--green);
            font-weight: 700;
        }

        /* OTHER DOCTORS CAROUSEL / STRIP */
        .other-docs-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
        }

        .colleague-card {
            background: #fff;
            border-radius: 14px;
            border: 1px solid var(--line);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
            transition: all 0.25s ease;
            display: flex;
            flex-direction: column;
        }

        .colleague-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-md);
            border-color: #9cd6b4;
        }

        .colleague-img {
            height: 220px;
            object-fit: cover;
            object-position: top center;
            background: #f1f5f9;
        }

        .colleague-body {
            padding: 18px 20px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }

        .colleague-body h4 {
            font-size: 17px;
            margin: 0 0 4px;
            color: var(--blue);
            font-weight: 800;
        }

        .colleague-body .col-deg {
            font-size: 12px;
            color: var(--green);
            font-weight: 800;
            margin-bottom: 6px;
        }

        .colleague-body .col-spec {
            font-size: 13px;
            color: var(--muted);
            margin-bottom: 14px;
            line-height: 1.4;
            flex-grow: 1;
        }

        .colleague-body .btn-profile {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            font-size: 13px;
            font-weight: 800;
            color: var(--blue);
            background: var(--blue-light);
            padding: 8px 14px;
            border-radius: 6px;
            transition: all 0.2s;
        }

        .colleague-body .btn-profile:hover {
            background: var(--blue);
            color: #fff;
        }

        /* EMPANELLED CASHLESS STRIP */
        .empanelled-section {
            background: #f8fafc;
            border-top: 1px solid var(--line);
            border-bottom: 1px solid var(--line);
            padding: 38px 0;
        }

        .empanelled-grid {
            display: grid;
            grid-template-columns: 240px 1fr;
            gap: 36px;
            align-items: center;
        }

        .empanelled-text h4 {
            font-size: 16px;
            color: var(--blue);
            margin: 0 0 4px;
            font-weight: 800;
        }

        .empanelled-text p {
            margin: 0;
            font-size: 13px;
            color: var(--muted);
        }

        .empanelled-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .empanelled-tag {
            background: #fff;
            border: 1px solid #dbe6f0;
            padding: 6px 14px;
            border-radius: 6px;
            font-size: 12.5px;
            font-weight: 700;
            color: var(--blue);
        }

        /* FOOTER */
        .footer {
            padding: 56px 0 0;
            background: linear-gradient(180deg, #03205A 0%, #011338 100%);
            color: #cbd5e1;
            border-top: 4px solid var(--green);
            position: relative;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: 1.35fr .9fr 1.35fr 1.15fr;
            gap: 36px;
            padding-bottom: 44px;
        }

        .footer-brand-wrap {
            background: #fff;
            padding: 10px 18px;
            border-radius: 10px;
            display: inline-block;
            box-shadow: 0 6px 20px rgba(0, 0, 0, .18);
            margin-bottom: 16px;
            max-width: 230px;
        }

        .footer-brand-wrap .footer-logo {
            width: 100%;
            height: auto;
            object-fit: contain;
            margin: 0;
        }

        .footer-tagline {
            font-size: 13px;
            font-weight: 800;
            color: #68d493;
            letter-spacing: .3px;
            margin: 0 0 10px;
            text-transform: uppercase;
        }

        .footer-desc {
            font-size: 13.5px;
            line-height: 1.6;
            color: #94a3b8;
            margin: 0 0 16px;
        }

        .footer-nabh-badge {
            display: inline-flex;
            align-items: center;
            gap: 12px;
            background: rgba(255, 255, 255, .06);
            border: 1px solid rgba(255, 255, 255, .12);
            padding: 8px 14px;
            border-radius: 8px;
            backdrop-filter: blur(4px);
        }

        .footer-nabh-badge .nabh-icon-img {
            width: 32px;
            height: 32px;
            object-fit: contain;
            border-radius: 4px;
            background: #fff;
            padding: 2px;
            flex-shrink: 0;
        }

        .footer-nabh-badge b {
            display: block;
            font-size: 13px;
            color: #fff;
            line-height: 1.2;
        }

        .footer-nabh-badge small {
            display: block;
            font-size: 11px;
            color: #94a3b8;
        }

        .footer-col h4 {
            font-size: 15px;
            font-weight: 800;
            color: #fff;
            text-transform: uppercase;
            letter-spacing: .6px;
            margin: 0 0 18px;
            position: relative;
            padding-left: 12px;
        }

        .footer-col h4::before {
            content: '';
            position: absolute;
            left: 0;
            top: 2px;
            bottom: 2px;
            width: 3.5px;
            background: var(--green);
            border-radius: 2px;
        }

        .footer-nav {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 9px;
        }

        .footer-nav a {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 13.5px;
            color: #cbd5e1;
            transition: all .2s ease;
        }

        .footer-nav a span {
            color: var(--green);
            font-size: 14px;
            font-weight: 800;
        }

        .footer-nav a:hover {
            color: #fff;
            transform: translateX(4px);
        }

        .footer-hospital-card {
            background: rgba(255, 255, 255, .04);
            border: 1px solid rgba(255, 255, 255, .08);
            border-radius: 10px;
            padding: 12px 14px;
            margin-bottom: 12px;
            transition: border-color .2s ease, background .2s ease;
        }

        .footer-hospital-card:hover {
            background: rgba(255, 255, 255, .07);
            border-color: rgba(104, 212, 147, .35);
        }

        .f-hosp-header {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 5px;
        }

        .f-hosp-header i {
            width: 16px;
            height: 16px;
            color: var(--green);
            flex-shrink: 0;
        }

        .f-hosp-header b {
            font-size: 13.5px;
            color: #fff;
            line-height: 1.3;
        }

        .footer-hospital-card p {
            font-size: 12.5px;
            color: #94a3b8;
            line-height: 1.45;
            margin: 0 0 6px;
        }

        .f-hosp-phone {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 12.5px;
            font-weight: 700;
            color: #e2e8f0;
            transition: color .2s ease;
        }

        .f-hosp-phone:hover {
            color: #68d493;
        }

        .footer-emergency-box {
            display: flex;
            align-items: center;
            gap: 12px;
            background: linear-gradient(135deg, rgba(42, 130, 56, .22) 0%, rgba(3, 32, 90, .45) 100%);
            border: 1px solid rgba(104, 212, 147, .35);
            padding: 12px 14px;
            border-radius: 10px;
            margin-bottom: 14px;
        }

        .f-emg-icon {
            width: 38px;
            height: 38px;
            border-radius: 8px;
            background: var(--green);
            color: #fff;
            display: grid;
            place-items: center;
            flex-shrink: 0;
        }

        .f-emg-icon i {
            width: 20px;
            height: 20px;
        }

        .footer-emergency-box small {
            display: block;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: .6px;
            color: #68d493;
            font-weight: 700;
            margin-bottom: 2px;
        }

        .f-emg-num {
            display: block;
            font-size: 16px;
            font-weight: 900;
            color: #fff;
            line-height: 1.2;
        }

        .footer-contact-list {
            display: flex;
            flex-direction: column;
            gap: 9px;
            margin-bottom: 14px;
        }

        .f-cnt-item {
            display: flex;
            align-items: center;
            gap: 9px;
            font-size: 13px;
            color: #cbd5e1;
            padding: 7px 10px;
            background: rgba(255, 255, 255, .03);
            border: 1px solid rgba(255, 255, 255, .07);
            border-radius: 7px;
            transition: all .2s ease;
        }

        .f-cnt-item:hover {
            background: rgba(255, 255, 255, .08);
            color: #fff;
            border-color: rgba(104, 212, 147, .3);
        }

        .f-cnt-item.whatsapp:hover {
            color: #25d366;
            border-color: rgba(37, 211, 102, .4);
        }

        .footer-motto {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 13px;
            font-weight: 800;
            color: #68d493;
            padding-top: 4px;
        }

        .bottom {
            background: #010c22;
            padding: 18px 0;
            font-size: 13px;
            color: #94a3b8;
            border-top: 1px solid rgba(255, 255, 255, .08);
        }

        .bottom .wrap {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }

        .bottom-badges {
            display: flex;
            align-items: center;
            gap: 14px;
            flex-wrap: wrap;
            color: #cbd5e1;
            font-size: 12.5px;
        }

        .bottom-badges span {
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }

        .bottom-badges span i {
            width: 13px;
            height: 13px;
            color: var(--green);
        }

        /* STICKY BOTTOM BAR FOR MOBILE */
        .sticky-bottom-bar {
            display: none;
            position: fixed;
            bottom: 16px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 999;
            background: rgba(3, 32, 90, 0.96);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 99px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
            padding: 6px 10px;
            width: calc(100% - 32px);
            max-width: 440px;
            align-items: center;
            justify-content: space-around;
        }

        .sticky-bar-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 3px;
            color: #fff;
            font-size: 11px;
            font-weight: 700;
            padding: 6px 12px;
            border-radius: 99px;
            text-decoration: none;
            transition: all 0.2s;
            flex: 1;
            text-align: center;
        }

        .sticky-bar-item i {
            width: 18px;
            height: 18px;
            color: #68d493;
        }

        .sticky-bar-item.whatsapp i {
            color: #25d366;
        }

        .sticky-bar-divider {
            width: 1px;
            height: 24px;
            background: rgba(255, 255, 255, 0.2);
        }

        /* MOBILE MENU & RESPONSIVENESS */
        .mobile-menu-head,
        .mobile-menu-footer,
        .nav-overlay {
            display: none;
        }

        @media (max-width: 1024px) {
            .doc-hero-grid {
                grid-template-columns: 260px 1fr;
                gap: 32px;
            }

            .doc-page-layout {
                grid-template-columns: 1fr;
            }

            .doc-sidebar {
                position: static;
            }

            .other-docs-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .reviews-grid {
                grid-template-columns: 1fr;
            }

            .footer-grid {
                grid-template-columns: 1fr 1fr;
            }
        }

        @media (max-width: 768px) {
            .top {
                display: none;
            }

            .hamb {
                display: block;
            }

            .nav > .wrap > .primary {
                display: none;
            }

            .menu {
                position: fixed;
                top: 0;
                right: -100%;
                width: 82%;
                max-width: 320px;
                height: 100vh;
                background: #fff;
                flex-direction: column;
                align-items: flex-start;
                gap: 0;
                padding: 0;
                box-shadow: -6px 0 25px rgba(0, 0, 0, 0.25);
                z-index: 1000;
                transition: right 0.3s ease;
                overflow-y: auto;
            }

            .nav.open .menu {
                right: 0;
            }

            .nav-overlay {
                display: block;
                position: fixed;
                inset: 0;
                background: rgba(0, 0, 0, 0.5);
                z-index: 999;
                opacity: 0;
                pointer-events: none;
                transition: opacity 0.3s ease;
            }

            .nav.open .nav-overlay {
                opacity: 1;
                pointer-events: auto;
            }

            .mobile-menu-head {
                display: flex;
                align-items: center;
                justify-content: space-between;
                width: 100%;
                padding: 18px 20px;
                background: var(--blue);
            }

            .mobile-menu-head img {
                width: 140px;
            }

            .mobile-close-btn {
                background: none;
                border: none;
                color: #fff;
                font-size: 22px;
                cursor: pointer;
            }

            .mobile-nav-links {
                display: flex;
                flex-direction: column;
                width: 100%;
                padding: 16px 0;
            }

            .mobile-nav-links a {
                padding: 14px 24px;
                font-size: 15px;
                font-weight: 700;
                border-bottom: 1px solid #edf2f7;
                width: 100%;
            }

            .mobile-menu-footer {
                display: flex;
                flex-direction: column;
                gap: 10px;
                width: 100%;
                padding: 20px;
                margin-top: auto;
            }

            .doc-hero-grid {
                grid-template-columns: 1fr;
                text-align: center;
            }

            .doc-photo-box {
                max-width: 280px;
                margin: 0 auto;
            }

            .doc-top-tags {
                justify-content: center;
            }

            .doc-hero-info h1 {
                font-size: 30px;
            }

            .doc-hero-stats {
                grid-template-columns: repeat(2, 1fr);
                gap: 12px;
                text-align: left;
            }

            .doc-hero-actions {
                justify-content: center;
            }

            .speciality-chips {
                grid-template-columns: 1fr;
            }

            .opd-item {
                grid-template-columns: 1fr;
                gap: 12px;
            }

            .opd-time {
                border-left: none;
                border-top: 1px solid #d0e1ed;
                padding-left: 0;
                padding-top: 10px;
            }

            .other-docs-grid {
                grid-template-columns: 1fr;
            }

            .empanelled-grid {
                grid-template-columns: 1fr;
                gap: 16px;
            }

            .footer-grid {
                grid-template-columns: 1fr;
            }

            /* MOBILE ACCORDION STYLES */
            .nav-group {
                display: flex;
                flex-direction: column;
                align-items: stretch;
                width: 100%;
            }

            .nav-group>a {
                justify-content: space-between;
            }

            .nav-group .nav-chevron {
                transition: transform 0.25s ease;
                color: #71879f;
            }

            .nav-group.open>a .nav-chevron {
                transform: rotate(180deg);
                color: var(--green);
            }

            .nav-drop {
                display: none;
                position: static !important;
                min-width: 0 !important;
                box-shadow: none !important;
                border: 1px solid #e2edf6 !important;
                border-radius: 8px !important;
                background: #f7fafc !important;
                margin: 0 0 10px !important;
                padding: 4px 0 !important;
            }

            .nav-group.open .nav-drop {
                display: flex !important;
                flex-direction: column !important;
            }

            .nav-drop a {
                padding: 10px 14px !important;
                font-size: 13.5px !important;
                font-weight: 600 !important;
                color: #355070 !important;
                border-bottom: 1px solid #edf3f8 !important;
            }

            .nav-drop a:last-child {
                border-bottom: 0 !important;
            }

            .nav-drop a:hover {
                background: #eaf5ec !important;
                color: var(--green) !important;
            }

            /* MOBILE SERVICES MEGA ACCORDION */
            .nav-group.open .services-mega {
                display: flex !important;
                flex-direction: column !important;
                position: static !important;
                transform: none !important;
                width: 100% !important;
                box-shadow: none !important;
                border: 1px solid #e2edf6 !important;
                border-radius: 8px !important;
                margin: 0 0 10px !important;
                padding: 0 !important;
                background: #f7fafc !important;
                overflow: hidden !important;
                animation: none !important;
            }

            .services-mega .mega-body {
                display: flex !important;
                flex-direction: column !important;
                background: transparent !important;
            }

            .services-mega .mega-col {
                padding: 12px 14px !important;
            }

            .services-mega .mega-col.medpark-col {
                border-left: 0 !important;
                border-top: 1px solid #e2edf6 !important;
                background: #f1f7fc !important;
            }

            .services-mega .mega-col-header {
                display: flex !important;
                align-items: center !important;
                gap: 8px !important;
                margin-bottom: 8px !important;
                padding-bottom: 8px !important;
                border-bottom: 1px solid #e2edf6 !important;
            }

            .services-mega .mega-col-icon {
                width: 28px !important;
                height: 28px !important;
                border-radius: 6px !important;
            }

            .services-mega .mega-col-icon i,
            .services-mega .mega-col-icon svg {
                width: 15px !important;
                height: 15px !important;
            }

            .services-mega .mega-col-title {
                font-size: 13px !important;
                font-weight: 800 !important;
            }

            .services-mega .mega-col-sub {
                font-size: 10.5px !important;
            }

            .services-mega .mega-links-grid {
                display: flex !important;
                flex-direction: column !important;
                gap: 0 !important;
            }

            .services-mega .mega-links-grid a {
                padding: 8px 10px !important;
                font-size: 13px !important;
                border-bottom: 1px solid #edf3f8 !important;
                border-radius: 0 !important;
            }

            .services-mega .mega-links-grid a:last-child {
                border-bottom: 0 !important;
            }

            .services-mega .mega-footer {
                display: flex !important;
                flex-direction: column !important;
                align-items: flex-start !important;
                gap: 8px !important;
                padding: 10px 14px !important;
                background: #edf4fa !important;
                border-top: 1px solid #dce7f2 !important;
            }

            .sticky-bottom-bar {
                display: flex;
            }
        }
    </style>
</head>

<body>

    <!-- TOP BAR -->
    <div class="top">
        <div class="wrap">
            <div class="links">
                <a href="https://wa.me/919996544005" target="_blank" class="top-wa"><i data-lucide="message-circle" style="color:#25D366"></i> WhatsApp Us (24/7)</a>
                <a href="tel:01662249473" class="top-emergency" style="color:#ff4d4f"><b>☎ 01662-249473 (24/7 Emergency Helpline)</b></a>
            </div>
            <div class="links">
                <a href="index.php#empanelled">Cashless / TPA</a>
                <a href="index.php#specialities">OPD Schedule</a>
                <a href="contact.php">Contact Us</a>
            </div>
        </div>
    </div>

    <!-- HEADER / NAVIGATION -->
    <header class="nav">
        <div class="wrap">
            <a href="index.php" aria-label="Sukhda Healthcare home">
                <img class="logo" src="assets/images/sukhda-logo.png" alt="Sukhda Multispeciality Hospital Hisar">
            </a>
            <nav class="menu">
                <div class="mobile-menu-head">
                    <img src="assets/images/sukhda-logo.png" alt="Sukhda Hospital">
                    <button type="button" class="mobile-close-btn" aria-label="Close menu">✕</button>
                </div>
                <div class="mobile-nav-links">
                    <span class="nav-group">
                        <a href="about.php">About Us <i data-lucide="chevron-down" class="nav-chevron"></i></a>
                        <span class="nav-drop">
                            <a href="about.php">About Sukhda</a>
                            <a href="about.php#leadership">Medical Leadership</a>
                            <a href="index.php#why">Why Choose Us</a>
                            <a href="index.php#infrastructure">Infrastructure &amp; Facilities</a>
                            <a href="about.php#vision">Vision &amp; Mission</a>
                        </span>
                    </span>
                    <span class="nav-group">
                        <a href="index.php#hospitals">Our Hospitals <i data-lucide="chevron-down" class="nav-chevron"></i></a>
                        <span class="nav-drop">
                            <a href="index.php#hospitals">Sukhda Multispeciality Hospital</a>
                            <a href="index.php#hospitals">Sukhda MedPark (Cancer &amp; Super Speciality)</a>
                        </span>
                    </span>
                    <span class="nav-group mega-group">
                        <a href="index.php#specialities">Our Services <i data-lucide="chevron-down" class="nav-chevron"></i></a>
                        <div class="nav-drop services-mega">
                            <div class="mega-body">
                                <div class="mega-col">
                                    <div class="mega-col-header">
                                        <div class="mega-col-icon"><i data-lucide="building-2"></i></div>
                                        <div>
                                            <div class="mega-col-title">Sukhda Multispeciality Hospital</div>
                                            <div class="mega-col-sub">Comprehensive Multispeciality &amp; Emergency Hub</div>
                                        </div>
                                    </div>
                                    <div class="mega-links-grid">
                                        <a href="gynaecology.php"><i data-lucide="baby"></i><span>Gynaecology &amp; Obstetrics</span></a>
                                        <a href="index.php#specialities"><i data-lucide="heart-pulse"></i><span>Interventional Cardiology</span></a>
                                        <a href="index.php#specialities"><i data-lucide="droplets"></i><span>Nephrology &amp; Dialysis</span></a>
                                        <a href="index.php#specialities"><i data-lucide="bone"></i><span>Arthroscopy &amp; Joint Replacement</span></a>
                                        <a href="index.php#specialities"><i data-lucide="baby"></i><span>Paediatrics &amp; Neonatology</span></a>
                                        <a href="index.php#specialities"><i data-lucide="shield-check"></i><span>Advanced Laparoscopy &amp; Bariatric</span></a>
                                        <a href="index.php#specialities"><i data-lucide="headphones"></i><span>ENT (Ear, Nose &amp; Throat)</span></a>
                                        <a href="index.php#specialities"><i data-lucide="sparkles"></i><span>Dermatology &amp; Cosmetology</span></a>
                                        <a href="index.php#specialities"><i data-lucide="scan"></i><span>CT &amp; Radiology Imaging</span></a>
                                        <a href="index.php#specialities"><i data-lucide="zap"></i><span>Emergency &amp; Trauma Care (24×7)</span></a>
                                        <a href="index.php#specialities"><i data-lucide="stethoscope"></i><span>Internal Medicine &amp; Critical Care</span></a>
                                        <a href="index.php#specialities"><i data-lucide="heart"></i><span>Psychiatry &amp; Mental Health</span></a>
                                        <a href="index.php#specialities"><i data-lucide="smile"></i><span>Dentistry &amp; Maxillofacial</span></a>
                                        <a href="index.php#specialities"><i data-lucide="activity"></i><span>Physiotherapy &amp; Rehab</span></a>
                                    </div>
                                </div>
                                <div class="mega-col medpark-col">
                                    <div class="mega-col-header">
                                        <div class="mega-col-icon medpark"><i data-lucide="activity"></i></div>
                                        <div>
                                            <div class="mega-col-title">Sukhda MedPark</div>
                                            <div class="mega-col-sub">Cancer &amp; Super Speciality Hospital</div>
                                        </div>
                                    </div>
                                    <div class="mega-links-grid single-col">
                                        <a href="index.php#specialities" class="featured-service">
                                            <i data-lucide="ribbon"></i>
                                            <div>
                                                <b>Medical Oncology (Chemo &amp; Daycare)</b>
                                                <small>Chemotherapy, Daycare Suite &amp; Immunotherapy</small>
                                            </div>
                                        </a>
                                        <a href="index.php#specialities"><i data-lucide="shield-alert"></i><span>Surgical Oncology</span></a>
                                        <a href="index.php#specialities"><i data-lucide="scan"></i><span>Radiation Oncology (LINAC)</span></a>
                                        <a href="index.php#specialities"><i data-lucide="brain"></i><span>Neuro Surgery &amp; Spine</span></a>
                                        <a href="index.php#specialities"><i data-lucide="activity"></i><span>Gastroenterology &amp; Hepatology</span></a>
                                        <a href="index.php#specialities"><i data-lucide="activity"></i><span>Advanced Laparoscopy &amp; Urology</span></a>
                                        <a href="index.php#specialities"><i data-lucide="stethoscope"></i><span>Critical Care &amp; Tumour Board</span></a>
                                    </div>
                                </div>
                            </div>
                            <div class="mega-footer">
                                <a href="index.php#specialities" class="mega-view-all"><i data-lucide="layout-grid"></i> View All 21 Clinical Specialities &amp; Services →</a>
                                <div class="mega-emergency-tag"><i data-lucide="phone-call"></i> 24×7 ER: <b>01662-249473</b> | MedPark: <b>+91-99965-44005</b></div>
                            </div>
                        </div>
                    </span>
                    <a class="on" href="index.php#doctors">Our Doctors</a>
                    <a href="index.php#infrastructure">Technology</a>
                    <a href="index.php#cases">Case Stories</a>
                    <a href="contact.php">Contact Us</a>
                </div>
                <div class="mobile-menu-footer">
                    <a class="btn primary" href="#appointment"><i data-lucide="calendar-days"></i>Book Appointment</a>
                    <a class="btn" href="tel:01662249473" style="background:#fff;border-color:#b9cfe2;color:var(--blue);font-size:13px"><i data-lucide="phone-call" style="color:var(--green)"></i>ER: 01662-249473</a>
                </div>
            </nav>
            <a class="btn primary" href="#appointment"><i data-lucide="calendar-days"></i>Book Appointment</a>
            <button class="hamb" aria-label="Open menu">☰</button>
        </div>
        <div class="nav-overlay"></div>
    </header>

    <!-- 3. DOCTOR PROFILE HERO SECTION -->
    <section class="doctor-hero">
        <div class="wrap">
            <div class="crumb">
                <a href="index.php">Home</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <a href="index.php#doctors">Doctors</a>
                <i data-lucide="chevron-right" style="width:14px;height:14px"></i>
                <span><?= htmlspecialchars($doc['name']) ?></span>
            </div>

            <div class="doc-hero-grid">
                <div class="doc-photo-box">
                    <img src="<?= htmlspecialchars($doc['photo']) ?>" alt="<?= htmlspecialchars($doc['name']) ?> — Sukhda Hospital Hisar">
                    <div class="doc-photo-badge">
                        <span class="badge-left"><i data-lucide="award"></i> <?= htmlspecialchars($doc['experience']) ?> Exp.</span>
                        <span><i data-lucide="check-circle-2"></i> Verified</span>
                    </div>
                </div>

                <div class="doc-hero-info">
                    <div class="doc-top-tags">
                        <span class="pill-verified"><i data-lucide="shield-check" style="width:14px;height:14px"></i> Senior Faculty</span>
                        <span class="pill-hosp-tag"><i data-lucide="building-2" style="width:14px;height:14px;color:#68d493"></i> <?= htmlspecialchars($doc['hospitals']) ?></span>
                    </div>

                    <h1><?= htmlspecialchars($doc['name']) ?></h1>
                    <div class="doc-degrees"><?= htmlspecialchars($doc['degrees']) ?></div>
                    <div class="doc-role"><?= htmlspecialchars($doc['role']) ?></div>
                    <p class="doc-summary"><?= htmlspecialchars($doc['summary']) ?></p>

                    <div class="doc-hero-stats">
                        <div class="stat-item">
                            <b><?= htmlspecialchars($doc['experience']) ?></b>
                            <small>Clinical Experience</small>
                        </div>
                        <div class="stat-item">
                            <b><?= htmlspecialchars($doc['patients']) ?></b>
                            <small>Patients Treated</small>
                        </div>
                        <div class="stat-item rating">
                            <b><i data-lucide="star" style="width:18px;height:18px;fill:#f59e0b;stroke:#f59e0b"></i> <?= htmlspecialchars($doc['rating']) ?></b>
                            <small><?= htmlspecialchars($doc['reviews_count']) ?> Reviews</small>
                        </div>
                        <div class="stat-item">
                            <b><?= htmlspecialchars($doc['location_tag']) ?></b>
                            <small>Hospital Presence</small>
                        </div>
                    </div>

                    <div class="doc-hero-actions">
                        <a href="#appointment" class="btn green"><i data-lucide="calendar-check"></i> Book OPD Consultation</a>
                        <a href="https://wa.me/919996544005?text=Hello%20Dr.%20<?= urlencode($doc['name']) ?>,%20I%20would%20like%20to%20inquire%20about%20OPD%20consultation" target="_blank" rel="noopener" class="btn whatsapp"><i data-lucide="message-circle"></i> WhatsApp Query</a>
                        <a href="tel:01662249473" class="btn outline" style="color:#fff;border-color:rgba(255,255,255,0.35);background:rgba(255,255,255,0.08)"><i data-lucide="phone"></i> 01662-249473</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. DOCTOR PROFILE MAIN BODY (TWO COLUMNS) -->
    <section class="section">
        <div class="wrap">
            <div class="doc-page-layout">
                
                <!-- MAIN LEFT CONTENT -->
                <div class="doc-main-col">
                    
                    <!-- A. ABOUT THE DOCTOR -->
                    <article class="content-card">
                        <h3><i data-lucide="user-check"></i> Professional Profile &amp; Clinical Background</h3>
                        <div class="bio-text">
                            <p><?= $doc['about'] ?></p>
                        </div>
                    </article>

                    <!-- B. OPD TIMINGS & CONSULTATION LOCATIONS -->
                    <article class="content-card">
                        <h3><i data-lucide="clock"></i> OPD Schedule &amp; Hospital Locations</h3>
                        <div class="opd-grid">
                            <?php foreach ($doc['opd_schedule'] as $opd): ?>
                                <div class="opd-item">
                                    <div class="opd-loc">
                                        <b><?= htmlspecialchars($opd['hospital']) ?></b>
                                        <small><i data-lucide="map-pin" style="width:14px;height:14px;color:var(--green)"></i> <?= htmlspecialchars($opd['address']) ?></small>
                                    </div>
                                    <div class="opd-time">
                                        <span class="days"><?= htmlspecialchars($opd['days']) ?></span>
                                        <span class="hours"><?= htmlspecialchars($opd['timings']) ?></span>
                                        <span class="room"><?= htmlspecialchars($opd['room']) ?></span>
                                    </div>
                                    <div>
                                        <a href="#appointment" class="btn primary" style="padding:8px 16px;font-size:13px"><i data-lucide="calendar"></i> Book Slot</a>
                                    </div>
                                </div>
                            <?php endforeach; ?>
                        </div>
                    </article>

                    <!-- C. AREAS OF CLINICAL EXPERTISE -->
                    <article class="content-card">
                        <h3><i data-lucide="stethoscope"></i> Areas of Clinical Specialization</h3>
                        <div class="speciality-chips">
                            <?php foreach ($doc['specializations'] as $spec): ?>
                                <div class="spec-chip">
                                    <i data-lucide="check-circle-2"></i>
                                    <span><?= htmlspecialchars($spec) ?></span>
                                </div>
                            <?php endforeach; ?>
                        </div>
                    </article>

                    <!-- D. EDUCATION & QUALIFICATIONS TIMELINE -->
                    <article class="content-card">
                        <h3><i data-lucide="graduation-cap"></i> Qualifications &amp; Clinical Training</h3>
                        <div class="timeline">
                            <?php foreach ($doc['education'] as $edu): ?>
                                <div class="timeline-item">
                                    <div class="timeline-dot"></div>
                                    <h4><?= htmlspecialchars($edu['degree']) ?> (<?= htmlspecialchars($edu['year']) ?>)</h4>
                                    <span class="inst"><?= htmlspecialchars($edu['institution']) ?></span>
                                    <p><?= htmlspecialchars($edu['desc']) ?></p>
                                </div>
                            <?php endforeach; ?>
                        </div>
                    </article>

                    <!-- E. CLINICAL EXPERIENCE & LEADERSHIP -->
                    <article class="content-card">
                        <h3><i data-lucide="briefcase"></i> Professional Experience &amp; Appointments</h3>
                        <div class="timeline">
                            <?php foreach ($doc['experience_timeline'] as $exp): ?>
                                <div class="timeline-item">
                                    <div class="timeline-dot"></div>
                                    <h4><?= htmlspecialchars($exp['role']) ?></h4>
                                    <span class="inst"><?= htmlspecialchars($exp['org']) ?> (<?= htmlspecialchars($exp['period']) ?>)</span>
                                    <p><?= htmlspecialchars($exp['desc']) ?></p>
                                </div>
                            <?php endforeach; ?>
                        </div>
                    </article>

                    <!-- F. AWARDS & HONOURS -->
                    <?php if (!empty($doc['awards'])): ?>
                        <article class="content-card">
                            <h3><i data-lucide="trophy"></i> Awards &amp; Professional Recognitions</h3>
                            <div class="awards-grid">
                                <?php foreach ($doc['awards'] as $aw): ?>
                                    <div class="award-card">
                                        <div class="award-icon"><i data-lucide="award"></i></div>
                                        <div>
                                            <h4><?= htmlspecialchars($aw['title']) ?></h4>
                                            <p><?= htmlspecialchars($aw['body']) ?></p>
                                        </div>
                                    </div>
                                <?php endforeach; ?>
                            </div>
                        </article>
                    <?php endif; ?>

                    <!-- G. PROFESSIONAL MEMBERSHIPS -->
                    <?php if (!empty($doc['memberships'])): ?>
                        <article class="content-card">
                            <h3><i data-lucide="bookmark-check"></i> Professional Memberships &amp; Fellowships</h3>
                            <div class="speciality-chips">
                                <?php foreach ($doc['memberships'] as $mem): ?>
                                    <div class="spec-chip" style="background:#fff">
                                        <i data-lucide="badge-check"></i>
                                        <span><?= htmlspecialchars($mem) ?></span>
                                    </div>
                                <?php endforeach; ?>
                            </div>
                        </article>
                    <?php endif; ?>

                </div>

                <!-- RIGHT SIDEBAR (STICKY APPOINTMENT BOOKING WIDGET) -->
                <aside class="doc-sidebar" id="appointment">
                    <div class="booking-card">
                        <div class="booking-header">
                            <h3>Book OPD Appointment</h3>
                            <p>Direct consultation with <?= htmlspecialchars($doc['name']) ?></p>
                        </div>
                        <form action="contact.php" method="GET">
                            <input type="hidden" name="doctor" value="<?= htmlspecialchars($doc['slug']) ?>">
                            
                            <div class="form-group">
                                <label for="docSelect">Consulting Specialist</label>
                                <input type="text" id="docSelect" class="form-control" value="<?= htmlspecialchars($doc['name']) ?> (<?= htmlspecialchars($doc['department']) ?>)" readonly style="background:#f8fafc;font-weight:700">
                            </div>

                            <div class="form-group">
                                <label for="hospLoc">Select Hospital Location *</label>
                                <select id="hospLoc" name="hospital" class="form-control" required>
                                    <option value="Sukhda Multispeciality Hospital">Sukhda Multispeciality Hospital (Model Town)</option>
                                    <option value="Sukhda MedPark">Sukhda MedPark Super Speciality Hospital</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label for="appDate">Preferred Date *</label>
                                <input type="date" id="appDate" name="date" class="form-control" value="<?= date('Y-m-d', strtotime('+1 day')) ?>" required>
                            </div>

                            <div class="form-group">
                                <label for="appTime">Preferred Time Slot *</label>
                                <select id="appTime" name="slot" class="form-control" required>
                                    <option value="Morning (10:00 AM – 12:00 PM)">Morning (10:00 AM – 12:00 PM)</option>
                                    <option value="Afternoon (12:00 PM – 02:00 PM)">Afternoon (12:00 PM – 02:00 PM)</option>
                                    <option value="Evening (03:00 PM – 05:00 PM)">Evening (03:00 PM – 05:00 PM)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label for="patientName">Patient Full Name *</label>
                                <input type="text" id="patientName" name="name" class="form-control" placeholder="Enter patient name" required>
                            </div>

                            <div class="form-group">
                                <label for="patientPhone">Mobile Number *</label>
                                <input type="tel" id="patientPhone" name="phone" class="form-control" placeholder="10-digit mobile number" required>
                            </div>

                            <div class="booking-help-box">
                                <i data-lucide="shield-check"></i>
                                <span>No upfront payment required. Instant confirmation via SMS &amp; WhatsApp.</span>
                            </div>

                            <button type="submit" class="btn green" style="width:100%;padding:14px;font-size:15px">
                                <i data-lucide="calendar-plus"></i> Confirm OPD Appointment
                            </button>
                        </form>
                    </div>

                    <div class="sidebar-direct-card">
                        <h4>Need Immediate Assistance?</h4>
                        <p>Our hospital reception and emergency care coordinators are available 24 hours a day to assist you.</p>
                        <a href="tel:01662249473" class="direct-phone-btn">
                            <span><i data-lucide="phone-call" style="vertical-align:middle;margin-right:6px"></i> 01662-249473</span>
                            <small>24/7 Emergency</small>
                        </a>
                        <div style="height:10px"></div>
                        <a href="https://wa.me/919996544005" target="_blank" rel="noopener" class="direct-phone-btn" style="background:#25D366;border-color:#25D366">
                            <span><i data-lucide="message-circle" style="vertical-align:middle;margin-right:6px"></i> WhatsApp Desk</span>
                            <small>+91 99965-44005</small>
                        </a>
                    </div>
                </aside>

            </div>
        </div>
    </section>

    <!-- 5. PATIENT REVIEWS & TESTIMONIALS -->
    <?php if (!empty($doc['testimonials'])): ?>
    <section class="section soft">
        <div class="wrap">
            <div class="kicker">PATIENT EXPERIENCES</div>
            <h2 class="section-title">Verified Reviews for <?= htmlspecialchars($doc['name']) ?></h2>
            <p class="section-sub">Read genuine testimonials and recovery experiences from patients and their families.</p>

            <div class="reviews-grid">
                <?php foreach ($doc['testimonials'] as $rev): ?>
                    <article class="review-card">
                        <div>
                            <div class="rev-stars">
                                <i data-lucide="star" style="width:16px;height:16px;fill:#f59e0b"></i>
                                <i data-lucide="star" style="width:16px;height:16px;fill:#f59e0b"></i>
                                <i data-lucide="star" style="width:16px;height:16px;fill:#f59e0b"></i>
                                <i data-lucide="star" style="width:16px;height:16px;fill:#f59e0b"></i>
                                <i data-lucide="star" style="width:16px;height:16px;fill:#f59e0b"></i>
                            </div>
                            <p class="rev-quote">"<?= htmlspecialchars($rev['quote']) ?>"</p>
                        </div>
                        <div class="rev-author">
                            <div class="rev-avatar"><?= substr($rev['name'], 0, 1) ?></div>
                            <div>
                                <b><?= htmlspecialchars($rev['name']) ?></b>
                                <small><?= htmlspecialchars($rev['service']) ?> · <?= htmlspecialchars($rev['place']) ?></small>
                            </div>
                        </div>
                    </article>
                <?php endforeach; ?>
            </div>
        </div>
    </section>
    <?php endif; ?>

    <!-- 6. OTHER DOCTORS & COLLEAGUES -->
    <section class="section">
        <div class="wrap">
            <div class="kicker">CLINICAL FACULTY</div>
            <h2 class="section-title">Meet Other Senior Consultants at Sukhda</h2>
            <p class="section-sub">Consult specialized doctors across oncology, cardiology, obstetrics, nephrology, and surgery.</p>

            <div class="other-docs-grid">
                <?php
                $colleagueCount = 0;
                foreach ($allDoctors as $cSlug => $cDoc):
                    if ($cSlug === $reqDoc) continue;
                    if ($colleagueCount >= 4) break;
                    $colleagueCount++;
                ?>
                    <article class="colleague-card">
                        <img class="colleague-img" src="<?= htmlspecialchars($cDoc['photo']) ?>" alt="<?= htmlspecialchars($cDoc['name']) ?>">
                        <div class="colleague-body">
                            <h4><?= htmlspecialchars($cDoc['name']) ?></h4>
                            <div class="col-deg"><?= htmlspecialchars($cDoc['degrees']) ?></div>
                            <div class="col-spec"><?= htmlspecialchars($cDoc['role']) ?></div>
                            <a href="<?= htmlspecialchars($cSlug) ?>.php" class="btn-profile">View Profile →</a>
                        </div>
                    </article>
                <?php endforeach; ?>
            </div>
        </div>
    </section>

    <!-- 7. CASHLESS INSURANCE TRUST STRIP -->
    <div class="empanelled-section">
        <div class="wrap empanelled-grid">
            <div class="empanelled-text">
                <h4>Cashless &amp; Govt Empanelments</h4>
                <p>Accepted across all OPD, surgical &amp; ICU admissions.</p>
            </div>
            <div class="empanelled-tags">
                <?php foreach (array_merge($empanelledGov, $empanelledTPA) as $emp): ?>
                    <span class="empanelled-tag"><?= htmlspecialchars($emp) ?></span>
                <?php endforeach; ?>
            </div>
        </div>
    </div>

    <!-- 8. FOOTER -->
    <footer class="footer">
        <div class="wrap footer-grid">
            <div>
                <div class="footer-brand-wrap">
                    <img class="footer-logo" src="assets/images/sukhda-logo.png"
                        alt="Sukhda Multispeciality Hospital Hisar">
                </div>
                <p class="footer-tagline">Compassion &bull; Expertise &bull; Care</p>
                <p class="footer-desc">Delivering advanced multispeciality care and comprehensive cancer management with
                    trusted specialists, 24×7 trauma ICU, and NABH accredited standards in Hisar.</p>
                <div class="footer-nabh-badge">
                    <img src="assets/images/nabh.jpg" alt="NABH Accredited" class="nabh-icon-img">
                    <div>
                        <b>NABH Accredited</b>
                        <small>Highest Healthcare Quality Standards</small>
                    </div>
                </div>
            </div>
            <div class="footer-col">
                <h4>Quick Links</h4>
                <ul class="footer-nav">
                    <li><a href="index.php"><span>›</span> Home</a></li>
                    <li><a href="about.php"><span>›</span> About Sukhda</a></li>
                    <li><a href="index.php#hospitals"><span>›</span> Our Hospitals</a></li>
                    <li><a href="index.php#specialities"><span>›</span> Centres of Excellence</a></li>
                    <li><a href="index.php#doctors"><span>›</span> Our Doctors</a></li>
                    <li><a href="#appointment"><span>›</span> Book Appointment</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Our Hospitals</h4>
                <div class="footer-hospital-card">
                    <div class="f-hosp-header">
                        <i data-lucide="building-2"></i>
                        <b>Sukhda Multispeciality Hospital</b>
                    </div>
                    <p>Delhi Road, Model Town, Hisar, Haryana 125005</p>
                    <a href="tel:01662249473" class="f-hosp-phone">
                        <i data-lucide="phone"></i> 01662-249473 / 248473
                    </a>
                </div>
                <div class="footer-hospital-card">
                    <div class="f-hosp-header">
                        <i data-lucide="activity"></i>
                        <b>Sukhda MedPark</b>
                    </div>
                    <p>Cancer &amp; Super Speciality Hospital, Delhi Road, Hisar</p>
                    <a href="tel:+919996544005" class="f-hosp-phone">
                        <i data-lucide="phone"></i> +91-99965-44005
                    </a>
                </div>
            </div>
            <div class="footer-col">
                <h4>24×7 Emergency &amp; OPD</h4>
                <div class="footer-emergency-box">
                    <div class="f-emg-icon">
                        <i data-lucide="phone-call"></i>
                    </div>
                    <div>
                        <small>24×7 Emergency Helpline</small>
                        <a href="tel:01662249473" class="f-emg-num">01662-249473</a>
                    </div>
                </div>
                <div class="footer-contact-list">
                    <a href="mailto:info@sukhdahospitalhisar.com" class="f-cnt-item">
                        <i data-lucide="mail"></i>
                        <span>info@sukhdahospitalhisar.com</span>
                    </a>
                    <a href="https://wa.me/919996544005" target="_blank" class="f-cnt-item whatsapp">
                        <i data-lucide="message-circle"></i>
                        <span>WhatsApp: +91 99965-44005</span>
                    </a>
                </div>
                <div class="footer-motto">
                    <i data-lucide="heart-handshake"></i>
                    <span>Care &amp; Cure for Whole Family</span>
                </div>
            </div>
        </div>
        <div class="bottom">
            <div class="wrap">
                <span>© <?= $year ?> Sukhda Healthcare. All rights reserved.</span>
                <div class="bottom-badges">
                    <span><i data-lucide="map-pin"></i> Delhi Road, Hisar</span>
                    <span><i data-lucide="shield-check"></i> NABH Accredited</span>
                    <span><i data-lucide="phone"></i> 24×7 ER: 01662-249473</span>
                </div>
            </div>
        </div>
    </footer>

    <!-- STICKY BOTTOM BAR FOR MOBILE -->
    <div class="sticky-bottom-bar" aria-label="Quick Actions">
        <a href="#appointment" class="sticky-bar-item">
            <i data-lucide="calendar"></i>
            <span>Book OPD</span>
        </a>
        <div class="sticky-bar-divider"></div>
        <a href="tel:01662249473" class="sticky-bar-item">
            <i data-lucide="phone-call"></i>
            <span>Call ER</span>
        </a>
        <div class="sticky-bar-divider"></div>
        <a href="https://wa.me/919996544005" target="_blank" rel="noopener" class="sticky-bar-item whatsapp">
            <i data-lucide="message-circle"></i>
            <span>WhatsApp</span>
        </a>
    </div>

    <!-- SCRIPT INITIALIZATION -->
    <script>
        lucide.createIcons();

        // Mobile Navigation Handler
        (() => {
            const nav = document.querySelector('.nav');
            const button = document.querySelector('.hamb');
            const closeBtn = document.querySelector('.mobile-close-btn');
            const overlay = document.querySelector('.nav-overlay');
            const menu = document.querySelector('.menu');
            if (!nav || !button || !menu) return;

            menu.id = 'mobile-menu';
            button.type = 'button';
            button.setAttribute('aria-controls', menu.id);
            button.setAttribute('aria-expanded', 'false');
            button.setAttribute('aria-label', 'Open menu');

            const close = () => {
                nav.classList.remove('open');
                document.body.style.overflow = '';
                button.setAttribute('aria-expanded', 'false');
                button.setAttribute('aria-label', 'Open menu');
                button.blur();
            };

            const open = () => {
                nav.classList.add('open');
                document.body.style.overflow = 'hidden';
                button.setAttribute('aria-expanded', 'true');
                button.setAttribute('aria-label', 'Close menu');
            };

            button.onclick = e => {
                e.preventDefault();
                e.stopPropagation();
                nav.classList.contains('open') ? close() : open();
            };

            if (closeBtn) closeBtn.onclick = e => { e.preventDefault(); close(); };
            if (overlay) overlay.onclick = e => { e.preventDefault(); close(); };

            const navGroups = menu.querySelectorAll('.nav-group');
            navGroups.forEach(group => {
                const parentLink = group.querySelector(':scope > a');
                if (!parentLink) return;
                parentLink.addEventListener('click', e => {
                    if (window.innerWidth <= 900) {
                        e.preventDefault();
                        e.stopPropagation();
                        const isOpen = group.classList.contains('open');
                        navGroups.forEach(g => { if (g !== group) g.classList.remove('open'); });
                        group.classList.toggle('open', !isOpen);
                    }
                });
            });

            menu.addEventListener('click', e => {
                const a = e.target.closest('a');
                if (!a) return;
                if (a.closest('.nav-drop') || !a.closest('.nav-group')) {
                    close();
                }
            });

            document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
        })();
    </script>
</body>
</html>
