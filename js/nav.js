// js/nav.js
// Shared navigation auth state handler.
// Updates nav to show user color circle + profile link when logged in,
// or Login/Sign Up buttons when logged out.

import { onAuthChange, getUserProfile } from './auth.js';
import { startAutoUpdate } from './auto-update.js';
import { initAiKeyboardCam } from './ai-keyboard-cam.js';
import { initProfanityWarning } from './profanity-warning.js';
import { initTypingFingerGuide } from './typing-finger-guide.js';
import { initSuperCalculator } from './super-calculator.js';
import { initUiSounds } from './ui-sounds.js';

// ─── Google Analytics 4 (site-wide page-view counting) ──────────────
// nav.js loads on ~2,220 pages, so injecting GA here counts the whole
// site. Guard: skip if a gtag tag is already on the page (the homepage
// embeds it inline in <head>) so we never double-count.
(function loadGA() {
  const GA_ID = 'G-Z7TFRFQDQJ';
  if (document.querySelector('script[src*="googletagmanager.com/gtag/js"]')) return;
  const s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
  document.head.appendChild(s);
  window.dataLayer = window.dataLayer || [];
  window.gtag = function gtag() { window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', GA_ID);
})();

function getColorValue(colorName) {
  const colors = {
    blue: '#3b82f6',
    green: '#22c55e',
    orange: '#f97316',
    purple: '#8b5cf6',
    cyan: '#06b6d4',
    pink: '#ec4899',
    gray: '#6b7280'
  };
  return colors[colorName] || colors.blue;
}

/**
 * Initialize nav auth state. Call this on every page.
 * Looks for .nav-links container and replaces Login/Sign Up
 * with color circle + profile link when user is authenticated.
 *
 * @param {string} basePath - relative path to root (e.g., '' for root pages, '../../' for course lessons)
 */
export function initNav(basePath = '') {
  // Run auto-update + cache-clear on every page
  startAutoUpdate();

  // Edge-style UI sound layer (synthesized chimes, off-friendly mute toggle).
  initUiSounds();

  // Toggle body.lang-es / body.lang-pt so language-gated widgets (typing finger
  // guide, Ñ button, etc.) work on every page, not just the catalog.
  _initLangClass();

  // Suppress Google Translate's banner/toolbar (both the in-place widget's
  // and the .translate.goog proxy's). Must run on every page, not just when
  // the in-place widget loads, because the proxy injects its own toolbar.
  injectGoogleTranslateSuppressionStyles();

  // Add Google Translate widget
  addTranslateWidget();

  // If we landed on the .translate.goog proxy, the page is already being
  // translated by Google's proxy — run the courses-grid resort once on load
  // so tiles end up in the translated locale's alphabetical order.
  if (location.hostname.endsWith('.translate.goog') && document.querySelector('.courses-grid')) {
    const m = location.search.match(/[?&]_x_tr_tl=([^&]+)/);
    const targetLang = m ? decodeURIComponent(m[1]) : 'en';
    scheduleResortAfterTranslation(targetLang);
  }

  // AI Security Camera — watches keyboard input across the site for slurs.
  // Idempotent: safe to call repeatedly across pages.
  initAiKeyboardCam();

  // Soft profanity warning — toast on common cuss words; no strike, no redirect.
  // Idempotent: safe to call repeatedly across pages.
  initProfanityWarning();

  // AI Camera Finger Guide — auto-activates only on Typing Skills pages.
  // Shows a color-coded keyboard and tells you which finger to use.
  initTypingFingerGuide();

  // Super Calculator — floating 🧮 button in the bottom-left of every page.
  // Modes: Basic, Trig (DEG/RAD), Stats (mean/median/stdev/normalcdf/nCk/binompdf),
  // and Calc (numerical derivative, integral, limit).
  initSuperCalculator();

  onAuthChange(async (user) => {
    const navLinks = document.querySelector('.nav-links');
    if (!navLinks) return;

    // Find and remove existing auth links
    const loginLink = navLinks.querySelector('[data-auth="login"]');
    const signupLink = navLinks.querySelector('[data-auth="signup"]');
    const userNav = navLinks.querySelector('[data-auth="user"]');

    if (user) {
      // Check if user is banned or suspended
      try {
        const { db } = await import('./firebase-config.js');
        const { doc, getDoc, updateDoc } = await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js');
        const userDoc = await getDoc(doc(db, 'users', user.uid));
        if (userDoc.exists()) {
          const data = userDoc.data();
          const reason = data.banReason || 'Violation of Community Safety Rules';
          if (data.banned) {
            window.location.href = basePath + 'violation.html?strike=3&reason=' + encodeURIComponent(reason);
            return;
          }
          if (data.suspended && data.suspendedUntil) {
            const until = new Date(data.suspendedUntil.seconds ? data.suspendedUntil.seconds * 1000 : data.suspendedUntil);
            if (until > new Date()) {
              window.location.href = basePath + 'violation.html?strike=2&reason=' + encodeURIComponent(reason) + '&until=' + encodeURIComponent(until.toISOString());
              return;
            }
          }
          if (data.strikes >= 1 && data.unseenWarning) {
            try { await updateDoc(doc(db, 'users', user.uid), { unseenWarning: false }); } catch(e) {}
            window.location.href = basePath + 'violation.html?strike=1&reason=' + encodeURIComponent(reason);
            return;
          }
        }
      } catch(e) {}

      // Hide login/signup
      if (loginLink) loginLink.style.display = 'none';
      if (signupLink) signupLink.style.display = 'none';

      // Don't duplicate if already added
      if (userNav) {
        userNav.style.display = 'flex';
        return;
      }

      // Get user profile for color
      let displayName = 'Profile';
      let userColor = 'blue';
      try {
        const profile = await getUserProfile();
        if (profile) {
          userColor = profile.color || 'blue';
          displayName = profile.displayName || 'Profile';
        }
      } catch (e) {
        // Use defaults if profile fetch fails
      }

      // Create user nav element
      const initial = displayName.charAt(0).toUpperCase();
      const userEl = document.createElement('div');
      userEl.setAttribute('data-auth', 'user');
      userEl.style.cssText = 'display:flex; align-items:center; gap:8px;';
      userEl.innerHTML = `
        <a href="${basePath}profile.html" style="display:flex; align-items:center; gap:8px; text-decoration:none; color:inherit; padding:4px 12px; border-radius:8px; transition:background 0.2s;">
          <img src="${basePath}assets/avatars/${userColor}.svg" alt="" style="width:28px; height:28px; border-radius:50%;">
          <span style="font-size:0.85rem; font-weight:600;">${escapeHtml(displayName)}</span>
        </a>
      `;
      navLinks.appendChild(userEl);
    } else {
      // Show login/signup
      if (loginLink) loginLink.style.display = '';
      if (signupLink) signupLink.style.display = '';
      if (userNav) userNav.style.display = 'none';
    }
  });
}

function escapeHtml(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

function addTranslateWidget() {
  // Don't add twice
  if (document.getElementById('translate-btn')) return;

  const navLinks = document.querySelector('.nav-links');
  if (!navLinks) return;

  // Create translate button
  const btn = document.createElement('button');
  btn.id = 'translate-btn';
  btn.title = 'Translate';
  btn.setAttribute('aria-label', 'Translate page');
  btn.style.cssText = 'background:none; border:none; cursor:pointer; padding:4px 8px; font-size:1.2rem; color:var(--color-text-secondary); transition:color 0.2s; display:flex; align-items:center; gap:4px;';
  btn.innerHTML = '<span style="font-size:1.1rem;">&#127760;</span><span style="font-size:0.75rem; font-weight:600;">Translate</span>';

  // Create dropdown
  const dropdown = document.createElement('div');
  dropdown.id = 'translate-dropdown';
  dropdown.style.cssText = 'display:none; position:absolute; top:100%; right:0; background:var(--color-white); border:1px solid var(--color-border); border-radius:var(--radius); box-shadow:var(--shadow-lg); z-index:999; min-width:240px; max-height:420px; flex-direction:column;';

  // Mascot header — Lingo & Babel, your translation guides
  const mascotHeader = document.createElement('div');
  mascotHeader.style.cssText = 'display:flex; align-items:center; gap:10px; padding:12px 14px 10px; background:linear-gradient(135deg,#1FA45C 0%,#FFD93D 50%,#FF6B6B 100%); color:#fff; border-radius:var(--radius) var(--radius) 0 0;';
  mascotHeader.innerHTML = `
    <div style="display:flex; gap:-8px;">
      <img src="/assets/characters/lingo.svg" alt="Lingo the Parrot" width="40" height="40" style="background:#fff; border-radius:50%; padding:2px; box-shadow:0 2px 6px rgba(0,0,0,0.15);" onerror="this.style.display='none'">
      <img src="/assets/characters/babel.svg" alt="Babel the Owl" width="40" height="40" style="background:#fff; border-radius:50%; padding:2px; box-shadow:0 2px 6px rgba(0,0,0,0.15); margin-left:-10px;" onerror="this.style.display='none'">
    </div>
    <div style="flex:1; min-width:0;">
      <div style="font-weight:800; font-size:0.85rem; line-height:1.2;">Lingo &amp; Babel</div>
      <div style="font-size:0.7rem; opacity:0.95; line-height:1.2;">Your translation mascots — pick a language!</div>
    </div>`;
  dropdown.appendChild(mascotHeader);

  // Search header
  const searchWrap = document.createElement('div');
  searchWrap.style.cssText = 'padding:10px 12px 8px; border-bottom:1px solid var(--color-border); position:sticky; top:0; background:var(--color-white); z-index:1;';
  const search = document.createElement('input');
  search.type = 'search';
  search.placeholder = 'Search 130+ languages…';
  search.setAttribute('aria-label', 'Search languages');
  search.style.cssText = 'width:100%; padding:6px 10px; border:1px solid var(--color-border); border-radius:6px; font-size:0.85rem; font-family:inherit; box-sizing:border-box;';
  searchWrap.appendChild(search);
  dropdown.appendChild(searchWrap);

  // Scrollable language list
  const list = document.createElement('div');
  list.style.cssText = 'overflow-y:auto; flex:1; padding:6px 0;';
  dropdown.appendChild(list);

  const languages = [
    ['en','English'],
    ['af','Afrikaans'],['sq','Albanian'],['am','Amharic'],['ar','Arabic'],['hy','Armenian'],['as','Assamese'],
    ['ay','Aymara'],['az','Azerbaijani'],['bm','Bambara'],['eu','Basque'],['be','Belarusian'],['bn','Bengali'],
    ['bho','Bhojpuri'],['bs','Bosnian'],['bg','Bulgarian'],['ca','Catalan'],['ceb','Cebuano'],
    ['ny','Chichewa'],['zh-CN','Chinese (Simplified)'],['zh-TW','Chinese (Traditional)'],['co','Corsican'],
    ['hr','Croatian'],['cs','Czech'],['da','Danish'],['dv','Dhivehi'],['doi','Dogri'],['nl','Dutch'],
    ['eo','Esperanto'],['et','Estonian'],['ee','Ewe'],['tl','Filipino'],['fi','Finnish'],['fr','French'],
    ['fy','Frisian'],['gl','Galician'],['ka','Georgian'],['de','German'],['el','Greek'],['gn','Guarani'],
    ['gu','Gujarati'],['ht','Haitian Creole'],['ha','Hausa'],['haw','Hawaiian'],['he','Hebrew'],['hi','Hindi'],
    ['hmn','Hmong'],['hu','Hungarian'],['is','Icelandic'],['ig','Igbo'],['ilo','Ilocano'],['id','Indonesian'],
    ['ga','Irish'],['it','Italian'],['ja','Japanese'],['jw','Javanese'],['kn','Kannada'],['kk','Kazakh'],
    ['km','Khmer'],['rw','Kinyarwanda'],['gom','Konkani'],['ko','Korean'],['kri','Krio'],['ku','Kurdish (Kurmanji)'],
    ['ckb','Kurdish (Sorani)'],['ky','Kyrgyz'],['lo','Lao'],['la','Latin'],['lv','Latvian'],['ln','Lingala'],
    ['lt','Lithuanian'],['lg','Luganda'],['lb','Luxembourgish'],['mk','Macedonian'],['mai','Maithili'],
    ['mg','Malagasy'],['ms','Malay'],['ml','Malayalam'],['mt','Maltese'],['mi','Maori'],['mr','Marathi'],
    ['mni-Mtei','Meiteilon (Manipuri)'],['lus','Mizo'],['mn','Mongolian'],['my','Myanmar (Burmese)'],
    ['ne','Nepali'],['no','Norwegian'],['or','Odia (Oriya)'],['om','Oromo'],['ps','Pashto'],['fa','Persian'],
    ['pl','Polish'],['pt','Portuguese'],['pa','Punjabi'],['qu','Quechua'],['ro','Romanian'],['ru','Russian'],
    ['sm','Samoan'],['sa','Sanskrit'],['gd','Scots Gaelic'],['nso','Sepedi'],['sr','Serbian'],['st','Sesotho'],
    ['sn','Shona'],['sd','Sindhi'],['si','Sinhala'],['sk','Slovak'],['sl','Slovenian'],['so','Somali'],
    ['es','Spanish', { popular: true }],['su','Sundanese'],['sw','Swahili'],['sv','Swedish'],['tg','Tajik'],['ta','Tamil'],
    ['tt','Tatar'],['te','Telugu'],['th','Thai'],['ti','Tigrinya'],['ts','Tsonga'],['tr','Turkish'],
    ['tk','Turkmen'],['ak','Twi'],['uk','Ukrainian'],['ur','Urdu'],['ug','Uyghur'],['uz','Uzbek'],
    ['vi','Vietnamese'],['cy','Welsh'],['xh','Xhosa'],['yi','Yiddish'],['yo','Yoruba'],['zu','Zulu']
  ];

  const items = [];
  languages.forEach(([code, name, opts]) => {
    const item = document.createElement('button');
    const popular = opts && opts.popular;
    const baseBg = popular ? 'linear-gradient(90deg, rgba(255,217,61,0.18) 0%, rgba(255,217,61,0) 70%)' : 'none';
    item.style.cssText = `display:flex; align-items:center; justify-content:space-between; gap:8px; width:100%; text-align:left; padding:8px 16px; border:none; background:${baseBg}; cursor:pointer; font-size:0.85rem; font-family:inherit; color:var(--color-text); transition:background 0.15s; ${popular ? 'font-weight:700;' : ''}`;
    if (popular) {
      item.innerHTML = `<span>${name}</span><span style="font-size:0.6rem; font-weight:800; letter-spacing:0.06em; text-transform:uppercase; color:#92400e; background:#fde047; padding:2px 6px; border-radius:999px;">★ Popular</span>`;
    } else {
      item.textContent = name;
    }
    item.dataset.search = name.toLowerCase();
    item.addEventListener('mouseenter', () => { item.style.background = 'var(--color-bg)'; });
    item.addEventListener('mouseleave', () => { item.style.background = baseBg; });
    item.addEventListener('click', () => {
      translatePage(code);
      dropdown.style.display = 'none';
    });
    list.appendChild(item);
    items.push(item);
  });

  search.addEventListener('input', () => {
    const q = search.value.trim().toLowerCase();
    for (const it of items) {
      it.style.display = !q || it.dataset.search.includes(q) ? 'block' : 'none';
    }
  });
  search.addEventListener('click', (e) => e.stopPropagation());

  // Wrapper for positioning
  const wrapper = document.createElement('div');
  wrapper.style.cssText = 'position:relative; display:flex; align-items:center;';
  wrapper.appendChild(btn);
  wrapper.appendChild(dropdown);

  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    const isOpen = dropdown.style.display === 'flex';
    dropdown.style.display = isOpen ? 'none' : 'flex';
    if (!isOpen) { search.value = ''; for (const it of items) it.style.display = 'block'; setTimeout(() => search.focus(), 0); }
  });

  document.addEventListener('click', () => { dropdown.style.display = 'none'; });

  // ── One-tap quick translate button — flag-aware for every translation language ──
  // Detects the page's current Google-Translate language (proxy URL params or the
  // in-place widget's googtrans cookie) and renders:
  //   • on English  → 🇲🇽 Español (one-tap shortcut to Spanish, our most-used target)
  //   • on any non-English language → the flag of THAT language + "English" label
  //     so the user always sees what they're currently in and can hop back in one tap.
  const LANG_FLAGS = {
    en:'🇺🇸', es:'🇲🇽', fr:'🇫🇷', de:'🇩🇪', it:'🇮🇹', pt:'🇧🇷', nl:'🇳🇱',
    pl:'🇵🇱', ru:'🇷🇺', uk:'🇺🇦', be:'🇧🇾', cs:'🇨🇿', sk:'🇸🇰', sl:'🇸🇮',
    sr:'🇷🇸', hr:'🇭🇷', bs:'🇧🇦', bg:'🇧🇬', ro:'🇷🇴', hu:'🇭🇺', mk:'🇲🇰',
    mt:'🇲🇹', sq:'🇦🇱', el:'🇬🇷', tr:'🇹🇷', az:'🇦🇿', hy:'🇦🇲', ka:'🇬🇪',
    he:'🇮🇱', yi:'🇮🇱', ar:'🇸🇦', fa:'🇮🇷', ur:'🇵🇰', ps:'🇦🇫', ku:'🇮🇶',
    ckb:'🇮🇶', kk:'🇰🇿', ky:'🇰🇬', uz:'🇺🇿', tg:'🇹🇯', tk:'🇹🇲', mn:'🇲🇳',
    'zh-CN':'🇨🇳','zh-TW':'🇹🇼', ja:'🇯🇵', ko:'🇰🇷', vi:'🇻🇳', th:'🇹🇭',
    lo:'🇱🇦', km:'🇰🇭', my:'🇲🇲', id:'🇮🇩', ms:'🇲🇾', jw:'🇮🇩', su:'🇮🇩',
    tl:'🇵🇭', ceb:'🇵🇭', ilo:'🇵🇭', haw:'🇺🇸', sm:'🇼🇸', mi:'🇳🇿',
    hi:'🇮🇳', bn:'🇧🇩', as:'🇮🇳', mr:'🇮🇳', ta:'🇮🇳', te:'🇮🇳', kn:'🇮🇳',
    ml:'🇮🇳', gu:'🇮🇳', pa:'🇮🇳', ne:'🇳🇵', si:'🇱🇰', or:'🇮🇳', sd:'🇵🇰',
    bho:'🇮🇳', doi:'🇮🇳', sa:'🇮🇳', mai:'🇮🇳', gom:'🇮🇳', dv:'🇲🇻',
    'mni-Mtei':'🇮🇳', lus:'🇮🇳', kri:'🇸🇱', om:'🇪🇹', am:'🇪🇹', ti:'🇪🇷',
    so:'🇸🇴', sw:'🇹🇿', rw:'🇷🇼', lg:'🇺🇬', ny:'🇲🇼', sn:'🇿🇼', mg:'🇲🇬',
    yo:'🇳🇬', ig:'🇳🇬', ha:'🇳🇬', zu:'🇿🇦', xh:'🇿🇦', af:'🇿🇦', st:'🇱🇸',
    nso:'🇿🇦', ts:'🇿🇦', bm:'🇲🇱', ee:'🇬🇭', ak:'🇬🇭', ln:'🇨🇩',
    sv:'🇸🇪', no:'🇳🇴', da:'🇩🇰', fi:'🇫🇮', is:'🇮🇸', et:'🇪🇪', lv:'🇱🇻',
    lt:'🇱🇹', cy:'🇬🇧', gd:'🇬🇧', ga:'🇮🇪', gl:'🇪🇸', ca:'🇪🇸', eu:'🇪🇸',
    co:'🇫🇷', fy:'🇳🇱', lb:'🇱🇺', la:'🇻🇦', hmn:'🇱🇦', ht:'🇭🇹', tt:'🇷🇺',
    ay:'🇧🇴', qu:'🇵🇪', gn:'🇵🇾', eo:'🌐'
  };
  const quickBtn = document.createElement('button');
  quickBtn.id = 'translate-quick-btn';
  quickBtn.type = 'button';
  quickBtn.style.cssText = 'border:none; cursor:pointer; padding:5px 10px; font-size:0.78rem; font-weight:800; border-radius:999px; display:flex; align-items:center; gap:5px; transition:transform 0.08s, box-shadow 0.12s; margin-left:6px;';
  function _getCurrentLang() {
    // 1) On .translate.goog proxy → read _x_tr_tl from URL
    if (location.hostname.endsWith('.translate.goog')) {
      const m = location.search.match(/[?&]_x_tr_tl=([^&]+)/);
      return m ? decodeURIComponent(m[1]) : 'en';
    }
    // 2) On mathagram.org with the in-place widget → parse googtrans cookie
    const ck = document.cookie.split(';').map(s => s.trim()).find(s => s.startsWith('googtrans='));
    if (!ck) return 'en';
    const v = decodeURIComponent(ck.split('=').slice(1).join('=') || '');
    // googtrans value is "/en/es" (source/target) — grab the target
    const m = v.match(/\/[a-z-]*\/([a-zA-Z\-]+)/);
    return m && m[1] ? m[1] : 'en';
  }
  function _flagFor(code) {
    return LANG_FLAGS[code] || LANG_FLAGS[code.split('-')[0]] || '🌐';
  }
  function _renderQuickBtn() {
    const cur = _getCurrentLang();
    if (cur === 'en' || !cur) {
      // English → offer Spanish (Mexican flag for our most-used quick target)
      quickBtn.title = 'Traducir al español';
      quickBtn.setAttribute('aria-label', 'Translate this page to Spanish');
      quickBtn.style.background = 'linear-gradient(135deg,#FF6B6B,#FFD93D)';
      quickBtn.style.color      = '#0f172a';
      quickBtn.style.boxShadow  = '0 2px 6px rgba(255,107,107,0.25)';
      quickBtn.dataset.target   = 'es';
      quickBtn.innerHTML = '<span style="font-size:1rem;line-height:1;">🇲🇽</span><span style="letter-spacing:0.04em;">Español</span>';
    } else {
      // Any other language → always show 🇺🇸 English as the return path
      quickBtn.title = 'Switch back to English';
      quickBtn.setAttribute('aria-label', 'Switch this page back to English from ' + cur);
      quickBtn.style.background = 'linear-gradient(135deg,#3B82F6,#FFFFFF 50%,#EF4444)';
      quickBtn.style.color      = '#0f172a';
      quickBtn.style.boxShadow  = '0 2px 6px rgba(59,130,246,0.25)';
      quickBtn.dataset.target   = 'en';
      quickBtn.innerHTML = '<span style="font-size:1rem;line-height:1;">🇺🇸</span><span style="letter-spacing:0.04em;">English</span>';
    }
  }
  _renderQuickBtn();
  quickBtn.addEventListener('mouseenter', () => { quickBtn.style.transform = 'translateY(-1px)'; });
  quickBtn.addEventListener('mouseleave', () => { quickBtn.style.transform = 'translateY(0)'; });
  quickBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const target = quickBtn.dataset.target || 'es';
    try { translatePage(target); } catch (err) { console.warn('Quick-translate failed:', err); }
  });
  // The googtrans cookie is set asynchronously by the Google Translate widget,
  // so re-render the button briefly after click + on every focus return.
  window.addEventListener('focus', _renderQuickBtn);
  setInterval(_renderQuickBtn, 1500);
  wrapper.appendChild(quickBtn);

  // Insert before the first link in nav
  navLinks.insertBefore(wrapper, navLinks.firstChild);
}

// Suppress Google Translate's UI chrome from BOTH translation paths:
//   (a) the in-place widget that we load on mathagram.org, and
//   (b) the .translate.goog proxy that Google serves with its own banner injected.
// Idempotent — safe to call on every page.
function injectGoogleTranslateSuppressionStyles() {
  if (document.getElementById('google-translate-suppress-style')) return;
  const style = document.createElement('style');
  style.id = 'google-translate-suppress-style';
  // Goals:
  // 1. Hide the in-place widget's "Translated to X | Show original" banner iframe.
  // 2. Hide the .translate.goog proxy's persistent toolbar (top of viewport).
  // 3. Cancel the body offset both banners apply via inline styles.
  // 4. Make Google's <font style="vertical-align: inherit"> wrappers layout-
  //    transparent so they don't break flex/grid or :nth-child() selectors —
  //    this is what otherwise makes the learning-path zigzag and unit headers
  //    collapse once translation runs.
  style.textContent = `
    /* In-place widget chrome */
    .goog-te-banner-frame.skiptranslate, iframe.goog-te-banner-frame { display:none !important; }
    .goog-tooltip, .goog-tooltip:hover, #goog-gt-tt, .goog-te-balloon-frame, .goog-te-spinner-pos { display:none !important; }
    .goog-text-highlight { background:transparent !important; box-shadow:none !important; border:none !important; }
    .skiptranslate iframe { display:none !important; }
    /* .translate.goog proxy banner — Google injects an iframe + a fixed div
       at the top of <body>. Hide both. */
    body > iframe.skiptranslate,
    body > .skiptranslate,
    iframe[src*="translate.goog"],
    iframe[src*="googleusercontent.com"][name*="goog"],
    iframe[name="goog-gt-tt"],
    div[id^="goog-gt-"] { display:none !important; }
    /* Cancel offset both banners apply */
    html { margin-top: 0 !important; }
    body { top: 0 !important; position: static !important; }
    /* Translated text wrappers — must be layout-transparent */
    font[style*="vertical-align: inherit"], font[style*="vertical-align:inherit"] { display: contents !important; }`;
  (document.head || document.documentElement).appendChild(style);
}

// In-place translation via Google Translate Element widget. Loaded once per page,
// then we drive the hidden .goog-te-combo <select> programmatically each time the
// user picks a language from our own dropdown.
let _googTransPromise = null;

function loadGoogleTranslateElement() {
  if (_googTransPromise) return _googTransPromise;
  _googTransPromise = new Promise((resolve, reject) => {
    if (!document.getElementById('google_translate_element')) {
      const host = document.createElement('div');
      host.id = 'google_translate_element';
      host.style.cssText = 'position:fixed; top:-9999px; left:-9999px; opacity:0; pointer-events:none;';
      document.body.appendChild(host);
    }
    injectGoogleTranslateSuppressionStyles();
    window.googleTranslateElementInit = function() {
      try {
        new window.google.translate.TranslateElement({
          pageLanguage: 'en',
          autoDisplay: false,
          layout: window.google.translate.TranslateElement.InlineLayout.SIMPLE
        }, 'google_translate_element');
        const start = Date.now();
        const tryFind = () => {
          const sel = document.querySelector('.goog-te-combo');
          if (sel) resolve(sel);
          else if (Date.now() - start > 6000) reject(new Error('Translate widget did not initialize'));
          else setTimeout(tryFind, 120);
        };
        tryFind();
      } catch (e) { reject(e); }
    };
    const s = document.createElement('script');
    s.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
    s.async = true;
    s.onerror = () => reject(new Error('Translate script failed to load'));
    document.head.appendChild(s);
  });
  return _googTransPromise;
}

// Snapshot the logged-in user's identity into the URL hash so the SAME
// account follows them to the .translate.goog cross-origin proxy:
//   • _mga_u=<base64(JSON profile)>   — name, XP, color (always; for nav badge)
//   • _mga_t=<custom Firebase token>  — only if /api/mga-token is configured;
//     translate.goog uses this to call signInWithCustomToken() and become
//     fully logged in with the same UID + Firestore data.
async function buildUserHashFragment() {
  try {
    const { auth, db } = await import('./firebase-config.js');
    const user = auth?.currentUser;
    if (!user) return '';
    const { doc, getDoc } = await import('https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js');
    let data = {};
    try {
      const snap = await getDoc(doc(db, 'users', user.uid));
      if (snap.exists()) data = snap.data() || {};
    } catch (e) { /* offline / rules issue → fall back to auth profile */ }
    const info = {
      uid: user.uid,
      name: data.name || data.displayName || user.displayName || (user.email || '').split('@')[0] || 'Learner',
      xp: data.xp || 0,
      color: data.avatarColor || data.color || 'blue',
      streak: data.streak || 0,
      ts: Date.now()
    };
    const profilePart = '_mga_u=' + btoa(unescape(encodeURIComponent(JSON.stringify(info))));

    // Try to mint a Firebase custom token via the Netlify Edge Function so
    // translate.goog can fully sign in. If the function isn't configured
    // (env vars missing), this returns 503 and we just skip — display still
    // works via the profile snapshot above.
    let tokenPart = '';
    try {
      const idToken = await user.getIdToken();
      const res = await fetch('/api/mga-token', {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ idToken })
      });
      if (res.ok) {
        const out = await res.json();
        if (out?.customToken) {
          tokenPart = '&_mga_t=' + encodeURIComponent(out.customToken);
        }
      }
    } catch (e) { /* no SSO available, fall back to display-only */ }

    return '#' + profilePart + tokenPart;
  } catch (e) { return ''; }
}

function translatePage(lang) {
  // If we're on the .translate.goog proxy, language switching has to be a navigation.
  if (location.hostname.endsWith('.translate.goog')) {
    if (lang === 'en') {
      const original = location.hostname.replace(/\.translate\.goog$/, '').replace(/-/g, '.');
      const cleaned = location.search.replace(/[?&]_x_tr_[a-z]+=[^&]*/g, '').replace(/^&/, '?');
      window.location.href = `${location.protocol}//${original}${location.pathname}${cleaned}${location.hash}`;
      return;
    }
    const cleaned = location.search.replace(/[?&]_x_tr_[a-z]+=[^&]*/g, '').replace(/^&/, '?');
    const sep = cleaned ? '&' : '?';
    // We're already on translate.goog; preserve any existing #_mga_u info.
    const preservedHash = location.hash && location.hash !== '#' ? location.hash : '';
    window.location.href = `${location.protocol}//${location.hostname}${location.pathname}${cleaned}${sep}_x_tr_sl=en&_x_tr_tl=${encodeURIComponent(lang)}&_x_tr_hl=${encodeURIComponent(lang)}&_x_tr_pto=wapp${preservedHash}`;
    return;
  }

  // Reset to English: clear cookies + drive widget back to ''
  if (lang === 'en') {
    document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
    document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; domain=' + location.hostname;
    if (_googTransPromise) {
      _googTransPromise.then((sel) => { sel.value = ''; sel.dispatchEvent(new Event('change')); }).catch(() => location.reload());
    }
    scheduleResortAfterTranslation('en');
    return;
  }

  // In-place translation: load the widget once, then trigger the language change.
  loadGoogleTranslateElement().then((sel) => {
    sel.value = lang;
    sel.dispatchEvent(new Event('change'));
    scheduleResortAfterTranslation(lang);
  }).catch(async (err) => {
    // Fallback: navigate the SAME tab to the .translate.goog proxy.
    // Using window.open() here would be popup-blocked — we're outside the
    // synchronous user-gesture from the language click by the time this
    // .catch() fires, so browsers refuse to open a new tab.
    console.warn('In-place translate unavailable, navigating to proxy:', err);
    const host = location.hostname;
    if (host === 'localhost' || /^\d+(\.\d+){3}$/.test(host) || !host.includes('.')) {
      // No public hostname to proxy — surface the failure rather than silently doing nothing.
      alert('Translation unavailable on localhost. Please try again on the deployed site.');
      return;
    }
    const proxyHost = host.replace(/\./g, '-') + '.translate.goog';
    const sep = location.search ? '&' : '?';
    const url = `https://${proxyHost}${location.pathname}${location.search}${sep}_x_tr_sl=en&_x_tr_tl=${encodeURIComponent(lang)}&_x_tr_hl=${encodeURIComponent(lang)}&_x_tr_pto=wapp`;
    // Carry the logged-in user's name/XP/color across to translate.goog so
    // the translated page shows the SAME Mathagram identity as on the
    // original origin. Hash fragments survive cross-origin redirects.
    const userHash = await buildUserHashFragment();
    window.location.href = url + userHash;
  });
}

// Re-sort the courses grid alphabetically by *translated* title once translation
// settles. The HTML ships in English-alphabetical order; without this, picking
// Spanish leaves "Algebra → Acting" out of order in the translated locale.
let _resortTimer = null;
let _resortObserver = null;

function scheduleResortAfterTranslation(lang) {
  const grid = document.querySelector('.courses-grid');
  if (!grid) return;

  if (_resortObserver) { _resortObserver.disconnect(); _resortObserver = null; }
  clearTimeout(_resortTimer);

  // Translation arrives in waves; debounce until h3 text stops changing.
  const debounce = () => {
    clearTimeout(_resortTimer);
    _resortTimer = setTimeout(() => sortCourseTilesByTranslatedTitle(grid, lang), 600);
  };

  _resortObserver = new MutationObserver(debounce);
  _resortObserver.observe(grid, { subtree: true, childList: true, characterData: true });
  debounce();
}

function sortCourseTilesByTranslatedTitle(grid, lang) {
  if (_resortObserver) { _resortObserver.disconnect(); _resortObserver = null; }

  // Map Google Translate codes to BCP-47 locale codes for localeCompare.
  const localeMap = { 'zh-CN': 'zh-Hans', 'zh-TW': 'zh-Hant', 'mni-Mtei': 'mni', 'iw': 'he' };
  const locale = localeMap[lang] || lang || 'en';

  const tiles = Array.from(grid.querySelectorAll(':scope > .course-item'));
  if (tiles.length < 2) return;

  const titled = tiles.map(tile => {
    const h3 = tile.querySelector('h3');
    return { tile, title: (h3 ? h3.textContent : '').trim() };
  });
  try {
    titled.sort((a, b) => a.title.localeCompare(b.title, locale, { sensitivity: 'base', usage: 'sort' }));
  } catch (e) {
    titled.sort((a, b) => a.title.localeCompare(b.title));
  }

  // Bail if order didn't change — no need to re-append.
  let changed = false;
  for (let i = 0; i < titled.length; i++) {
    if (titled[i].tile !== tiles[i]) { changed = true; break; }
  }
  if (!changed) return;

  const frag = document.createDocumentFragment();
  for (const { tile } of titled) frag.appendChild(tile);
  grid.appendChild(frag);
}

// ─── Body language class (lang-es / lang-pt) ──────────────────────────
// Same detection logic used by courses.html so language-gated widgets
// (typing finger guide, Ñ button, etc.) work on every page.
function _activeTranslateLang() {
  if (location.hostname.endsWith('.translate.goog')) {
    const m = location.search.match(/[?&]_x_tr_tl=([^&]+)/);
    return m ? decodeURIComponent(m[1]).toLowerCase().split('-')[0] : null;
  }
  const ck = document.cookie.match(/(?:^|; )googtrans=([^;]+)/);
  if (ck) {
    const parts = decodeURIComponent(ck[1]).split('/').filter(Boolean);
    if (parts.length >= 2 && parts[1]) return parts[1].toLowerCase().split('-')[0];
  }
  const html = (document.documentElement.lang || '').toLowerCase();
  if (html && !html.startsWith('en')) return html.split('-')[0];
  return null;
}

function _syncLangClass() {
  if (!document.body) return;
  const lang = _activeTranslateLang();
  document.body.classList.toggle('lang-es', lang === 'es');
  document.body.classList.toggle('lang-pt', lang === 'pt');
}

function _initLangClass() {
  if (!document.body) {
    document.addEventListener('DOMContentLoaded', _initLangClass, { once: true });
    return;
  }
  _syncLangClass();
  // Google Translate finishes asynchronously (cookie write + page re-render
  // can take 1–3s). Poll a handful of times to pick that up without sitting
  // on a permanent timer.
  let i = 0;
  const tick = () => {
    _syncLangClass();
    if (++i < 8) setTimeout(tick, i < 4 ? 500 : 1500);
  };
  setTimeout(tick, 300);
  // Catch explicit <html lang> changes too (in-place widget sets these).
  try {
    new MutationObserver(_syncLangClass).observe(document.documentElement, {
      attributes: true, attributeFilter: ['lang']
    });
  } catch {}
}
