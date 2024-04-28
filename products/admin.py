from django.contrib import admin

from products.models import *

admin.site.register(SiteUser)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(NewsletterSubscriber)



