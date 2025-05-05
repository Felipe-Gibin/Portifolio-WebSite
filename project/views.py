from django.shortcuts import render
from typing import Any
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Project, Tags

class ProjectItem(TemplateView):
    # Detalhe de um único projeto
    template_name = 'projectItems/projects.html'
    
class ProjectList(ListView):
    # Listagem dos projetos em formato de cards
    template_name = 'projectItems/cardProject.html'
    model = Project
    context_object_name = 'projects'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        tag_slug = self.request.GET.get('tag')
        if tag_slug:
            tag = get_object_or_404(Tags, slug=tag_slug)
            queryset = queryset.filter(tags=tag)
        return queryset
    
        
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["tags"] = Tags.objects.all
        context["filter_tag"] = self.request.GET.get('tag')
        return context
    
    
