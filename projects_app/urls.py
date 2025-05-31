from django.urls import path, include
from . import views

app_name = 'projects_app'

urlpatterns = [
    path('', views.ProjectsHome.as_view(), name='home'),
    path('detail/<slug:slug>/', views.ProjectDetail.as_view(), name='project_detail'),
]