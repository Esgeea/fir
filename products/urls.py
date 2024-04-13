from django.urls import path

from products import views

urlpatterns=[
    path('', views.HomeTemplateView.as_view(), name='home_page')
]