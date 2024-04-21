from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from fir.settings import EMAIL_HOST_USER
from products.filters import ProductFilter
from products.forms import ContactForm, SubscribeForm
from products.models import Product, Contact, NewsletterSubscriber


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'


class AboutTemplateView(TemplateView):
    template_name = 'about/about.html'


class ProductListView(ListView):
    template_name = 'gallery/gallery.html'
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


class ContactCreateView(CreateView):
    template_name = 'contact/contact.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contact-form-sent')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save(commit=False)
            subject = 'Fir Contact Message - ' + new_form.subject
            message = 'Subject: ' + new_form.subject + '\n'+ 'Message: ' + new_form.message + '\n' + 'Email:' + new_form.email + '\n' + 'Phone:' + new_form.phone_number

            mail = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                ['esgeea@gmail.com']
            )

            mail.send()
            new_form.save()

            return redirect('contact-form-sent')
        return super().form_valid(form)
        

class SentTemplateView(TemplateView):
    template_name = 'contact/sent.html'


class SubscribeCreateView(CreateView):
    template_name = 'newsletter/subscribe.html'
    model = NewsletterSubscriber
    form_class = SubscribeForm
    success_url = reverse_lazy('subscribe_successful')

    def form_valid(self, form):
        if form.is_valid():
            email = form.cleaned_data['email']
            existing_subscriber = NewsletterSubscriber.objects.filter(email=email).first()
            if existing_subscriber:
                existing_subscriber.delete()
                message = "Hello,\n\nThank you for choosing Fir. Your action has been successfully made. You have been unsubscribed."
            else:
                new_form = form.save()
                message = "Hello,\n\nThank you for choosing Fir. Your action has been successfully made. You have been subscribed."

            mail = EmailMessage(
                "Fir Subscription",
                message,
                EMAIL_HOST_USER,
                [email]
            )

            mail.send()

            return redirect('subscribe_successful')
        return super().form_valid(form)

class SubscribeTemplateView(TemplateView):
    template_name = 'newsletter/subscribe_succsessful.html'