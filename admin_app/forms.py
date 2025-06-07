from django import forms
from django.contrib.auth import authenticate
from projects_app.models import ProjectModel, TagModel

# Custom authentication form for user login
class CustomMyAdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    error_messages = {
        'invalid_login': "Username or password is incorrect.",
    }
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
    
    # Customizing the form fields to automatically handle the request and authenticate the user
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                )
        return self.cleaned_data
    
    # Method to get the authenticated user from the form
    def get_user(self):
        return getattr(self, 'user_cache', None)

# Form for creating or updating a project    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['name', 'short_desc', 'long_desc', 'img_icon', 'tags', 'visibility', 'featured']
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
            'img_icon': forms.ClearableFileInput(attrs={
                'class': 'input-img',
                'accept': 'image/*'
            }),
            'tags': forms.CheckboxSelectMultiple(),
        }

# Form for creating or updating a tag        
class TagsForm(forms.ModelForm):
    class Meta:
        model = TagModel
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
    
