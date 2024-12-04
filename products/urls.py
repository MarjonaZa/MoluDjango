from products.views import product

from django.urls import path
from products import views
from .views import basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', product, name='index'),
    path('category/<int:cat_id>/', product, name='category'),
    path('page/<int:page>/', product, name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]