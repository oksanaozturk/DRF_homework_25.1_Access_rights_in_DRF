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
        verbose_name = "Пользователь"
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
    amount = models.PositiveIntegerField(verbose_name="Сумма оплаты", help_text='Укажите сумму платежа',)
    payment_method = models.CharField(max_length=50, choices=CHOICES_PAYMENT_METHOD, verbose_name="Способ оплаты",
                                      null=True, blank=True)
    session_id = models.CharField(max_length=255, verbose_name="ID сессии",
                                  help_text='Укажите ID Сессии', **NULLABLE)
    # ССылка длинная, поэтому символов даем больше
    link = models.URLField(max_length=400, verbose_name="Ссылка на оплату",
                           help_text='Укажите ссылку на оплату', **NULLABLE)

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        if self.course:
            subject = f'курс {self.course.name}'
        else:
            subject = f'урок {self.lesson.name}'
        return f"{self.amount} рублей от {self.user} за {subject}"
