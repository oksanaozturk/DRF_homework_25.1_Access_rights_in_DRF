from rest_framework import serializers
from materials.models import Course, Lesson, SubscriptionCourse
from materials.validators import ValidateURLResource


class LessonSerializer(serializers.ModelSerializer):
    """Класс создания сериализатора для модели Lesson"""

    class Meta:
        model = Lesson
        fields = "__all__"  # Или кортеж полей, которые необходимо вывести
        validators = [ValidateURLResource(field='video')]


class CourseSerializer(serializers.ModelSerializer):
    """Класс создания сериализатора для модели Course"""

    class Meta:
        model = Course
        fields = "__all__"   # Или кортеж полей, которые необходимо вывести


class CourseDetailSerializer(serializers.ModelSerializer):
    """Класс создания сериализатора для модели Course"""
    # Задаем новое поле для модели. которое будет передаваться через Serializer
    count_lessons_for_course = serializers.SerializerMethodField()
    # Получаем новое поле для модели. которое будет передаваться через Serializer
    # Обращаюсь через lessons, а не lesson_set, так как в модели настроен related_name
    # lessons = LessonSerializer(source='lessons', many=True, read_only=True)

    # Излишним указывать `source='lessons'` в поле ListSerializer в сериализаторе CourseSerializer,
    # поскольку оно совпадает с именем поля.
    # При использовании сериализатора для связанной модели LessonSerializer
    # read_only=True означает, что открыт только для чтения, write_only=True - можно будет записывать,
    # но откроются все поля для заполнения
    lessons = LessonSerializer(many=True, read_only=True)

    # Вариант выведения lessons с использованием SerializerMethodField()
    # lessons = SerializerMethodField()
    #
    # def get_lessons(self, course):
    #     """Метод для получения списка назвпний уроков"""
    #     lessons = [lesson.name for lesson in Lesson.objects.filter(course=course)]
    #
    #     return lessons
    # course_subscription = serializers.SerializerMethodField()     # Создаем поле подписки на курс
    is_subscription = serializers.SerializerMethodField()  # поле подписки на курс

    class Meta:
        model = Course
        fields = "__all__"

    def get_is_subscription(self, course):
        """Метод для показа наличия подписки у пользователя."""
        return SubscriptionCourse.objects.filter(course=course, user=self.context['request'].user).exists()

    @staticmethod
    def get_count_lessons_for_course(course):
        """Метод для получения количества уроков, входящих в курс"""

        return course.lessons.count()


class SubscriptionCourseSerializer(serializers.ModelSerializer):
    """Класс создания сериализатора для модели Подписки."""
    class Meta:
        model = SubscriptionCourse
        fields = '__all__'
