from django.urls import path
# Используем SimpleRouter так как с ним можно создать несколько экземпляров класса, а с DefaultRouter только один
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet

app_name = MaterialsConfig.name

# Создаем экземпляр класса SimpleRouter(), он обеспечивает маршрутизацию всех путей CRUD
router = SimpleRouter()
router.register("course", CourseViewSet)

urlpatterns = [

    ] + router.urls

# Другой вариант добавления
# urlpatterns += router.urls
