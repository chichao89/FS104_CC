from rest_framework import viewsets
from .serializers import HeroSerializer
from .serializers import ToDoListSerializer
from .models import Hero
from .models import ToDoList
# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all().order_by('priority')
    serializer_class = ToDoListSerializer

