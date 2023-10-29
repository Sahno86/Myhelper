from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return HttpResponse('Переход на <a href=http://127.0.0.1:8000/todo/>todo</a>')
