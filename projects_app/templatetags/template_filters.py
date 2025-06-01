from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def img_or_default(imagem, fallback_url='/media/defaults/image_not_found_placeholder.jpg'):
    try:
        return imagem.url
    except ValueError:
        return fallback_url