from django.contrib import admin

from materials.models import Course, Lesson, SubscriptionCourse


# Чтобы отобразить все уроки определенного курса в админе, можно использовать InlineModelAdmin
# Здесь мы определили класс LessonInline,
# который будет отображать связанные уроки для каждого курса в интерфейсе админки.
# Параметр extra=0 указывает, что изначально не будет отображаться пустая форма для добавления нового урока.
# В классе CourseAdmin мы добавили LessonInline в список inlines,
# чтобы связанные уроки отображались в форме редактирования курса.
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Класс для регистрации модели Урок в админке."""

    list_display = ("id", "name", "course", "preview", "description", "video", "owner")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Класс для регистрации модели Курс в админке."""

    inlines = [LessonInline]

    list_display = ("id", "name", "preview", "description", "owner")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(SubscriptionCourse)
class SubscriptionCourse(admin.ModelAdmin):
    """Класс для модели Полписки в админке."""

    list_display = ("id", "user", "course")
