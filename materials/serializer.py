from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Класс создания сериализатора для модели Course"""

    class Meta:
        model = Course
        fields = "__all__"   # Или кортеж полей, которые необходимо вывести


class LessonSerializer(ModelSerializer):
    """Класс создания сериализатора для модели Lesson"""

    class Meta:
        model = Lesson
        fields = "__all__"  # Или кортеж полей, которые необходимо вывести
