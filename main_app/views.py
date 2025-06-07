from typing import Any
from django.views.generic import ListView, FormView
from projects_app.models import ProjectModel, TagModel
from .forms import SendEmailForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Main application views for the portfolio website
class MainHomeView(ListView):
    model = ProjectModel
    template_name = 'main_app/home.html'
    context_object_name = "projects"

    # Customizing the queryset to filter projects that are visible and featured
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(visibility=True, featured=True).order_by('-id')[:3]
        return queryset
    
    # Customizing the context data to include additional information
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        project_tags_list = {}
        
        context["cargo"] = 'Python Developer | Data Scientist'
        context["tags"] = TagModel.objects.all()
        
        if context.get('projects'):
            for project in context['projects']:
                tags_list = list(project.tags.all())
                project_tags_list[project.pk] = tags_list[:5]

        context["custom_tags_list"] = project_tags_list
        return context

# View for the "About Me" page, which includes a contact form
class AboutMeView(FormView):
    template_name = 'main_app/about_me.html'
    form_class = SendEmailForm
    success_url = reverse_lazy('main_app:about_me')
    
    # Method to get the context data for the template, including the form
    def form_valid(self, form):
        response = super().form_valid(form)
        contact = form.save(commit=False)
        
        # Capturing form data
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone', 'N/A')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        
        # Preparing the email content
        context = {
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message
        }
        html_content = render_to_string('global/emails/contact_message.html', context)
        
        # Sending the email using Django's EmailMultiAlternatives
        try:
            email_message = EmailMultiAlternatives(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.DEFAULT_FROM_EMAIL]
            )
            email_message.attach_alternative(html_content, "text/html")
            email_message.send()
            
            contact.email_send = True
            
            messages.success(self.request, "Message sent successfully!")
        except Exception as e:
            
            print(f"Erros sending email: {e}")
            messages.error(self.request, "Message saved but failed to send email.")
        
        contact.save()
        return response
    
    # Method to handle form submission when the form is invalid
    def form_invalid(self, form):
        messages.error(self.request, "Error submitting form. Check required fields.")
        return super().form_invalid(form)
    