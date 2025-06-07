from django.urls import path
from . import views

app_name = 'admin_app'

urlpatterns = [
    path('', views.CustomMyAdminLoginView.as_view(), name='login'),
    path('logout/', views.CustomMyAdminLogoutView.as_view(), name='logout'),
    path('protected/', views.CustomMyAdminHomeView.as_view(), name='home'),
    
    path('protected/emails/', views.SentEmailsView.as_view(), name='email_table'),
    path('protected/email/<int:pk>/', views.SentEmailDetailView.as_view(), name='email_detail'),
    
    path('protected/project/new/', views.ProjectAddView.as_view(), name='project_new'),
    path('protected/project/<slug:slug>/', views.ProjectEditView.as_view(), name='project_edit'),
    path('protected/project/<slug:slug>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    
    path('protected/tag/new/', views.TagAddView.as_view(), name='tag_new'),
    path('protected/tag/<slug:slug>/', views.TagEditView.as_view(), name='tag_edit'),
    path('protected/tag/<slug:slug>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),
    
    path('projects/toggle/<int:pk>/<str:field>/', views.ToggleBooleanFields.as_view(), name='toggle_boolean'),
]