import re
from django import forms
from main_app.models import ContactMeEmail

class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMeEmail
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
                'name': forms.TextInput(attrs={
                    'class': 'input-name', 
                    'placeholder': 'Name'
                }),
                'email': forms.TextInput(attrs={
                    'class': 'input-email', 
                    'placeholder': 'Email'
                }),
                'subject': forms.TextInput(attrs={
                    'class': 'input-subject', 
                    'placeholder': 'Subject'
                }),
                'message': forms.Textarea(attrs={
                    'id': 'text', 
                    'class': 'input-text',
                    'placeholder': 'Enter message..'
                }),
            }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        phone_field = self.fields.get('phone')
        if phone_field:
            phone_field.widget = forms.TextInput(attrs={
                'placeholder': '+000 000 00000-0000',
                'id': 'input-phone'
            })
            phone_field.widget.attrs.pop('maxlength', None)
            
    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        if not phone:
            return None
        
        cleaned = re.sub(r'\D', '', phone) 
        if not (10 <= len(cleaned) <= 15):
            raise forms.ValidationError("Type between 10 and 15 digits.")
        return cleaned
        
        