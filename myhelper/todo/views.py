from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, TemplateView

from .forms import ToDoForm
from .models import ToDo
from django.views.decorators.http import require_http_methods


# Отображение страницы todo
class ToDo(ListView):
    template_name = 'todo/todo.html'
    model = ToDo
    extra_context = {'title': 'todo'}


# Добавление задания

class AddToDo(CreateView):
    template_name = 'todo/todo_form.html'
    form_class = ToDoForm
    success_url = reverse_lazy('succes_add_todo')


class SuccesAddToDo(TemplateView):
    template_name = 'todo/succes_add_todo.html'


def del_todo(request):
    pass
