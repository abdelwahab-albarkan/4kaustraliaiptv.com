/**
 * IPTV AUSTRALIA RESELLER PANEL - INTERACTIVE LOGIC
 * High-performance, pure vanilla JavaScript
 */

// Site root relative to the current page, taken from this script's own URL
const SITE_BASE = (function () {
  const el = document.querySelector('script[src*="assets/js/app.js"]');
  return el ? el.getAttribute('src').split('?')[0].replace('assets/js/app.js', '') : '';
})();

document.addEventListener('DOMContentLoaded', () => {
  initAustralianClock();
  initHeaderScroll();
  initRoiCalculator();
  initPricingToggle();
  initChannelSearchAndFilter();
  initSetupTabs();
  initFaqAccordion();
  initModalHandlers();
  initLiveReviewToasts();
});

/* ==========================================================================
   1. AUSTRALIAN TIME ZONE LIVE CLOCK (AEST / AEDT)
   ========================================================================== */
function initAustralianClock() {
  const clockEl = document.getElementById('ausLiveClock');
  if (!clockEl) return;

  function updateTime() {
    try {
      const options = {
        timeZone: 'Australia/Sydney',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true,
        timeZoneName: 'short' // AEST in winter, AEDT during daylight saving
      };
      const formatter = new Intl.DateTimeFormat('en-AU', options);
      clockEl.textContent = `Sydney/Melbourne: ${formatter.format(new Date())}`;
    } catch (e) {
      clockEl.textContent = 'Sydney/Melbourne time';
    }
  }

  updateTime();
  setInterval(updateTime, 1000);
}

/* ==========================================================================
   2. HEADER SCROLL STATE
   ========================================================================== */
function initHeaderScroll() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
}

/* ==========================================================================
   3. RESELLER PROFIT & ROI CALCULATOR (IN AUD $)
   ========================================================================== */
function initRoiCalculator() {
  const subsRange = document.getElementById('calcSubsRange');
  const subsVal = document.getElementById('calcSubsVal');
  const retailPriceRange = document.getElementById('calcPriceRange');
  const retailPriceVal = document.getElementById('calcPriceVal');

  const outCost = document.getElementById('calcCostOut');
  const outRevenue = document.getElementById('calcRevenueOut');
  const outMonthlyProfit = document.getElementById('calcMonthlyProfitOut');
  const outYearlyProfit = document.getElementById('calcYearlyProfitOut');

  if (!subsRange || !retailPriceRange) return;

  const WHOLESALE_COST_PER_CREDIT_AUD = 4.50; // Wholesale cost per 1-month credit in AUD

  function calculate() {
    const subs = parseInt(subsRange.value, 10);
    const retailPrice = parseFloat(retailPriceRange.value);

    subsVal.textContent = subs.toLocaleString('en-AU') + ' Subscribers';
    retailPriceVal.textContent = '$' + retailPrice.toFixed(0) + ' AUD';

    const monthlyCost = subs * WHOLESALE_COST_PER_CREDIT_AUD;
    const monthlyRevenue = subs * retailPrice;
    const monthlyProfit = monthlyRevenue - monthlyCost;
    const yearlyProfit = monthlyProfit * 12;

    if (outCost) outCost.textContent = '$' + Math.round(monthlyCost).toLocaleString('en-AU') + ' AUD';
    if (outRevenue) outRevenue.textContent = '$' + Math.round(monthlyRevenue).toLocaleString('en-AU') + ' AUD';
    if (outMonthlyProfit) outMonthlyProfit.textContent = '$' + Math.round(monthlyProfit).toLocaleString('en-AU') + ' AUD';
    if (outYearlyProfit) outYearlyProfit.textContent = '$' + Math.round(yearlyProfit).toLocaleString('en-AU') + ' AUD';
  }

  subsRange.addEventListener('input', calculate);
  retailPriceRange.addEventListener('input', calculate);
  calculate();
}

/* ==========================================================================
   4. PRICING TOGGLE (CONSUMER AUD VS RESELLER CREDITS)
   ========================================================================== */
function initPricingToggle() {
  const btnConsumer = document.getElementById('toggleConsumerBtn');
  const btnReseller = document.getElementById('toggleResellerBtn');
  const gridConsumer = document.getElementById('consumerPricingGrid');
  const gridReseller = document.getElementById('resellerPricingGrid');

  if (!btnConsumer || !btnReseller || !gridConsumer || !gridReseller) return;

  btnConsumer.addEventListener('click', () => {
    btnConsumer.classList.add('active');
    btnReseller.classList.remove('active');
    gridConsumer.style.display = 'grid';
    gridReseller.style.display = 'none';
  });

  btnReseller.addEventListener('click', () => {
    btnReseller.classList.add('active');
    btnConsumer.classList.remove('active');
    gridConsumer.style.display = 'none';
    gridReseller.style.display = 'grid';
  });
}

/* ==========================================================================
   5. CHANNEL SEARCH & CATEGORY FILTER
   ========================================================================== */
function initChannelSearchAndFilter() {
  const searchInput = document.getElementById('channelSearchInput');
  const filterBtns = document.querySelectorAll('.filter-btn');
  const channelCards = document.querySelectorAll('.channel-item-card');

  if (!channelCards.length) return;

  let activeCategory = 'all';
  let searchTerm = '';

  function filterItems() {
    channelCards.forEach(card => {
      const cat = card.getAttribute('data-category') || '';
      const name = card.getAttribute('data-name') || '';
      const matchCat = (activeCategory === 'all' || cat.includes(activeCategory));
      const matchSearch = name.toLowerCase().includes(searchTerm.toLowerCase());

      if (matchCat && matchSearch) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchTerm = e.target.value.trim();
      filterItems();
    });
  }

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeCategory = btn.getAttribute('data-filter') || 'all';
      filterItems();
    });
  });
}

/* ==========================================================================
   6. SETUP TABS (DEVICE GUIDES)
   ========================================================================== */
function initSetupTabs() {
  const tabBtns = document.querySelectorAll('.setup-tab-btn');
  const tabContents = document.querySelectorAll('.setup-tab-content');

  if (!tabBtns.length || !tabContents.length) return;

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.getAttribute('data-tab');

      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.style.display = 'none');

      btn.classList.add('active');
      const targetEl = document.getElementById(target);
      if (targetEl) {
        targetEl.style.display = 'block';
      }
    });
  });
}

/* ==========================================================================
   7. INTERACTIVE FAQ ACCORDION & SEARCH
   ========================================================================== */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');
  const faqSearch = document.getElementById('faqSearch');
  const catBtns = document.querySelectorAll('.faq-cat-btn');

  // Accordion toggle
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');

    if (question && answer) {
      question.addEventListener('click', () => {
        const isActive = item.classList.contains('active');

        // Close all others
        faqItems.forEach(i => {
          i.classList.remove('active');
          const ans = i.querySelector('.faq-answer');
          if (ans) ans.style.maxHeight = null;
        });

        if (!isActive) {
          item.classList.add('active');
          answer.style.maxHeight = answer.scrollHeight + 'px';
        }
      });
    }
  });

  // Filter & Search
  let currentCat = 'all';
  let query = '';

  function filterFaq() {
    faqItems.forEach(item => {
      const cat = item.getAttribute('data-category') || '';
      const text = item.textContent.toLowerCase();
      const matchCat = (currentCat === 'all' || cat === currentCat);
      const matchQuery = text.includes(query.toLowerCase());

      if (matchCat && matchQuery) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  }

  if (faqSearch) {
    faqSearch.addEventListener('input', (e) => {
      query = e.target.value.trim();
      filterFaq();
    });
  }

  catBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      catBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentCat = btn.getAttribute('data-cat') || 'all';
      filterFaq();
    });
  });
}

/* ==========================================================================
   8. MODAL HANDLERS (FREE TRIAL & RESELLER APPLICATION)
   ========================================================================== */
function initModalHandlers() {
  const trialModal = document.getElementById('trialModal');
  const resellerModal = document.getElementById('resellerModal');

  // Trigger buttons
  document.querySelectorAll('[data-open-modal="trial"]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (trialModal) trialModal.classList.add('active');
      else window.location.href = SITE_BASE + 'iptv-free-trial-australia/index.html';
    });
  });

  document.querySelectorAll('[data-open-modal="reseller"]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (resellerModal) resellerModal.classList.add('active');
      else window.location.href = SITE_BASE + 'contact.html';
    });
  });

  // Close buttons
  document.querySelectorAll('.modal-close-btn, .modal-overlay').forEach(el => {
    el.addEventListener('click', (e) => {
      if (e.target === el || e.target.closest('.modal-close-btn')) {
        document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('active'));
      }
    });
  });

  // Escape key closes modal
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-overlay').forEach(m => m.classList.remove('active'));
    }
  });

  // Forms hand the details to WhatsApp, so the request really reaches the team
  bindWhatsAppForm(document.getElementById('trialForm'), 'Hi, I would like a free 24-hour IPTV trial.', trialModal);
  bindWhatsAppForm(document.getElementById('resellerForm'), 'Hi, I would like to apply for the IPTV reseller panel.', resellerModal);
  bindWhatsAppForm(document.getElementById('contactPageForm'), 'Hi, I have a question about IPTV.', null);
}

const WHATSAPP_NUMBER = '212625218443';

/**
 * Builds a WhatsApp message from a form's labelled fields and opens the chat.
 * Nothing is sent until the visitor presses Send in WhatsApp.
 */
function bindWhatsAppForm(form, intro, modal) {
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const lines = [intro];
    form.querySelectorAll('.form-group').forEach((group) => {
      const label = group.querySelector('label');
      const field = group.querySelector('input, select, textarea');
      if (!label || !field) return;
      let value = field.value;
      if (field.tagName === 'SELECT') value = field.options[field.selectedIndex]?.text || value;
      value = (value || '').trim();
      if (value) lines.push(label.textContent.replace(/:\s*$/, '').replace(/\s*\(.*?\)\s*/g, ' ').trim() + ': ' + value);
    });
    const url = 'https://wa.me/' + WHATSAPP_NUMBER + '?text=' + encodeURIComponent(lines.join('\n'));
    const win = window.open(url, '_blank', 'noopener');
    if (!win) window.location.href = url;

    let note = form.querySelector('.form-success');
    if (!note) {
      note = document.createElement('p');
      note.className = 'form-success';
      note.setAttribute('role', 'status');
      form.appendChild(note);
    }
    note.innerHTML = '<i class="fa-brands fa-whatsapp"></i> WhatsApp is opening with your details. Press <strong>Send</strong> in WhatsApp and we will reply there. You can also email <a href="mailto:support@4kaustraliaiptv.com">support@4kaustraliaiptv.com</a>.';
    if (typeof gtag === 'function') gtag('event', 'form_submit', { form_id: form.id, page_path: location.pathname });
    setTimeout(() => { if (modal) modal.classList.remove('active'); form.reset(); }, 2500);
  });
}

// Mobile / compact navigation toggle (button is injected so every page gets it)
(function () {
  const header = document.querySelector('.site-header');
  const actions = header && header.querySelector('.header-actions');
  if (!actions || header.querySelector('.mobile-menu-btn')) return;
  const btn = document.createElement('button');
  btn.className = 'mobile-menu-btn';
  btn.type = 'button';
  btn.setAttribute('aria-label', 'Menu');
  btn.innerHTML = '<i class="fa-solid fa-bars"></i>';
  btn.addEventListener('click', () => {
    const open = header.classList.toggle('nav-open');
    btn.innerHTML = '<i class="fa-solid fa-' + (open ? 'xmark' : 'bars') + '"></i>';
  });
  header.querySelectorAll('.main-nav a').forEach(a => a.addEventListener('click', () => header.classList.remove('nav-open')));
  actions.appendChild(btn);
})();

// Skip link for keyboard users (injected so every page gets it)
(function () {
  if (document.querySelector('.skip-link')) return;
  const target = document.querySelector('main, .hero-section, section');
  if (!target) return;
  if (!target.id) target.id = 'main-content';
  target.setAttribute('tabindex', '-1');
  const a = document.createElement('a');
  a.className = 'skip-link';
  a.href = '#' + target.id;
  a.textContent = 'Skip to main content';
  document.body.insertBefore(a, document.body.firstChild);
})();

// Sticky mobile action bar: Free Trial + WhatsApp on every page
(function () {
  if (document.querySelector('.sticky-cta')) return;
  const bar = document.createElement('div');
  bar.className = 'sticky-cta';
  bar.innerHTML =
    '<button type="button" class="btn btn-gold" data-open-modal="trial" data-cta="trial"><i class="fa-solid fa-play"></i> Free Trial</button>' +
    '<a class="btn btn-whatsapp" data-cta="whatsapp" target="_blank" rel="noopener" href="https://wa.me/212625218443?text=' +
    encodeURIComponent('Hi, I would like a free IPTV trial') + '"><i class="fa-brands fa-whatsapp"></i> WhatsApp</a>';
  document.body.appendChild(bar);
  document.body.classList.add('has-sticky-cta');
  // the shared modal handler binds this button (opens the modal, or the free-trial page when a page has no modal)
})();

// ---------------------------------------------------------------------------
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
  function show() { el.hidden = false; setTimeout(function () { el.classList.add('show'); }, 30); }
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
})();

// Pricing: 3 / 6 / 12 month plans with 1-4 accounts
(function () {
  const wrap = document.getElementById('consumerPricingGrid');
  if (!wrap || !wrap.querySelector('[data-acct]')) return;
  const PRICES = { 3: [39.99, 59.99, 79.99, 99.99], 6: [56.99, 84.99, 109.99, 134.99], 12: [79.99, 119.99, 149.99, 179.99] };
  const money = v => v.toFixed(2);
  function render(acct) {
    const i = acct - 1;
    wrap.querySelectorAll('.pricing-card[data-months]').forEach(card => {
      const months = +card.dataset.months;
      const price = PRICES[months][i];
      const perMonth = price / months;
      const base = PRICES[3][i] / 3;
      const save = Math.round((1 - perMonth / base) * 100);
      card.querySelector('[data-price]').textContent = money(price);
      card.querySelector('[data-permonth]').textContent = '$' + money(perMonth) + ' / month';
      const pill = card.querySelector('[data-save]');
      if (pill) { pill.hidden = save <= 0; pill.textContent = 'Save ' + save + '%'; }
      card.querySelector('[data-accounts]').textContent = acct + (acct === 1 ? ' account included' : ' accounts included');
      const a = card.querySelector('[data-order]');
      if (a) a.href = 'https://wa.me/212625218443?text=' + encodeURIComponent('Hi, I want the ' + months + ' months IPTV plan with ' + acct + ' account' + (acct === 1 ? '' : 's') + ' ($' + money(price) + ')');
    });
  }
  wrap.querySelectorAll('.acct-btn').forEach(btn => btn.addEventListener('click', () => {
    wrap.querySelectorAll('.acct-btn').forEach(b => { b.classList.toggle('active', b === btn); b.setAttribute('aria-checked', b === btn ? 'true' : 'false'); });
    render(+btn.dataset.acct);
  }));
})();

// Copy-link buttons on share rows
document.addEventListener('click', function (e) {
  const b = e.target.closest('[data-copy-link]');
  if (!b) return;
  const url = b.getAttribute('data-copy-link');
  const done = () => { const t = b.innerHTML; b.innerHTML = '<i class="fa-solid fa-check"></i> Copied'; setTimeout(() => { b.innerHTML = t; }, 1800); };
  if (navigator.clipboard) navigator.clipboard.writeText(url).then(done, done); else done();
});

/* ==========================================================================
   9. LIVE AUSTRALIAN CUSTOMER REVIEW NOTIFICATION TOAST ROTATOR
   ========================================================================== */
const LIVE_REVIEWS = [
  {
    name: "Liam O'Connor",
    city: "Sydney, NSW",
    avatar: "public/images/revriw/avatars/avatar-1.webp",
    rating: 5,
    quote: "AFL in 4K on Telstra NBN with zero buffering. Cancelled Foxtel and saved $90/mo!",
    tag: "Verified 12M Plan",
    timeAgo: "2 mins ago"
  },
  {
    name: "Sarah Jenkins",
    city: "Melbourne, VIC",
    avatar: "public/images/revriw/avatars/avatar-2.webp",
    rating: 5,
    quote: "Apple TV 4K setup took 3 minutes. Premier League and movies stream crystal clear.",
    tag: "Verified Subscriber",
    timeAgo: "4 mins ago"
  },
  {
    name: "David Miller",
    city: "Brisbane, QLD",
    avatar: "public/images/revriw/avatars/avatar-3.webp",
    rating: 5,
    quote: "Every NRL Broncos match in true 4K 60FPS on my Nvidia Shield. Absolutely unreal!",
    tag: "Verified Subscriber",
    timeAgo: "7 mins ago"
  },
  {
    name: "Callum Smith",
    city: "Perth, WA",
    avatar: "public/images/revriw/avatars/avatar-4.webp",
    rating: 5,
    quote: "AWST time zone guide is spot on for Perth. IBO Player on Samsung TV runs super fast.",
    tag: "Verified Subscriber",
    timeAgo: "11 mins ago"
  },
  {
    name: "Sophie Tremblay",
    city: "Adelaide, SA",
    avatar: "public/images/revriw/avatars/avatar-5.webp",
    rating: 5,
    quote: "WhatsApp support replied in 2 mins and sent my trial login immediately. 10/10 service!",
    tag: "Free Trial User",
    timeAgo: "14 mins ago"
  },
  {
    name: "Marcus Henderson",
    city: "Gold Coast, QLD",
    avatar: "public/images/revriw/avatars/avatar-6.webp",
    rating: 5,
    quote: "Top reseller panel in AUD. Already made over $2,400 profit this month from local clients.",
    tag: "Reseller Partner",
    timeAgo: "19 mins ago"
  },
  {
    name: "Jessica Taylor",
    city: "Newcastle, NSW",
    avatar: "public/images/revriw/avatars/avatar-7.webp",
    rating: 5,
    quote: "F1 Grand Prix with Sky Sports & UFC Main Card included without extra pay-per-view fees.",
    tag: "Verified Subscriber",
    timeAgo: "26 mins ago"
  },
  {
    name: "Matthew Wright",
    city: "Hobart, TAS",
    avatar: "public/images/revriw/avatars/avatar-8.webp",
    rating: 5,
    quote: "Replaced Kayo, Stan and Netflix into one. Firestick 4K with TiviMate works like magic.",
    tag: "Verified Subscriber",
    timeAgo: "33 mins ago"
  },
  {
    name: "Chloe Zhang",
    city: "Melbourne, VIC",
    avatar: "public/images/revriw/avatars/avatar-9.webp",
    rating: 5,
    quote: "Amazing international and Asian channel lineup plus all Aussie Free-to-Air in HD.",
    tag: "Verified Subscriber",
    timeAgo: "41 mins ago"
  }
];

function initLiveReviewToasts() {
  let toast = document.getElementById('liveReviewToast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'liveReviewToast';
    toast.className = 'live-toast review-toast';
    toast.setAttribute('role', 'status');
    toast.setAttribute('aria-live', 'polite');
    toast.innerHTML = `
      <div class="toast-avatar-box">
        <img id="toastAvatar" src="${SITE_BASE}public/images/revriw/avatars/avatar-1.webp" alt="Liam O'Connor" class="toast-avatar-img" width="44" height="44" loading="lazy" />
        <span class="toast-badge-check" title="Verified Australian Subscriber"><i class="fa-solid fa-check"></i></span>
      </div>
      <div class="toast-body">
        <div class="toast-top-row">
          <span class="toast-author" id="toastName">Liam O'Connor</span>
          <span class="toast-city" id="toastCity"><i class="fa-solid fa-location-dot"></i> Sydney, NSW</span>
          <span class="toast-stars" id="toastStars">
            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          </span>
        </div>
        <div class="toast-message" id="toastQuote">"Watched AFL in 4K on Telstra NBN with zero buffering. Unreal!"</div>
        <div class="toast-footer">
          <span class="toast-activity" id="toastTag"><i class="fa-solid fa-bolt" style="color:var(--aus-green);"></i> Verified Subscriber</span>
          <span class="toast-time" id="toastTime">2 mins ago</span>
        </div>
      </div>
      <button type="button" class="toast-close" id="toastCloseBtn" aria-label="Close notification">&times;</button>
    `;
    document.body.appendChild(toast);
  }

  const avatarEl = document.getElementById('toastAvatar');
  const nameEl = document.getElementById('toastName');
  const cityEl = document.getElementById('toastCity');
  const quoteEl = document.getElementById('toastQuote');
  const tagEl = document.getElementById('toastTag');
  const timeEl = document.getElementById('toastTime');
  const closeBtn = document.getElementById('toastCloseBtn');

  let currentIndex = 0;
  let isHovered = false;
  let isDismissed = false;
  let hideTimeout = null;
  let nextTimeout = null;

  function updateReview(index) {
    const item = LIVE_REVIEWS[index];
    if (!item) return;
    if (avatarEl) {
      avatarEl.src = (SITE_BASE || '') + item.avatar;
      avatarEl.alt = item.name + ' - ' + item.city;
    }
    if (nameEl) nameEl.textContent = item.name;
    if (cityEl) cityEl.innerHTML = `<i class="fa-solid fa-location-dot"></i> ${item.city}`;
    if (quoteEl) quoteEl.textContent = `"${item.quote}"`;
    if (tagEl) tagEl.innerHTML = `<i class="fa-solid fa-bolt" style="color:var(--aus-green);"></i> ${item.tag}`;
    if (timeEl) timeEl.textContent = item.timeAgo;
  }

  function showToast() {
    if (isDismissed) return;
    updateReview(currentIndex);
    toast.classList.add('show');

    clearTimeout(hideTimeout);
    hideTimeout = setTimeout(() => {
      if (!isHovered && !isDismissed) {
        hideToast();
      }
    }, 5500);
  }

  function hideToast() {
    toast.classList.remove('show');
    clearTimeout(hideTimeout);
    clearTimeout(nextTimeout);
    currentIndex = (currentIndex + 1) % LIVE_REVIEWS.length;
    if (!isDismissed) {
      nextTimeout = setTimeout(showToast, 6000);
    }
  }

  toast.addEventListener('mouseenter', () => {
    isHovered = true;
  });

  toast.addEventListener('mouseleave', () => {
    isHovered = false;
    if (toast.classList.contains('show')) {
      clearTimeout(hideTimeout);
      hideTimeout = setTimeout(hideToast, 2000);
    }
  });

  toast.addEventListener('click', (e) => {
    if (e.target.closest('#toastCloseBtn')) return;
    const target = document.getElementById('reviews') || document.getElementById('support');
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    } else {
      window.location.href = (SITE_BASE || '') + 'index.html#reviews';
    }
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      toast.classList.remove('show');
      isDismissed = true;
      clearTimeout(hideTimeout);
      clearTimeout(nextTimeout);
      setTimeout(() => {
        isDismissed = false;
        showToast();
      }, 45000);
    });
  }

  // Start rotation 3.5 seconds after page loads
  setTimeout(showToast, 3500);
}


// Light / dark theme switch (choice is remembered in this browser)
(function () {
  const root = document.documentElement;
  const actions = document.querySelector('.site-header .header-actions');
  if (!actions || actions.querySelector('.theme-toggle')) return;
  const meta = document.querySelector('meta[name="theme-color"]');
  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'theme-toggle';
  btn.innerHTML = '<i class="fa-solid fa-moon" aria-hidden="true"></i><i class="fa-solid fa-sun" aria-hidden="true"></i>';
  function paint() {
    const dark = root.getAttribute('data-theme') === 'dark';
    btn.setAttribute('aria-pressed', dark ? 'true' : 'false');
    btn.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
    btn.title = dark ? 'Light theme' : 'Dark theme';
    if (meta) meta.setAttribute('content', dark ? '#070d19' : '#0f172a');
  }
  btn.addEventListener('click', function () {
    const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (e) {}
    paint();
  });
  actions.insertBefore(btn, actions.querySelector('.mobile-menu-btn') || null);
  paint();
})();
