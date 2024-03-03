from django.forms import ModelForm

from todo.models import ToDo


class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'is_done']
