from django.contrib import admin
from products_App.models import Products, Order, Category
# Register your models here.
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Category)


