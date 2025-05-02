from __future__ import annotations
from django.db import models

class Project(models.Model):
    project_name= models.CharField(max_length=40)
    short_desc_project = models.TextField(max_length=400)
    long_desc_project = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tags', default='', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.project_name}'
    
class Tags(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'
    tag_name = models.CharField(max_length=20)
    tag_desc_short = models.TextField(max_length=200)
    tag_desc_long = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.tag_name}'