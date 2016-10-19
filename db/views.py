from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from models import Product, CriterionAnswer

# Create your views here.

class ProductListView(ListView):

    model = Product
    template_name = 'db/db_assessments.html'

class ProductDetailView(DetailView):

    model = Product
    template_name = 'db/db_assessments_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.exclude(id=self.get_object().id)
        context['crits_CE'] = CriterionAnswer.objects.filter(product = self.get_object()).filter(criterion__category = 'CE')
        context['crits_EC'] = CriterionAnswer.objects.filter(product = self.get_object()).filter(criterion__category = 'EC')
        context['crits_WR'] = CriterionAnswer.objects.filter(product = self.get_object()).filter(criterion__category = 'WR')
        context['crits_CM'] = CriterionAnswer.objects.filter(product = self.get_object()).filter(criterion__category = 'CM')
        context['crits_TR'] = CriterionAnswer.objects.filter(product = self.get_object()).filter(criterion__category = 'TR')
        context['crits_PR'] = CriterionAnswer.objects.filter(product = self.get_object()).filter(criterion__category = 'PR')
        return context

    