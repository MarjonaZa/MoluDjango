from django.shortcuts import render, HttpResponseRedirect
from unicodedata import category

from products.models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
#создаём функции = для обработки запроса=вьюхи

def index(request):
    context = {'title': 'Test title',
               # 'is_promotion': True,
               }
    return  render(request, 'products/index.html', context)

def product(request, cat_id= None, page=1):
    products = Product.objects.filter(category_id=cat_id) if cat_id else Product.objects.all()
    per_page=3
    paginator = Paginator(products, per_page)

    products_paginator = paginator.page(page)
    context = {
        'title': 'Store - Каталог',
        'products': products_paginator,
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'products/products.html', context)

@login_required
def basket_add(request, product_id):
    products = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=products)
    if not baskets.exists():
        Basket.objects.create(user=request.user,product=products, quantity=1 )
    else:
         basket = baskets.first()
         basket.quantity += 1
         basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER']) #та страница на которой находиться пользователь, прикол в том не отправлятьего либо на корзину либо на стр каталого а редериктеть его на страницу где он находиться

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.filter(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



# def products(request):
#     context = {
#         'title': 'Store = каталог',
#         'products': [
#             {
#                 'image': '/static/vendor/img/products/Adidas-hoodie.png',
#                 'name': 'Куди черного цвета с монограммами adidas Originals',
#                 'price': 6090,
#                 'description': 'Мягкая ткань для свитшотов. Стиль и комфорт - это образ жизни.',
#             },
#             {
#                 'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
#                 'name': 'Синяя куртка The North Face',
#                 'price': 23725,
#                 'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
#             },
#             {
#                 'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
#                 'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
#                 'price': 3390,
#                 'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
#             },
#         ]
#     }
