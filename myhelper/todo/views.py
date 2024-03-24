from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, TemplateView, DeleteView

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
    success_url = reverse_lazy('todo')




class DelToDo(DeleteView):
    template_name = 'todo/todo.html'
    model = ToDo
    # success_url =
