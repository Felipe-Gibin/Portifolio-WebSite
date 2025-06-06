from typing import Any
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomLoginForm, ProjectForm, TagsForm
from .mixins import ProjectFormMixin, TagFormMixin
from projects_app.models import Project, Tags
from main_app.models import ContactMeEmail

class MyAdminLogin(FormView):
    template_name = 'admin_app/login.html'
    form_class = CustomLoginForm
    
    def get_success_url(self):
        return reverse('admin_app:home') + '?switch_state=projects'
    
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
        return redirect('admin_app:login')

class MyAdminHome(LoginRequiredMixin, ListView):
    template_name = 'admin_app/home.html'
    login_url = 'admin_app:login'
    context_object_name = 'objects'
    paginate_by = 10
    ordering = ['-id']

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
        querydict = self.request.GET.copy()
        querydict.pop('page', None)
        context['querystring'] = querydict.urlencode()
        return context
    
class SentEmailsView(LoginRequiredMixin, ListView):
    model = ContactMeEmail
    context_object_name = 'emails'
    template_name = 'admin_app/email_table.html'
    login_url = 'admin_app:login'
    paginate_by = 10
    ordering = ['-id']
    
    def get_ordering(self):
        ordering = self.request.GET.get('order_by', '-id')
        return ordering
    
class SentEmailDetailView(LoginRequiredMixin, DetailView):
    model = ContactMeEmail
    context_object_name = 'email'
    template_name = 'admin_app/email_detail.html'

class ProjectAdd(LoginRequiredMixin, ProjectFormMixin, CreateView):
    model = Project
    form_class = ProjectForm
    login_url = 'admin_app:login'
    
class ProjectEdit(LoginRequiredMixin, ProjectFormMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    login_url = 'admin_app:login'

class ProjectDelete(LoginRequiredMixin, View):
    login_url = 'admin_app:login'
    def post(self, request, slug):
        obj = get_object_or_404(Project, slug=slug)
        obj.delete()
        return JsonResponse({'success': True})

class ToggleBooleanFields(LoginRequiredMixin, View):
    login_url = 'admin_app:login'
    def post(self, request, pk, field):
        project = get_object_or_404(Project, pk=pk)
        
        if field in ['visibility', 'featured']:
            value = request.POST.get('value') == 'on'
            setattr(project, field, value)
            project.save()
        
        return redirect(request.META.get('HTTP_REFERER', 'admin_app:home'))

class TagAdd(LoginRequiredMixin, TagFormMixin, CreateView):
    model = Tags
    form_class = TagsForm
    login_url = 'admin_app:login'
    
class TagEdit(LoginRequiredMixin, TagFormMixin, UpdateView):
    model = Tags
    form_class = TagsForm
    login_url = 'admin_app:login'

class TagDelete(LoginRequiredMixin, View):
    login_url = 'admin_app:login'
    def post(self, request, slug):
        obj = get_object_or_404(Tags, slug=slug)
        obj.delete()
        return JsonResponse({'success': True})
    

