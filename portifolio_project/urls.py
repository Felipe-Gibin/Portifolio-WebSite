from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

app_name='portifolio_project'

urlpatterns = [
    path('', include('main_app.urls')),
    path('projects/', include('projects_app.urls')),
    path('admin/', include(('admin_app.urls', 'admin_app'), namespace='admin-a')),
    path('captcha/', include('captcha.urls')),
]

# Disable the django admin and reload script if debug is False
if settings.DEBUG:
    urlpatterns.append(path('dj-admin/', admin.site.urls))
    urlpatterns.append(path("__reload__/", include("django_browser_reload.urls")))

# Static and media files configuration
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)