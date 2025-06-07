from django.urls import path
from . import views

app_name = 'projects_app'

urlpatterns = [
    path('', views.ProjectsHomeView.as_view(), name='home'),
    path('detail/<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
]