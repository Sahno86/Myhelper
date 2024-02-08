from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import *
from django.views.decorators.http import require_http_methods


class ToDo(TemplateView):
    template_name = 'todo/todo.html'


class ToDoList(ListView):
    template_name = 'todo/list_todo'
    model = ToDo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def todo(request):
#     todo_obj = ToDo.objects.all()
#     return render(request, 'todo/todo.html', {'todo_obj': todo_obj, 'title': 'todo'})


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
