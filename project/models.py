from __future__ import annotations
import os
from io import BytesIO
from django.utils.timezone import now
from PIL import Image
from django.db import models
from django.core.files import File
from django.core.files.images import ImageFile
from django.utils.text import slugify
from django.conf import settings
from utils.img_processer import resize_image_square, remove_background

class Project(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(unique=True, blank=True)
    short_desc = models.TextField(max_length=400)
    long_desc= models.TextField(null=True, blank=True)
    img_icon = models.ImageField(upload_to='project_icon/%Y-%m/', null=True, blank=True)
    tags = models.ManyToManyField('Tags', default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def process_img_p(self) -> None:
        """
        Processa a imagem de icone do Projeto
        Ajustando o tamanho
        Alterando o formato para .png, caso necessário
        Alterando o nome para o nome do projeto
        """
        
        # Abre a imagem
        # NOTE: Caso falha na imagem (projeto)
        # '.file' para uso normal
        # '.path' para injeção de dados
        img = Image.open(self.img_icon.path)
        
        # Cria o caminho para a nova imagem
        sub_dir = now().strftime("project_icon/%Y-%m/")
        new_img_file_name = f'{self.name}.{img.format}'
        new_img_path = os.path.join(settings.MEDIA_ROOT, sub_dir, new_img_file_name)
        
        # Garante que o diretório existe
        os.makedirs(os.path.dirname(new_img_path), exist_ok=True)
        
        new_img = resize_image_square(img, 160)
        new_img.save(new_img_path, quality=80)
        with open(new_img_path, 'rb') as f:
            img_file = File(f)
            file_name = f'{self.name}-formated.png'
            self.img_icon.save(file_name, img_file, save=False)
        os.remove(new_img_path)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{count}'
                count += 1
            self.slug = slug
        
        if self.img_icon:
            self.process_img_p()
            
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
class Tags(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, blank=True)
    short_desc = models.TextField(max_length=200)
    long_desc = models.TextField(null=True, blank=True)
    img_icon = models.ImageField(upload_to='tag_icon/%Y-%m/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    # FIXME: Retificar func
    # Criar Func unica para uso em ambos os modelos
    def process_img(self) -> None:
        """
        Processa a imagem da tag
        Removendo fundo branco
        Ajustando o tamanho
        Alterando o formato para .png
        Alterando o nome para o nome da tag
        """
        
        # Abre a imagem
        # NOTE: Caso falha na imagem (tag)
        # '.file' para uso normal
        # '.path' para injeção de dados
        img = Image.open(self.img_icon.path)
        
        # Cria o caminho para a nova imagem
        sub_dir = now().strftime("tag_icon/%Y-%m/")
        new_img_file_name = f'{self.name}.{img.format}'
        new_img_path = os.path.join(settings.MEDIA_ROOT, sub_dir, new_img_file_name)
        
        # Garante que o diretório existe
        os.makedirs(os.path.dirname(new_img_path), exist_ok=True)
        
        # Processa a imagem
        if img.format != 'PNG':
            img = remove_background(img)
        
        new_img = resize_image_square(img, 40)
        new_img.save(new_img_path, quality=60)
        with open(new_img_path, 'rb') as f:
            img_file = File(f)
            file_name = f'{self.name}-formated.png'
            self.img_icon.save(file_name, img_file, save=False)
        os.remove(new_img_path)


        
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while Tags.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{count}'
                count += 1
            self.slug = slug
        
        
        if self.img_icon:
            self.process_img()
        
        super().save(*args, **kwargs)
            

    
    def __str__(self) -> str:
        return f'{self.name}'