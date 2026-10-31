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
            var parentLink = group.querySelector(':scope > a') || group.querySelector('a');
            var dropdown = group.querySelector('.nav-drop, .services-mega');
            if (!parentLink || !dropdown) return;

            parentLink.onclick = function (e) {
                if (window.innerWidth <= 900) {
                    e.preventDefault();
                    e.stopPropagation();
                    var isOpen = group.classList.contains('open');
                    navGroups.forEach(function (g) {
                        if (g !== group) g.classList.remove('open');
                    });
                    group.classList.toggle('open', !isOpen);
                } else {
                    e.preventDefault();
                }
            };
        });

        // Close menu on clicking links that navigate away
        menu.onclick = function (e) {
            var link = e.target.closest('a');
            if (!link) return;

            // Never close drawer if clicking an accordion parent toggle
            if (link.matches('.nav-group > a') || (link.parentElement && link.parentElement.classList.contains('nav-group') && link.parentElement.querySelector('.nav-drop, .services-mega'))) {
                return;
            }

            // Normal destination links close the menu
            var href = link.getAttribute('href') || '';
            if (href && href !== 'javascript:void(0)' && !href.startsWith('#')) {
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

    // "Read More / Read Less" for long paragraphs in page content
    function initReadMore() {
        var MIN_CHARS = 400;
        var SKIP = 'header, footer, nav, .nav, .top, .footer-disclaimers, .faq-item, table, .cta-banner, .no-read-more, [data-no-read-more]';
        var paras = document.querySelectorAll('main p, section p, article p');

        Array.prototype.forEach.call(paras, function (p) {
            if (p.closest(SKIP) || p.classList.contains('rm-text')) return;
            if (p.textContent.replace(/\s+/g, ' ').trim().length < MIN_CHARS) return;

            p.classList.add('rm-text', 'rm-collapsed');
            // Visible and already fits in the clamped height: nothing to hide
            if (p.offsetParent !== null && p.scrollHeight <= p.clientHeight + 2) {
                p.classList.remove('rm-text', 'rm-collapsed');
                return;
            }

            var btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'rm-toggle';
            btn.setAttribute('aria-expanded', 'false');
            btn.innerHTML = '<span>Read More</span><i data-lucide="chevron-down"></i>';
            btn.addEventListener('click', function () {
                var open = p.classList.toggle('rm-collapsed') === false;
                btn.setAttribute('aria-expanded', open ? 'true' : 'false');
                btn.querySelector('span').textContent = open ? 'Read Less' : 'Read More';
                btn.classList.toggle('rm-open', open);
                if (!open) {
                    var top = p.getBoundingClientRect().top;
                    if (top < 80) window.scrollBy({ top: top - 120, behavior: 'smooth' });
                }
            });
            p.parentNode.insertBefore(btn, p.nextSibling);
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

        initReadMore();

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
