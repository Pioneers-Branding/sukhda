/**
 * Sukhda Healthcare - Site Search
 * Adds a search icon to the main header and a search panel with:
 *  - free-text search across specialities, doctors and key pages
 *  - "Search by Hospital" filter (All / Multispeciality / MedPark)
 *  - full list of specialities shown before the visitor types
 * Loaded on every page by include/include.js. Self-contained (own CSS + data).
 */
(function () {
    if (window.__sukhdaSearchLoaded) return;
    window.__sukhdaSearchLoaded = true;

    var MULTI = 'multispeciality', MEDPARK = 'medpark', BOTH = 'both';
    var HOSPITAL_LABEL = {};
    HOSPITAL_LABEL[MULTI] = 'Sukhda Multispeciality Hospital';
    HOSPITAL_LABEL[MEDPARK] = 'Sukhda MedPark (Cancer & Super-Speciality)';
    HOSPITAL_LABEL[BOTH] = 'Both Hospitals';

    // ---------- DATA ----------
    // k = extra keywords people may type (symptoms, procedures, Hindi-English terms)
    var SPECIALITIES = [
        { n: 'Critical Care & ICU', u: 'critical-care.html', h: BOTH, k: 'icu intensive care ventilator' },
        { n: 'Internal Medicine (DNB Centre)', u: 'internal-medicine.html', h: MULTI, k: 'physician fever diabetes bp general medicine' },
        { n: 'Interventional Cardiology', u: 'cardiology.html', h: MULTI, k: 'heart cath lab angioplasty angiography stent chest pain' },
        { n: 'Nephrology & Dialysis', u: 'nephrology.html', h: MULTI, k: 'kidney dialysis renal' },
        { n: 'Gastroenterology & Hepatology', u: 'gastroenterology.html', h: MULTI, k: 'stomach liver endoscopy colonoscopy digestive' },
        { n: 'Urology & Endourology', u: 'urology.html', h: BOTH, k: 'kidney stone prostate urine bladder' },
        { n: '24/7 Emergency & Trauma Care', u: 'emergency-trauma.html', h: MULTI, k: 'emergency accident trauma casualty ambulance' },
        { n: 'Robotic Joint Replacement & Orthopaedics', u: 'orthopaedics.html', h: MULTI, k: 'bone knee hip joint fracture ortho arthroscopy' },
        { n: 'General & Laparoscopic Surgery', u: 'general-surgery.html', h: MULTI, k: 'surgery hernia gallbladder appendix laparoscopy' },
        { n: 'Advanced Laparoscopy & Bariatric Surgery', u: 'bariatric-surgery.html', h: MULTI, k: 'weight loss obesity bariatric' },
        { n: 'Gynaecology & Obstetrics', u: 'gynaecology.html', h: MULTI, k: 'pregnancy delivery women maternity ivf' },
        { n: 'ENT (Ear, Nose & Throat)', u: 'ent.html', h: MULTI, k: 'ear nose throat sinus hearing tonsil' },
        { n: 'Anaesthesiology & Pain Management', u: 'anaesthesiology.html', h: BOTH, k: 'anaesthesia anesthesia pain palliative' },
        { n: 'CT Scan & Radiology', u: 'radiology.html', h: BOTH, k: 'ct scan mri x-ray xray ultrasound mammography imaging diagnostics' },
        { n: 'Physiotherapy & Rehabilitation', u: 'physiotherapy.html', h: MULTI, k: 'physio rehab neuro physiotherapy' },
        { n: 'Paediatrics & Neonatology', u: 'paediatrics.html', h: MULTI, k: 'child children baby nicu pediatrics' },
        { n: 'Dermatology & Cosmetology', u: 'dermatology.html', h: MULTI, k: 'skin hair cosmetic' },
        { n: 'Psychiatry & Rehabilitation', u: 'psychiatry.html', h: MULTI, k: 'mental health depression anxiety de-addiction' },
        { n: 'Medical Oncology (Chemo & Daycare)', u: 'medical-oncology.html', h: MEDPARK, k: 'cancer chemotherapy immunotherapy oncology' },
        { n: 'Surgical Oncology', u: 'surgical-oncology.html', h: MEDPARK, k: 'cancer surgery tumour tumor oncology' },
        { n: 'Radiation Oncology (LINAC)', u: 'radiation-oncology.html', h: MEDPARK, k: 'cancer radiation radiotherapy linac oncology' },
        { n: 'Neurosurgery & Spine', u: 'neurosurgery.html', h: BOTH, k: 'brain spine neuro surgery' }
    ];

    var DOCTORS = [
        { n: 'Dr. Amit Mehta', s: 'Director & Head - Internal Medicine & Critical Care', u: 'dr-amit-mehta.html', h: BOTH },
        { n: 'Dr. Manisha Mehta', s: 'Director - Healthcare Quality', u: 'dr-manisha-mehta.html', h: MULTI },
        { n: 'Dr. Hemant Dahiya', s: 'Consultant Physician - Internal Medicine', u: 'dr-hemant-dahiya.html', h: MULTI },
        { n: 'Dr. Trivikrama Rao', s: 'Consultant - Medical Oncology', u: 'dr-trivikrama-rao.html', h: BOTH },
        { n: 'Dr. Amit Kumar Garg', s: 'Consultant Surgical Oncologist', u: 'dr-amit-kumar-garg.html', h: BOTH },
        { n: 'Dr. Ankur Kamra', s: 'HOD - Interventional Cardiology', u: 'dr-ankur-kamra.html', h: MULTI },
        { n: 'Dr. Bharath', s: 'HOD - Gastroenterology, Hepatology & Endoscopy', u: 'dr-bharath.html', h: MULTI },
        { n: 'Dr. Anil Khyalia', s: 'Consultant Neurosurgeon (Brain & Spine)', u: 'dr-anil-khyalia.html', h: BOTH },
        { n: 'Dr. Nidhi Mehta', s: 'Senior Obstetrician & Gynaecologist', u: 'dr-nidhi-mehta.html', h: MULTI },
        { n: 'Dr. Pankaj Sharma', s: 'Joint Replacement, Arthroscopy & Sports Injury', u: 'dr-pankaj-sharma.html', h: MULTI },
        { n: 'Dr. Deepti Singh', s: 'HOD - ENT (Otorhinolaryngology)', u: 'dr-deepti-singh.html', h: MULTI },
        { n: 'Dr. Anil Bansal', s: 'HOD - Radiology', u: 'dr-anil-bansal.html', h: MULTI },
        { n: 'Dr. Deepam Das', s: 'HOD - Laparoscopic & Bariatric Surgery', u: 'dr-deepam-das.html', h: MULTI },
        { n: 'Dr. Devilal', s: 'Anaesthesiology & Pain Management', u: 'dr-devilal.html', h: MULTI },
        { n: 'Dr. Parveen', s: 'Anaesthesiologist & Critical Care Intensivist', u: 'dr-parveen.html', h: MULTI },
        { n: 'Dr. Sanjeet Sahu', s: 'Consultant Neuro-Physiotherapist', u: 'dr-sanjeet-sahu.html', h: MULTI },
        { n: 'Dr. Megha Gupta', s: 'Consultant Dermatologist & Cosmetologist', u: 'dr-megha-gupta.html', h: MULTI },
        { n: 'Dr. Shubham Mehta', s: 'Consultant Psychiatrist & De-addiction Specialist', u: 'dr-shubham-mehta.html', h: MULTI }
    ];

    var PAGES = [
        { n: 'Sukhda Multispeciality Hospital', s: 'Opposite Green Belt, Delhi Road, Hisar', u: 'sukhda-multispecialty-hospital.html', h: MULTI, k: 'hospital nabh delhi road' },
        { n: 'Sukhda MedPark (Cancer & Super-Speciality)', s: 'NH 1P-4P, Sector-5, Hisar', u: 'sukhda-medpark-hospital.html', h: MEDPARK, k: 'hospital cancer sector 5 tumour board' },
        { n: 'Find a Doctor', s: 'All consultants & specialists', u: 'doctor.html', h: BOTH, k: 'doctors consultant specialist' },
        { n: 'OPD Schedule', s: 'Doctor timings & availability', u: 'opd-schedule.html', h: BOTH, k: 'opd timing timings schedule' },
        { n: 'Book Appointment / Contact', s: 'Call, WhatsApp or visit us', u: 'contact.html', h: BOTH, k: 'appointment contact phone address directions' },
        { n: 'Cashless / TPA & Empanelment', s: 'Insurance, Ayushman Bharat, ECHS', u: 'empanelled-corporate.html', h: BOTH, k: 'cashless tpa insurance ayushman echs cghs panel' },
        { n: 'About Sukhda', s: 'Our story, leadership & vision', u: 'about.html', h: BOTH, k: 'about history founder' },
        { n: 'Careers', s: 'Jobs at Sukhda Healthcare', u: 'careers.html', h: BOTH, k: 'job jobs career vacancy' },
        { n: 'Media Coverage', s: 'News & press', u: 'media-coverage.html', h: BOTH, k: 'media news press' },
        { n: 'CSR', s: 'Community initiatives', u: 'csr.html', h: BOTH, k: 'csr camp community' }
    ];

    // ---------- HELPERS ----------
    function esc(s) {
        return String(s).replace(/[&<>"]/g, function (c) {
            return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
        });
    }
    function norm(s) { return String(s || '').toLowerCase().replace(/&/g, ' and ').replace(/[^a-z0-9\s]/g, ' ').replace(/\s+/g, ' ').trim(); }
    function inHospital(item, filter) { return filter === 'all' || item.h === BOTH || item.h === filter; }
    function score(item, terms) {
        var name = norm(item.n), hay = norm([item.n, item.s, item.k].join(' '));
        var total = 0;
        for (var i = 0; i < terms.length; i++) {
            var t = terms[i];
            if (hay.indexOf(t) === -1) return 0;            // every word must match
            if (name.indexOf(t) === 0) total += 5;
            else if (name.indexOf(' ' + t) !== -1) total += 3;
            else if (name.indexOf(t) !== -1) total += 2;
            else total += 1;
        }
        return total;
    }
    function rank(list, terms, filter) {
        return list.filter(function (it) { return inHospital(it, filter); })
            .map(function (it) { return { it: it, sc: score(it, terms) }; })
            .filter(function (r) { return r.sc > 0; })
            .sort(function (a, b) { return b.sc - a.sc; })
            .map(function (r) { return r.it; });
    }

    var ICON_SEARCH = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>';
    var ICON = {
        spec: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.8 2.3A.3.3 0 1 0 5 2H4a2 2 0 0 0-2 2v5a6 6 0 0 0 6 6 6 6 0 0 0 6-6V4a2 2 0 0 0-2-2h-1a.2.2 0 1 0 .3.3"/><path d="M8 15v1a6 6 0 0 0 6 6 6 6 0 0 0 6-6v-4"/><circle cx="20" cy="10" r="2"/></svg>',
        doc: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21v-1a7 7 0 0 1 16 0v1"/></svg>',
        page: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21h18M5 21V7l7-4 7 4v14M10 9h4M12 7v4M9 21v-5h6v5"/></svg>'
    };

    // ---------- STYLES ----------
    var CSS = '' +
        '.ss-trigger{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:44px;min-width:44px;padding:0 14px;margin-right:12px;border:1px solid #c9d6ea;border-radius:10px;background:#fff;color:#052159;font:inherit;font-size:15px;font-weight:600;cursor:pointer;transition:border-color .2s,box-shadow .2s,color .2s;flex-shrink:0}' +
        '.ss-trigger:hover,.ss-trigger:focus-visible{border-color:#278132;color:#278132;box-shadow:0 0 0 3px rgba(39,129,50,.12);outline:none}' +
        '.ss-trigger .ss-trigger-label{white-space:nowrap}' +
        '@media(max-width:1180px){.ss-trigger .ss-trigger-label{display:none}.ss-trigger{padding:0}}' +
        '@media(max-width:900px){.ss-trigger{margin-right:8px;margin-left:auto;height:40px;min-width:40px}}' +
        '.ss-overlay{position:fixed;inset:0;z-index:100000;background:rgba(2,22,61,.55);backdrop-filter:blur(3px);display:none;align-items:flex-start;justify-content:center;padding:70px 16px 16px}' +
        '.ss-overlay.open{display:flex}' +
        '.ss-panel{width:min(820px,100%);max-height:calc(100vh - 100px);display:flex;flex-direction:column;background:#fff;border-radius:16px;box-shadow:0 24px 60px rgba(2,22,61,.35);overflow:hidden;color:#1d2b45;font-size:15px}' +
        '.ss-head{padding:18px 20px 14px;border-bottom:1px solid #e3eaf3}' +
        '.ss-input-row{display:flex;align-items:center;gap:10px;border:2px solid #d5e0ee;border-radius:12px;padding:0 12px;transition:border-color .2s}' +
        '.ss-input-row:focus-within{border-color:#278132}' +
        '.ss-input-row svg{color:#6a7a93;flex-shrink:0}' +
        '.ss-input{flex:1;min-width:0;border:0;outline:0;font:inherit;font-size:17px;padding:13px 0;color:#052159;background:transparent}' +
        '.ss-input::-webkit-search-cancel-button{-webkit-appearance:none;display:none}' +
        '.ss-close{border:0;background:#eef3fb;color:#052159;border-radius:8px;width:34px;height:34px;font-size:16px;cursor:pointer;flex-shrink:0}' +
        '.ss-close:hover{background:#dfe8f5}' +
        '.ss-filter-label{margin:14px 0 8px;font-size:12px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;color:#6a7a93}' +
        '.ss-tabs{display:flex;flex-wrap:wrap;gap:8px}' +
        '.ss-tab{border:1px solid #c9d6ea;background:#fff;color:#052159;border-radius:999px;padding:7px 14px;font:inherit;font-size:13.5px;font-weight:600;cursor:pointer}' +
        '.ss-tab:hover{border-color:#052159}' +
        '.ss-tab.active{background:#052159;border-color:#052159;color:#fff}' +
        '.ss-body{overflow-y:auto;padding:8px 20px 20px;overscroll-behavior:contain}' +
        '.ss-group-title{margin:16px 0 8px;font-size:12px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;color:#278132}' +
        '.ss-list{list-style:none;margin:0;padding:0;display:grid;gap:6px}' +
        '.ss-list.cols{grid-template-columns:repeat(2,minmax(0,1fr))}' +
        '.ss-item a{display:flex;align-items:center;gap:12px;padding:10px 12px;border:1px solid #e3eaf3;border-radius:10px;color:#052159;text-decoration:none;background:#fff;transition:background .15s,border-color .15s}' +
        '.ss-item a:hover,.ss-item a.ss-active{background:#f2f7f3;border-color:#278132}' +
        '.ss-ico{width:34px;height:34px;border-radius:8px;background:#eaf5ec;color:#278132;display:flex;align-items:center;justify-content:center;flex-shrink:0}' +
        '.ss-txt{min-width:0;display:flex;flex-direction:column}' +
        '.ss-txt b{font-weight:700;font-size:14.5px;line-height:1.3}' +
        '.ss-txt small{color:#6a7a93;font-size:12.5px;line-height:1.35;margin-top:2px}' +
        '.ss-badge{margin-left:auto;flex-shrink:0;font-size:11px;font-weight:700;padding:3px 8px;border-radius:6px;background:#eef3fb;color:#052159;white-space:nowrap}' +
        '.ss-badge.medpark{background:#fdf0f5;color:#9b1f55}' +
        '.ss-empty{padding:28px 8px;text-align:center;color:#6a7a93}' +
        '.ss-empty a{color:#278132;font-weight:700}' +
        '.ss-hint{padding:10px 20px;border-top:1px solid #e3eaf3;font-size:12.5px;color:#6a7a93;display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap}' +
        '.ss-hint kbd{border:1px solid #c9d6ea;border-bottom-width:2px;border-radius:4px;padding:0 5px;font-size:11px;background:#f7f9fc}' +
        '@media(max-width:640px){.ss-overlay{padding:0}.ss-panel{max-height:100vh;height:100%;border-radius:0}.ss-list.cols{grid-template-columns:1fr}.ss-badge{display:none}.ss-hint{display:none}}' +
        'body.ss-lock{overflow:hidden}';

    // ---------- UI ----------
    var overlay, input, body, filter = 'all', activeIdx = -1, lastFocus = null;

    function badge(h) {
        if (h === BOTH) return '<span class="ss-badge">Both Hospitals</span>';
        if (h === MEDPARK) return '<span class="ss-badge medpark">MedPark</span>';
        return '<span class="ss-badge">Multispeciality</span>';
    }
    function itemHtml(it, kind) {
        var sub = it.s || HOSPITAL_LABEL[it.h];
        return '<li class="ss-item"><a href="' + esc(it.u) + '">' +
            '<span class="ss-ico">' + ICON[kind] + '</span>' +
            '<span class="ss-txt"><b>' + esc(it.n) + '</b><small>' + esc(sub) + '</small></span>' +
            badge(it.h) + '</a></li>';
    }
    function group(title, items, kind, cols) {
        if (!items.length) return '';
        return '<div class="ss-group-title">' + esc(title) + ' (' + items.length + ')</div>' +
            '<ul class="ss-list' + (cols ? ' cols' : '') + '">' + items.map(function (it) { return itemHtml(it, kind); }).join('') + '</ul>';
    }

    function render() {
        var q = norm(input.value);
        var html;
        if (!q) {
            var specs = SPECIALITIES.filter(function (s) { return inHospital(s, filter); });
            var hosp = PAGES.filter(function (p) { return (p.u.indexOf('sukhda-') === 0) && inHospital(p, filter); });
            html = group(filter === 'all' ? 'All Specialities' : 'Specialities at ' + HOSPITAL_LABEL[filter], specs, 'spec', true) +
                group(filter === 'all' ? 'Our Hospitals' : 'Hospital', hosp, 'page', true);
        } else {
            var terms = q.split(' ');
            var s = rank(SPECIALITIES, terms, filter), d = rank(DOCTORS, terms, filter), p = rank(PAGES, terms, filter);
            html = group('Specialities', s, 'spec') + group('Doctors', d, 'doc') + group('Hospitals & Pages', p, 'page');
            if (!html) {
                html = '<div class="ss-empty">No results for "<b>' + esc(input.value.trim()) + '</b>"' +
                    (filter !== 'all' ? ' at ' + esc(HOSPITAL_LABEL[filter]) + '. <a href="#" data-ss-all>Search both hospitals</a>' : '.') +
                    '<br><br>Need help? Call <a href="tel:01662249473">01662-249473</a> or <a href="contact.html">contact us</a>.</div>';
            }
        }
        body.innerHTML = html;
        body.scrollTop = 0;
        activeIdx = -1;
    }

    function links() { return body.querySelectorAll('.ss-item a'); }
    function setActive(i) {
        var l = links();
        if (!l.length) return;
        activeIdx = (i + l.length) % l.length;
        for (var j = 0; j < l.length; j++) l[j].classList.toggle('ss-active', j === activeIdx);
        l[activeIdx].scrollIntoView({ block: 'nearest' });
    }

    function open() {
        if (!overlay) build();
        lastFocus = document.activeElement;
        overlay.classList.add('open');
        document.body.classList.add('ss-lock');
        render();
        setTimeout(function () { input.focus(); }, 30);
    }
    function close() {
        if (!overlay) return;
        overlay.classList.remove('open');
        document.body.classList.remove('ss-lock');
        if (lastFocus && lastFocus.focus) lastFocus.focus();
    }

    function build() {
        var st = document.createElement('style');
        st.textContent = CSS;
        document.head.appendChild(st);

        overlay = document.createElement('div');
        overlay.className = 'ss-overlay';
        overlay.setAttribute('role', 'dialog');
        overlay.setAttribute('aria-modal', 'true');
        overlay.setAttribute('aria-label', 'Search Sukhda Healthcare');
        overlay.innerHTML =
            '<div class="ss-panel">' +
            '<div class="ss-head">' +
            '<div class="ss-input-row">' + ICON_SEARCH +
            '<input class="ss-input" type="search" autocomplete="off" placeholder="Search specialities, doctors, treatments…" aria-label="Search">' +
            '<button type="button" class="ss-close" aria-label="Close search">✕</button></div>' +
            '<div class="ss-filter-label">Search by Hospital</div>' +
            '<div class="ss-tabs" role="tablist">' +
            '<button type="button" class="ss-tab active" data-h="all">All Hospitals</button>' +
            '<button type="button" class="ss-tab" data-h="' + MULTI + '">Sukhda Multispeciality Hospital</button>' +
            '<button type="button" class="ss-tab" data-h="' + MEDPARK + '">Sukhda MedPark (Cancer)</button>' +
            '</div></div>' +
            '<div class="ss-body"></div>' +
            '<div class="ss-hint"><span><kbd>↑</kbd> <kbd>↓</kbd> to navigate &nbsp; <kbd>Enter</kbd> to open &nbsp; <kbd>Esc</kbd> to close</span><span>24/7 Emergency: <b>01662-249473</b></span></div>' +
            '</div>';
        document.body.appendChild(overlay);

        input = overlay.querySelector('.ss-input');
        body = overlay.querySelector('.ss-body');

        input.addEventListener('input', render);
        overlay.querySelector('.ss-close').addEventListener('click', close);
        overlay.addEventListener('click', function (e) {
            if (e.target === overlay) close();
            var all = e.target.closest('[data-ss-all]');
            if (all) { e.preventDefault(); setFilter('all'); }
        });
        Array.prototype.forEach.call(overlay.querySelectorAll('.ss-tab'), function (t) {
            t.addEventListener('click', function () { setFilter(t.getAttribute('data-h')); input.focus(); });
        });
        overlay.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') { e.preventDefault(); close(); }
            else if (e.key === 'ArrowDown') { e.preventDefault(); setActive(activeIdx + 1); }
            else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(activeIdx - 1); }
            else if (e.key === 'Enter' && e.target === input) {
                var l = links();
                var target = l[activeIdx >= 0 ? activeIdx : 0];
                if (target) { e.preventDefault(); window.location.href = target.getAttribute('href'); }
            }
        });
    }

    function setFilter(h) {
        filter = h;
        Array.prototype.forEach.call(overlay.querySelectorAll('.ss-tab'), function (t) {
            t.classList.toggle('active', t.getAttribute('data-h') === h);
        });
        render();
    }

    function addTrigger() {
        var wrap = document.querySelector('header.nav > .wrap');
        if (!wrap || wrap.querySelector('.ss-trigger')) return;
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'ss-trigger';
        btn.setAttribute('aria-label', 'Search specialities, doctors and hospitals');
        btn.setAttribute('title', 'Search (Ctrl + K)');
        btn.innerHTML = ICON_SEARCH + '<span class="ss-trigger-label">Search</span>';
        btn.addEventListener('click', open);
        // Place it just before the header "Book Appointment" button (or the menu toggle)
        var anchor = wrap.querySelector(':scope > a.btn') || wrap.querySelector(':scope > .hamb');
        if (anchor) wrap.insertBefore(btn, anchor); else wrap.appendChild(btn);
        if (!document.getElementById('ss-style-trigger')) {
            var st = document.createElement('style');
            st.id = 'ss-style-trigger';
            st.textContent = CSS.split('.ss-overlay')[0]; // trigger styles only, rest added on first open
            document.head.appendChild(st);
        }
    }

    document.addEventListener('keydown', function (e) {
        var tag = (e.target && e.target.tagName) || '';
        var typing = /INPUT|TEXTAREA|SELECT/.test(tag) || (e.target && e.target.isContentEditable);
        if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) { e.preventDefault(); open(); }
        else if (e.key === '/' && !typing && !(overlay && overlay.classList.contains('open'))) { e.preventDefault(); open(); }
    });

    window.SukhdaSearch = { open: open, close: close };

    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', addTrigger);
    else addTrigger();
})();
