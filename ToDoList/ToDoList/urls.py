from django.contrib import admin
from django.urls import path, include, re_path
urlpatterns = [
    path('admin/', admin.site.urls),
    # подключаем маршруты из наших приложений
    path('', include('tasks.urls')),
    path('', include('users.urls')),
    # подключаем маршруты авторизации
    re_path(r'^api/', include('djoser.urls')),
    re_path(r'^api/', include('djoser.urls.jwt')),
]
