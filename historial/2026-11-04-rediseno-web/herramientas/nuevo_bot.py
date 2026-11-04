"""Prepara el flujo del blog con la plantilla nueva. Solo cambia 2 nodos de código:
- «Preparar GitHub»: plantilla del artículo (diseño 2026) y categoría «IA medioambiental».
- «Preparar Blog Index»: la etiqueta de la tarjeta («IA medioambiental») y la tilde de «artículo».
No sube nada: deja el resultado en flujo-nuevo.json."""
import json, os, sys
W = os.path.dirname(os.path.abspath(__file__))
copia = sys.argv[1]
w = json.load(open(copia, encoding='utf-8'))
plantilla = open(os.path.join(W, 'plantilla.js'), encoding='utf-8').read()
cambios = 0
for n in w['nodes']:
    if n['name'] == 'Preparar GitHub':
        c = n['parameters']['jsCode']
        assert c.count("const categoria = 'Gestión Forestal';") == 1
        c = c.replace("const categoria = 'Gestión Forestal';", "const categoria = 'IA medioambiental';")
        i = c.index('const css = [')
        j = c.index("const base64_content = Buffer.from(html)")
        nuevo = (plantilla + '\n'
                 "const wordCount = articleBody.replace(/<[^>]+>/g,' ').split(/\\s+/).filter(w=>w.length>2).length;\n"
                 "const readMins = Math.max(2, Math.round(wordCount / 200));\n"
                 "const readTimeStr = readMins + ' min lectura';\n"
                 "const html = construirArticulo({ slug, titulo, metaDesc, imagen, canonicalUrl, fechaISO, fechaLegible, categoria, readTimeStr, articleBody });\n\n")
        n['parameters']['jsCode'] = c[:i] + nuevo + c[j:]
        cambios += 1
    if n['name'] == 'Preparar Blog Index':
        c = n['parameters']['jsCode']
        assert c.count('<span class="blog-tag">IA Forestal</span>') == 1
        c = c.replace('<span class="blog-tag">IA Forestal</span>', '<span class="blog-tag">IA medioambiental</span>')
        c = c.replace('Leer articulo &rarr;', 'Leer artículo &rarr;')
        n['parameters']['jsCode'] = c
        cambios += 1
assert cambios == 2
json.dump(w, open(os.path.join(W, 'flujo-nuevo.json'), 'w', encoding='utf-8'), ensure_ascii=False)
for n in w['nodes']:
    if n['name'] in ('Preparar GitHub', 'Preparar Blog Index'):
        open(os.path.join(W, n['name'].replace(' ', '_') + '.js'), 'w', encoding='utf-8').write(n['parameters']['jsCode'])
print('ok, nodos cambiados:', cambios)
