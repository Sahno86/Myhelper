from django.db import models


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100, name='title')
    is_done = models.BooleanField(default=False, name='is_done')
