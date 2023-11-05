from django.http import HttpResponse
from django.shortcuts import render
from .models import ToDo
def todo(request):
    table = ToDo.objects.all()
    return render(request, 'todo/todo.html', {'table': table})

def add_todo(request):
    add_button_test = request.GET.get("add")
    return print(add_button_test)

def del_todo(request):
    del_button_test = request.GET.get("del")
    return HttpResponse(f'{del_button_test}Сработала кнопка удаления')
