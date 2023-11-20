from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import ToDo
from django.views.decorators.http import require_http_methods


def todo(request):
    todo_obj = ToDo.objects.all()
    return render(request, 'todo/todo.html', {'todo_obj': todo_obj, 'title': 'todo'})


@require_http_methods(["POST"])
def add_todo(request):
    if request.method == "POST":
        add_todo_task = ToDo()
        add_todo_task.title = request.POST.get("add")
        add_todo_task.is_done = False
        add_todo_task.save()
    return HttpResponseRedirect('/todo')


# def del_todo(request):
#     del_button_test = request.GET.get("del")
#     return HttpResponse(f'{del_button_test}Сработала кнопка удаления')
