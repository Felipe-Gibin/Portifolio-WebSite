
document.addEventListener("DOMContentLoaded", () => {

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


    // ------------------------------------------------------
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
    // Criaçao do contador de caracteres para a TextArea
    // ------------------------------------------------------




    // ------------------------------------------------------
    // Pop-up de confirmação de exclusao de registro
    const modal = document.getElementById('confirm-delete-modal');
    const btnYes = document.getElementById('confirm-delete-yes');
    const btnNo = document.getElementById('confirm-delete-no');
    let deleteUrl = '';

    // Para todos os botões, adicione o evento de click
    // Ao clicar, pega o 'data-url' do botão
    document.querySelectorAll('.btn-delete').forEach(btn => {
        btn.addEventListener('click', (e) => {
        e.preventDefault();
        deleteUrl = e.currentTarget.getAttribute('data-url');
        modal.style.display = 'flex';
        });
    });

    // Botão de confirmar a exclusão do registro
    btnYes.addEventListener('click', () => {
        fetch(deleteUrl, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json',
        }
        })
        .then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert("Erro ao deletar.");
            }
    });

    modal.style.display = 'none';
    deleteUrl = '';
    });

    // Botão de negar a exclusão do registro
    btnNo.addEventListener('click', () => {
        modal.style.display = 'none';
        deleteUrl = '';
    });

    // Fecha modal se clicar fora da área do conteúdo
    window.addEventListener('click', (e) => {
        if (e.target == modal) {
        modal.style.display = 'none';
        deleteUrl = '';
        }
    });
    // Pop-up de confirmação de exclusao de registro
    // ------------------------------------------------------
});