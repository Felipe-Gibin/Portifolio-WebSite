document.addEventListener('DOMContentLoaded', function () {

   // FIXME: Poder ter código do país com 1 ou 3 numeros
  const input = document.querySelector('#input-phone');

  function formatPhone(rawValue) {
    // Remove tudo que não for dígito
    rawValue = rawValue.replace(/\D/g, '');

    // DDI: 3 dígitos (preenche com zero à esquerda)
    let ddi = rawValue.substring(0, 3).padStart(3, '0');
    // DDD: 3 dígitos (preenche com zero à esquerda)
    let ddd = rawValue.substring(3, 6).padStart(3, '0');
    // Local: até 9 dígitos
    let local = rawValue.substring(6, 15);

    let formattedLocal = '';
    if (local.length > 5) {
      formattedLocal = `${local.substring(0, 5)}-${local.substring(5, 9)}`;
    } else {
      formattedLocal = local;
    }

    let formatted = `+${ddi} ${ddd}`;
    if (formattedLocal) {
      formatted += ` ${formattedLocal}`;
    }
    return formatted.trim();
  }


  if (input) {
    input.addEventListener('input', function () {
      // Permite apenas dígitos e '+'
      let rawValue = input.value.replace(/[^\d+]/g, '').substring(0, 16);
      // Remove '+' se não for o primeiro caractere
      input.value = rawValue;
      input.setCustomValidity('');
    });

    input.addEventListener('blur', function () {
      let rawValue = input.value.replace(/\D/g, '');
      if (!rawValue) {
        input.value = '';
        input.setCustomValidity('');
        return;
      }
      input.value = formatPhone(rawValue);

      // Validação: mínimo 10, máximo 15 dígitos
      if (rawValue.length < 10 || rawValue.length > 16) {
        input.setCustomValidity('Por favor, insira um telefone válido com DDI, DDD e número (mín. 10, máx. 15 dígitos).');
      } else {
        input.setCustomValidity('');
      }
    });

    // Para enviar apenas dígitos no submit:
    input.form && input.form.addEventListener('submit', function (e) {
      input.value = input.value.replace(/\D/g, '');
      input.setCustomValidity('');
    });
  }
});
