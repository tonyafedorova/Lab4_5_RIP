from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.views import View


def first(request):
    data = {
        'bios': [{'name': 'Childhood', 'text': 'jfkvnvn'}, {'name': 'Education', 'text': 'jfkbhbh'} ]
    }

    return render(request, 'first.html', data)


def pictures(request):
    picture = [
        {
            'pic': 'new-york.jpg',
            'text': 'Нью-Йорк',
            'price': 500
        },
        {
            'text': 'Венеция',
            'price': 600
        },
        {
            'text': 'Фреди',
        },
    ]
    return render(request, 'pictures.html', context={'pictures': picture})


def bios(request, name):
    data={
        'bio':{
            'name': name,
        }
    }

    return render(request, 'bio.html', data)