from django.apps import AppConfig


class MyAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_app'
