import django_filters
from django import forms
from django.forms import RadioSelect

from products.models import Product, Category


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter product name'}))
    description = django_filters.CharFilter(lookup_expr='icontains', label='Description', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter description'}))
    category = django_filters.ChoiceFilter(widget=RadioSelect(), choices=[(category.id, category) for category in Category.objects.filter()])

    class Meta:
        model = Product
        fields = ['name', 'description', 'category']