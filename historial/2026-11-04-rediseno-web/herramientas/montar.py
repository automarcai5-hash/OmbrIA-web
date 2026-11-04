"""Monta una página de ombria.es con el estilo 2026: cabecera y pie comunes de la portada.
Uso: python montar.py <pagina.html> <cuerpo.html> <cabecera_extra.html>
- cuerpo.html: el contenido entre la cabecera y el pie.
- cabecera_extra.html: primera línea = título; segunda = descripción; resto = JSON-LD u otras etiquetas del <head>.
"""
import sys, os, re
D = os.path.dirname(os.path.abspath(__file__))
pagina, cuerpo, extra = sys.argv[1], sys.argv[2], sys.argv[3]
nombre = os.path.basename(pagina)
url = 'https://ombria.es/' + nombre
lineas = open(extra, encoding='utf-8').read().split('\n', 2)
titulo, desc, resto = lineas[0].strip(), lineas[1].strip(), (lineas[2] if len(lineas) > 2 else '')

hdr = open(os.path.join(D, 'header.html'), encoding='utf-8').read()
hdr = hdr.replace(' aria-current="page"', '')
hdr = hdr.replace(f'<a href="{nombre}">', f'<a href="{nombre}" aria-current="page">')
ftr = open(os.path.join(D, 'footer.html'), encoding='utf-8').read()
scr = open(os.path.join(D, 'scripts.html'), encoding='utf-8').read()
body = open(cuerpo, encoding='utf-8').read()

head = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="icon" type="image/png" href="assets/logo.png" />
  <title>{titulo}</title>
  <meta name="description" content="{desc}" />
  <meta name="robots" content="index, follow" />
  <meta name="author" content="OmbrIA" />
  <link rel="canonical" href="{url}" />
  <meta property="og:title" content="{titulo}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="https://ombria.es/assets/ombria-1.jpg" />
  <meta property="og:locale" content="es_ES" />
  <meta property="og:site_name" content="OmbrIA" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{titulo}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="https://ombria.es/assets/ombria-1.jpg" />
  <meta name="geo.region" content="ES-VC" />
  <meta name="geo.placename" content="Valencia, España" />
  <meta name="theme-color" content="#06110f" />
  <script src="/cookies.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/assets/css/ombria-2026.css" />
{resto.rstrip()}
</head>
<body>

'''
out = head + hdr + '\n' + body.rstrip() + '\n\n' + ftr + '\n' + scr + '</body>\n</html>\n'
open(pagina, 'w', encoding='utf-8').write(out)
t = re.sub(r'<[^>]+>', ' ', re.sub(r'(?s)<(script|style|svg)[^>]*>.*?</\1>', '', body))
print(nombre, 'palabras:', len(t.split()))
