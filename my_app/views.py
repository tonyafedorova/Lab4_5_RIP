from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.views import View


def function_view(request):
    return HttpResponse('response from function view')


class ExampleClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')


def first(request):
    params = {
        'phrase': 'P.A.stel',
        'text': 'Сайт картин Пустовой Анны',
        'big_text': """    Эти картины написаны мной под впечатлением, увиденного в разных уголках мира.
    Я в своих работах не переворачиваю мир вверх ногами и не создаю фантасмагорий."""
    }

    return render(request, 'first.html', context={'first': params})


def pictures(request):
    picture = [
        {
            # 'pic': "",
            'text': 'Нью-Йорк',
            'price': 500
        },
        {
            # 'pic': "",
            'text': 'Венеция',
            'price': 600
        },
        {
            # 'pic': "",
            'text': 'Фреди',
            # 'price': 800
        },
    ]
    return render(request, 'pictures.html', context={'pictures': picture})