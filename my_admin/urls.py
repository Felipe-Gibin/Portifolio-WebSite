from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'my_admin'

urlpatterns = [
    path('', views.MyAdminLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='my_admin:login'), name='logout'),
    path('protegido/', views.MyAdminLoginTest.as_view(), name='login_success'),
]