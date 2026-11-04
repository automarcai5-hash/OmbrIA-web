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
