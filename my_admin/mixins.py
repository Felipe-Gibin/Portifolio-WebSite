from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

# Mixin utilizado para controle do botao em project new/edit
class ProjectFormMixin:
    template_name = 'my_admin/my_admin_form_project.html'

    def form_valid(self, form):
        response = super().form_valid(form)  # pyright: ignore
        action = self.request.POST.get('action')  # pyright: ignore
        if action == 'continue':
            slug = getattr(self.object, 'slug', None) # pyright: ignore
            if slug:
                return redirect(reverse('my_admin:project_edit', kwargs={'slug': slug}))
            else:
                return redirect(self.request.path) # pyright: ignore
        return response

    def get_success_url(self):
        return reverse_lazy('my_admin:home') + '?switch_state=projects'

# Mixin utilizado para controle do botao em tag new/edit  
class TagFormMixin:
    template_name = 'my_admin/my_admin_form_tag.html'

    def form_valid(self, form):
        response = super().form_valid(form)  # pyright: ignore
        action = self.request.POST.get('action')  # pyright: ignore
        if action == 'continue':
            slug = getattr(self.object, 'slug', None) # pyright: ignore
            if slug:
                return redirect(reverse('my_admin:tag_edit', kwargs={'slug': slug}))
            else:
                return redirect(self.request.path) # pyright: ignore
        return response

    def get_success_url(self):
        return reverse_lazy('my_admin:home') + '?switch_state=tags'