from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    #home-page
    url('^$', views.home, name='home'),
    # url(r'^en$', views.home_en, name='home_en'),
    # url(r'^de$', views.home_de, name='home_de'),
]
