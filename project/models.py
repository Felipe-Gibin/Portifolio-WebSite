from __future__ import annotations
from typing import Iterable
from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(unique=True, blank=True)
    short_desc = models.TextField(max_length=400)
    long_desc= models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tags', default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{count}'
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
class Tags(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, blank=True)
    desc_short = models.TextField(max_length=200)
    desc_long = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while Tags.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{count}'
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.name}'