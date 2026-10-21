/* Antispam de los formularios.
   Añade un campo trampa invisible a cada formulario y mide el tiempo de relleno:
   los bots rellenan todos los campos y envían al instante; una persona no ve el campo.
   Cada formulario llama a ombriaEsBot(form, data) antes de enviar. */
(function () {
  var CAMPO = 'sitio_web_hp';
  var TIEMPO_MINIMO = 2500; // ms desde que carga la página
  var inicio = Date.now();

  function preparar() {
    document.querySelectorAll('form').forEach(function (form) {
      if (form.querySelector('input[name="' + CAMPO + '"]')) return;
      var caja = document.createElement('div');
      caja.setAttribute('aria-hidden', 'true');
      caja.style.cssText = 'position:absolute;left:-10000px;width:1px;height:1px;overflow:hidden;';
      var input = document.createElement('input');
      input.type = 'text';
      input.name = CAMPO;
      input.tabIndex = -1;
      input.autocomplete = 'off';
      caja.appendChild(input);
      form.appendChild(caja);
    });
  }

  // Devuelve true si parece un bot. Quita el campo trampa de los datos que se envían.
  window.ombriaEsBot = function (form, data) {
    var input = form.querySelector('input[name="' + CAMPO + '"]');
    if (data) delete data[CAMPO];
    return Boolean(input && input.value) || Date.now() - inicio < TIEMPO_MINIMO;
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', preparar);
  else preparar();
})();
