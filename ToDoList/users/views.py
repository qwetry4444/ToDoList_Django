from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ViewSet


# Create your views here.
class UserViewSet(ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()