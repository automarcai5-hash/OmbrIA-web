/* Captura de UTMs para el ERP.
   Guarda las UTMs de la URL de entrada (se mantienen aunque la visita cambie de página)
   y rellena los campos ocultos utm_* de cualquier formulario de la web. */
(function () {
  var CAMPOS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'];
  var CLAVE = 'ombria_utm';

  function leer() {
    try { return JSON.parse(localStorage.getItem(CLAVE)) || {}; } catch (e) { return {}; }
  }
  function guardar(datos) {
    try { localStorage.setItem(CLAVE, JSON.stringify(datos)); } catch (e) {}
  }

  var params = new URLSearchParams(window.location.search);
  var nuevas = {};
  CAMPOS.forEach(function (c) { if (params.get(c)) nuevas[c] = params.get(c); });

  var datos = leer();
  if (Object.keys(nuevas).length) {
    // Una campaña nueva sustituye a la anterior (último clic)
    datos = nuevas;
    datos.pagina_entrada = window.location.pathname;
    datos.referrer = document.referrer || '';
    guardar(datos);
  } else if (!datos.pagina_entrada) {
    datos.pagina_entrada = window.location.pathname;
    datos.referrer = document.referrer || '';
    guardar(datos);
  }

  function rellenar() {
    document.querySelectorAll('form').forEach(function (form) {
      CAMPOS.concat(['pagina_entrada', 'referrer']).forEach(function (c) {
        var input = form.querySelector('input[name="' + c + '"]');
        if (!input) {
          input = document.createElement('input');
          input.type = 'hidden';
          input.name = c;
          form.appendChild(input);
        }
        input.value = datos[c] || '';
      });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', rellenar);
  else rellenar();
})();
