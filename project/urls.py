from django.urls import path, include
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.ProjectList.as_view(), name='projectList'),
    path('detalhe/', views.ProjectItem.as_view(), name='projectDetail'),
]