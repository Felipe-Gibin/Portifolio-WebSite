from django.shortcuts import render
from typing import Any
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Project, Tags

class ProjectItem(DetailView):
    # Detalhe de um único projeto
    model = Project
    context_object_name = 'project'
    template_name = 'projectItems/projects.html'
    
class ProjectList(ListView):
    # Listagem dos projetos em formato de cards
    template_name = 'projectItems/cardProject.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = 15
    ordering = ['-id']
    
    def get_queryset(self):
        tag_slug = self.request.GET.get('tag')
        queryset = super().get_queryset()
        if tag_slug:
            tag = get_object_or_404(Tags, slug=tag_slug)
            queryset = queryset.filter(tags=tag)
        return queryset
    
        
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        filter_tag = self.request.GET.get('tag')
        context["tags"] = Tags.objects.all()
        context["filter_tag"] = filter_tag
        
        querydict = self.request.GET.copy()
        querydict.pop('page', None)
        context['querystring'] = querydict.urlencode()
        
        custom_tags_list = {}
        
        filter_tag_obj = None
        if filter_tag:
            try:
                filter_tag_obj = Tags.objects.get(slug=filter_tag)
            except Tags.DoesNotExist:
                filter_tag_obj = None
            
        for project in context['projects']:
            tags_list = list(project.tags.all())
            if filter_tag_obj in tags_list:
                tags_list.remove(filter_tag_obj)
                tags_list = [filter_tag_obj] + tags_list
            custom_tags_list[project.pk] = tags_list[:5]
        context["custom_tags_list"] = custom_tags_list  
            
        return context
    
    
