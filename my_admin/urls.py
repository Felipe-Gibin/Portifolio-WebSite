from django.urls import path
from . import views

app_name = 'my_admin'

urlpatterns = [
    path('', views.MyAdminLogin.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('protegido/', views.MyAdminHome.as_view(), name='home'),
    path('protegido/project/new/', views.ProjectAdd.as_view(), name='project_new'),
    path('protegido/project/<slug:slug>/', views.ProjectEdit.as_view(), name='project_edit'),
    path('protegido/project/<slug:slug>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
    path('protegido/tag/new/', views.TagAdd.as_view(), name='tag_new'),
    path('protegido/tag/<slug:slug>/', views.TagEdit.as_view(), name='tag_edit'),
    path('protegido/tag/<slug:slug>/delete/', views.TagDelete.as_view(), name='tag_delete'),
]