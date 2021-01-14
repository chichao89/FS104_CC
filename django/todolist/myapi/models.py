from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name


class ToDoList(models.Model):
    title = models.CharField(max_length=70)
    priority = models.CharField(max_length=10)
    due_date = models.DateField()
    def __str__(self):
        return self.title