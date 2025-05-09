from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class MyAdminLogin(FormView):
    template_name = 'my_admin/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('my_admin:login_success')
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)

class MyAdminLoginTest(LoginRequiredMixin, TemplateView):
    template_name = 'my_admin/loginSucess.html'
    login_url = 'mainSite:home'
    