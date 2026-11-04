// ── PLANTILLA DEL ARTÍCULO · estilo 2026 (web ombria.es) ──
// Mismas partes que antes (article-hero, article-container, article-body). Estilos en /assets/css/ombria-2026.css.
const OMBRIA_HEADER = "  <header class=\"top\">\n    <div class=\"wrap\">\n      <a href=\"https://ombria.es/\" class=\"logo\"><img src=\"https://ombria.es/assets/logo.png\" alt=\"\" width=\"44\" height=\"44\" /><span>Ombr<b>IA</b></span></a>\n      <nav class=\"menu\" id=\"menu\">\n        <a href=\"https://ombria.es/\">Inicio</a>\n        <a href=\"https://ombria.es/servicios.html\">Servicios</a>\n        <a href=\"https://ombria.es/nosotros.html\">Nosotros</a>\n        <a href=\"https://ombria.es/blog.html\" aria-current=\"page\">Blog</a>\n        <a href=\"https://ombria.es/contacto.html\">Contacto</a>\n      </nav>\n      <a href=\"https://ombria.es/diagnostico\" class=\"btn sm\">Reserva tu llamada</a>\n      <button class=\"burger\" id=\"burger\" aria-label=\"Abrir el menú\" aria-expanded=\"false\"><span></span><span></span><span></span></button>\n    </div>\n  </header>\n";
const OMBRIA_FOOTER = "  <footer>\n    <div class=\"wrap\">\n      <div class=\"row\">\n        <div><a href=\"https://ombria.es/\" class=\"logo\"><img src=\"https://ombria.es/assets/logo.png\" alt=\"\" width=\"44\" height=\"44\" /><span>Ombr<b>IA</b></span></a><p style=\"margin-top:10px;\">IA y automatización para empresas · Valencia<br />info@ombria.es · 644 34 24 30</p></div>\n        <div class=\"social\">\n          <a href=\"https://www.instagram.com/marcchirlaque.ia/\" target=\"_blank\" rel=\"noopener\" aria-label=\"Instagram\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><rect x=\"2\" y=\"2\" width=\"20\" height=\"20\" rx=\"5\"/><circle cx=\"12\" cy=\"12\" r=\"4\"/><circle cx=\"17.5\" cy=\"6.5\" r=\"1\" fill=\"currentColor\" stroke=\"none\"/></svg></a>\n          <a href=\"https://www.linkedin.com/in/marc-chirlaque-zapata-64b06b268/\" target=\"_blank\" rel=\"noopener\" aria-label=\"LinkedIn\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.7c0-1.36-.02-3.1-1.9-3.1-1.9 0-2.2 1.48-2.2 3v5.8H9z\"/></svg></a>\n          <a href=\"https://www.youtube.com/@marcchirlaque\" target=\"_blank\" rel=\"noopener\" aria-label=\"YouTube\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.6A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.6 9.4.6 9.4.6s7.5 0 9.4-.6a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.5v-7l6.3 3.5z\"/></svg></a>\n        </div>\n      </div>\n      <div class=\"legal\" style=\"margin-top:24px;\">\n        <a href=\"https://ombria.es/privacidad.html\">Política de Privacidad</a>\n        <a href=\"https://ombria.es/cookies.html\">Política de Cookies</a>\n        <a href=\"https://ombria.es/aviso-legal.html\">Aviso Legal</a>\n        <a href=\"#\" data-cookie-settings>Configurar cookies</a>\n      </div>\n      <p class=\"copy\">© 2026 OmbrIA. Todos los derechos reservados.</p>\n    </div>\n  </footer>\n";
function construirArticulo(d) {
  const NL = String.fromCharCode(10);
  const heroStyle = 'background: linear-gradient(180deg, rgba(6,17,15,0.35) 0%, rgba(6,17,15,0.92) 100%), url(' + d.imagen + ') center/cover no-repeat;';
  const cta = '<div class="article-cta"><h3>¿Qué puedes automatizar en tu empresa?</h3><p>Te lo decimos en una llamada gratuita y sin compromiso.</p><a href="https://ombria.es/diagnostico?utm_source=blog&utm_medium=organico&utm_content=' + d.slug + '" class="btn light">Reserva tu llamada gratuita →</a></div>';
  return [
    '<!DOCTYPE html>',
    '<html lang="es">',
    '<head>',
    '<meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />',
    '<link rel="icon" type="image/png" href="https://ombria.es/assets/logo.png" />',
    '<title>' + d.titulo + ' | OmbrIA</title>',
    '<meta name="description" content="' + d.metaDesc + '" />',
    '<meta name="robots" content="index, follow" /><meta name="author" content="OmbrIA" />',
    '<link rel="canonical" href="' + d.canonicalUrl + '" />',
    '<meta property="og:title" content="' + d.titulo + '" /><meta property="og:description" content="' + d.metaDesc + '" />',
    '<meta property="og:type" content="article" /><meta property="og:url" content="' + d.canonicalUrl + '" />',
    '<meta property="og:image" content="' + d.imagen + '" /><meta property="og:locale" content="es_ES" /><meta property="og:site_name" content="OmbrIA" />',
    '<meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="' + d.titulo + '" /><meta name="twitter:description" content="' + d.metaDesc + '" /><meta name="twitter:image" content="' + d.imagen + '" />',
    '<meta name="theme-color" content="#06110f" />',
    '<script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"' + d.titulo + '","description":"' + d.metaDesc + '","image":"' + d.imagen + '","author":{"@type":"Organization","name":"OmbrIA","url":"https://ombria.es"},"publisher":{"@type":"Organization","name":"OmbrIA","logo":{"@type":"ImageObject","url":"https://ombria.es/assets/logo.png"}},"datePublished":"' + d.fechaISO + '","dateModified":"' + (d.fechaModISO || d.fechaISO) + '","url":"' + d.canonicalUrl + '","mainEntityOfPage":"' + d.canonicalUrl + '"}</script>',
    '<script src="/cookies.js"></script>',
    '<script src="/assets/utm.js"></script>',
    '<link rel="preconnect" href="https://fonts.googleapis.com" /><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />',
    '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet" />',
    '<link rel="stylesheet" href="/assets/css/ombria-2026.css" />',
    '</head>',
    '<body>',
    OMBRIA_HEADER,
    '<div class="article-hero" style="' + heroStyle + '">',
    '<div class="article-hero-content"><div class="article-meta"><span class="article-tag">' + d.categoria + '</span><span class="article-date">' + d.fechaLegible + '</span><span class="article-read-time">· ' + d.readTimeStr + '</span></div><h1>' + d.titulo + '</h1></div>',
    '</div>',
    '<div class="article-container"><a href="https://ombria.es/blog.html" class="back-link">&#8592; Volver al blog</a><div class="article-body">' + d.articleBody + '</div>' + cta + '</div>',
    OMBRIA_FOOTER,
    '<script>var b=document.getElementById("burger");if(b){b.addEventListener("click",function(){var o=document.getElementById("menu").classList.toggle("open");b.setAttribute("aria-expanded",o);});}</script>',
    '</body></html>'
  ].join(NL);
}
