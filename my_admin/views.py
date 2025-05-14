from typing import Any
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import CustomLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from project.models import Project, Tags

#TODO: Arrumar nomes

class MyAdminLogin(FormView):
    template_name = 'my_admin/login.html'
    form_class = CustomLoginForm
    success_url = reverse_lazy('my_admin:home')
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)

class CustomLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('my_admin:login')

class MyAdminHome(LoginRequiredMixin, ListView):
    template_name = 'my_admin/my_admin_home.html'
    login_url = 'mainSite:home'
    context_object_name = 'objects'

    def get_ordering(self):
        ordering = self.request.GET.get('order_by', '-id')
        return ordering
    
    def get_queryset(self):
        switch = self.request.GET.get('switch_state')
        ordering = self.get_ordering()
        
        if switch == 'tags':
            return Tags.objects.all().order_by(ordering)

        return Project.objects.all().order_by(ordering)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['switch_state'] = self.request.GET.get("switch_state", "tags")
        return context
    