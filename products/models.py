import os
import django

from users.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')


from django.db import models
# создание таблиц для бд
# Create your models here.P
class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    descreption = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    descreption = models.TextField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_image/', null=True, blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"Продукт {self.name} | kategoty: {self.category.name} descreption: {self.descreption}"


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()
    # objects=Basket.objects.all()



    def __str__(self):
        return f"Корзина для {self.user.username} | продукт {self.product.name}"


# #не работал без
#     @property
    def sum(self):
        return self.product.price * self.quantity

    # def total_sum(self):
    #     baskets = Basket.objects.filter(user=self.user)
    #     return sum(basket.sum() for basket in baskets)
    #
    # def total_quantity(self):
    #     baskets = Basket.objects.filter(user=self.user)
    #     return sum(basket.quantity() for basket in baskets)
    #

    #отображаеться Продукт Куди черного цвета с монограммами adidas Originals | kategoty: odejda