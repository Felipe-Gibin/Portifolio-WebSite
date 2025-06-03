from typing import Any
from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from projects_app.models import Project, Tags

class Home(ListView):
    model = Project
    template_name = 'main_app/home.html'
    context_object_name = "projects"

    def get_queryset(self):
        queryset = super().get_queryset()
        
        queryset = queryset.filter(visibility=True, featured=True)
        
        
        return queryset
    

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        project_tags_list = {}
        
        context["cargo"] = 'Python Developer | Data Scientist'
        context["tags"] = Tags.objects.all()
        
        if context.get('projects'):
            for project in context['projects']:
                tags_list = list(project.tags.all())
                project_tags_list[project.pk] = tags_list[:5]

        context["custom_tags_list"] = project_tags_list
        return context

class AboutMe(TemplateView):
    template_name = 'main_app/about_me.html'