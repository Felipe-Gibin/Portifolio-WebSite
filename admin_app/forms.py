from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from projects_app.models import Project, Tags

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    error_messages = {
        'invalid_login': "Usuário ou senha incorretos. Tente novamente.",
    }
    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'short_desc', 'long_desc', 'img_icon', 'tags']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input-name', 
                'placeholder': 'Project name'}),
            'short_desc': forms.Textarea(attrs={
                'id': 'short-desc', 
                'class': 'input-short-desc',
                'placeholder': 'Enter a short description..',
                'maxlength': 400}),
            'long_desc': forms.Textarea(attrs={
                'id': 'long-desc',
                'class': 'input-long-desc',
                'placeholder': 'Enter a longer description..'}),
            'img_icon': forms.ClearableFileInput(attrs={'class': 'input-img'}),
            'tags': forms.CheckboxSelectMultiple(),
        }
        
class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['name', 'short_desc', 'long_desc', 'img_icon']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input-name', 
                'placeholder': 'Project name'}),
            'short_desc': forms.Textarea(attrs={
                'id': 'short-desc', 
                'class': 'input-short-desc',
                'placeholder': 'Enter a short description..',
                'maxlength': 200}),
            'long_desc': forms.Textarea(attrs={
                'id': 'long-desc',
                'class': 'input-long-desc',
                'placeholder': 'Enter a longer description..'}),
            'img_icon': forms.ClearableFileInput(attrs={'class': 'input-img'}),
        }
    
