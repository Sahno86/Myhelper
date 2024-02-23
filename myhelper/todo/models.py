from django.db import models
from django.forms import ModelForm


class ToDo(models.Model):
    title = models.CharField('Название', max_length=100, name='title')
    is_done = models.BooleanField('Завершено', default=False, name='is_done')


class ToDoForm(ModelForm):
    model = ToDo
    fields = ['title', 'is_done']


# form = ToDoForm()
