document.addEventListener("DOMContentLoaded", () => {
    // Criaçao do contador de caracteres para a TextArea

    // Coleta as informações
    const short_desc = document.getElementById('short-desc');
    const long_desc = document.getElementById('long-desc');
    const counter_short = document.getElementById('counter-short');
    const counter_long = document.getElementById('counter-long');

    // Função de atualizacao da TextArea menor
    function updateShortCounter() {
        counter_short.textContent = `${short_desc.value.length} / ${short_desc.maxLength}`;
    }
    
    // Função de atualizacao da TextArea maior
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

    const inputFile = document.getElementById("id_img_icon");
    const customButton = document.getElementById("custom_file_button");
    const fileNameSpan = document.getElementById("file_name");

    // Quando clicar no botão, aciona o input
    customButton.addEventListener("click", () => {
        inputFile.click();
    });

    // Quando um arquivo for escolhido
    inputFile.addEventListener("change", () => {
        const fileName = inputFile.files[0]?.name || "Nenhum arquivo selecionado";
        fileNameSpan.textContent = `File selected: ${fileName}`;
    });
});