from django.contrib import admin

from materials.models import Lesson, Course


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Класс для регистрации модели Урок в админке."""

    list_display = ("id", "name", "preview", "description", "video")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Класс для регистрации модели Курс в админке."""

    list_display = ("id", "name", "preview", "description")
    list_filter = ("name",)
    search_fields = ("name",)
