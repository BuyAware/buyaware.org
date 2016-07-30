from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

app_name = 'about'
urlpatterns = [
    
    # About page url
    url('^$', views.about_index, name='about_index'),
     url('^assessements$', TemplateView.as_view(template_name='about/about_assessements.html'), name='assessements'),
    url('^drive$', TemplateView.as_view(template_name='about/about_drive.html'), name='drive'),
    url('^spiderweb$', TemplateView.as_view(template_name='about/about_spiderweb.html'), name='spiderweb'),
    url('^personal_service$', TemplateView.as_view(template_name='about/about_personal_service.html'), name='personal_service'),
]
