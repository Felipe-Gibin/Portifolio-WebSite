from __future__ import annotations
from django.db import models
from django.utils.text import slugify
from utils.img_processor import process_img
import utils.constants as consts

# Model for Projects
class ProjectModel(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(unique=True, blank=True)
    short_desc = models.TextField(max_length=400)
    long_desc= models.TextField(null=True, blank=True)
    img_icon = models.ImageField(upload_to=consts.MEDIA_PROJECT.name, null=True, blank=True)
    tags = models.ManyToManyField('TagModel', default='', blank=True)
    visibility = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Automatically generate a slug if not provided
        # Ensure the slug is unique by appending a number if necessary
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while ProjectModel.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{count}'
                count += 1
            self.slug = slug
        
        # Process the image icon if it exists
        # If the project already exists, check if the image has changed
        if self.pk:
            old = ProjectModel.objects.filter(pk=self.pk).only("img_icon").first()
            if old and old.img_icon != self.img_icon and self.img_icon:
                self.img_icon = process_img(self.img_icon, self.name)
        else:
            if self.img_icon:
                self.img_icon = process_img(self.img_icon, self.name)
            
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.name}'

# Models for the tags associated with projects
class TagModel(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, blank=True)
    short_desc = models.TextField(max_length=200)
    long_desc = models.TextField(null=True, blank=True)
    img_icon = models.ImageField(upload_to=consts.MEDIA_TAG.name, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
        
    def save(self, *args, **kwargs):
        # Automatically generate a slug if not provided
        # Ensure the slug is unique by appending a number if necessary
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while TagModel.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{count}'
                count += 1
            self.slug = slug
        
        # Process the image icon if it exists
        # If the tag already exists, check if the image has changed
        if self.pk:
            old = TagModel.objects.filter(pk=self.pk).only("img_icon").first()
            if old and old.img_icon != self.img_icon and self.img_icon:
                self.img_icon = process_img(self.img_icon, self.name)
        else:
            if self.img_icon:
                self.img_icon = process_img(self.img_icon, self.name)
        
        super().save(*args, **kwargs)
            
    def __str__(self) -> str:
        return f'{self.name}'