from django.urls import path

from .views import *


urlpatterns = [
    path('', ToDo.as_view(), name='todo'),
    path('add_todo/', AddToDoForm.as_view(), name='add_todo'),
    # path('del_todo/', del_todo, name='del_todo')
]