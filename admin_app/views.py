from typing import Any
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomLoginForm, ProjectForm, TagsForm
from .mixins import ProjectFormMixin, TagFormMixin
from projects_app.models import Project, Tags

class MyAdminLogin(FormView):
    template_name = 'admin_app/login.html'
    form_class = CustomLoginForm
    success_url = reverse_lazy('admin_app:home')
    
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

class ProjectAdd(ProjectFormMixin, CreateView):
    model = Project
    form_class = ProjectForm
    
class ProjectEdit(ProjectFormMixin, UpdateView):
    model = Project
    form_class = ProjectForm

class ProjectDelete(View):
    def post(self, request, slug):
        obj = get_object_or_404(Project, slug=slug)
        obj.delete()
        return JsonResponse({'success': True})

class TagAdd(TagFormMixin, CreateView):
    model = Tags
    form_class = TagsForm
    
class TagEdit(TagFormMixin, UpdateView):
    model = Tags
    form_class = TagsForm

class TagDelete(View):
    def post(self, request, slug):
        obj = get_object_or_404(Tags, slug=slug)
        obj.delete()
        return JsonResponse({'success': True})
