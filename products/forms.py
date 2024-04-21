from django import forms
from django.forms import TextInput, EmailInput, Textarea

from products.models import Product, Contact, NewsletterSubscriber


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form'})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            'subject': TextInput(attrs={'placeholder': 'Short description for your message', 'class': 'form-control'}),
            'message': Textarea(
                attrs={'placeholder': 'Type your message, questions and feedback are welcomed', 'class': 'form-control',
                       'rows': 10}),
            'email': EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'phone_number': TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'})
        }

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = "__all__"

        widgets= {
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form'})
        }