from django.shortcuts import redirect
from django.urls import reverse_lazy

# Mixin utilizado para controle de ambos os botões
class ProjectTagsFormMixin:
    template_name = 'my_admin/my_admin_form_tag.html'

    def form_valid(self, form):
        response = super().form_valid(form)  # pyright: ignore
        action = self.request.POST.get('action')  # pyright: ignore
        if action == 'continue':
            return redirect(self.request.path) # pyright: ignore
        return response

    def get_success_url(self):
        return reverse_lazy('my_admin:home') + '?switch_state=projects'