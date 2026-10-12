import os

with open('temp_header.html', 'r', encoding='utf-8') as f:
    base_header = f.read()

with open('temp_footer.html', 'r', encoding='utf-8') as f:
    base_footer = f.read()

# Make sure quick links in footer contain all new pages
new_quick_links = """                <ul class="footer-nav">
                    <li><a href="index.html"><span>›</span> Home</a></li>
                    <li><a href="about.html"><span>›</span> About Sukhda</a></li>
                    <li><a href="doctor.html"><span>›</span> Find Doctors</a></li>
                    <li><a href="patient-stories.html"><span>›</span> Patient Stories</a></li>
                    <li><a href="careers.html"><span>›</span> Careers</a></li>
                    <li><a href="csr.html"><span>›</span> CSR &amp; Community</a></li>
                    <li><a href="media-centre.html"><span>›</span> Media Centre</a></li>
                    <li><a href="contact.html"><span>›</span> Contact Us</a></li>
                </ul>"""

import re
base_footer_updated = re.sub(r'<ul class="footer-nav">[\s\S]*?</ul>', new_quick_links, base_footer)

# Common shared CSS for header, top bar, buttons, footer, drawer
common_css = """
        :root {
            --blue: #052159;
            --blue-dark: #02163d;
            --green: #278132;
            --green-light: #eaf5ec;
            --pale: #f2f7fb;
            --muted: #53677f;
            --line: #dce7f0
        }

        * {
            box-sizing: border-box
        }

        html {
            scroll-behavior: smooth
        }

        body {
            margin: 0;
            color: var(--blue);
            font: 16.5px/1.6 'Lato', sans-serif;
            background: #fff;
            overflow-x: hidden
        }

        h1, h2, h3, h4, h5, h6,
        .btn, .kicker, .eyebrow,
        .nav-group > a, .nav-drop a,
        .mega-col-title, .about-stat-card b,
        .stat-card b, .stat-value, .metric-value,
        .highlight-box b, .badge, .counter,
        .sec-title, .header-cta, .phone-pill,
        .doc-card-name, .dept-title, .facility-body h3,
        .t-card-name, .review-author, .meta-label,
        .brand, .logo-text, .h-info h3, .card-title,
        .footer-col h4, .footer-col h5, .stat-num,
        .story-patient-name, .tab-btn, .pill-tag,
        .job-card-title, .csr-card-title, .news-title {
            font-family: 'Montserrat', sans-serif;
        }

        a {
            text-decoration: none;
            color: inherit
        }

        img {
            display: block;
            width: 100%
        }

        .wrap {
            width: min(1400px, calc(100% - 100px));
            margin: auto
        }

        /* TOP BAR */
        .top {
            height: 42px;
            background: var(--blue);
            color: #fff;
            font-size: 14px
        }

        .top .wrap,
        .nav .wrap {
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between
        }

        .links {
            display: flex;
            gap: 20px;
            align-items: center
        }

        .links a {
            color: #fff;
            transition: color 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px
        }

        .links a:hover {
            color: #278132
        }

        .links a.top-wa,
        .links a[href*="wa.me"] {
            color: #25D366 !important;
        }

        .links a.top-emergency,
        .links a[href^="tel:"] {
            color: #ff4d4f !important;
        }

        .links span+span,
        .links a+a {
            border-left: 1px solid #ffffff55;
            padding-left: 20px
        }

        /* NAVIGATION */
        .nav {
            height: 80px;
            box-shadow: 0 2px 9px #05215919;
            position: relative;
            z-index: 100;
            background: #fff
        }

        .logo {
            width: 230px;
            height: 62px;
            object-fit: contain;
            object-position: left center
        }

        .menu {
            display: flex;
            gap: 30px;
            align-items: center;
            font-size: 16px;
            font-weight: 700
        }

        .menu a {
            padding: 28px 0;
            position: relative;
            transition: color 0.2s ease
        }

        .menu a.on,
        .menu a:hover {
            color: var(--green)
        }

        .menu a.on::after,
        .menu a:hover::after {
            content: "";
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: var(--green)
        }

        .menu a.btn.primary {
            padding: 10px 20px;
            color: #fff !important;
        }

        .menu a.btn.primary:hover {
            color: #fff !important;
            background: var(--blue) !important;
        }

        .menu a.btn.primary::after {
            display: none !important;
        }

        .hamb {
            display: none;
            background: none;
            border: 0;
            cursor: pointer;
            padding: 8px;
            color: var(--blue);
            align-items: center;
            justify-content: center
        }}

        .nav-group {
            position: relative;
            display: inline-flex;
            align-items: center
        }

        .nav-group>a {
            display: inline-flex;
            align-items: center;
            gap: 4px
        }

        .nav-chevron {
            width: 16px;
            height: 16px;
            transition: transform 0.2s ease;
            stroke-width: 2.2px
        }

        .nav-group:hover .nav-chevron {
            transform: rotate(180deg)
        }

        .nav-drop {
            position: absolute;
            top: 100%;
            left: 0;
            min-width: 240px;
            background: #fff;
            border-radius: 0 0 10px 10px;
            box-shadow: 0 12px 30px #05215926;
            padding: 10px 0;
            opacity: 0;
            visibility: hidden;
            transform: translateY(10px);
            transition: all 0.25s ease;
            z-index: 200;
            display: flex;
            flex-direction: column
        }

        .nav-group:hover .nav-drop {
            opacity: 1;
            visibility: visible;
            transform: translateY(0)
        }

        .nav-drop a {
            padding: 10px 20px;
            font-size: 14.5px;
            font-weight: 600;
            color: var(--blue);
            transition: background 0.2s ease, color 0.2s ease, padding-left 0.2s ease;
            display: flex;
            align-items: center;
            gap: 8px;
            border-bottom: 1px solid #f0f4f8
        }

        .nav-drop a:last-child {
            border-bottom: none
        }

        .nav-drop a:hover {
            background: var(--pale);
            color: var(--green);
            padding-left: 24px
        }

        .nav-drop a::after {
            display: none !important
        }

        /* MEGA MENU */
        .nav-group.mega-group {
            position: static
        }

        .nav-drop.services-mega {
            left: 50%;
            transform: translateX(-50%) translateY(10px);
            width: min(1380px, calc(100% - 60px));
            padding: 0;
            border-radius: 12px;
            overflow: hidden;
            border-top: 3px solid var(--green);
            box-shadow: 0 18px 45px #05215930
        }

        .nav-group.mega-group:hover .nav-drop.services-mega {
            transform: translateX(-50%) translateY(0)
        }

        .mega-body {
            display: grid;
            grid-template-columns: 1.4fr 1fr;
            background: #fff
        }

        .mega-col {
            padding: 24px 28px
        }

        .mega-col.medpark-col {
            background: #f8fbfa;
            border-left: 1px solid var(--line)
        }

        .mega-col-header {
            display: flex;
            align-items: center;
            gap: 12px;
            padding-bottom: 14px;
            margin-bottom: 16px;
            border-bottom: 2px solid #eef3f7
        }

        .mega-col-icon {
            width: 38px;
            height: 38px;
            border-radius: 8px;
            background: #eaf5ec;
            color: var(--green);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0
        }

        .mega-col-icon.medpark {
            background: #e8f0fe;
            color: #1a73e8
        }}

        .mega-col-title {
            font-size: 16px;
            font-weight: 800;
            color: var(--blue);
            line-height: 1.2
        }

        .mega-col-sub {
            font-size: 12px;
            color: var(--muted);
            font-weight: 500;
            margin-top: 2px
        }

        .mega-links-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 4px 14px
        }

        .mega-links-grid.single-col {
            grid-template-columns: 1fr;
            gap: 4px
        }

        .mega-links-grid a {
            padding: 7px 10px;
            font-size: 13.5px;
            font-weight: 600;
            color: #1a3353;
            border-radius: 6px;
            display: flex;
            align-items: center;
            gap: 9px;
            transition: all 0.15s ease;
            border-bottom: none
        }

        .mega-links-grid a i {
            width: 15px;
            height: 15px;
            color: var(--green);
            flex-shrink: 0;
            transition: transform 0.15s ease
        }

        .mega-links-grid a:hover {
            background: #eaf5ec;
            color: var(--green);
            padding-left: 12px
        }

        .mega-links-grid a:hover i {
            transform: scale(1.15)
        }

        .mega-links-grid a.featured-service {
            background: #edf4fe;
            border: 1px solid #d2e3fc;
            padding: 10px 12px;
            margin-bottom: 6px;
            align-items: flex-start
        }

        .mega-links-grid a.featured-service i {
            color: #1a73e8;
            margin-top: 3px;
            width: 18px;
            height: 18px
        }

        .mega-links-grid a.featured-service b {
            display: block;
            font-size: 13.5px;
            color: var(--blue);
            line-height: 1.2
        }

        .mega-links-grid a.featured-service small {
            display: block;
            font-size: 11.5px;
            color: #5f6368;
            font-weight: 400;
            margin-top: 2px
        }

        .mega-footer {
            background: #052159;
            color: #fff;
            padding: 12px 28px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 13px
        }

        .mega-view-all {
            color: #8ce09e;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 0 !important;
            transition: color 0.2s ease
        }

        .mega-view-all:hover {
            color: #fff;
            background: none !important
        }

        .mega-emergency-tag {
            color: #dce7f0;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 12.5px
        }

        .mega-emergency-tag b {
            color: #ffb4b4
        }

        .mobile-menu-head,
        .mobile-menu-footer,
        .nav-overlay {
            display: none
        }

        /* BUTTONS & GENERAL UI */
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: var(--blue);
            color: #fff;
            padding: 12px 26px;
            border-radius: 8px;
            font-weight: 700;
            transition: all 0.25s ease;
            font-size: 15px;
            border: 2px solid transparent;
            cursor: pointer
        }

        .btn:hover {
            background: var(--blue-dark);
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(5,33,89,0.2)
        }

        .btn.primary {
            background: var(--green);
            color: #fff
        }

        .btn.primary:hover {
            background: #1f6b28;
            box-shadow: 0 6px 18px rgba(39,129,50,0.25)
        }

        .btn.outline {
            background: transparent;
            border-color: var(--blue);
            color: var(--blue)
        }

        .btn.outline:hover {
            background: var(--blue);
            color: #fff
        }

        .btn.white {
            background: #fff;
            color: var(--blue)
        }

        .btn.white:hover {
            background: var(--pale);
            color: var(--blue-dark)
        }

        /* HERO COMMON */
        .hero-banner {
            position: relative;
            background: linear-gradient(135deg, #02163d 0%, #052159 60%, #0d3880 100%);
            color: #fff;
            padding: 70px 0 80px;
            overflow: hidden
        }

        .hero-banner::before {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at 85% 20%, rgba(39, 129, 50, 0.25) 0%, transparent 50%);
            pointer-events: none
        }

        .hero-grid {
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 40px;
            align-items: center;
            position: relative;
            z-index: 2
        }

        .badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(39, 129, 50, 0.25);
            border: 1px solid rgba(140, 224, 158, 0.4);
            color: #8ce09e;
            padding: 6px 16px;
            border-radius: 50px;
            font-size: 13.5px;
            font-weight: 700;
            letter-spacing: 0.5px;
            margin-bottom: 16px;
            text-transform: uppercase
        }

        .hero-banner h1 {
            font-size: clamp(32px, 4.2vw, 46px);
            font-weight: 800;
            line-height: 1.2;
            margin: 0 0 16px;
            color: #fff
        }

        .hero-banner h1 span {
            color: #4ade80
        }

        .hero-banner p {
            font-size: 17px;
            color: #e2e8f0;
            margin: 0 0 28px;
            line-height: 1.6;
            max-width: 640px
        }

        .hero-actions {
            display: flex;
            gap: 14px;
            flex-wrap: wrap
        }

        .hero-stats-card {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.16);
            border-radius: 16px;
            padding: 28px;
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px
        }

        .hero-stat-item {
            display: flex;
            flex-direction: column;
            gap: 4px
        }

        .hero-stat-num {
            font-size: 32px;
            font-weight: 800;
            color: #8ce09e;
            line-height: 1.1;
            font-family: 'Montserrat', sans-serif
        }

        .hero-stat-label {
            font-size: 13.5px;
            color: #cbd5e1;
            font-weight: 500
        }

        /* SECTION HEADERS */
        .sec-header {
            text-align: center;
            max-width: 780px;
            margin: 0 auto 50px
        }

        .kicker {
            color: var(--green);
            font-size: 14px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
            display: block
        }

        .sec-title {
            font-size: clamp(28px, 3.5vw, 38px);
            font-weight: 800;
            color: var(--blue);
            margin: 0 0 14px;
            line-height: 1.25
        }

        .sec-desc {
            color: var(--muted);
            font-size: 16.5px;
            margin: 0
        }

        /* TABS */
        .filter-section {
            background: #fff;
            padding: 24px 0 10px;
            border-bottom: 1px solid var(--line);
            position: sticky;
            top: 0;
            z-index: 40;
            box-shadow: 0 4px 15px rgba(0,0,0,0.03)
        }

        .tab-bar {
            display: flex;
            gap: 10px;
            overflow-x: auto;
            padding-bottom: 12px;
            scrollbar-width: thin
        }

        .tab-btn {
            background: var(--pale);
            border: 1px solid var(--line);
            color: var(--blue);
            padding: 10px 20px;
            border-radius: 30px;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            white-space: nowrap;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s ease
        }

        .tab-btn:hover {
            background: #e2ecf5;
            border-color: #bcd4e8
        }

        .tab-btn.active {
            background: var(--blue);
            color: #fff;
            border-color: var(--blue)
        }

        /* FORM COMMON */
        .form-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-top: 24px
        }

        .form-full {
            grid-column: 1 / -1
        }

        .form-group {
            display: flex;
            flex-direction: column;
            gap: 6px
        }

        .form-group label {
            font-size: 13.5px;
            font-weight: 700;
            color: var(--blue);
            font-family: 'Montserrat', sans-serif
        }

        .form-control {
            width: 100%;
            padding: 12px 14px;
            border: 1.5px solid var(--line);
            border-radius: 8px;
            font: inherit;
            font-size: 14.5px;
            color: var(--blue);
            background: #fff;
            transition: border-color 0.2s ease, box-shadow 0.2s ease
        }

        .form-control:focus {
            outline: none;
            border-color: var(--green);
            box-shadow: 0 0 0 3px rgba(39,129,50,0.15)
        }

        textarea.form-control {
            resize: vertical;
            min-height: 110px
        }

        /* CTA BANNER */
        .sec-cta {
            padding: 60px 0;
            background: var(--blue);
            color: #fff
        }

        .cta-box {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 30px
        }

        .cta-box h2 {
            font-size: 28px;
            margin: 0 0 8px;
            color: #fff
        }

        .cta-box p {
            margin: 0;
            color: #cbd5e1;
            font-size: 16px
        }

        .cta-actions {
            display: flex;
            gap: 14px;
            flex-shrink: 0
        }

        /* RESPONSIVENESS */
        @media (max-width: 1080px) {
            .footer-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 30px
            }
        }

        @media (max-width: 900px) {
            .top {
                display: none
            }
            .hamb {
                display: flex
            }
            .menu {
                position: fixed;
                top: 0;
                right: -100%;
                width: min(340px, 85vw);
                height: 100vh;
                background: #fff;
                flex-direction: column;
                align-items: stretch;
                gap: 0;
                padding: 0;
                box-shadow: -5px 0 25px rgba(0,0,0,0.2);
                transition: right 0.3s ease;
                z-index: 1000;
                overflow-y: auto
            }
            .nav.open .menu {
                right: 0
            }
            .mobile-menu-head {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 16px 20px;
                border-bottom: 1px solid var(--line);
                background: var(--pale)
            }
            .mobile-menu-head img {
                width: 140px;
                height: auto
            }
            .mobile-close-btn {
                background: none;
                border: 0;
                font-size: 20px;
                color: var(--blue);
                cursor: pointer;
                padding: 4px
            }
            .mobile-nav-links {
                display: flex;
                flex-direction: column;
                padding: 10px 0
            }
            .mobile-nav-links a,
            .mobile-nav-links .nav-group > a {
                padding: 12px 20px;
                font-size: 15px;
                border-bottom: 1px solid #f0f4f8;
                justify-content: space-between
            }
            .nav-drop,
            .nav-drop.services-mega {
                position: static !important;
                opacity: 1 !important;
                visibility: visible !important;
                transform: none !important;
                box-shadow: none !important;
                width: 100% !important;
                display: none;
                background: #f8fafc !important;
                padding: 0 !important;
                border-radius: 0 !important;
                border-top: none !important
            }
            .nav-group.open .nav-drop {
                display: block
            }
            .mega-body {
                grid-template-columns: 1fr !important
            }
            .mega-links-grid {
                grid-template-columns: 1fr !important
            }
            .mega-col {
                padding: 14px 20px !important
            }
            .mega-footer {
                display: none
            }
            .mobile-menu-footer {
                display: flex;
                flex-direction: column;
                gap: 10px;
                padding: 20px;
                margin-top: auto;
                border-top: 1px solid var(--line)
            }
            .nav-overlay {
                display: block;
                position: fixed;
                inset: 0;
                background: rgba(0,0,0,0.5);
                z-index: 999;
                opacity: 0;
                visibility: hidden;
                transition: all 0.3s ease
            }
            .nav.open .nav-overlay {
                opacity: 1;
                visibility: visible
            }
            .sticky-bottom-bar {
                display: flex
            }
            .hero-grid {
                grid-template-columns: 1fr;
                gap: 30px
            }
            .cta-box {
                flex-direction: column;
                text-align: center
            }
            .cta-actions {
                justify-content: center
            }
        }

        @media (max-width: 640px) {
            .hero-stats-card {
                grid-template-columns: 1fr;
                gap: 16px
            }
            .form-grid {
                grid-template-columns: 1fr
            }
            .footer-grid {
                grid-template-columns: 1fr;
                gap: 30px
            }
        }
"""

print("Common base loaded successfully!")
