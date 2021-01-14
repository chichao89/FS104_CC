from django.contrib import admin
from .models import Hero
from .models import ToDoList
# Register your models here.
admin.site.register(Hero)
admin.site.register(ToDoList)