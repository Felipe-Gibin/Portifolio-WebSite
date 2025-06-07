from django.test import TestCase, Client
from django.urls import reverse
from .forms import ProjectForm, TagsForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from utils.img_processor import generate_test_image

# Test cases for the project form
class ProjectFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'name': 'Test Project',
            'short_desc': 'A short description of the project.',
            'long_desc': 'A longer description of the project.',
            'img_icon': None,
            'tags': [],
            'visibility': True,
            'featured': False,
        }

    def test_form_valid_data(self):
        form = ProjectForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_name_empty(self):
        data = self.valid_data.copy()
        data['name'] = ''
        form = ProjectForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_form_invalid_short_desc_empty(self):
        data = self.valid_data.copy()
        data['short_desc'] = ''
        form = ProjectForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('short_desc', form.errors)

    def test_form_invalid_short_desc_too_long(self):
        data = self.valid_data.copy()
        data['short_desc'] = 'x' * 401
        form = ProjectForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('short_desc', form.errors)
        
    def test_form_invalid_img_icon_invalid_type(self):
        data = self.valid_data.copy()
        fake_file = SimpleUploadedFile("invalid_file.txt", b"not an image", content_type="text/plain")
        form = ProjectForm(data=data, files={'img_icon': fake_file})
        self.assertFalse(form.is_valid())
        self.assertIn('img_icon', form.errors)
        
    def test_form_valid_img_icon(self):
        data = self.valid_data.copy()
        fake_image = generate_test_image()
        form = ProjectForm(data=data, files={'img_icon': fake_image})
        form = ProjectForm(data=data)
        self.assertTrue(form.is_valid())
        
# Test cases for the tags form
class TagsFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'name': 'Test Tag',
            'short_desc': 'A short description of the tag.',
            'long_desc': 'A longer description of the tag.',
            'img_icon': None,
        }
        
    def test_form_valid_data(self):
        form = TagsForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
        
    def test_form_invalid_name_empty(self):
        data = self.valid_data.copy()
        data['name'] = ''
        form = TagsForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        
    def test_form_invalid_short_desc_empty(self):
        data = self.valid_data.copy()
        data['short_desc'] = ''
        form = TagsForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('short_desc', form.errors)
        
    def test_form_invalid_short_desc_too_long(self):
        data = self.valid_data.copy()
        data['short_desc'] = 'x' * 201
        form = TagsForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('short_desc', form.errors)
        
    def test_form_invalid_img_icon_invalid_type(self):
        data = self.valid_data.copy()
        fake_file = SimpleUploadedFile("invalid_file.txt", b"not an image", content_type="text/plain")
        form = TagsForm(data=data, files={'img_icon': fake_file})
        self.assertFalse(form.is_valid())
        self.assertIn('img_icon', form.errors)
        
    def test_form_valid_img_icon(self):
        data = self.valid_data.copy()
        fake_image = generate_test_image()
        form = TagsForm(data=data, files={'img_icon': fake_image})
        print(form.errors)
        self.assertTrue(form.is_valid())
        
# Test cases for the admin app authentication
class AdminAppAuthTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='adminpass')
        self.client = Client()

    def test_login_required_for_admin_home(self):
        url = reverse('admin_app:home')
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)