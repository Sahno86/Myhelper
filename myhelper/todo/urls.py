from django.urls import path

from .views import *

urlpatterns = [
    path('', ToDo.as_view(), name='todo'),
    path('todo_form/', AddToDo.as_view(), name='add_todo'),
    path('succes_add_todo/', SuccesAddToDo.as_view(), name='succes_add_todo'),
    path('del_todo/', del_todo, name='del_todo')
]