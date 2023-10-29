from django.http import HttpResponse
from django.shortcuts import render
from .models import ToDo
def todo(request):
    table = ToDo.objects.all()
    return render(request, 'todo/todo.html', {'table': table})
