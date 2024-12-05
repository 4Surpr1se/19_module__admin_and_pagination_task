from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.

def sign_up(request):
    buyers = Buyer.objects.all()
    info = {
    }
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        if password == repeat_password and int(age) >= 18 and username not in buyers:
            Buyer.objects.create(name=username, balance=2000.0, age=age)
            return HttpResponse(f"Приветствуем, {username}!")
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in buyers:
            info['error'] = 'Пользователь уже существует'

    return render(request, 'task1/registration_page.html', context=info)


def game_platform(request):
    return render(request, 'task1/platform.html')


def games(request):
    games = Game.objects.all()
    return render(request, 'task1/games.html', {'games': games})


def cart(request):
    return render(request, 'task1/cart.html')


def news(request):
    news_list = News.objects.all()  # Замените на ваш запрос
    paginator = Paginator(news_list, 10)  # 10 новостей на странице
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    return render(request, 'task1/news.html', {'news': news})
