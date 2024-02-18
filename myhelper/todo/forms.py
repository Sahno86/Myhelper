from django import forms


class AddToDo(forms.Form):
    name = forms.CharField(max_length=100)
    is_done = forms.BooleanField()

