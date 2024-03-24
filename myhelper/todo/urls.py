from django.urls import path

from .views import *

urlpatterns = [
    path('', ToDo.as_view(), name='todo'),
    path('todo_form/', AddToDo.as_view(), name='add_todo'),
    path('del_todo/', DelToDo.as_view(), name='del_todo')
]