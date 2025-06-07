from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.MainHomeView.as_view(), name='home'),
    path('about-me/', views.AboutMeView.as_view(), name='about_me'),
    
]
