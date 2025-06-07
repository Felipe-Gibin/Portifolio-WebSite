from __future__ import annotations
from PIL import Image
from pathlib import Path
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files import File
import utils.constants as consts
from django.core.files.uploadedfile import SimpleUploadedFile
import io

# Function to generate a new image name based on the provided name
def new_image_name(name: str) -> str:
    new_name = name.replace(" ", "_")
    new_name += ".png"
    
    project_path = consts.MEDIA_PROJECT / new_name
    tag_path = consts.MEDIA_TAG / new_name
    
    if not project_path.exists() and not tag_path.exists():
        return new_name

    if project_path.exists():
        return unique_name(project_path)

    return unique_name(tag_path)

# Function to generate a unique name for an image file if it already exists
def unique_name(path: Path) -> str:
    name = path.stem
    ext = path.suffix
    new_path = path
    counter = 1
    
    while new_path.exists():
        new_name = f"{name}{counter}{ext}"
        new_path = path.parent / new_name
        counter += 1
        
    return new_path.name

# Function to resize an image to 1000x1000 pixels
# FIXME: this function should be more flexible, allowing different sizes
def resize_image(image_obj: Image.Image) -> Image.Image:
    img = image_obj.resize((1000, 1000))
    return img
    
# Function to process an image file, resizing it and returning a ContentFile
def process_img(image_obj: File, name: str) -> ContentFile:
    img = Image.open(image_obj)
    
    resize_image(img)
    
    # Save the resized image to a BytesIO buffer
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    # Create a new ContentFile with the resized image
    return ContentFile(buffer.read(), name=new_image_name(name))

# Function to generate a test image for testing purposes
def generate_test_image():
    file = io.BytesIO()
    image = Image.new('RGB', (10, 10), color='red')
    image.save(file, 'PNG')
    file.seek(0)
    return SimpleUploadedFile('test.png', file.read(), content_type='image/png')