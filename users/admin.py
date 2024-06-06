from django.contrib import admin
from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс для регистрации User в админке."""

    list_display = ("id", "email", "is_active", "password", "avatar", "phone_number")
    list_filter = ("email",)
    search_fields = ("email",)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Класс для регистрации и отображения модели Payment в админке."""

    list_display = ("id", "user", "date_payment", "course", "lesson", "amount", "payment_method")
    list_filter = ("user",)
