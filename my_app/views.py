from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.views import View


def function_view(request):
    return HttpResponse('response from function view')


class ExampleClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')