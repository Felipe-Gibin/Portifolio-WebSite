from __future__ import annotations
from django import forms
from django.contrib import admin
from projects_app import models

# Django admin customization for the Project model
class ProjectFormAdmin(forms.ModelForm):
    class Meta:
        model = models.ProjectModel
        fields = '__all__'
        widgets = {
            'tags': forms.CheckboxSelectMultiple(), 
        }
        
# Django admin dispplay for project model
@admin.register(models.ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', 'visibility', 'featured')
    list_display_links = ('id', 'name')
    form = ProjectFormAdmin
    
# Django admin display for Tag model
@admin.register(models.TagModel)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','created_at', 'updated_at')
    list_display_links = ('id', 'name')
