// JavaScript for counter of characters in TextArea and file input handling

document.addEventListener("DOMContentLoaded", () => {

    const short_desc = document.getElementById('short-desc');
    const long_desc = document.getElementById('long-desc');
    const counter_short = document.getElementById('counter-short');
    const counter_long = document.getElementById('counter-long');

    // Function to update the character counter for the short description
    function updateShortCounter() {
        counter_short.textContent = `${short_desc.value.length} / ${short_desc.maxLength}`;
    }
    
    // Function to update the character counter for the long description
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


    // File input handling
    // Get the file input, custom button, and file name display elements
    const inputFile = document.getElementById("id_img_icon");
    const customButton = document.getElementById("custom_file_button");
    const fileNameSpan = document.getElementById("file_name");

    customButton.addEventListener("click", () => {
        inputFile.click();
    });

    // Update the file name display when a file is selected
    inputFile.addEventListener("change", () => {
        const fileName = inputFile.files[0]?.name || "No file selected";
        fileNameSpan.textContent = `File selected: ${fileName}`;
    });
});