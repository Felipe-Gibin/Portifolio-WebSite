from django import template

register = template.Library()

# Custom template filter for getting items from a dictionary
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# Custom template filter for formatting image URLs or returning a default image URL
@register.filter
def img_or_default(imagem, fallback_url='/static/global/images/image_not_found_placeholder.jpg'):
    if not imagem:
        return fallback_url
    try:
        if hasattr(imagem, 'url') and imagem.name:
            return imagem.url
    except Exception:
        pass
    return fallback_url

# Custom template filter for formatting phone numbers
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