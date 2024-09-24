from django.shortcuts import render

from .models import Tasks
from .serializers import TasksSerializer
from rest_framework.viewsets import ModelViewSet


class TasksViewSet(ModelViewSet):
    # Класс сериализатора, который следует использовать для проверки
    # и десериализации входных данных, а также для сериализации выходных данных.
    serializer_class = TasksSerializer
    # QuerySet представляет набор запросов к базе данных,
    # а его методы создают подобные запросы.
    queryset = Tasks.objects.all()
