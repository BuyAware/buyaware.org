# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns


# Language independant urls
urlpatterns = [
    # Example:
    # url(r'^test_project/', include('test_project.foo.urls')),

    # Enables the language_redirect_view which redirects requests 
    # to the same page but in an other language
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # Tinymce, a WYSIWIG text editor
    url(r'^tinymce/', include('tinymce.urls')),

    # Photologue 
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Localized urls (various languages available)
urlpatterns += i18n_patterns(
    url('^about/', include('about.urls', namespace='about')),
    url('^blog/', include('blog.urls', namespace='blog')),
    url('^db/', include('db.urls', namespace='db')),
    url('^admin/', include(admin.site.urls)),
    url('^', include('home.urls', namespace='home')),
)

