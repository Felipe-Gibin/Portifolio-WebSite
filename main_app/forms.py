import re
import bleach
from django import forms
from main_app.models import EmailModel
from captcha.fields import CaptchaField

# Django form for sending emails
class SendEmailForm(forms.ModelForm):
    # Captcha field for spam protection
    captcha = CaptchaField()
    
    class Meta:
        model = EmailModel
        fields = ['name', 'email', 'phone', 'subject', 'message']
        # Customizing the form widgets
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
    
    # Customizing the form initialization to modify the phone field
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        phone_field = self.fields.get('phone')
        if phone_field:
            phone_field.widget = forms.TextInput(attrs={
                'placeholder': '+000 000 00000-0000',
                'id': 'input-phone'
            })
            phone_field.widget.attrs.pop('maxlength', None)

    # Custom validation fpr the phone field to ensure it contains only digits
    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        if not phone:
            return None
        
        cleaned = re.sub(r'\D', '', phone) 
        if not (10 <= len(cleaned) <= 15):
            raise forms.ValidationError("Type between 10 and 15 digits.")
        return cleaned
    
    # Custom validation for the message field to remove HTML tags
    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        return bleach.clean(message, tags=[], strip=True)
        
        