/* Consentimiento de cookies de OmbrIA.
   Google Analytics (G-SFWQ53K1MT) solo se carga si el visitante pulsa "Aceptar".
   La elección se guarda 12 meses en localStorage ("ombria_consent").
   Cualquier enlace con data-cookie-settings vuelve a abrir el banner. */
(function () {
  var GA_ID = 'G-SFWQ53K1MT';
  var KEY = 'ombria_consent';
  var MAX_AGE = 365 * 24 * 60 * 60 * 1000;

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };

  function read() {
    try {
      var c = JSON.parse(localStorage.getItem(KEY));
      if (c && (c.v === 'granted' || c.v === 'denied') && Date.now() - c.t < MAX_AGE) return c.v;
    } catch (e) {}
    return null;
  }

  function save(v) {
    try { localStorage.setItem(KEY, JSON.stringify({ v: v, t: Date.now() })); } catch (e) {}
  }

  var gaLoaded = false;
  function loadGA() {
    if (gaLoaded) return;
    gaLoaded = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    gtag('js', new Date());
    gtag('config', GA_ID);
  }

  function deleteGACookies() {
    document.cookie.split(';').forEach(function (c) {
      var name = c.split('=')[0].trim();
      if (name.indexOf('_ga') === 0) {
        ['', '; domain=.ombria.es', '; domain=ombria.es'].forEach(function (d) {
          document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + d;
        });
      }
    });
  }

  var css =
    '#ombria-cookies{position:fixed;left:16px;right:16px;bottom:16px;z-index:9999;max-width:760px;margin:0 auto;' +
    'background:#0f1e1e;color:rgba(255,255,255,.85);border:1px solid rgba(45,148,148,.45);border-radius:14px;' +
    'box-shadow:0 10px 40px rgba(0,0,0,.35);padding:20px 22px;font-family:Outfit,system-ui,sans-serif;font-size:.92rem;line-height:1.55}' +
    '#ombria-cookies p{margin:0 0 14px}' +
    '#ombria-cookies strong{color:#fff}' +
    '#ombria-cookies a{color:#7dd9d9}' +
    '#ombria-cookies .oc-btns{display:flex;gap:10px;flex-wrap:wrap}' +
    '#ombria-cookies button{flex:1 1 160px;font:inherit;font-weight:600;padding:11px 18px;border-radius:50px;cursor:pointer;' +
    'border:2px solid #2d9494;background:#2d9494;color:#fff}' +
    '#ombria-cookies button.oc-reject{background:transparent;color:#fff;border-color:rgba(255,255,255,.6)}' +
    '#ombria-cookies button:focus-visible{outline:3px solid #7dd9d9;outline-offset:2px}';

  function showBanner() {
    if (document.getElementById('ombria-cookies')) return;
    if (!document.getElementById('ombria-cookies-css')) {
      var st = document.createElement('style');
      st.id = 'ombria-cookies-css';
      st.textContent = css;
      document.head.appendChild(st);
    }
    var box = document.createElement('div');
    box.id = 'ombria-cookies';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-label', 'Preferencias de cookies');
    box.innerHTML =
      '<p><strong>Usamos cookies de analítica</strong> (Google Analytics) para saber cuántas personas visitan la web y qué páginas les interesan. ' +
      'Solo se activan si las aceptas. Puedes cambiar tu elección cuando quieras. ' +
      '<a href="/cookies.html">Más información</a></p>' +
      '<div class="oc-btns"><button type="button" class="oc-reject">Rechazar</button>' +
      '<button type="button" class="oc-accept">Aceptar</button></div>';
    document.body.appendChild(box);
    box.querySelector('.oc-accept').addEventListener('click', function () {
      save('granted');
      box.remove();
      loadGA();
    });
    box.querySelector('.oc-reject').addEventListener('click', function () {
      var wasGranted = gaLoaded;
      save('denied');
      box.remove();
      deleteGACookies();
      if (wasGranted) location.reload();
    });
  }

  window.ombriaCookies = { open: showBanner };

  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('[data-cookie-settings]');
    if (t) { e.preventDefault(); showBanner(); }
  });

  var choice = read();
  if (choice === 'granted') loadGA();
  else if (choice === null) {
    if (document.body) showBanner();
    else document.addEventListener('DOMContentLoaded', showBanner);
  }
})();
