from django.urls import path
# Используем SimpleRouter так как с ним можно создать несколько экземпляров класса, а с DefaultRouter только один
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateAPIView,
                             LessonDestroyAPIView, LessonListAPIView,
                             LessonRetrieveAPIView, LessonUpdateAPIView,
                             SubscriptionCourseAPIView)

app_name = MaterialsConfig.name

# Создаем экземпляр класса SimpleRouter(), он обеспечивает маршрутизацию всех путей CRUD
router = SimpleRouter()
router.register("course", CourseViewSet)

urlpatterns = [
    # Путь для вывода страницы со всеми объектами модели Lesson
    path("lessons/", LessonListAPIView.as_view(), name="lessons-list"),
    # Путь для вывода страницы с одним объектом модели Lesson
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lessons-retrieve"),
    # Путь для вывода страницы при создании нового объекта модели Lesson
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lessons-create"),
    # Путь для редактирования объекта модели Lesson
    path("lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lessons-update"),
    # Путь для удаления объекта модели Lesson
    path("lessons/<int:pk>/destroy/", LessonDestroyAPIView.as_view(), name="lessons-destroy"),

    # Путь для отображения модели SubscriptionCourse (Подписки на курс)
    path('subscription/', SubscriptionCourseAPIView.as_view(), name='subscription'),

] + router.urls

# Другой вариант добавления
# urlpatterns += router.urls
