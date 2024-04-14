from rest_framework.serializers import ModelSerializer

from materials.models import Course


class CourseSerializer(ModelSerializer):
    """Класс для создания сериализатора"""

    class Meta:
        model = Course
        fields = "__all__"   # Или кортеж полей, которые необходимо вывести
