from __future__ import annotations
from PIL import Image
from pathlib import Path

def remove_background(image_obj: Image.Image) -> Image.Image:
    """
    Função para remover pixel branco de imagens
    
    Abre a imagem, converte para valores RGBA
    Pega os pixels individuais
    Verifíca se o pixel é branco, se for, o deixa transparente
    se não, adiciona a nova imagem
    """
    
    img = image_obj.convert('RGBA')
    img_data = img.getdata()
    new_img = []

    for pixel in img_data:
        if relative_color(pixel[:3], (255,255,255), 30):
            new_img.append((0, 0, 0, 0))
        else:
            new_img.append(pixel)
    img.putdata(new_img) 
    return img

def relative_color(c1: tuple, c2: tuple, tolerance: int) -> float:
    """
    Verifica se a cor1 está dentro da tolerância da cor2, se são cores próximas uma da outra
    """
    dist = sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5
    return dist < tolerance

def resize_image_square(image_obj: Image.Image, size: int = 200) -> Image.Image:
    img = image_obj.resize((size, size))
    return img

if __name__ == '__main__':
    BASE_DIR = Path(__file__).parent.parent
    PATH_MEDIA = BASE_DIR / 'media' 
    PATH_IMG = PATH_MEDIA / 'test1.jpeg'
    PATH_IMG_RESIZED = PATH_MEDIA / 'test3.png'
    
    img = Image.open(PATH_IMG)
    
    img = remove_background(img)
    new_img_path = PATH_MEDIA / 'test2.png'
    img.save(new_img_path)
    resize_img = resize_image_square(img, 14)
    resize_img.save(PATH_IMG_RESIZED)
    
    
    
    