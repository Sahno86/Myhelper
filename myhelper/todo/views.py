from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from . import models
from .models import ToDo
from django.views.decorators.http import require_http_methods


class ToDo(ListView):
    template_name = 'todo/todo.html'
    model = ToDo


@require_http_methods(["POST"])
def add_todo(request):
    if request.method == "POST":
        add_todo_task = models.ToDo()
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
