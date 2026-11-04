// Pasa los artículos publicados de /blog a la plantilla nueva sin tocar su texto.
// Uso: node convertir_articulos.js <carpeta de la web>
const fs = require('fs'), path = require('path');
eval(fs.readFileSync(path.join(__dirname, 'plantilla.js'), 'utf8'));
const web = process.argv[2];
const dir = path.join(web, 'blog');
const EMPRESAS = ['michael-burry-criticas-crecimiento-ia'];
const limpio = t => t.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
let ok = 0;
for (const f of fs.readdirSync(dir).filter(x => x.endsWith('.html'))) {
  let s = fs.readFileSync(path.join(dir, f), 'utf8').replace(/\r\n/g, '\n');
  if (s.includes('/assets/css/ombria-2026.css')) { console.log('ya convertido', f); continue; }
  // Artículo antiguo con el bloque «También te puede interesar» (forestal): se quita y lo sustituye la llamada nueva
  s = s.replace(/<\/div><\/div>\n\n  <!-- Enlazado interno SEO -->\n  <section[\s\S]*?<\/section>\n\n  <footer>/, '</div></div>\n<footer>');
  const slug = f.replace(/\.html$/, '');
  const g = (re, nombre) => { const m = s.match(re); if (!m) throw new Error(f + ': falta ' + nombre); return m[1]; };
  const d = {
    slug,
    titulo: g(/<h1>([\s\S]*?)<\/h1>/, 'h1'),
    metaDesc: g(/<meta name="description" content="([^"]*)"/, 'description'),
    imagen: g(/class="article-hero" style="[^"]*url\(([^)]+)\)/, 'imagen'),
    canonicalUrl: g(/<link rel="canonical" href="([^"]+)"/, 'canonical'),
    fechaISO: g(/"datePublished":"([^"]+)"/, 'datePublished'),
    fechaModISO: g(/"dateModified":"([^"]+)"/, 'dateModified'),
    fechaLegible: g(/<span class="article-date">([^<]*)<\/span>/, 'fecha'),
    readTimeStr: g(/<span class="article-read-time">·\s*([^<]*)<\/span>/, 'lectura'),
    categoria: EMPRESAS.includes(slug) ? 'IA para empresas' : 'IA medioambiental',
    articleBody: g(/<div class="article-body">([\s\S]*?)<\/div><\/div>\n<footer>/, 'cuerpo'),
  };
  const html = construirArticulo(d);
  // comprobación: el cuerpo del artículo sale idéntico
  const nuevoCuerpo = html.match(/<div class="article-body">([\s\S]*?)<\/div><div class="article-cta">/)[1];
  if (nuevoCuerpo !== d.articleBody) throw new Error(f + ': el cuerpo cambió');
  fs.writeFileSync(path.join(dir, f), html);
  ok++;
  console.log('ok', slug, '|', d.categoria, '| palabras:', limpio(d.articleBody).split(' ').length);
}
console.log('convertidos:', ok);
