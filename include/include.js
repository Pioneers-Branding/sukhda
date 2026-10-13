/**
 * Sukhda Healthcare - Dynamic Include Engine
 * Dynamically loads and synchronizes shared Header & Footer across all pages.
 * Handles active navigation state, mobile drawer, dropdowns, and Lucide icon rendering.
 */

(function () {
    // Current page filename e.g. "about.html" or "csr.html"
    function getCurrentPage() {
        var path = window.location.pathname;
        var page = path.split('/').pop().split('#')[0].split('?')[0];
        return page || 'index.html';
    }

    // Render Lucide icons safely
    function renderIcons() {
        if (window.lucide && typeof window.lucide.createIcons === 'function') {
            window.lucide.createIcons({ attrs: { 'stroke-width': 1.8 } });
        }
    }

    // Attach Mobile Drawer & Dropdown Events
    function initHeaderInteractions() {
        var nav = document.querySelector('.nav');
        var hambBtn = document.querySelector('.hamb');
        var closeBtn = document.querySelector('.mobile-close-btn');
        var overlay = document.querySelector('.nav-overlay');
        var menu = document.querySelector('.menu');

        if (!nav || !menu) return;

        function closeMenu() {
            nav.classList.remove('open');
            document.body.style.overflow = '';
            if (hambBtn) {
                hambBtn.setAttribute('aria-expanded', 'false');
                hambBtn.blur();
            }
        }

        function openMenu() {
            nav.classList.add('open');
            document.body.style.overflow = 'hidden';
            if (hambBtn) {
                hambBtn.setAttribute('aria-expanded', 'true');
            }
        }

        if (hambBtn) {
            hambBtn.onclick = function (e) {
                e.preventDefault();
                e.stopPropagation();
                if (nav.classList.contains('open')) {
                    closeMenu();
                } else {
                    openMenu();
                }
            };
        }

        if (closeBtn) {
            closeBtn.onclick = function (e) {
                e.preventDefault();
                closeMenu();
            };
        }

        if (overlay) {
            overlay.onclick = function (e) {
                e.preventDefault();
                closeMenu();
            };
        }

        // Mobile dropdown accordion toggles
        var navGroups = menu.querySelectorAll('.nav-group');
        navGroups.forEach(function (group) {
            var parentLink = group.querySelector(':scope > a');
            if (!parentLink) return;

            parentLink.onclick = function (e) {
                if (window.innerWidth <= 900) {
                    var href = parentLink.getAttribute('href') || '';
                    if (href === 'javascript:void(0)' || href.startsWith('#') || href.includes('#')) {
                        e.preventDefault();
                        e.stopPropagation();
                        var isOpen = group.classList.contains('open');
                        navGroups.forEach(function (g) {
                            if (g !== group) g.classList.remove('open');
                        });
                        group.classList.toggle('open', !isOpen);
                    }
                }
            };
        });

        // Close menu on clicking links that navigate away
        menu.onclick = function (e) {
            var link = e.target.closest('a');
            if (!link) return;
            var href = link.getAttribute('href') || '';
            if (href !== 'javascript:void(0)' && !href.startsWith('#')) {
                closeMenu();
            }
        };

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') closeMenu();
        });

        // Highlight Active Page in Navigation
        highlightActiveLink(menu);

        // Sync Language UI state
        if (typeof window.syncLanguageUI === 'function') {
            window.syncLanguageUI();
        } else {
            var savedLang = localStorage.getItem('sukhda_site_lang') || 'en';
            document.querySelectorAll('.lang-btn, .mobile-lang-btn, .f-btn').forEach(function (btn) {
                if (btn.getAttribute('data-lang') === savedLang) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });
        }

        renderIcons();
    }

    // Ensure no links are highlighted
    function highlightActiveLink(menu) {
        if (!menu) return;
        var links = menu.querySelectorAll('.mobile-nav-links a, .nav a, a.on');
        links.forEach(function (a) {
            a.classList.remove('on');
        });
    }


    // Load include snippet via fetch (or fallback to existing static content)
    function loadSnippet(selector, file, onDone) {
        var container = document.querySelector(selector);
        if (!container) return;

        fetch(file)
            .then(function (response) {
                if (!response.ok) throw new Error('Could not fetch ' + file);
                return response.text();
            })
            .then(function (html) {
                container.innerHTML = html;
                if (onDone) onDone();
            })
            .catch(function (err) {
                // If fetch fails (e.g. file:/// protocol), initialize with static fallback
                if (onDone) onDone();
            });
    }

    // Initialize when DOM is ready
    function init() {
        var hasHeaderContainer = document.querySelector('#site-header, [data-include="header"]');
        var hasFooterContainer = document.querySelector('#site-footer, [data-include="footer"]');

        if (hasHeaderContainer) {
            loadSnippet('#site-header, [data-include="header"]', 'include/header.html', function () {
                initHeaderInteractions();
            });
        } else {
            initHeaderInteractions();
        }

        if (hasFooterContainer) {
            loadSnippet('#site-footer, [data-include="footer"]', 'include/footer.html', function () {
                renderIcons();
            });
        } else {
            renderIcons();
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
