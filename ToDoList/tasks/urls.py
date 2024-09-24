from rest_framework import routers
from tasks.views import TasksViewSet

# создаем маршруты по умолчанию и убираем слеш в конце
router = routers.DefaultRouter(trailing_slash=False)
# регистрируем маршррут и привязываем контроллер
router.register('tasks', viewset=TasksViewSet)
# добавляем сгенерированные маршруты в коллекцию urlpatterns
urlpatterns = router.urls
