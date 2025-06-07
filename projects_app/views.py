from typing import Any
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from .models import ProjectModel, TagModel

# View for listing projects and filtering by tags if provided
class ProjectsHomeView(ListView):
    template_name = 'projects_app/home.html'
    model = ProjectModel
    context_object_name = 'projects'
    paginate_by = 3
    ordering = ['-id']
    
    # Method to get the queryset of projects, filtering by tag if provided
    def get_queryset(self):
        tag_slug = self.request.GET.get('tag')
        queryset = super().get_queryset()
        if tag_slug:
            tag = get_object_or_404(TagModel, slug=tag_slug)
            queryset = queryset.filter(tags=tag)
            
        queryset = queryset.filter(visibility=True)
        return queryset
    
    # Method to get the context data for the template, including tags and filtered projects
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        filter_tag = self.request.GET.get('tag')
        context["tags"] = TagModel.objects.all()
        context["filter_tag"] = filter_tag
        
        querydict = self.request.GET.copy()
        querydict.pop('page', None)
        context['querystring'] = querydict.urlencode()
        
        project_tags_list = {}
        
        # If a filter tag is provided, get the corresponding Tag object
        # If no filter tag is provided, set filter_tag_obj to None
        filter_tag_obj = None
        if filter_tag:
            try:
                filter_tag_obj = TagModel.objects.get(slug=filter_tag)
            except TagModel.DoesNotExist:
                filter_tag_obj = None
        
        # If a filter tag is provided, reorder the tags for each project
        # to ensure the filter tag appears first in the list
        if context.get('projects'):    
            for project in context['projects']:
                tags_list = list(project.tags.all())
                if filter_tag_obj in tags_list:
                    tags_list.remove(filter_tag_obj)
                    tags_list = [filter_tag_obj] + tags_list
                project_tags_list[project.pk] = tags_list[:5]
                    
        context["custom_tags_list"] = project_tags_list
            
        return context
    
    
# View for displaying the details of a single project
class ProjectDetailView(DetailView):
    model = ProjectModel
    context_object_name = 'project'
    template_name = 'projects_app/project_detail.html'