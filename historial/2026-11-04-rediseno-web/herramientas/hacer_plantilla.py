import json, re, os
D = os.path.dirname(os.path.abspath(__file__))
h = open(os.path.join(D, 'header.html'), encoding='utf-8').read().replace(' aria-current="page"', '')
f = open(os.path.join(D, 'footer.html'), encoding='utf-8').read()

def absol(t):
    t = re.sub(r'href="(?!https?:|#|mailto:|tel:|/)([^"]+)"', r'href="https://ombria.es/\1"', t)
    t = t.replace('href="/diagnostico"', 'href="https://ombria.es/diagnostico"')
    t = re.sub(r'src="(?!https?:)([^"]+)"', r'src="https://ombria.es/\1"', t)
    return t

h = absol(h).replace('<a href="https://ombria.es/blog.html">', '<a href="https://ombria.es/blog.html" aria-current="page">')
f = absol(f)
cuerpo = open(os.path.join(D, 'plantilla_cuerpo.js'), encoding='utf-8').read()
js = ('// ── PLANTILLA DEL ARTÍCULO · estilo 2026 (web ombria.es) ──\n'
      '// Mismas partes que antes (article-hero, article-container, article-body). Estilos en /assets/css/ombria-2026.css.\n'
      'const OMBRIA_HEADER = ' + json.dumps(h, ensure_ascii=False) + ';\n'
      'const OMBRIA_FOOTER = ' + json.dumps(f, ensure_ascii=False) + ';\n' + cuerpo)
open(os.path.join(D, 'plantilla.js'), 'w', encoding='utf-8').write(js)
print('plantilla.js', len(js))
