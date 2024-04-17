from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    """Класс для модели Курса"""

    name = models.CharField(
        max_length=150, verbose_name="Курс", help_text="Введите название курса"
    )
    preview = models.ImageField(
        upload_to="course_foto", verbose_name="Изображение", **NULLABLE
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """Класс для модели Урока"""
    course = models.ForeignKey(
        Course, verbose_name="Курс", related_name="lessons", on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(
        max_length=150, verbose_name="Урок", help_text="Введите название урока"
    )
    preview = models.ImageField(
        upload_to="lesson_foto", verbose_name="Изображение", **NULLABLE
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    video = models.FileField(upload_to="video_lesson", verbose_name="Видео", **NULLABLE)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
