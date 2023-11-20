from django.urls import path

from .views import *


urlpatterns = [
    path('', todo, name='todo'),
    path('add_todo', add_todo, name='add_todo')
]