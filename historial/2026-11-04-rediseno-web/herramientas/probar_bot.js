// Ejecuta en local los 2 nodos cambiados con datos de prueba, imitando a n8n.
const fs = require('fs'), path = require('path');
const W = __dirname;
const datos = {
  'Insertar SEO Links internos | Agente': { message: { content: '```html\n## Cómo ahorrar tiempo en un vivero\nTexto de **prueba** con un [enlace](https://ombria.es/servicios.html) y una fuente [fuente](https://www.mapa.gob.es/es/).\n\n- Punto uno\n- Punto dos\n\n### Subapartado\nOtro párrafo.\n```' } },
  'Generador de Slug | Agente': { message: { content: 'ahorrar tiempo vivero prueba' } },
  'Título del Blog | Agente': { message: { content: 'Cómo ahorrar tiempo en un vivero (prueba)' } },
  'Copy SEO Meta Descripción | Agente': { message: { content: 'Descripción de prueba del artículo.' } },
  'Store Cover Image URL': { 'image-url': 'https://ombria.es/assets/blog-fotos/b6bfbe1b-e83d-427d-be10-c170867b6c33.jpg' },
};
const $ = n => ({ item: { json: datos[n] }, first: () => ({ json: datos[n] }) });
function correr(archivo, $json) {
  const code = fs.readFileSync(path.join(W, archivo), 'utf8');
  return new Function('$', '$json', 'Buffer', code)($, $json, Buffer);
}
// 1) Artículo
const r1 = correr('Preparar_GitHub.js', {});
const html = Buffer.from(r1[0].json.base64_content, 'base64').toString('utf8');
fs.writeFileSync(path.join(W, 'prueba-articulo.html'), html);
console.log('artículo ok:', r1[0].json.slug, '| bytes:', html.length,
  '| css nuevo:', html.includes('ombria-2026.css'), '| categoría:', html.includes('IA medioambiental'),
  '| forestal en plantilla:', (html.match(/forestal/gi) || []).length);
// 2) Índice del blog
const blog = fs.readFileSync(process.argv[2], 'utf8');
const r2 = correr('Preparar_Blog_Index.js', { sha: 'x', content: Buffer.from(blog).toString('base64') });
const nuevo = Buffer.from(r2.json.base64Content, 'base64').toString('utf8');
fs.writeFileSync(path.join(W, 'prueba-blog.html'), nuevo);
console.log('índice ok: tarjetas antes', (blog.match(/<article class="blog-card/g) || []).length, '→ después', (nuevo.match(/<article class="blog-card/g) || []).length);
