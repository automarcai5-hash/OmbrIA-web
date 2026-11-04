"""Bot del blog con dos líneas que se alternan en cada publicación:
IA medioambiental (como hasta ahora) e IA para empresas (cualquier pyme).
Toca 5 nodos y deja el resultado en flujo-dos-lineas.json (no sube nada)."""
import json, os, sys
W = os.path.dirname(os.path.abspath(__file__))
w = json.load(open(sys.argv[1], encoding='utf-8'))
N = {n['name']: n for n in w['nodes']}
EMP = '(Math.floor($now.ordinal / 2) % 2 === 1)'   # true = toca IA para empresas (alterna en cada ejecución, cada 2 días)
IDX = 'Math.floor($now.ordinal / 4)'                # índice que avanza solo con las ejecuciones de cada línea

MEDIO_SEM = "['jardinería','agricultura','incendios forestales','viveros','desbroce','poda de árboles','riego','parques y jardines','gestión forestal','plagas en cultivos']"
EMP_SEM = "['automatizar procesos','software de gestión','facturación electrónica','presupuestos','CRM','atención al cliente','ChatGPT empresa','inteligencia artificial pymes','gestión de proyectos','kit digital']"

# 1) Google Trends: la semilla depende de la línea
p = N['Get Google Trends']['parameters']['queryParameters']['parameters']
q = [x for x in p if x['name'] == 'q'][0]
viejo = "={{ " + MEDIO_SEM + "[Math.floor($now.ordinal / 2) % 10] }}"
assert q['value'] == viejo, q['value']
q['value'] = "={{ " + EMP + " ? " + EMP_SEM + "[" + IDX + " % 10] : " + MEDIO_SEM + "[" + IDX + " % 10] }}"

# 2) Elegir el mejor tema SEO
m = N['Elegir el mejor tema SEO']['parameters']['messages']['values'][0]
c = m['content']
desc_vieja = ("OmbrIA es una empresa española (Valencia) que implementa inteligencia artificial y automatización en empresas del sector medioambiental y verde: "
              "empresas forestales y de desbroces, jardinería y mantenimiento de parques y zonas verdes, viveros, agricultura y explotaciones agrarias, riego, poda y prevención de incendios. "
              "Sus lectores son dueños y gerentes de esas empresas (pymes y autónomos), técnicos de ayuntamientos y profesionales del campo en España.")
assert desc_vieja in c
reglas_ini = c.index('Elige UN tema para el artículo de hoy con estas reglas:')
reglas_fin = c.index('Devuelve ÚNICAMENTE el tema elegido')
reglas_medio = c[reglas_ini:reglas_fin]
reglas_medio = reglas_medio.replace('[Math.floor($now.ordinal / 2) % 14]', '[' + IDX + ' % 14]')
assert '[' + IDX + ' % 14]' in reglas_medio
reglas_emp = ("Elige UN tema para el artículo de hoy con estas reglas:\n"
  "1. Tiene que interesar de verdad al dueño o gerente de una pyme o autónomo de cualquier sector (servicios, construcción y reformas, comercios, asesorías, clínicas, talleres…): ahorrar tiempo, papeleo, presupuestos, facturas, seguimiento de clientes, ventas, atención al cliente, organización del equipo, datos y seguridad.\n"
  "2. Siempre con un ángulo práctico de automatización o IA aplicada al día a día de la empresa. NO valen noticias de empresas tecnológicas, inversores, lanzamientos de productos, famosos, deportes, política ni economía general, aunque sean tendencia.\n"
  "3. Evita temas que solo interesen al sector medioambiental (jardinería, forestal, viveros, agricultura): eso es la otra línea del blog.\n"
  "4. Si alguna keyword sirve, conviértela en un tema útil y práctico. Ejemplo: «facturación electrónica» → «cómo automatizar la facturación electrónica en una pyme».\n"
  "5. Si ninguna sirve, usa la keyword de reserva de hoy: «{{ ['cómo automatizar presupuestos en una pyme','partes de trabajo digitales para empresas de servicios','automatizar la facturación en pequeñas empresas','CRM sencillo para pymes y autónomos','cómo usar ChatGPT en una empresa sin riesgos con los datos','automatizar el seguimiento de clientes y presupuestos','agentes de inteligencia artificial para atención al cliente en pymes','cómo saber qué tareas automatizar en tu empresa','automatizar correos y respuestas en una pequeña empresa','digitalizar el papeleo de una empresa paso a paso','inteligencia artificial para pymes en España por dónde empezar','ayudas del Kit Digital para digitalizar pymes','protección de datos al usar inteligencia artificial en la empresa','automatizar la gestión de citas y reservas'][" + IDX + " % 14] }}».\n\n")
# n8n: cada bloque va en su propia expresión; el que no toca sale vacío
def bloque(cond, texto):
    return "{{ " + cond + " ? " + json.dumps(texto, ensure_ascii=False) + " : '' }}"
# las reglas llevan {{ }} dentro (la keyword de reserva): se dejan fuera del texto condicional partiéndolas
def bloque_con_reserva(cond, texto):
    a, resto = texto.split('{{ ', 1)
    expr, b = resto.split(' }}', 1)
    return "{{ " + cond + " ? " + json.dumps(a, ensure_ascii=False) + " + (" + expr + ") + " + json.dumps(b, ensure_ascii=False) + " : '' }}"
desc_nueva = ("OmbrIA es una empresa española (Valencia) que implementa inteligencia artificial y automatización en cualquier empresa, con especialidad en el sector medioambiental y verde. "
  "El blog tiene dos líneas que se alternan: «IA medioambiental» (empresas forestales y de desbroces, jardinería y mantenimiento de parques y zonas verdes, viveros, agricultura y explotaciones agrarias, riego, poda y prevención de incendios) "
  "e «IA para empresas» (dueños y gerentes de pymes y autónomos de cualquier sector en España).\n\n"
  "Hoy toca la línea: {{ " + EMP + " ? '«IA para empresas»' : '«IA medioambiental»' }}.")
c = c.replace(desc_vieja, desc_nueva)
reglas_ini = c.index('Elige UN tema para el artículo de hoy con estas reglas:')
reglas_fin = c.index('Devuelve ÚNICAMENTE el tema elegido')
c = c[:reglas_ini] + bloque_con_reserva('!' + EMP, reglas_medio) + bloque_con_reserva(EMP, reglas_emp) + c[reglas_fin:]
m['content'] = c

# 3) Borrador inicial
m = N['Borrador inicial | Agente']['parameters']['messages']['values'][0]
c = m['content']
d_vieja = ("OmbrIA es una empresa española (Valencia) que implementa inteligencia artificial y automatización en empresas del sector medioambiental y verde: "
           "empresas forestales y de desbroces, jardinería y mantenimiento de parques y zonas verdes, viveros, agricultura, riego, poda y prevención de incendios. "
           "Sus lectores son dueños y gerentes de esas empresas (pymes y autónomos), técnicos de ayuntamientos y profesionales del campo en España.")
assert d_vieja in c
d_emp = ("OmbrIA es una empresa española (Valencia) que implementa inteligencia artificial y automatización en cualquier empresa. "
         "Los lectores de este artículo son dueños y gerentes de pymes y autónomos de cualquier sector en España (servicios, construcción y reformas, comercios, asesorías, clínicas, talleres…) que quieren quitarse trabajo repetitivo y papeleo.")
c = c.replace(d_vieja, "{{ " + EMP + " ? " + json.dumps(d_emp, ensure_ascii=False) + " : " + json.dumps(d_vieja, ensure_ascii=False) + " }}")
t1 = '- **Tema**: El tema elegido para hoy, del sector medioambiental'
assert t1 in c
c = c.replace(t1, "- **Tema**: El tema elegido para hoy{{ " + EMP + " ? ', para pymes de cualquier sector' : ', del sector medioambiental' }}")
t2 = '- Sea muy detallado y práctico para las empresas del sector medioambiental español (jardinería, parques, desbroces y trabajos forestales, viveros, agricultura…)'
assert t2 in c
c = c.replace(t2, "- Sea muy detallado y práctico para {{ " + EMP + " ? 'pymes y autónomos españoles de cualquier sector, con ejemplos de negocios reales (una empresa de reformas, una asesoría, un taller, una clínica…)' : 'las empresas del sector medioambiental español (jardinería, parques, desbroces y trabajos forestales, viveros, agricultura…)' }}")
m['content'] = c

# 4) y 5) Etiqueta del artículo y de la tarjeta
CAT = "(Math.floor($now.ordinal / 2) % 2 === 1) ? 'IA para empresas' : 'IA medioambiental'"
n = N['Preparar GitHub']['parameters']
assert n['jsCode'].count("const categoria = 'IA medioambiental';") == 1
n['jsCode'] = n['jsCode'].replace("const categoria = 'IA medioambiental';", "const categoria = " + CAT + ";  // dos líneas que se alternan en cada publicación")
n = N['Preparar Blog Index']['parameters']
assert n['jsCode'].count('<span class="blog-tag">IA medioambiental</span>') == 1
n['jsCode'] = n['jsCode'].replace('const newCard =', "const categoria = " + CAT + ";\nconst newCard =", 1)
n['jsCode'] = n['jsCode'].replace('<span class="blog-tag">IA medioambiental</span>', '<span class="blog-tag">${categoria}</span>')

json.dump(w, open(os.path.join(W, 'flujo-dos-lineas.json'), 'w', encoding='utf-8'), ensure_ascii=False)
for k in ['Get Google Trends', 'Elegir el mejor tema SEO', 'Borrador inicial | Agente']:
    pass
print('ok')
