from django.urls import path

from products import views

urlpatterns=[
    path('', views.HomeTemplateView.as_view(), name='home_page'),
    path('about/', views.AboutTemplateView.as_view(), name='about_page')
]