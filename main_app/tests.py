from django.test import TestCase, Client
from django.urls import reverse
from .forms import SendEmailForm

# Test cases for the SendEmailForm
class SendEmailFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'phone': '+055 011 91234-5678',
            'subject': 'Test Subject',
            'message': 'Hello, this is a test!',
            'captcha_0': 'dummy',
            'captcha_1': 'PASSED',
        }

    def test_form_valid_data(self):
        form = SendEmailForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['phone'], '055011912345678')
       

    def test_form_invalid_phone_too_short(self):
        data = self.valid_data.copy()
        data['phone'] = '12345'
        form = SendEmailForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors)

    def test_form_invalid_phone_too_long(self):
        data = self.valid_data.copy()
        data['phone'] = '1' * 17
        form = SendEmailForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors)

    def test_form_invalid_phone_non_digits(self):
        data = self.valid_data.copy()
        data['phone'] = '+abc-def-ghij'
        form = SendEmailForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors)

    def test_clean_message_strips_html(self):
        data = self.valid_data.copy()
        data['message'] = '<b>Hello</b> <script>alert(1)</script>'
        form = SendEmailForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['message'], 'Hello alert(1)')
        assert form.is_valid(), form.errors

    def test_clean_phone_empty_returns_none(self):
        data = self.valid_data.copy()
        data['phone'] = ''
        form = SendEmailForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertIsNone(form.cleaned_data['phone'])
        assert form.is_valid(), form.errors

    def test_captcha_required(self):
        data = self.valid_data.copy()
        data.pop('captcha_0')
        data.pop('captcha_1')
        form = SendEmailForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('captcha', form.errors)

# Test cases for the main_app views      
class MainAppViewsTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        url = reverse('main_app:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_app/home.html')

    def test_about_me_view(self):
        url = reverse('main_app:about_me')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_app/about_me.html')