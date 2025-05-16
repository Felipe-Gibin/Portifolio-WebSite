from django.urls import path
from . import views

app_name = 'my_admin'

urlpatterns = [
    path('', views.MyAdminLogin.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('protegido/', views.MyAdminHome.as_view(), name='home'),
    path('protegido/project/<slug:slug>/', views.ProjectAdd.as_view(), name='projects_form')
]