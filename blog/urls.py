from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    
    # Main page of blog url
    url('^$', views.blog_index, name='blog_index'),
    
    # post detail url
    url('^(?P<slug>[-\w\d\_]+)/$', views.post_detail, name='post_detail'),

]
