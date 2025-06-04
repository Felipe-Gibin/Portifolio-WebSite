document.addEventListener('DOMContentLoaded', function () {
  const input = document.querySelector('#input-phone');
  let cleave = null;

  function applyPhoneMask() {
    cleave = new Cleave(input, {
      delimiters: [' ', ' ', '-'],
      blocks: [3, 2, 5, 4],
      numericOnly: true,
      noImmediatePrefix: true,
      prefix: '+',
      rawValueTrimPrefix: true
    });
  }

  if (input) {
    applyPhoneMask()

    input.addEventListener('input', function () {
      if (input.value === '' || input.value === '+') {
        cleave.destroy();
        input.value = '';
        setTimeout(() => {
           applyPhoneMask();
        }, 10);
      }
    });

    input.addEventListener('blur', function () {
      if (input.value === '+') {
        input.value = '';
      }
    });
  }
});
