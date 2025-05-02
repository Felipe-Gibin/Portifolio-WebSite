from __future__ import annotations
from django import forms
from django.contrib import admin
from project import models

class ProjectFormAdmin(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = '__all__'
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),  # Exibe como checkboxes
        }
        

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'created_at', 'updated_at')
    list_display_links = ('id', 'project_name')
    form = ProjectFormAdmin
    
@admin.register(models.Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name', 'updated_at')
    list_display_links = ('id', 'tag_name')
