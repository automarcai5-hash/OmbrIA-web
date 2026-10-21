# Web OmbrIA (ombria.es)

Proyecto de trabajo de la web de OmbrIA. Aquí se trabaja todo lo relacionado con ombria.es: contenido, diseño, SEO, formularios y seguridad.

## La empresa
- **OmbrIA**: inteligencia artificial y automatización para **empresas forestales**. Valencia capital (no Bocairent). Fundada en octubre de 2026.
- **Fundador: Marc.** Técnico Superior en Gestión Forestal y del Medio Natural (IES La Creueta, 2022–2024). Trabajo de campo: vivero en Camp de Mirra (2022), desbroces y plantación en Bretaña (2022), áreas cortafuegos con FORESMA (2023) y apeo y plantación en Islandia con la Icelandic Forestry Association (2024). Mensaje: "viene del monte"; quien hace el diagnóstico es quien lo implementa.
- Contacto: info@ombria.es · +34 644 34 24 30 · CP 46021 (debe coincidir en todo el schema).
- Redes: YouTube @Marc·IAForestal, LinkedIn e Instagram (enlazadas en el footer y en `sameAs` del schema).

### Oferta
1. **Llamadas previas: gratuitas** y sin compromiso.
2. **Diagnóstico Inicial IA & Cyber: de pago.** Pasos: auditoría y dibujo de procesos en BPMN (marketing, ventas, delivery y administración) → mejoras y oportunidades (stack, automatización, IA solo si tiene sentido) → revisión de ciberseguridad (accesos, datos, dependencias, riesgos) → roadmap priorizado por impacto y riesgo.
3. **Implementación**: ejecución del roadmap, orquestación de herramientas, agentes y flujos de IA, formación y seguimiento.

Tono: "sin humo", no vender IA por vender. Mantener este mensaje coherente en todas las páginas.

## Infraestructura
- Hosting: **Vercel** (plan gratuito). Código en GitHub `automarcai5-hash/OmbrIA-web`, rama `main`. **Cada push a `main` se publica automáticamente**: pedir confirmación antes de hacer push.
  - El despliegue automático a veces tarda **hasta unos 10–15 minutos** en arrancar (el 2026-10-21 tardó unos 10 min, aunque la conexión con GitHub estaba bien). Esperar antes de darlo por fallido. Ver despliegues con `vercel ls ombria-web` (el CLI de Vercel tiene sesión iniciada como `automarcai5-6363`, proyecto `marc-s-projects5/ombria-web`). Solo si no llega, publicar a mano con `vercel deploy --prod --yes` desde esta carpeta y con el árbol de git limpio.
- Dominio `ombria.es` en **IONOS** (renovación automática, próxima: 15/05/2027). Los DNS apuntan a Vercel (`ombria.es` → 216.198.79.1; `www` → CNAME `vercel-dns-017.com`). `www` redirige a `ombria.es` (308).
- Correo info@ombria.es: IONOS Correo Basic, redirigido a automarcai5@gmail.com.
- Coste aproximado: 46 €/año (10 € el dominio y 36 € el correo).
- Google Analytics 4 `G-SFWQ53K1MT`: lo carga `cookies.js` solo después de que el visitante acepte las cookies. Google Search Console verificado (`google5a9344feb8c55a99.html` y meta en index).
- Más documentación (fuera del repo): `Empresa OmbrIA/Info Página Web OmbrIA i Contrasenyes/`. En parte está desactualizada: la landing ya no es `diagnostico-automatizacion-ia.html` ni usa el webhook `diagnostico-leads`.

## Estructura del código
Web estática: HTML + CSS + JS sin framework ni build.
- Páginas: `index.html`, `servicios.html`, `nosotros.html`, `contacto.html`, `blog.html`, `diagnostico.html` (landing de captación, sin menú; servida en `/diagnostico` por el rewrite de `vercel.json`) y legales (`aviso-legal`, `privacidad`, `cookies`).
- `assets/css/ombria-tech.css`: diseño "HUD forestal" de las páginas principales. Colores y fuentes en variables de `:root` (`--brand #2d9494`, `--neon #3ee6c8`, fondo `--night #06110f`; Space Grotesk / Outfit / JetBrains Mono). Usar las variables, no colores sueltos.
- `cookies.js`: banner de consentimiento y carga de GA4. Va en todas las páginas.
- `assets/utm.js`: guarda las UTMs de entrada en `localStorage` y rellena los campos ocultos `utm_*`, `pagina_entrada` y `referrer` de cualquier formulario. Incluirlo en toda página nueva.
- `blog/`: artículos. Los dos `blog-*.html` de la raíz son antiguos y están huérfanos.
- `assets/antispam.js`: campo trampa y tiempo mínimo en los formularios (ver "Formularios").
- `vercel.json`: cabeceras de seguridad (incluida la CSP), caché de `/assets` y rewrites.
- `.vercelignore`: evita que se publiquen `CLAUDE.md` y `.claude/`.

## Blog: lo publica un bot
El flujo de n8n **Agente creador de blog OmbrIA** (`58WdGeVhd2HAnF2y`) hace commits como "OmbrIA Bot": crea `blog/<slug>.html`, añade la tarjeta en `blog.html` y la URL en `sitemap.xml`.
- Hacer `git pull` antes de trabajar.
- Si cambia la estructura de `blog.html` o la plantilla de los artículos, el flujo puede dejar de encajar: avisar a Marc antes.

## Formularios → ERP
`contacto.html` y `diagnostico.html` envían por `fetch` al webhook `https://ombria-n8n.fhqb2h.easypanel.host/webhook/captacion-leads` (flujo **ERP OmbrIA · 1 · Captación de leads con UTMs** `SkjjNtCU9B1FJcWl`, base del ERP `appM5QdRYE0ATXNic`).
- Cada formulario lleva un campo oculto `formulario` (`contacto` / `diagnostico`) que el ERP usa como fuente. Un formulario nuevo necesita su propio valor.
- Si falla el envío, se muestra un aviso con el email y el teléfono.
- **Lead magnets de la marca personal (2026-10-18):** `plantilla-apps.html` (servida en `/plantilla-apps`, `noindex`, fuera del sitemap) envía a otro webhook, `…/webhook/lead-magnet` (flujo **Marca personal · Lead magnet → ERP** `itHEc4poAv71nK6q`), con `formulario=plantilla-apps` y un campo `recurso`. El lead entra en el mismo CRM del ERP, pero recibe un email con la plantilla en vez del de «te contactamos en 24 h». Tras el formulario (o con `?acceso=1`, el enlace del email) se muestran los 3 prompts. Llega desde el DM de ManyChat del reel de Claude Artifacts con `?utm_source=instagram&utm_medium=reel&utm_campaign=reel-apps&utm_content=reel-apps`.
- **Antispam (2026-10-21):** `assets/antispam.js` añade a cada formulario un campo trampa invisible (`sitio_web_hp`) y exige 2,5 s desde la carga. Cada formulario llama a `ombriaEsBot(form, data)` antes del `fetch`: si es un bot, muestra el éxito sin enviar nada, y el campo trampa se quita de los datos. Un formulario nuevo debe incluir el script y hacer esa llamada. Solo frena a los bots que rellenan el formulario; los que llaman al webhook directamente tendrían que filtrarse en n8n (no está hecho).

## Seguridad (revisada el 2026-10-21)
- HTTPS con TLS 1.3 y certificado de Let's Encrypt renovado por Vercel. `http` → `https` con 308.
- Las cabeceras de `vercel.json` son HSTS (`includeSubDomains`, sin `preload`), `X-Frame-Options`, `nosniff`, `Referrer-Policy`, `Permissions-Policy` y **Content-Security-Policy**.
- La CSP solo permite estos orígenes externos: scripts de `www.googletagmanager.com`, CSS de Google Fonts, `fetch` a `ombria-n8n.fhqb2h.easypanel.host` y Google Analytics, e imágenes de cualquier `https:`. Admite scripts inline (`'unsafe-inline'`). **Si se añade un servicio externo nuevo (un vídeo de YouTube, un mapa, Calendly, otro script…), hay que añadir su dominio a la CSP**, porque si no el navegador lo bloquea. Se prueba con un servidor local que imite las cabeceras y Chrome headless, mirando si la consola muestra "violates the following Content Security Policy".
- La web es estática (sin WordPress, sin base de datos y sin panel), así que tiene muy poca superficie de ataque.

## SEO
- Cada página lleva title, description, `canonical`, Open Graph, Twitter Card y JSON-LD. Al crear o cambiar una página, mantenerlos y actualizar `sitemap.xml`.
- Objetivo: title de 50 a 60 caracteres y description de 150 a 155. Palabra clave principal: "IA / automatización para empresas forestales".

### Kit de auditoría SEO
La skill **`auditoria-seo`** está en [.claude/skills/auditoria-seo/SKILL.md](.claude/skills/auditoria-seo/SKILL.md). Se activa con "audita el SEO" y es una copia del kit original de `Empresa OmbrIA/Skills-HERRAMIENTAS/kit-auditoria-seo/`.
- Analiza 8 categorías con estos pesos: meta 20 %, headings 15 %, imágenes 10 %, enlaces 10 %, OG/social 10 %, schema 10 %, técnico 15 % y contenido 10 %. Genera un dashboard HTML con la nota de 0 a 100 y las 5 correcciones principales.
- Regla: solo datos reales medidos en la web publicada.
- Los informes se guardan en la carpeta del kit (no en este repo, porque se publicarían). El último es `auditoria-seo-ombria-es.html`, del 10/10/2026.

### Estado de la auditoría del 10/10/2026 (revisado el 15/10/2026)
- ✅ Páginas legales, banner de cookies con GA4 tras el consentimiento y enlaces sociales.
- ✅ Código postal unificado (46021).
- ✅ Enlaces `target="<em>blank"` del blog corregidos.
- ⏳ **Imágenes pesadas**: `assets/` ocupa 24 MB y hay JPG de unos 1 MB (`ombria-13/14/16/17/1.jpg`). Falta pasarlas a WebP (máx. 1600 px, unos 150 KB), reducir el hero, usar `<img loading="lazy">` en la galería y aligerar el logo.
- ⏳ **Canibalización por "drones forestales España"**: hay 5 artículos (tecnologia, aplicaciones-tendencias, revolucion, incendios…) y no hay redirecciones 301 en `vercel.json`. Los temas ajenos al sector (Chip Roy, Michael Burry, riesgo existencial, Anthropic) diluyen la autoridad temática.
- ⏳ **Artículos huérfanos**: `blog-agente-ia-empresa-forestal.html` y `blog-automatizacion-procesos-forestales.html` no están en el blog ni en el sitemap.
- ⏳ Titles: home 35 caracteres (corto), contacto 70 y diagnóstico 68 (largos), artículos de 67 a 84.
- ⏳ Errata "ombreia" en `blog/mejores-apps-inteligencia-artificial-gratis.html`.
- ⏳ `/favicon.ico` devuelve 404.

## Forma de trabajar
- Todo en español, también los commits (cortos, estilo "Sección: qué cambia").
- Para probar en local: `python -m http.server` en esta carpeta. Las rutas con `/` inicial (`/cookies.js`, `/diagnostico`) no funcionan abriendo el archivo directamente.
- Nunca poner claves (n8n, Airtable…) en el código de la web: todo lo que hay aquí es público.
