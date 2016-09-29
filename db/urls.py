from django.conf.urls import url
from django.views.generic.base import TemplateView

from views import *

app_name = 'db'
urlpatterns = [
    url('^assessments', ProductListView.as_view(), name='assessments'),
    url('^product/(?P<pk>[0-9]+)', ProductDetailView.as_view() , name='assessments_detail'),
]

