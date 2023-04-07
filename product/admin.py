from django.contrib import admin

from category.models import Category
from product.models import Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
