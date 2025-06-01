from __future__ import annotations
from PIL import Image
from pathlib import Path
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files import File
import utils.constants as consts


# Define um novo nome para o arquivo de imagem
def new_image_name(name: str) -> str:
    new_name = "".join(name + '.png')
    
    project_path = consts.MEDIA_PROJECT / new_name
    tag_path = consts.MEDIA_TAG / new_name
    
    if not project_path.exists() or tag_path.exists():
        return new_name

    if project_path.exists() and not tag_path.exists():
        return unique_name(project_path)

    return unique_name(tag_path)

# Garante que o nome do arquivo de imagem seja unico
def unique_name(path: Path) -> str:
    name, _ = path.name.split('.')
    local_path = path
    i = 0
    
    while local_path.exists():
        new_name = ''.join(name + str(i) + '.png')
        local_path = path.parent / new_name
        i += 1
        
    return new_name

def resize_image(image_obj: Image.Image) -> Image.Image:
    img = image_obj.resize((1000, 1000))
    return img
    
    
def process_img(image_obj: File, name: str) -> ContentFile:
    img = Image.open(image_obj)
    
    resize_image(img)
    
    # Salva em memória
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    # Retorna um ContentFile com os dados da imagem
    return ContentFile(buffer.read(), name=new_image_name(name))