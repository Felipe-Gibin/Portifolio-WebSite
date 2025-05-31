from django.urls import path
from . import views

app_name = 'admin_app'

urlpatterns = [
    path('', views.MyAdminLogin.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('protected/', views.MyAdminHome.as_view(), name='home'),
    
    path('protected/project/new/', views.ProjectAdd.as_view(), name='project_new'),
    path('protected/project/<slug:slug>/', views.ProjectEdit.as_view(), name='project_edit'),
    path('protected/project/<slug:slug>/delete/', views.ProjectDelete.as_view(), name='project_delete'),
    
    path('protected/tag/new/', views.TagAdd.as_view(), name='tag_new'),
    path('protected/tag/<slug:slug>/', views.TagEdit.as_view(), name='tag_edit'),
    path('protected/tag/<slug:slug>/delete/', views.TagDelete.as_view(), name='tag_delete'),
]