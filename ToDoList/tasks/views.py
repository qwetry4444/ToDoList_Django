from django.shortcuts import render

from .models import Tasks
from .serializers import TasksSerializer
from rest_framework.viewsets import ModelViewSet


from rest_framework.permissions import IsAuthenticated
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
    # разрешаем доступ только зарегистрированным пользователям
    permission_classes = (IsAuthenticated,)
    # отображаем элементы принадлежащие только текущему юзеру,
    # для админа разрешаем все
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tasks.objects.all()
        else:
            return Tasks.objects.filter(user=self.request.user)
