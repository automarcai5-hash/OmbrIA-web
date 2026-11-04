"""Pasa las páginas legales al estilo 2026 sin tocar el texto legal (solo 'sector forestal' -> 'sector medioambiental')."""
import re, os, subprocess, sys, shutil
W = os.path.dirname(os.path.abspath(__file__))
os.chdir(sys.argv[1])
for f in ['aviso-legal.html', 'privacidad.html', 'cookies.html']:
    s = open(f, encoding='utf-8').read()
    shutil.copy(f, os.path.join(W, f.replace('.html', '-antiguo.html')))
    titulo = re.search(r'<title>(.*?)</title>', s).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)"', s).group(1)
    h1 = re.search(r'<h1>(.*?)</h1>', s).group(1)
    main = re.search(r'(?s)<main class="legal">(.*?)</main>', s).group(1)
    main = main.replace('especialmente del sector forestal', 'especialmente del sector medioambiental')
    cuerpo = f'''  <section class="page-hero legal-hero">
    <div class="wrap">
      <span class="pill">Información legal</span>
      <h1>{h1}</h1>
    </div>
  </section>

  <section class="white">
    <div class="wrap narrow legal-text">
{main.rstrip()}
    </div>
  </section>
'''
    open(os.path.join(W, 'tmp-cuerpo.html'), 'w', encoding='utf-8').write(cuerpo)
    open(os.path.join(W, 'tmp-head.html'), 'w', encoding='utf-8').write(titulo + '\n' + desc + '\n')
    subprocess.run([sys.executable, os.path.join(W, 'montar.py'), f, os.path.join(W, 'tmp-cuerpo.html'), os.path.join(W, 'tmp-head.html')], check=True)
    n = open(f, encoding='utf-8').read()
    n = n.replace('<meta name="robots" content="index, follow" />', '<meta name="robots" content="noindex, follow" />')
    open(f, 'w', encoding='utf-8').write(n)
    # comprobar que el texto legal es el mismo
    limpio = lambda t: ' '.join(re.sub(r'<[^>]+>', ' ', t).split())
    nuevo_main = re.search(r'(?s)<div class="wrap narrow legal-text">(.*?)    </div>\n  </section>', n).group(1)
    print(f, 'texto legal igual:', limpio(nuevo_main) == limpio(main), '| forestal:', n.lower().count('forestal'))
