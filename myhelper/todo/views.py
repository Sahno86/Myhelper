from django.http import HttpResponseRedirect
from django.shortcuts import render
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

def add_todo(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ToDoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/todo/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ToDoForm()

    return render(request, "todo/todo.html", {"form": form})

