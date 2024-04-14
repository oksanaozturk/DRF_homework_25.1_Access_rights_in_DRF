from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from materials.serializer import CourseSerializer


class CourseViewSet(ModelViewSet):
    """Класс для настройки CRUD для модели Course"""
    serializer_class = CourseSerializer
    # Получаем все данне из БД
    queryset = Course.objects.all()
