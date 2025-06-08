from __future__ import annotations
from typing import BinaryIO
from PIL import Image, UnidentifiedImageError
from PIL.Image import DecompressionBombError
from pathlib import Path
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files import File
import utils.constants as consts
from django.core.files.uploadedfile import SimpleUploadedFile
import io

# Function to generate a new image name based on the provided name
def new_image_name(name: str, ext: str = ".png") -> str:
    new_name = name.replace(" ", "_") + ext
    
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
def resize_image(image_obj: Image.Image, max_side: int = 800) -> Image.Image:
    original_size = image_obj.size
    img = image_obj.copy()
    width, height = img.size
    if width > height:
        new_width = max_side
        new_height = int((max_side / width) * height)
    else:
        new_height = max_side
        new_width = int((max_side / height) * width)
        
    img = img.resize((new_width, new_height), Image.LANCZOS)
    
    return img
    
# Function to process an image file, resizing it and returning a ContentFile
def process_img(image_obj: File , name: str, max_side: int = 800) -> ContentFile | None:
    
    try:
        img = Image.open(image_obj)
        img_format = img.format
        img = resize_image(img, max_side=max_side)
        # Save the resized image to a BytesIO buffer
        buffer = BytesIO()
        
        # Determine the image format and save accordingly
        if img_format == 'PNG':
            img.save(buffer, format='PNG', optimize=True, compress_level=9)
            ext = '.png'
        elif img_format in ['JPEG', 'JPG']:
            img = img.convert("RGB")
            img.save(buffer, format='JPEG', quality=85, optimize=True)
            ext = '.jpg'
        else:
            # fallback to PNG if format is not recognized
            img.save(buffer, format='PNG', optimize=True, compress_level=9)
            ext = '.png'
        buffer.seek(0)

        # Create a new ContentFile with the resized image
        return ContentFile(buffer.read(), name=new_image_name(name, ext))
    except DecompressionBombError as e:
        # Handle the case where the image is too large
        print(f"[FLAG] Image processing error: {name} - {e}")
    except UnidentifiedImageError as e:
        # Handle the case where the image cannot be identified
        print(f"[FLAG] Unidentified image error: {name} - {e}")
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"[FLAG] Unexpected error processing image {name}: {e}")
    return None
        

# Function to generate a test image for testing purposes
def generate_test_image():
    file = io.BytesIO()
    image = Image.new('RGB', (10, 10), color='red')
    image.save(file, 'PNG')
    file.seek(0)
    return SimpleUploadedFile('test.png', file.read(), content_type='image/png')