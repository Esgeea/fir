from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='static/products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, unique=True)  # id that will be shown in the website

    def __str__(self):
        return self.name


class SiteUser(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.get_full_name()


class Contact(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.subject


class NewsletterSubscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    send_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject
