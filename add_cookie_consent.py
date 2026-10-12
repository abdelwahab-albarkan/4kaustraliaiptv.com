"""Cookie consent: analytics only loads after the visitor accepts; banner + footer 'Cookie settings' link; privacy policy wording."""
import os, re, sys
sys.stdout.reconfigure(encoding='utf8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- JS
js = open('assets/js/app.js', encoding='utf8').read()
a = js.find('// Analytics (Google Analytics 4)')
a = js.rfind('// -----', 0, a)
b = js.find('})();', a) + len('})();')
NEW = r"""// ---------------------------------------------------------------------------
// Analytics (Google Analytics 4). Paste your Measurement ID below, e.g. 'G-ABC123XYZ9'.
// Nothing is loaded until the visitor presses Accept in the cookie banner, and never when
// the browser sends Do Not Track. Clicks on trial / WhatsApp buttons become 'cta_click' events.
// ---------------------------------------------------------------------------
(function () {
  const GA_MEASUREMENT_ID = '';
  const dnt = navigator.doNotTrack === '1' || window.doNotTrack === '1';
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  let loaded = false;
  function consent() { try { return localStorage.getItem('cookie-consent'); } catch (e) { return null; } }
  function load() {
    if (loaded || !GA_MEASUREMENT_ID || dnt || consent() !== 'all') return;
    loaded = true;
    const s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA_MEASUREMENT_ID);
    document.head.appendChild(s);
    gtag('js', new Date());
    gtag('config', GA_MEASUREMENT_ID, { anonymize_ip: true });
  }
  window.__loadAnalytics = load;
  document.addEventListener('click', function (e) {
    if (!loaded) return;
    const el = e.target.closest('[data-cta], a[href*="wa.me"], a[href^="mailto:"]');
    if (!el) return;
    const type = el.getAttribute('data-cta') || (el.href.indexOf('wa.me') > -1 ? 'whatsapp' : 'email');
    gtag('event', 'cta_click', { cta_type: type, page_path: location.pathname, link_text: (el.textContent || '').trim().slice(0, 40) });
  }, true);
  load();
})();

// Cookie banner: Accept analytics or keep essential storage only. The choice is saved in this browser.
(function () {
  if (document.querySelector('.cookie-banner')) return;
  function get() { try { return localStorage.getItem('cookie-consent'); } catch (e) { return null; } }
  function set(v) { try { localStorage.setItem('cookie-consent', v); } catch (e) {} }
  const policy = SITE_BASE + 'privacy-policy/index.html';
  const el = document.createElement('div');
  el.className = 'cookie-banner';
  el.setAttribute('role', 'dialog');
  el.setAttribute('aria-live', 'polite');
  el.setAttribute('aria-label', 'Cookie settings');
  el.hidden = true;
  el.innerHTML =
    '<div class="cookie-text"><strong><i class="fa-solid fa-cookie-bite" aria-hidden="true"></i> Cookies</strong>' +
    '<p>We save a few choices in your browser, like dark mode. With your OK we also use analytics to see which pages help. ' +
    '<a href="' + policy + '">Read the Privacy Policy</a>.</p></div>' +
    '<div class="cookie-actions"><button type="button" class="btn btn-primary btn-sm" data-consent="all">Accept</button>' +
    '<button type="button" class="btn btn-secondary btn-sm" data-consent="essential">Essential only</button></div>';
  document.body.appendChild(el);
  function show() { el.hidden = false; requestAnimationFrame(function () { el.classList.add('show'); }); }
  function hide() { el.classList.remove('show'); setTimeout(function () { el.hidden = true; }, 250); }
  el.addEventListener('click', function (e) {
    const b = e.target.closest('[data-consent]');
    if (!b) return;
    set(b.getAttribute('data-consent'));
    if (b.getAttribute('data-consent') === 'all' && window.__loadAnalytics) window.__loadAnalytics();
    hide();
  });
  // footer link to change the choice later
  const legal = document.querySelector('.footer-legal');
  if (legal && !legal.querySelector('[data-cookie-settings]')) {
    const a = document.createElement('a');
    a.href = '#cookie-settings';
    a.setAttribute('data-cookie-settings', '');
    a.textContent = 'Cookie settings';
    a.addEventListener('click', function (e) { e.preventDefault(); show(); });
    legal.appendChild(a);
  }
  if (!get()) setTimeout(show, 900);
})();"""
js = js[:a] + NEW + js[b:]
open('assets/js/app.js', 'w', encoding='utf8').write(js)
print('js updated')

# ---------------------------------------------------------------- CSS
css = open('assets/css/style.css', encoding='utf8').read()
if '.cookie-banner' not in css:
    css += '''
/* Cookie banner */
.cookie-banner { position: fixed; left: 1rem; bottom: 1rem; z-index: 95; max-width: 460px; display: flex; flex-direction: column; gap: .85rem; padding: 1.1rem 1.2rem; background: var(--surface); color: var(--ink); border: 1px solid var(--border-color); border-radius: 16px; box-shadow: var(--shadow-lg); opacity: 0; transform: translateY(14px); transition: opacity .25s var(--ease), transform .25s var(--ease); }
.cookie-banner[hidden] { display: none; }
.cookie-banner.show { opacity: 1; transform: none; }
.cookie-banner strong { font-size: .98rem; }
.cookie-banner strong i { color: #f59e0b; margin-right: .35rem; }
.cookie-banner p { margin: .35rem 0 0; font-size: .88rem; line-height: 1.6; color: var(--text-muted); }
.cookie-banner a { text-decoration: underline; text-underline-offset: 2px; }
.cookie-actions { display: flex; gap: .5rem; flex-wrap: wrap; }
.cookie-actions .btn { flex: 1 1 140px; }
@media (max-width: 768px) { .cookie-banner { left: .6rem; right: .6rem; max-width: none; bottom: 78px; } }
@media (prefers-reduced-motion: reduce) { .cookie-banner { transition: none; } }
'''
    open('assets/css/style.css', 'w', encoding='utf8').write(css)
    print('css added')

# ---------------------------------------------------------------- privacy policy wording
OLD = 'We may use cookies and similar technologies to remember your preferences and, if enabled, to measure traffic with Google Analytics. You can block or delete cookies in your browser settings. If your browser sends a Do Not Track signal, our analytics will not load.'
NEWT = ('We save a small amount of data in your browser to remember your choices, such as the light or dark theme and your cookie choice. '
        'Analytics cookies (Google Analytics) are only set if you press Accept in the cookie banner, and they are not loaded if your browser sends a Do Not Track signal. '
        'You can change your choice at any time with the Cookie settings link in the footer, or clear cookies in your browser settings.')
for p in ('privacy-policy/index.html', 'build_legal_pages.py'):
    t = open(p, encoding='utf8').read()
    if OLD in t:
        open(p, 'w', encoding='utf8').write(t.replace(OLD, NEWT)); print('privacy wording updated in', p)
print('DONE')
