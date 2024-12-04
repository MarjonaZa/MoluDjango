from django.contrib import admin
# если хотим чтоб табличка отображалась в админке и мы могла как-то работать с ним то нужно зарегать таблицку здесть
# Register your models here.

from products.models import ProductCategory, Product
admin.site.register(ProductCategory)
admin.site.register(Product)


