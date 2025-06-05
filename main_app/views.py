from typing import Any
from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, FormView
from projects_app.models import Project, Tags
from .forms import ContactMeForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail

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

class AboutMe(FormView):
    template_name = 'main_app/about_me.html'
    form_class = ContactMeForm
    success_url = reverse_lazy('main_app:about_me')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        contact = form.save(commit=False)
        
        # Dados do formulário
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone', 'N/A')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        
        # Gerar corpo do e-mail via template HTML
        context = {
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message
        }
        html_content = render_to_string('global/emails/contact_message.html', context)
        
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
    
    def form_invalid(self, form):
        messages.error(self.request, "Error submitting form. Check required fields.")
        return super().form_invalid(form)
    