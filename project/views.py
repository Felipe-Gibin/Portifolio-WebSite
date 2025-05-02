from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Project

class ProjectItem(TemplateView):
    # Detalhe de um único projeto
    template_name = 'projectItems/projects.html'
    
class ProjectList(ListView):
    # Listagem dos projetos em formato de cards
    template_name = 'projectItems/cardProject.html'
    model = Project
    context_object_name = 'projects'
    
