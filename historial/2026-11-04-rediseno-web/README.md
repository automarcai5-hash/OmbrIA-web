# 2026-11-04 · Rediseño de la web y del blog

Conversación con Claude Code, hecha desde el proyecto «Marca personal / Instagram». Marc avisó al final de que debería haberse hecho en el proyecto de la web, así que aquí queda todo para seguir desde este proyecto.

Commits del día en `main`:
- `a5b7956`: landing `/diagnostico` nueva.
- `c67b36c`: rediseño de toda la web.
- El commit siguiente: portadas de empresas y notas del bot.

---

## 1. Qué pidió Marc, en orden

1. **Landing del diagnóstico** (`diagnostico.html`). La pidió más corta y más directa («hay mucho texto»), para empresas en general, con:
   - el bloque «¿No tienes tiempo ni para respirar? Justo por eso.»;
   - el «para qué»: el tiempo que recuperas sirve para hacer crecer la empresa, con más clientes, más negocio y menos estrés.

   Publicada y enlazada con UTM:
   - Instagram: ya estaba enlazada.
   - YouTube: `?utm_source=youtube&utm_content=canal`.
   - LinkedIn: `?utm_source=linkedin&utm_content=perfil`.
2. **«Quitarlo de forestal y darle un meneo» a toda la web.** Primero se hizo una portada en estilo claro, como prueba.
   - Le gustó el contenido, pero **quiso el oscuro de antes** y **quitar su foto de la portada**.
   - Después pidió quitar «Del monte a la IA» y «Últimos artículos» de la portada, porque ya están en Nosotros y en Blog.
   - Para la imagen de la portada: «alguien sentado en una oficina, que la IA le quite trabajo. Invéntatela». Se hizo una **ilustración SVG propia**, animada: papeles que vuelan a la pantalla, café con humo y una tarea cargando.
3. **«IA forestal» le chirría.** El mensaje pasa a ser **IA para cualquier empresa, especializada en el sector medioambiental** (forestal, jardinería, viveros…), en la portada y en Nosotros. En la sección «Para quién» hay dos grupos de etiquetas: «Nuestra especialidad» y «Y también».
4. **Servicios, Nosotros, Contacto y legales**, una a una. A Marc le gustó que fueran **«claras, al grano y cortas, para que la gente no se aburra»**. Esa es la regla para cualquier página nueva.
5. **Blog.** Marc quiere seguir posicionándose en IA medioambiental, pero también para empresas en general. Se decidió:
   - **Dos líneas:** «IA medioambiental» e «IA para empresas», con pestañas en el blog.
   - No borrar los artículos antiguos (ya tienen SEO); solo cambiarles el diseño.
   - Tocar el bot de n8n con una copia guardada antes. Marc: «ahora funciona; luego lo quiero igual».
6. **«Lo de empresas también irá en automático, ¿no? No quiero tocar nada.»** El bot alterna las dos líneas en cada publicación.
7. **«En los de empresas, las fotos no me pongas los campos ni el monte. Invéntatela tú.»** Se hicieron 12 portadas ilustradas propias.
8. **«Si falla, ¿me llega un correo?»** No llegaba: Incidencias solo apuntaba el fallo en el ERP. Se añadió `blog` a las palabras críticas del flujo de Incidencias y ahora llega un email a info@ombria.es.
9. Al final: **«Esto de la web no deberíamos haberlo hecho aquí. Ponlo todo en el CLAUDE.md de la web y pasa la conversación.»** Eso es este archivo.

## 2. Decisiones de diseño (para no repetirlas)

- **Estilo oscuro** (`assets/css/ombria-2026.css`):
  - fondo `#06110f`, turquesa `#2d9494`, neón `#3ee6c8`;
  - fuente Outfit;
  - cabecera y pie comunes, tarjetas con borde fino y CTA final en una caja degradada.
- **Poco texto.** Portada unas 500 palabras, Nosotros unas 230 y Contacto unas 120.
- **Portada** (`index.html`):
  - pill «IA para cualquier empresa · Especialistas en medio ambiente»;
  - h1 «Quitamos el trabajo repetitivo de tu empresa para que tú te dediques a *hacerla crecer*.»;
  - ilustración con 3 avisos («Presupuesto hecho», «Parte del día enviado», «Cliente avisado»);
  - secciones: ¿Te suena? → Cómo trabajamos → **Ejemplos de lo que ya hemos montado** (partes por audio, presupuestos desde notas, seguimiento de clientes, concursos, borradores de correo, seguridad; todo real, sin cifras inventadas) → Para quién → CTA «No esperes a tener tiempo para ganar tiempo».
- **Sin foto de Marc en la portada.** Su foto (`marc-chirlaque-ombria-monte-v2.jpg`) va en Nosotros. Cuando haga la sesión de fotos, se puede cambiar.
- **Servicios:**
  - Paso 1 Diagnóstico Inicial, desde 500 € + IVA por área (llamadas previas gratis).
  - Paso 2 Implementación, con membresía mensual de horas sin permanencia.
  - «Nada de vender una pieza suelta», la guía del diagnóstico (se pide por Contacto) y 4 preguntas desplegables.
  - Sin jerga: fuera «BPMN» y «stack».
- **Nosotros:**
  - «Del monte a la IA» y su historia en 2 frases.
  - La frase destacada «Cuando hablas con OmbrIA, hablas conmigo: hago el diagnóstico y lo implemento».
  - 3 tarjetas (Práctico, Cercano y Honesto) y una línea de tiempo de 2022 a 2026.
- **Contacto:** mismos campos y valores que antes, para que el ERP siga igual. Solo cambian las etiquetas del desplegable.
- **Legales:** el texto es idéntico (comprobado con un script) y siguen con `noindex`. Solo cambia «especialmente del sector forestal» por «medioambiental».
- **UTMs:**
  - Los enlaces internos a `/diagnostico` van sin UTM: `utm.js` usa el último clic y una UTM interna borraría la fuente real (por ejemplo, Instagram).
  - Excepción: el recuadro final de cada artículo lleva `utm_source=blog&utm_medium=organico&utm_content=<slug>`, para saber qué artículo trae clientes.
- **Redes enlazadas:** instagram.com/marcchirlaque.ia, youtube.com/@marcchirlaque y el LinkedIn de siempre. Antes apuntaban a @marc.ia.forestal.

## 3. Blog y bot de n8n

- **Artículos publicados (22):** pasados a la plantilla nueva con `convertir_articulos.js`, que comprueba que el cuerpo queda idéntico.
  - `chip-roy-…` llevaba un bloque blanco «También te puede interesar» con textos forestales; se quitó.
  - Todos llevan ahora la CTA final al diagnóstico.
  - Categoría: «IA para empresas» solo `michael-burry-…`; el resto, «IA medioambiental».
- **`blog.html`:**
  - Conserva **una sola** marca `<div class="blog-grid">` (el bot inserta detrás) y las clases de tarjeta.
  - Se quitó una tarjeta repetida (`incendios-forestales-prevencion-tecnologia`).
  - Pestañas: la categoría sale del texto de `.blog-tag`.
- **Bot «Agente creador de blog OmbrIA» (`58WdGeVhd2HAnF2y`).** Copia de antes en `../../copias-flujos/blog-bot-58WdGeVhd2HAnF2y-2026-11-04-antes-rediseno.json`. Cambiaron 6 nodos (los otros 37 y las conexiones están igual):
  - **Preparar GitHub:** la plantilla `construirArticulo` (diseño 2026) y la categoría según la línea.
  - **Preparar Blog Index:** la etiqueta según la línea.
  - **Get Google Trends:** las semillas de cada línea. Empresas: automatizar procesos, software de gestión, facturación electrónica, presupuestos, CRM, atención al cliente, ChatGPT empresa, IA pymes, gestión de proyectos y Kit Digital.
  - **Elegir el mejor tema SEO:** las reglas y las 14 keywords de reserva de cada línea.
  - **Borrador inicial:** los lectores (pymes de cualquier sector o el sector medioambiental).
  - **Seleccionar Foto Portada:** en la línea de empresas usa `assets/blog-fotos-empresas/` (lista `FOTOS_EMPRESAS`).
- **Qué línea toca:** `Math.floor($now.ordinal / 2) % 2 === 1` → empresas. Como publica cada 2 días, alterna:
  - 2026-11-05 → medioambiental;
  - 2026-11-07 → primera de empresas.

  Las listas usan el índice `Math.floor($now.ordinal / 4)`, para que cada línea recorra todas sus semillas.
- **Portadas de empresas:** 12 ilustraciones de 1600×900, todas con la escena de oficina de la portada y un motivo cada una (presupuesto, factura, calendario, correo, chat, gráfica, seguridad, clientes, reloj, móvil, engranajes y tareas). Las genera `portadas_empresas.py` y se capturan con Edge headless.
- **Avisos de fallo:** en «ERP OmbrIA · 5 · Incidencias» (`hIUa7V6I6rNmx7E3`), nodo «Normalizar incidencia», se añadió `'blog'` a `CRITICOS`. Copia de antes en `../../copias-flujos/incidencias-hIUa7V6I6rNmx7E3-2026-11-04-antes-blog.json`.
- **Pruebas:** en local, con datos falsos y los dos tipos de día (`probar_bot.js` y `probar_dos_lineas.js`). **Falta ver un artículo real:** el del 5 y el del 7 de noviembre.

## 4. Herramientas (`herramientas/`)

| Archivo | Para qué |
|---|---|
| `montar.py` | Monta una página: `<head>` común + `header.html` + cuerpo + `footer.html` + `scripts.html`. Uso: `python montar.py pagina.html cuerpo.html cabecera.html` (la cabecera tiene título en la línea 1, descripción en la 2 y luego el JSON-LD). |
| `*-cuerpo.html`, `*-head.html` | Cuerpos y cabeceras con los que se montaron Servicios, Nosotros y Contacto. |
| `legales.py` | Pasa las 3 legales al estilo nuevo sin tocar el texto y les pone `noindex`. |
| `hacer_blog.py` | Monta `blog.html` con las tarjetas que ya había. |
| `plantilla_cuerpo.js` + `hacer_plantilla.py` → `plantilla.js` | Plantilla del artículo (la misma que lleva el bot). |
| `convertir_articulos.js` | Pasa los artículos de `blog/` a la plantilla (salta los ya convertidos). |
| `portadas_empresas.py` + `ilustracion.svg` | Genera las portadas de la línea de empresas. |
| `nuevo_bot.py`, `bot_dos_lineas.py` | Preparan el JSON del flujo con los cambios (no suben nada). |
| `probar_bot.js`, `probar_dos_lineas.js` | Ejecutan en local los nodos cambiados con datos falsos. |
| `subir_bot.py` | Sube el flujo por la API (lee `N8N_API_URL` y `N8N_API_KEY` del entorno). Antes comprueba que nadie lo haya cambiado desde la copia. |

Los scripts esperan sus archivos en la misma carpeta (`header.html`, `footer.html`…). Si se cambia la cabecera o el pie de la web, hay que regenerar `plantilla.js` y actualizar el nodo «Preparar GitHub» del bot. Si no, los artículos nuevos saldrán con la cabecera antigua.

## 5. Pendiente

- **5 y 7 de noviembre:** mirar el primer artículo de cada línea publicado por el bot.
- Las landings de recursos (`plantilla-apps`, `prompts-campo`, `crm-claude-code`, `buscador-clientes` y `cuestionario-clientes`) siguen con `ombria-tech.css` (el estilo antiguo). Se pueden pasar al nuevo.
- La foto de Nosotros, cuando haya sesión de fotos.
- **Prueba del formulario de `/diagnostico`** desde el móvil, con «PRUEBA»: comprobar que el lead llega al ERP con su fuente y después borrarlo.
- La lista SEO de antes sigue abierta: imágenes pesadas, canibalización por «drones forestales», artículos huérfanos y favicon.
