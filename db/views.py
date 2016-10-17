from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from models import Product

# Create your views here.

class ProductListView(ListView):

    model = Product
    template_name = 'db/db_assessments.html'

class ProductDetailView(DetailView):

    model = Product
    template_name = 'db/db_assessments_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        print(Product.objects.exclude(id=self.get_object().id))
        context['products'] = Product.objects.exclude(id=self.get_object().id)
        return context

    