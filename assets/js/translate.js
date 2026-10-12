/**
 * Sukhda Healthcare - Hindi / English Translation Engine
 * Seamlessly integrates Google Translate Element with high-fidelity Hindi translation.
 * Preserves user language preference across all 46 website pages via localStorage and cookies.
 */

(function () {
    // Cookie management for Google Translate
    function setGoogleTransCookie(lang) {
        var cookieVal = '/en/' + lang;
        var hostname = window.location.hostname;
        var domains = [
            hostname,
            '.' + hostname,
            ''
        ];
        domains.forEach(function (d) {
            var domainStr = d ? '; domain=' + d : '';
            document.cookie = 'googtrans=' + cookieVal + '; path=/' + domainStr;
            document.cookie = 'googtrans=' + cookieVal + '; path=' + window.location.pathname + domainStr;
        });
    }

    function clearGoogleTransCookie() {
        var hostname = window.location.hostname;
        var domains = [hostname, '.' + hostname, ''];
        domains.forEach(function (d) {
            var domainStr = d ? '; domain=' + d : '';
            document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/' + domainStr;
            document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=' + window.location.pathname + domainStr;
        });
    }

    // UI button state synchronization
    function updateLanguageUI(lang) {
        var allButtons = document.querySelectorAll('.lang-btn, .f-btn, .mobile-lang-btn');
        allButtons.forEach(function (btn) {
            if (btn.getAttribute('data-lang') === lang) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
    }

    // Trigger Google Translate dropdown
    function triggerGoogleTranslateCombo(lang) {
        var teCombo = document.querySelector('.goog-te-combo');
        if (teCombo) {
            teCombo.value = lang;
            teCombo.dispatchEvent(new Event('change'));
            return true;
        }
        return false;
    }

    // Global switcher called by UI buttons
    window.switchLanguage = function (lang) {
        var prevLang = localStorage.getItem('sukhda_site_lang') || 'en';
        if (lang === prevLang && !document.querySelector('.goog-te-combo')) {
            return;
        }

        localStorage.setItem('sukhda_site_lang', lang);
        updateLanguageUI(lang);

        if (lang === 'en') {
            clearGoogleTransCookie();
            setGoogleTransCookie('en');
            // If returning to English from Hindi, retrigger combo or reload for crisp reset
            if (prevLang === 'hi') {
                var teCombo = document.querySelector('.goog-te-combo');
                if (teCombo) {
                    teCombo.value = 'en';
                    teCombo.dispatchEvent(new Event('change'));
                    setTimeout(function () {
                        window.location.reload();
                    }, 250);
                } else {
                    window.location.reload();
                }
                return;
            }
        } else {
            setGoogleTransCookie(lang);
        }

        if (!triggerGoogleTranslateCombo(lang)) {
            var pollCount = 0;
            var pollInterval = setInterval(function () {
                pollCount++;
                if (triggerGoogleTranslateCombo(lang) || pollCount > 25) {
                    clearInterval(pollInterval);
                    if (pollCount > 25) {
                        window.location.reload();
                    }
                }
            }, 120);
        }
    };

    // Google Translate Element callback
    window.googleTranslateElementInit = function () {
        if (!document.getElementById('google_translate_element')) {
            var container = document.createElement('div');
            container.id = 'google_translate_element';
            document.body.appendChild(container);
        }

        new google.translate.TranslateElement({
            pageLanguage: 'en',
            includedLanguages: 'en,hi',
            autoDisplay: false
        }, 'google_translate_element');

        var savedLang = localStorage.getItem('sukhda_site_lang');
        if (!savedLang) {
            var m = document.cookie.match(/googtrans=\/en\/([a-z]{2})/i);
            if (m) savedLang = m[1];
        }
        if (!savedLang) savedLang = 'en';

        updateLanguageUI(savedLang);

        if (savedLang === 'hi') {
            var attempts = 0;
            var timer = setInterval(function () {
                attempts++;
                if (triggerGoogleTranslateCombo('hi') || attempts > 35) {
                    clearInterval(timer);
                }
            }, 100);
        }
    };

    // Initialize UI on load
    document.addEventListener('DOMContentLoaded', function () {
        var currentLang = localStorage.getItem('sukhda_site_lang') || 'en';
        updateLanguageUI(currentLang);
        if (window.lucide) {
            lucide.createIcons();
        }

        // Dropdown click & hover support for desktop & mobile
        var navGroups = document.querySelectorAll('.nav-group');
        navGroups.forEach(function (group) {
            var parentLink = group.querySelector(':scope > a');
            if (!parentLink) return;
            parentLink.addEventListener('click', function (e) {
                var href = parentLink.getAttribute('href');
                if (href === 'javascript:void(0)' || href === '#' || href === '#resources') {
                    e.preventDefault();
                    e.stopPropagation();
                    var isOpen = group.classList.contains('open');
                    navGroups.forEach(function (g) { if (g !== group) g.classList.remove('open'); });
                    group.classList.toggle('open', !isOpen);
                }
            });
        });

        document.addEventListener('click', function (e) {
            if (!e.target.closest('.nav-group')) {
                document.querySelectorAll('.nav-group.open').forEach(function (g) {
                    g.classList.remove('open');
                });
            }
        });

        // Mobile Menu Drawer Handler
        var nav = document.querySelector('.nav');
        var hambBtn = document.querySelector('.hamb');
        var closeBtn = document.querySelector('.mobile-close-btn');
        var overlay = document.querySelector('.nav-overlay');
        var menu = document.querySelector('.menu');

        if (nav && hambBtn && menu) {
            menu.id = menu.id || 'mobile-menu';
            hambBtn.type = 'button';
            hambBtn.setAttribute('aria-controls', menu.id);
            hambBtn.setAttribute('aria-expanded', 'false');
            hambBtn.setAttribute('aria-label', 'Open menu');

            var closeNav = function () {
                nav.classList.remove('open');
                document.body.style.overflow = '';
                hambBtn.setAttribute('aria-expanded', 'false');
                hambBtn.setAttribute('aria-label', 'Open menu');
            };
            var openNav = function () {
                nav.classList.add('open');
                document.body.style.overflow = 'hidden';
                hambBtn.setAttribute('aria-expanded', 'true');
                hambBtn.setAttribute('aria-label', 'Close menu');
            };

            hambBtn.onclick = function (e) {
                e.preventDefault();
                e.stopPropagation();
                nav.classList.contains('open') ? closeNav() : openNav();
            };
            if (closeBtn) closeBtn.onclick = function (e) { e.preventDefault(); closeNav(); };
            if (overlay) overlay.onclick = function (e) { e.preventDefault(); closeNav(); };

            document.addEventListener('keydown', function (e) {
                if (e.key === 'Escape') closeNav();
            });
        }
    });
})();
