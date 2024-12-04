from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages

from django.contrib.auth.decorators import login_required

from products.views import basket_add
from users.models import User
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from  django.urls import reverse
from products.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
        print(form.errors, 'form = UserLoginForm() 21')
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        print(form, 'это форма')  # Отладочный вывод
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно зарегистрированы')
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print("Ошибки формы:", form.errors)  # Покажите ошибки валидации в консоли
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def  profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    baskets=Basket.objects.filter(user=request.user)
    context = {'title': 'Store - Профиль',
               'form': form,
               'baskets': Basket.objects.filter(user=request.user),
               }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))