from django.contrib import admin
from .models import ContactMeEmail

@admin.register(ContactMeEmail)
class ContactMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'email_send', 'created_at')
    list_display_links = ('id', 'name', 'email')
    
