from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Класс для создания модели Пользователя"""

    username = None

    email = models.EmailField(
        max_length=150, unique=True, verbose_name="email", help_text="Введите email"
    )
    # Необходимо добавить библиотеку через команду pip install "django-phonenumber-field[phonenumberslite]"
    phone_number = PhoneNumberField(
        verbose_name="Номер телефона",
        help_text="Укажите Ваш номер телефона",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="users_avatar",
        verbose_name="Аватар пользователя",
        help_text="Загрузите изображение",
        **NULLABLE
    )
    counter = models.CharField(
        max_length=100,
        verbose_name="Страна",
        help_text="Введите страну проживания",
        **NULLABLE
    )

    # Выбираем полем для авторизации email
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользоаптель"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    """Класс для создания модели платежа"""

    CHOICES_PAYMENT_METHOD = [
        ("cash", "наличные"),
        ("transfer to account", "перевод на счет"),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="payments", verbose_name="Пользователь",
                             null=True, blank=True)
    date_payment = models.DateField(auto_now=True, verbose_name="Дата платежа")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name="payments",
                               verbose_name="Оплаченный курс", null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, related_name="payments",
                               verbose_name="Оплаченный урок", null=True, blank=True)
    amount = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(max_length=50, choices=CHOICES_PAYMENT_METHOD, verbose_name="Способ оплаты",
                                      null=True, blank=True)
