from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    #home-page
    url('^$', views.home, name='home'),
]
