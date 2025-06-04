from django import forms
import re
from main_app.models import ContactMeEmail

class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMeEmail
        fields = ['name', 'email', 'phone', 'text']
        widgets = {
                'name': forms.TextInput(attrs={
                    'class': 'input-name', 
                    'placeholder': 'Name'
                }),
                'email': forms.TextInput(attrs={
                    'class': 'input-email', 
                    'placeholder': 'Name'
                }),
                'text': forms.Textarea(attrs={
                    'id': 'text', 
                    'class': 'input-text',
                    'placeholder': 'Enter text..'
                }),
            }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        phone_field = self.fields.get('phone')
        if phone_field:
            phone_field.widget = forms.TextInput(attrs={
                'placeholder': '+55 11 98888-7777',
                'id': 'input-phone'
            })
            phone_field.widget.attrs.pop('maxlength', None)
            
    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        cleaned = re.sub(r'\D', '', phone) 
        if len(cleaned) != 13:
            raise forms.ValidationError("Type only 13 digits.")
        return cleaned
        
        