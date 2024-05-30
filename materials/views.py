from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, Lesson
from materials.serializer import CourseSerializer, LessonSerializer, CourseDetailSerializer
from users.permissions import IsModer


class CourseViewSet(ModelViewSet):
    """Класс для настройки CRUD для модели Course с помощью метеда ViewSet
    Create, Update, Retrieve, Delete."""
    serializer_class = CourseSerializer
    # Получаем все данне из БД
    queryset = Course.objects.all()

    def get_serializer_class(self):
        """Метод получения сериализатора в зависимости от запроса
        (вывод всего списка или просмотр одного объекта)"""

        if self.action == "retrieve":
            return CourseDetailSerializer

        return CourseSerializer

    def perform_create(self, serializer):
        """Метод для присоединения создателя курса к курсу"""
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        """Метод для проверки доступа к функцианалу сайта, в зависимости от группы Пользователя """
        if self.action in ['create', 'destroy']:
            # ~ это знак отрицания, то есть не Модератор
            self.permission_classes = (~IsModer,)
        elif self.action in ['list', 'retrieve', 'update']:
            self.permission_classes = (IsModer,)

        return super().get_permissions()


class LessonCreateAPIView(CreateAPIView):
    """Класс для создания экземпляра модели Lesson (CRUD)"""
    serializer_class = LessonSerializer
    # Получаем все данне из БД - не нужен для CREATE
    # queryset = Lesson.objects.all()

    def perform_create(self, serializer):
        """Метод для присоединения создателя урока к уроку"""
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonUpdateAPIView(UpdateAPIView):
    """Класс для редактирования экземпляра модели Lesson (CRUD)"""
    serializer_class = LessonSerializer
    # Получаем все данне из БД
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(DestroyAPIView):
    """Класс для удаления экземпляра модели Lesson (CRUD)"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListAPIView(ListAPIView):
    """Класс для выведения всех экземпляров модели Lesson (CRUD)"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(RetrieveAPIView):
    """Класс для выведения одного экземпляра модели Lesson (CRUD)"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
