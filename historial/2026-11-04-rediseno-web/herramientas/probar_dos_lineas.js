// Resuelve en local las expresiones {{ }} de los nodos cambiados para un día de cada línea,
// y ejecuta los dos nodos de código. Así se ve el texto exacto que recibirá la IA.
const fs = require('fs'), path = require('path');
const W = __dirname;
const w = JSON.parse(fs.readFileSync(path.join(W, 'flujo-dos-lineas.json'), 'utf8'));
const N = Object.fromEntries(w.nodes.map(n => [n.name, n]));
const stub = {
  'Get Google Trends': { search_parameters: { q: 'SEMILLA' } },
  'Extraer TOP 2': { 'most-trending': { '#1': { query: 'KW1' }, '#2': { query: 'KW2' } } },
  'Elegir el mejor tema SEO': { message: { content: 'TEMA ELEGIDO' } },
  'Insertar SEO Links internos | Agente': { message: { content: '## Hola\nTexto.' } },
  'Generador de Slug | Agente': { message: { content: 'prueba slug' } },
  'Título del Blog | Agente': { message: { content: 'Título prueba' } },
  'Copy SEO Meta Descripción | Agente': { message: { content: 'Desc' } },
  'Store Cover Image URL': { 'image-url': 'https://ombria.es/x.jpg' },
};
const $ = n => ({ item: { json: stub[n] }, first: () => ({ json: stub[n] }) });
function resolver(tpl, $now) {
  return tpl.replace(/^=/, '').replace(/\{\{([\s\S]*?)\}\}/g, (_, e) => String(new Function('$', '$now', '$json', 'return (' + e + ')')($, $now, { result: 'OTRAS', research: 'INVESTIGACION' })));
}
for (const ordinal of [309, 311]) {
  const $now = { ordinal };
  const linea = Math.floor(ordinal / 2) % 2 === 1 ? 'EMPRESAS' : 'MEDIOAMBIENTAL';
  console.log('\n########## día', ordinal, '→', linea);
  const q = N['Get Google Trends'].parameters.queryParameters.parameters.find(x => x.name === 'q').value;
  console.log('Trends q:', resolver(q, $now));
  const t = resolver(N['Elegir el mejor tema SEO'].parameters.messages.values[0].content, $now);
  console.log('--- Elegir tema ---\n' + t);
  const b = resolver(N['Borrador inicial | Agente'].parameters.messages.values[0].content, $now);
  console.log('--- Borrador (inicio) ---\n' + b.slice(0, 1400));
  const run = (name, $json) => new Function('$', '$json', '$now', 'Buffer', N[name].parameters.jsCode)($, $json, $now, Buffer);
  const r1 = run('Preparar GitHub', {});
  const html = Buffer.from(r1[0].json.base64_content, 'base64').toString();
  console.log('Artículo, etiqueta:', html.match(/<span class="article-tag">([^<]*)/)[1]);
  const r2 = run('Preparar Blog Index', { sha: 'x', content: Buffer.from('<div class="blog-grid">').toString('base64') });
  console.log('Tarjeta, etiqueta:', Buffer.from(r2.json.base64Content, 'base64').toString().match(/<span class="blog-tag">([^<]*)/)[1]);
}
