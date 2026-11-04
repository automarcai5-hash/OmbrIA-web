"""Genera portadas ilustradas (1600x900) para los artículos «IA para empresas».
Escena de oficina (la misma persona de la portada de la web) + una tarjeta grande con un motivo.
Salida: HTML por portada en <dir>/html/ (se capturan después con Edge)."""
import os, sys, re
W = os.path.dirname(os.path.abspath(__file__))
out = sys.argv[1]
os.makedirs(os.path.join(out, 'html'), exist_ok=True)
ilu = open(os.path.join(W, 'ilustracion.svg'), encoding='utf-8').read()
ilu = ilu.replace('<rect width="400" height="500" fill="url(#ilu-bg)"/>', '')
ilu = re.sub(r'<svg class="ilu"[^>]*>', '<svg x="170" y="110" width="640" height="800" viewBox="0 0 400 500">', ilu)
ilu = ilu.replace('class="ilu-p p1"', '').replace('class="ilu-p p2"', '').replace('class="ilu-p p3"', '').replace('class="ilu-spin"', '').replace('class="ilu-steam"', '')

A = '#3ee6c8'; T = '#2d9494'; L = '#eaf4f0'; S = '#9fb8af'; D = '#06110f'
def lineas(x, y, n, w=150, gap=26, op=.6):
    return ''.join(f'<rect x="{x}" y="{y+i*gap}" width="{w - (i%2)*40}" height="10" rx="5" fill="{S}" opacity="{op}"/>' for i in range(n))
def check(cx, cy, r=26):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{A}"/><path d="M{cx-r*.45} {cy} l{r*.32} {r*.32} l{r*.55} -{r*.6}" stroke="{D}" stroke-width="{r*.22}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
doc = lambda x, y, w=210, h=260: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{L}"/>'

MOTIVOS = {
 'presupuesto': doc(-105,-130) + f'<text x="0" y="-40" text-anchor="middle" font-family="Outfit,sans-serif" font-size="90" font-weight="700" fill="{T}">€</text>' + lineas(-70, 10, 4, 140, 24, .9).replace(S, '#8aa39a') + check(95, 120),
 'factura': doc(-105,-130) + ''.join(f'<rect x="-75" y="{-95+i*38}" width="150" height="22" rx="6" fill="{"#d3e6df" if i%2 else "#e6f2ee"}"/>' for i in range(5)) + f'<rect x="-75" y="100" width="150" height="16" rx="8" fill="{T}"/>' + check(95, 120),
 'calendario': f'<rect x="-130" y="-110" width="260" height="230" rx="18" fill="{L}"/><rect x="-130" y="-110" width="260" height="50" rx="18" fill="{T}"/><rect x="-130" y="-80" width="260" height="20" fill="{T}"/>' + ''.join(f'<rect x="{-110+c*56}" y="{-40+r*50}" width="40" height="36" rx="8" fill="{"#3ee6c8" if (r,c)==(1,2) else "#d3e6df"}"/>' for r in range(3) for c in range(4)) + check(110, 110),
 'correo': f'<rect x="-140" y="-90" width="280" height="190" rx="18" fill="{L}"/><path d="M-140 -80 L0 30 L140 -80" fill="none" stroke="{T}" stroke-width="12" stroke-linejoin="round"/>' + check(120, -90, 30),
 'chat': f'<rect x="-150" y="-120" width="220" height="110" rx="26" fill="{L}"/><path d="M-120 -12 l-10 40 l44 -40 z" fill="{L}"/>' + lineas(-120, -90, 2, 150, 30, .9).replace(S, '#8aa39a') + f'<rect x="-40" y="20" width="200" height="100" rx="26" fill="{T}"/><path d="M130 118 l14 38 l-50 -38 z" fill="{T}"/>' + lineas(-12, 48, 2, 140, 30, .9).replace(S, '#bfe9e0'),
 'grafica': f'<rect x="-150" y="-130" width="300" height="260" rx="18" fill="{L}"/>' + ''.join(f'<rect x="{-110+i*60}" y="{90-h}" width="38" height="{h}" rx="8" fill="{T if i<3 else A}"/>' for i, h in enumerate([50, 80, 120, 170])) + f'<path d="M-115 30 L-45 0 L15 -30 L85 -95" fill="none" stroke="{D}" stroke-width="7" stroke-linecap="round"/><path d="M85 -95 l-30 4 m30 -4 l-6 30" stroke="{D}" stroke-width="7" stroke-linecap="round"/>',
 'seguridad': f'<path d="M0 -140 L120 -95 L120 0 C120 80 60 125 0 150 C-60 125 -120 80 -120 0 L-120 -95 Z" fill="{T}"/><rect x="-48" y="-20" width="96" height="80" rx="14" fill="{L}"/><path d="M-30 -20 v-26 a30 30 0 0 1 60 0 v26" fill="none" stroke="{L}" stroke-width="14"/><circle cx="0" cy="15" r="11" fill="{T}"/>',
 'clientes': ''.join(f'<g transform="translate({-20+i*22} {-90+i*62})"><rect x="-120" y="-34" width="240" height="68" rx="16" fill="{L if i!=1 else A}"/><circle cx="-84" cy="0" r="20" fill="{T if i!=1 else D}"/>' + f'<rect x="-50" y="-12" width="120" height="10" rx="5" fill="{S if i!=1 else D}"/><rect x="-50" y="6" width="80" height="9" rx="4.5" fill="{S if i!=1 else D}" opacity=".6"/></g>' for i in range(3)),
 'reloj': f'<circle cx="0" cy="0" r="130" fill="{L}"/><circle cx="0" cy="0" r="112" fill="none" stroke="#d3e6df" stroke-width="8"/>' + ''.join(f'<rect x="-5" y="-105" width="10" height="22" rx="5" fill="{T}" transform="rotate({i*30})"/>' for i in range(12)) + f'<path d="M0 0 L0 -70 M0 0 L52 22" stroke="{D}" stroke-width="12" stroke-linecap="round"/><path d="M-125 -40 A132 132 0 0 1 40 -126" fill="none" stroke="{A}" stroke-width="14" stroke-linecap="round"/><path d="M40 -126 l-26 -14 m26 14 l-12 26" stroke="{A}" stroke-width="12" stroke-linecap="round"/>',
 'movil': f'<rect x="-90" y="-150" width="180" height="300" rx="26" fill="#0a1916" stroke="{L}" stroke-width="10"/>' + ''.join(f'<rect x="-66" y="{-112+i*72}" width="132" height="56" rx="12" fill="{L if i!=1 else A}"/><circle cx="-42" cy="{-84+i*72}" r="12" fill="{T if i!=1 else D}"/><rect x="-22" y="{-90+i*72}" width="70" height="9" rx="4.5" fill="{S if i!=1 else D}"/>' for i in range(3)),
 'engranajes': ''.join(f'<g transform="translate({x} {y}) rotate({r})">' + ''.join(f'<rect x="-{t/2}" y="-{R+20}" width="{t}" height="40" rx="6" fill="{c}" transform="rotate({k*45})"/>' for k in range(8)) + f'<circle r="{R}" fill="{c}"/><circle r="{R*.42}" fill="#0c1d1a"/></g>' for x, y, R, t, c, r in [(-40, -30, 80, 34, L, 10), (95, 85, 52, 24, A, 0)]),
 'tareas': f'<rect x="-140" y="-140" width="280" height="280" rx="20" fill="{L}"/>' + ''.join((check(-95, -85+i*62, 18) if i < 3 else f'<circle cx="-95" cy="{-85+i*62}" r="18" fill="none" stroke="{T}" stroke-width="6"/>') + f'<rect x="-60" y="{-92+i*62}" width="{170-(i%2)*40}" height="14" rx="7" fill="#8aa39a"/>' for i in range(4)),
}
FONDOS = ['#103430', '#0f2f3a', '#12322a', '#14303a']
for i, (nombre, motivo) in enumerate(MOTIVOS.items()):
    f = FONDOS[i % len(FONDOS)]
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{f}"/><stop offset="1" stop-color="#06110f"/></linearGradient>
<radialGradient id="r" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#3ee6c8" stop-opacity=".22"/><stop offset="1" stop-color="#3ee6c8" stop-opacity="0"/></radialGradient></defs>
<rect width="1600" height="900" fill="url(#g)"/>
<g opacity=".07" stroke="#3ee6c8">{''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="900"/>' for x in range(0, 1601, 80))}{''.join(f'<line x1="0" y1="{y}" x2="1600" y2="{y}"/>' for y in range(0, 901, 80))}</g>
<circle cx="1180" cy="430" r="380" fill="url(#r)"/>
{ilu}
<path d="M760 470 C 860 420, 920 420, 990 440" fill="none" stroke="#3ee6c8" stroke-width="4" stroke-dasharray="10 12" opacity=".55"/>
<g transform="translate(1180 430)"><rect x="-230" y="-230" width="460" height="460" rx="40" fill="#0c1d1a" stroke="#3ee6c8" stroke-width="4"/>{motivo}</g>
</svg>'''
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;background:#06110f}}svg{{display:block}}</style></head><body>{svg}</body></html>'
    open(os.path.join(out, 'html', f'empresa-{i+1:02d}-{nombre}.html'), 'w', encoding='utf-8').write(html)
print(len(MOTIVOS), 'portadas')
