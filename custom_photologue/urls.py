from django.conf.urls import url

from . import views

app_name = 'custom_photologue'
urlpatterns = [
    
    # link_list view for TinyMCE image link_list
    url('^image_link_list$', views.image_link_list, name='image_link_list')
]
