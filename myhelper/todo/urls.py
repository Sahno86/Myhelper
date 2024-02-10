from django.urls import path

from .views import *


urlpatterns = [
    path('', ToDo.as_view(), name='todo'),
    path('todo_list/', ToDoList.as_view(), name='todo_list'),
    path('add_todo/', add_todo, name='add_todo'),
    path('del_todo/', del_todo, name='del_todo')
]