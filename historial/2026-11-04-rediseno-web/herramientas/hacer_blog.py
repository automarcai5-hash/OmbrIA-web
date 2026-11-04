"""Monta blog.html con el estilo 2026. Conserva las tarjetas y la marca <div class="blog-grid"> que usa el bot de n8n."""
import re, os, sys, subprocess, shutil
W = os.path.dirname(os.path.abspath(__file__))
os.chdir(sys.argv[1])
s = open('blog.html', encoding='utf-8').read().replace('\r\n', '\n')
shutil.copy('blog.html', os.path.join(W, 'blog-antiguo.html'))
ini = s.index('<div class="blog-grid">') + len('<div class="blog-grid">')
fin = s.index('\n      </div>\n    </section>', ini)
tarjetas = re.findall(r'(?s)\s*<article class="blog-card reveal">.*?</article>', s[ini:fin])
EMPRESAS = ['michael-burry-criticas-crecimiento-ia']
vistos, limpias = set(), []
for t in tarjetas:
    slug = re.search(r'href="blog/([^"]+)\.html"', t).group(1)
    if slug in vistos:
        print('repetida, fuera:', slug); continue
    vistos.add(slug)
    cat = 'IA para empresas' if slug in EMPRESAS else 'IA medioambiental'
    t = t.replace('<span class="blog-tag">IA Forestal</span>', f'<span class="blog-tag">{cat}</span>')
    t = t.replace('Leer articulo &rarr;', 'Leer artículo &rarr;')
    limpias.append(t)
print('tarjetas:', len(limpias))

cuerpo = '''  <section class="page-hero">
    <div class="wrap">
      <span class="pill">Blog</span>
      <h1>Ideas para quitarte <em>trabajo de encima</em>.</h1>
      <p class="lead">Casos prácticos de IA y automatización para cualquier empresa, y a fondo para el sector medioambiental.</p>
    </div>
  </section>

  <section class="white">
    <div class="wrap">
      <div class="blog-tabs" role="group" aria-label="Filtrar artículos">
        <button type="button" data-filtro="todos" aria-pressed="true">Todos</button>
        <button type="button" data-filtro="medio" aria-pressed="false">IA medioambiental</button>
        <button type="button" data-filtro="empresas" aria-pressed="false">IA para empresas</button>
      </div>
      <div class="blog-grid">''' + ''.join(limpias) + '''
      </div>
      <p class="blog-empty" id="blog-empty" hidden>Muy pronto, nuevos artículos en esta sección.</p>
    </div>
  </section>

  <section class="cta">
    <div class="wrap">
      <div class="cta-box">
        <h2>¿Qué puedes automatizar en tu empresa?</h2>
        <p>Te lo decimos en una llamada gratuita y sin compromiso.</p>
        <a href="/diagnostico" class="btn light">Reserva tu llamada gratuita →</a>
      </div>
    </div>
  </section>

  <script>
    // Categoría de cada tarjeta según su etiqueta (las tarjetas nuevas las añade el bot del blog)
    (function () {
      var cards = document.querySelectorAll('.blog-card');
      cards.forEach(function (c) {
        var tag = (c.querySelector('.blog-tag') || {}).textContent || '';
        c.dataset.cat = /empresas/i.test(tag) ? 'empresas' : 'medio';
      });
      var botones = document.querySelectorAll('.blog-tabs button');
      botones.forEach(function (b) {
        b.addEventListener('click', function () {
          var f = b.dataset.filtro, visibles = 0;
          botones.forEach(function (x) { x.setAttribute('aria-pressed', x === b); });
          cards.forEach(function (c) {
            var ver = f === 'todos' || c.dataset.cat === f;
            c.hidden = !ver; if (ver) visibles++;
          });
          document.getElementById('blog-empty').hidden = visibles > 0;
        });
      });
    })();
  </script>
'''
head = '''Blog: IA y automatización para empresas y el sector medioambiental | OmbrIA
Casos prácticos de inteligencia artificial y automatización para empresas, y a fondo para el sector medioambiental: forestal, jardinería, viveros y agricultura.
  <meta name="google-site-verification" content="iO-g_4JYqSAIjRQbnookDrGr7Z85VDPK6Jcb-DGQB2k" />
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://ombria.es/"},
      {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://ombria.es/blog.html"}
    ]
  }
  </script>
'''
open(os.path.join(W, 'tmp-cuerpo.html'), 'w', encoding='utf-8').write(cuerpo)
open(os.path.join(W, 'tmp-head.html'), 'w', encoding='utf-8').write(head)
subprocess.run([sys.executable, os.path.join(W, 'montar.py'), 'blog.html', os.path.join(W, 'tmp-cuerpo.html'), os.path.join(W, 'tmp-head.html')], check=True)
n = open('blog.html', encoding='utf-8').read()
assert n.count('<div class="blog-grid">') == 1, 'la marca del bot tiene que estar una sola vez'
print('marca del bot: ok')
