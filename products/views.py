from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from products.filters import ProductFilter
from products.models import Product


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'


class AboutTemplateView(TemplateView):
    template_name = 'about/about.html'



class ContactTemplateView(TemplateView):
    template_name = 'contact/contact.html'


class ProductListView(ListView):
    template_name = 'galery/galery.html'
    model = Product
    context_object_name = 'all_products'

    def get_queryset(self):
        return Product.objects.filter()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        products = Product.objects.filter()
        myFilter = ProductFilter(self.request.GET, queryset=products)
        products = myFilter.qs
        data['all_products'] = products
        data['filters'] = myFilter.form

        return data

