from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    """Класс создания сериализатора для модели Lesson"""

    class Meta:
        model = Lesson
        fields = "__all__"  # Или кортеж полей, которые необходимо вывести


class CourseSerializer(ModelSerializer):
    """Класс создания сериализатора для модели Course"""

    class Meta:
        model = Course
        fields = "__all__"   # Или кортеж полей, которые необходимо вывести


class CourseDetailSerializer(ModelSerializer):
    """Класс создания сериализатора для модели Course"""
    # Задаем новое поле для модели. которое будет передаваться через Serializer
    count_lessons_for_course = SerializerMethodField()
    # Получаем новое поле для модели. которое будет передаваться через Serializer
    # Обращаюсь через lessons, а не lesson_set, так как в модели настроен related_name
    # lessons = LessonSerializer(source='lessons', many=True, read_only=True)

    # Излишним указывать `source='lessons'` в поле ListSerializer в сериализаторе CourseSerializer,
    # поскольку оно совпадает с именем поля.
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ("id", "name", "description", "preview", "lessons", "count_lessons_for_course")

    @staticmethod
    def get_count_lessons_for_course(course):
        """Метод для получения количества уроков, входящих в курс"""

        return course.lessons.count()
