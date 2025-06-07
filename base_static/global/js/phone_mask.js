// JavaScript for phone number input formatting
// This script formats phone numbers with DDI, DDD, and local number

document.addEventListener('DOMContentLoaded', function () {

  const input = document.querySelector('#input-phone');

  function formatPhone(rawValue) {
    // Remove everything except digits
    rawValue = rawValue.replace(/\D/g, '');

    // DDI: 3 digtis (fills with zero to the left)
    let ddi = rawValue.substring(0, 3).padStart(3, '0');
    // DDD: 3 digtis (fills with zero to the left)
    let ddd = rawValue.substring(3, 6).padStart(3, '0');
    // Local: rest of the digits (up to 9 digits)
    // If local number has more than 9 digits, it will be truncated
    let local = rawValue.substring(6, 15);

    let formattedLocal = '';
    if (local.length > 5) {
      formattedLocal = `${local.substring(0, 5)}-${local.substring(5, 9)}`;
    } else {
      formattedLocal = local;
    }

    // If DDI or DDD are not provided, they will be filled with zeros
    let formatted = `+${ddi} ${ddd}`;
    if (formattedLocal) {
      formatted += ` ${formattedLocal}`;
    }
    return formatted.trim();
  }


  // Add event listeners to the input field
  // to format the phone number and validate input
  if (input) {
    input.addEventListener('input', function () {
      let rawValue = input.value.replace(/[^\d+]/g, '').substring(0, 16);
      input.value = rawValue;
      input.setCustomValidity('');
    });

    // Format on blur (when the input loses focus)
    input.addEventListener('blur', function () {
      let rawValue = input.value.replace(/\D/g, '');
      if (!rawValue) {
        input.value = '';
        input.setCustomValidity('');
        return;
      }
      input.value = formatPhone(rawValue);

      // Validate length: DDI (3) + DDD (3) + local (7-9) = 10-16 digits total
      if (rawValue.length < 10 || rawValue.length > 16) {
        input.setCustomValidity('Please enter a valid phone number with DDI, DDD and number (min. 10, max. 15 digits).');
      } else {
        input.setCustomValidity('');
      }
    });

    // Make sure to clear the custom validity on form submission
    input.form && input.form.addEventListener('submit', function (e) {
      input.value = input.value.replace(/\D/g, '');
      input.setCustomValidity('');
    });
  }
});
