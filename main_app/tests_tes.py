from .forms import SendEmailForm

# test_tests.py
# Pseudocódigo:
# 1. Importar SendEmailForm do pacote relativo.
# 2. Criar um teste que instancia o formulário com os mesmos dados dos testes originais.
# 3. Imprimir form.errors se form.is_valid() for False.
# 4. Repetir para os três casos que falharam.

# Código:

def test_debug_form_valid_data():
    data = {
        'name': 'Test User',
        'email': 'test@example.com',
        'phone': '+055 011 91234-5678',
        'subject': 'Test Subject',
        'message': 'Hello, this is a test!',
        'captcha_0': 'dummy',
        'captcha_1': 'PASSED',
    }
    form = SendEmailForm(data=data)
    assert form.is_valid(), form.errors

def test_debug_clean_message_strips_html():
    data = {
        'name': 'Test User',
        'email': 'test@example.com',
        'phone': '+055 011 91234-5678',
        'subject': 'Test Subject',
        'message': '<b>Hello</b> <script>alert(1)</script>',
        'captcha_0': 'dummy',
        'captcha_1': 'PASSED',
    }
    form = SendEmailForm(data=data)
    assert form.is_valid(), form.errors

def test_debug_clean_phone_empty_returns_none():
    data = {
        'name': 'Test User',
        'email': 'test@example.com',
        'phone': '',
        'subject': 'Test Subject',
        'message': 'Hello, this is a test!',
        'captcha_0': 'dummy',
        'captcha_1': 'PASSED',
    }
    form = SendEmailForm(data=data)
    assert form.is_valid(), form.errors