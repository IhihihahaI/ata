from django.contrib import admin

# Register your models here.

from .models import Product, Group

admin.site.register(Product)
admin.site.register(Group)
