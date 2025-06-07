from django.test import TestCase, Client
from django.urls import reverse
from projects_app.models import ProjectModel, TagModel
from django.contrib.auth.models import User

# Test cases for the projects_app views and models
class ProjectsViewsTests(TestCase):
    def setUp(self):
        self.tag = TagModel.objects.create(name="TestTag")
        self.project = ProjectModel.objects.create(
            name="TestProject",
            short_desc="Short desc",
            long_desc="Long desc",
            created_at="2024-01-01",
            updated_at="2024-01-01",
        )
        self.project.tags.add(self.tag)
        self.client = Client()

    def test_projects_home_view_status_code(self):
        url = reverse('projects_app:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_project_detail_view(self):
        url = reverse('projects_app:project_detail', args=[self.project.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.name)

    def test_projects_home_template_used(self):
        url = reverse('projects_app:home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'projects_app/home.html')

    def test_project_detail_template_used(self):
        url = reverse('projects_app:project_detail', args=[self.project.slug])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'projects_app/project_detail.html')

# Test cases for the projects_app views and models with integration tests
class ProjectsIntegrationTest(TestCase):
    def setUp(self):
        self.tag = TagModel.objects.create(name="IntegrationTag")
        self.project = ProjectModel.objects.create(
            name="IntegrationProject",
            short_desc="Short desc",
            long_desc="Long desc",
            created_at="2024-01-01",
            updated_at="2024-01-01",
        )
        self.project.tags.add(self.tag)
        self.client = Client()

    def test_filter_by_tag(self):
        url = reverse('projects_app:home')
        response = self.client.get(url, {'tag': self.tag.slug})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.name)

# Test cases for the admin permissions in the projects_app
class AdminPermissionsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='adminpass')
        self.client = Client()

    def test_admin_login_required(self):
        url = reverse('admin_app:home')
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)