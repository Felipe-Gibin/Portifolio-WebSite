from django.urls import path, include
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about-me/', views.AboutMe.as_view(), name='about_me'),
]
