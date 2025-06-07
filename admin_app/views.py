from typing import Any
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomMyAdminLoginForm, ProjectForm, TagsForm
from .mixins import ProjectFormMixin, TagFormMixin
from projects_app.models import ProjectModel, TagModel
from main_app.models import EmailModel

import logging
logger = logging.getLogger(__name__)

# Custom admin views for handling login
class CustomMyAdminLoginView(FormView):
    template_name = 'admin_app/login.html'
    form_class = CustomMyAdminLoginForm
    
    def get_success_url(self):
        return reverse('admin_app:home') + '?switch_state=projects'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    # Customizing the form validation to handle login and logging
    def form_valid(self, form):
        user = form.get_user()
        if user is not None:
            login(self.request, user)
            logger.info(f"Successful login for user: {user.username} of IP: {self.request.META.get('REMOTE_ADDR')}")
            return redirect(self.get_success_url())
        else:
            logger.warning(f"Login attempt failed for user: {form.cleaned_data.get('username')} of IP: {self.request.META.get('REMOTE_ADDR')}")
            return self.form_invalid(form)

# Custom logout view to handle user logout
class CustomMyAdminLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('admin_app:login')

# Custom admin home view to list projects and tags with pagination and ordering
class CustomMyAdminHomeView(LoginRequiredMixin, ListView):
    template_name = 'admin_app/home.html'
    login_url = 'admin_app:login'
    context_object_name = 'objects'
    paginate_by = 10
    ordering = ['-id']

    def get_ordering(self):
        ordering = self.request.GET.get('order_by', '-id')
        return ordering
    
    # Customizing the queryset to switch between projects and tags based on the request parameter
    def get_queryset(self):
        switch = self.request.GET.get('switch_state')
        ordering = self.get_ordering()
        
        if switch == 'tags':
            return TagModel.objects.all().order_by(ordering)

        return ProjectModel.objects.all().order_by(ordering)
    
    # Customizing the context data to include additional information for the template
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['switch_state'] = self.request.GET.get("switch_state", "tags")
        querydict = self.request.GET.copy()
        querydict.pop('page', None)
        context['querystring'] = querydict.urlencode()
        return context

# Custom view for displaying the list of sent emails
class SentEmailsView(LoginRequiredMixin, ListView):
    model = EmailModel
    context_object_name = 'emails'
    template_name = 'admin_app/email_table.html'
    login_url = 'admin_app:login'
    paginate_by = 10
    ordering = ['-id']
    
    def get_ordering(self):
        ordering = self.request.GET.get('order_by', '-id')
        return ordering

# Custom View for displaying the details of a sent email  
class SentEmailDetailView(LoginRequiredMixin, DetailView):
    model = EmailModel
    context_object_name = 'email'
    template_name = 'admin_app/email_detail.html'

# Custom views for handling project management
# ProjectAddView used for creating new projects
class ProjectAddView(LoginRequiredMixin, ProjectFormMixin, CreateView):
    model = ProjectModel
    form_class = ProjectForm
    login_url = 'admin_app:login'

# ProjectEditView used for editing existing projects
class ProjectEditView(LoginRequiredMixin, ProjectFormMixin, UpdateView):
    model = ProjectModel
    form_class = ProjectForm
    login_url = 'admin_app:login'

# ProjectDeleteView used for deleting projects
class ProjectDeleteView(LoginRequiredMixin, View):
    login_url = 'admin_app:login'
    def post(self, request, slug):
        obj = get_object_or_404(ProjectModel, slug=slug)
        obj.delete()
        return JsonResponse({'success': True})

# Custom views for handling tag management
# TagAddView used for creating new tags
class TagAddView(LoginRequiredMixin, TagFormMixin, CreateView):
    model = TagModel
    form_class = TagsForm
    login_url = 'admin_app:login'

# TagEditView used for editing existing tags
class TagEditView(LoginRequiredMixin, TagFormMixin, UpdateView):
    model = TagModel
    form_class = TagsForm
    login_url = 'admin_app:login'

# TagDeleteView used for deleting tags
class TagDeleteView(LoginRequiredMixin, View):
    login_url = 'admin_app:login'
    def post(self, request, slug):
        obj = get_object_or_404(TagModel, slug=slug)
        obj.delete()
        return JsonResponse({'success': True})

# Custom view for toggling boolean fields in the project model
class ToggleBooleanFields(LoginRequiredMixin, View):
    login_url = 'admin_app:login'
    def post(self, request, pk, field):
        project = get_object_or_404(ProjectModel, pk=pk)
        
        if field in ['visibility', 'featured']:
            value = request.POST.get('value') == 'on'
            setattr(project, field, value)
            project.save()
        
        return redirect(request.META.get('HTTP_REFERER', 'admin_app:home'))
