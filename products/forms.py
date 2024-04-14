from django import forms
from django.forms import TextInput

from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form'})
        }