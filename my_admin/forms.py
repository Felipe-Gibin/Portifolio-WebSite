from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from project.models import Project, Tags

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    error_messages = {
        'invalid_login': "Usuário ou senha incorretos. Tente novamente.",
    }
    
class ProjectAddForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'short_desc', 'long_desc', 'img_icon']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }
    
