/**
 * Sukhda Healthcare - Hindi / English Translation Engine
 * Seamlessly integrates Google Translate Element with high-fidelity Hindi translation.
 * Preserves user language preference across all 46 website pages via localStorage and cookies.
 */

(function () {
    // Robust Cookie management for Google Translate across all domains and paths
    function getDomainList() {
        var host = window.location.hostname;
        var domains = [''];
        if (host && host !== 'localhost' && !/^[0-9.]+$/.test(host)) {
            domains.push(host);
            var parts = host.split('.');
            if (parts.length >= 2) {
                var rootDomain = parts.slice(-2).join('.');
                domains.push('.' + rootDomain);
                domains.push('.' + host);
            }
        }
        return domains;
    }

    function setGoogleTransCookie(lang) {
        var cookieVal = '/en/' + lang;
        var domains = getDomainList();
        domains.forEach(function (d) {
            var domainStr = d ? '; domain=' + d : '';
            document.cookie = 'googtrans=' + cookieVal + '; path=/; max-age=31536000; SameSite=Lax' + domainStr;
            document.cookie = 'googtrans=' + cookieVal + '; path=/; expires=Fri, 31 Dec 2030 23:59:59 GMT' + domainStr;
        });
    }

    function clearGoogleTransCookie() {
        var domains = getDomainList();
        var paths = ['/', window.location.pathname];
        domains.forEach(function (d) {
            var domainStr = d ? '; domain=' + d : '';
            paths.forEach(function (p) {
                document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=' + p + domainStr;
            });
        });
    }

    // Immediately synchronize cookies based on localStorage upon script load
    (function syncInitialCookie() {
        var current = localStorage.getItem('sukhda_site_lang') || 'en';
        if (current === 'hi') {
            setGoogleTransCookie('hi');
        } else {
            clearGoogleTransCookie();
            setGoogleTransCookie('en');
        }
    })();

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
    window.syncLanguageUI = function () {
        var lang = localStorage.getItem('sukhda_site_lang') || 'en';
        updateLanguageUI(lang);
    };

    // Trigger Google Translate dropdown
    function triggerGoogleTranslateCombo(lang) {
        var teCombo = document.querySelector('.goog-te-combo');
        if (!teCombo) return false;

        // Ensure options have been populated by Google Translate
        var targetOption = teCombo.querySelector('option[value="' + lang + '"]');
        if (!targetOption && teCombo.options.length <= 1) {
            return false;
        }

        if (teCombo.value !== lang) {
            teCombo.value = lang;
            teCombo.dispatchEvent(new Event('change', { bubbles: true, cancelable: true }));
            teCombo.dispatchEvent(new Event('input', { bubbles: true, cancelable: true }));
            if (typeof teCombo.onchange === 'function') {
                teCombo.onchange();
            }
        }
        return teCombo.value === lang;
    }

    // Global switcher called by UI buttons
    window.switchLanguage = function (lang) {
        var prevLang = localStorage.getItem('sukhda_site_lang') || 'en';
        localStorage.setItem('sukhda_site_lang', lang);
        updateLanguageUI(lang);

        if (lang === 'en') {
            clearGoogleTransCookie();
            setGoogleTransCookie('en');
            var teComboEn = document.querySelector('.goog-te-combo');
            if (teComboEn) {
                teComboEn.value = 'en';
                teComboEn.dispatchEvent(new Event('change', { bubbles: true, cancelable: true }));
            }
            if (prevLang === 'hi') {
                setTimeout(function () {
                    window.location.reload();
                }, 200);
            }
            return;
        }

        // Switching to Hindi
        setGoogleTransCookie('hi');
        if (!triggerGoogleTranslateCombo('hi')) {
            var pollCount = 0;
            var pollInterval = setInterval(function () {
                pollCount++;
                var comboReady = triggerGoogleTranslateCombo('hi');
                var isTranslated = document.documentElement.classList.contains('translated-ltr') ||
                                   document.documentElement.classList.contains('translated-rtl');
                if ((comboReady && isTranslated) || pollCount > 30) {
                    clearInterval(pollInterval);
                    if (!isTranslated && pollCount > 30) {
                        window.location.reload();
                    }
                }
            }, 100);
        }
    };

    // Auto-translation observer / checker
    function ensureAutoTranslate(targetLang) {
        if (targetLang !== 'hi') return;

        var attempts = 0;
        var maxAttempts = 80; // 8 seconds of verification
        var autoTimer = setInterval(function () {
            attempts++;
            var isTranslated = document.documentElement.classList.contains('translated-ltr') ||
                               document.documentElement.classList.contains('translated-rtl') ||
                               !!document.querySelector('font');

            var comboSuccess = triggerGoogleTranslateCombo('hi');

            if (isTranslated || attempts >= maxAttempts) {
                clearInterval(autoTimer);
            }
        }, 100);
    }

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

        var savedLang = localStorage.getItem('sukhda_site_lang') || 'en';
        updateLanguageUI(savedLang);

        if (savedLang === 'hi') {
            setGoogleTransCookie('hi');
            ensureAutoTranslate('hi');
        } else {
            clearGoogleTransCookie();
            setGoogleTransCookie('en');
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
