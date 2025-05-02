from django.urls import path, include
from . import views

app_name = 'mainSite'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('sobre', views.Sobre.as_view(), name='aboutMe'),
]
