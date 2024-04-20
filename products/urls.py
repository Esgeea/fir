from django.urls import path

from products import views

urlpatterns=[
    path('', views.HomeTemplateView.as_view(), name='home_page'),
    path('about/', views.AboutTemplateView.as_view(), name='about_page'),
    path('gallery/', views.ProductListView.as_view(), name='gallery_page'),
    path('contact/', views.ContactTemplateView.as_view(), name='contact_page')
]