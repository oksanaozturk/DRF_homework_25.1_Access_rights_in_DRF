from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, Lesson, SubscriptionCourse
from materials.paginators import CustomPagination
from materials.serializer import CourseSerializer, LessonSerializer, CourseDetailSerializer
from users.permissions import IsModer, IsOwner
from materials.tasks import send_message_about_update_course


class CourseViewSet(ModelViewSet):
    """Класс для настройки CRUD для модели Course с помощью метода ViewSet
    Create, Update, Retrieve, Delete."""
    serializer_class = CourseSerializer
    # Получаем все данне из БД
    queryset = Course.objects.all()
    pagination_class = CustomPagination

    def get_permissions(self):
        """Метод для проверки доступа к функцианалу сайта, в зависимости от группы Пользователя """
        if self.action == 'create':
            # ~ это знак отрицания, то есть не Модератор
            # IsAuthenticated можно не указыывать, так как он прописан у нас на уровне проекта
            self.permission_classes = (IsAuthenticated, ~IsModer)
        elif self.action in ['list', 'retrieve', 'update']:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (IsOwner | ~IsModer,)

        return super().get_permissions()

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

    def perform_update(self, serializer):
        """
        Метод для запуска функции отправки сообщения(письма на почту), при обновлении курса.
        """
        update_course = serializer.save()
        send_message_about_update_course.delay(update_course.id)
        update_course.save()


class LessonCreateAPIView(CreateAPIView):
    """Класс для создания экземпляра модели Lesson (CRUD)"""
    serializer_class = LessonSerializer
    # Получаем все данне из БД - не нужен для CREATE
    # queryset = Lesson.objects.all()

    # Необходимо указать IsAuthenticated, так как вносятся изменения на уровне проекта
    permission_classes = (~IsModer, IsAuthenticated)

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
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonDestroyAPIView(DestroyAPIView):
    """Класс для удаления экземпляра модели Lesson (CRUD)"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | ~IsModer)


class LessonListAPIView(ListAPIView):
    """Класс для выведения всех экземпляров модели Lesson (CRUD)"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModer | IsOwner)
    pagination_class = CustomPagination


class LessonRetrieveAPIView(RetrieveAPIView):
    """Класс для выведения одного экземпляра модели Lesson (CRUD)"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class SubscriptionCourseAPIView(APIView):
    """Класс для установки/удаления подписки пользователя."""
    def post(self, *args, **kwargs):
        """Метод управления подпиской."""
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = SubscriptionCourse.objects.filter(user=user, course=course_item)

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            SubscriptionCourse.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'
        # Возвращаем ответ в API
        return Response({"message": message})
