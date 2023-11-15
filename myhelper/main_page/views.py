from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    # return HttpResponse('<a href=http://127.0.0.1:8000/todo/>Переход на todo</a>'
    #                     '<br>'
    #                     '<a href=http://127.0.0.1:8000/admin/>Админка</a>')
    return render(request, 'main_page/main.html', {'title': 'Главная страница'})
