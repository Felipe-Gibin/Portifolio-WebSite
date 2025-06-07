from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

# Mixin used for handling the form submission and redirecting based on the action taken
class ProjectFormMixin:
    template_name = 'admin_app/project_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)  # pyright: ignore
        action = self.request.POST.get('action')  # pyright: ignore
        if action == 'continue':
            slug = getattr(self.object, 'slug', None) # pyright: ignore
            if slug:
                return redirect(reverse('admin_app:project_edit', kwargs={'slug': slug}))
            else:
                return redirect(self.request.path) # pyright: ignore
        return response

    def get_success_url(self):
        return reverse_lazy('admin_app:home') + '?switch_state=projects'

# Mixin used for handling the form submission and redirecting based on the action taken for tags
class TagFormMixin:
    template_name = 'admin_app/tag_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)  # pyright: ignore
        action = self.request.POST.get('action')  # pyright: ignore
        if action == 'continue':
            slug = getattr(self.object, 'slug', None) # pyright: ignore
            if slug:
                return redirect(reverse('admin_app:tag_edit', kwargs={'slug': slug}))
            else:
                return redirect(self.request.path) # pyright: ignore
        return response

    def get_success_url(self):
        return reverse_lazy('admin_app:home') + '?switch_state=tags'