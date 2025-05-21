
document.addEventListener("DOMContentLoaded", () => {
    const short_desc = document.getElementById('short-desc');
    const long_desc = document.getElementById('long-desc');
    const counter_short = document.getElementById('counter-short');
    const counter_long = document.getElementById('counter-long');

    function updateShortCounter() {
        counter_short.textContent = `${short_desc.value.length} / ${short_desc.maxLength}`;
    }

    function updateLongCounter() {
        counter_long.textContent = `${long_desc.value.length}`;
    }

    if (short_desc && counter_short) {
        short_desc.addEventListener("input", updateShortCounter);
        updateShortCounter();
    }

    if (long_desc && counter_long) {
        long_desc.addEventListener("input", updateLongCounter);
        updateLongCounter();
    }
});