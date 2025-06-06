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
    
@register.filter
def phone_number_format(phone):
    ddi = phone[:3].zfill(3)
    ddd = phone[3:6].zfill(3)
    local = phone[6:15]
    if len(local) > 5:
        local_formatted = f"{local[:5]}-{local[5:9]}"
    else:
        local_formatted = local
    formatted = f"+{ddi} {ddd}"
    if local_formatted:
        formatted += f" {local_formatted}"
    return formatted.strip()