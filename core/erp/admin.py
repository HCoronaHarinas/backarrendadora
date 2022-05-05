from django.contrib import admin

# Register your models here.

from core.erp.models import Category, Product


admin.site.register(Category)
admin.site.register(Product)

