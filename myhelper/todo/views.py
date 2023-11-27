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


@require_http_methods(["POST"])
def del_todo(request, todo_id):
    if request.method == "POST":
        del_todo_task = ToDo()
        del_todo_task.pk = request.POST.get(id=todo_id)
        del_todo_task.delete()
    return HttpResponseRedirect('/todo')


