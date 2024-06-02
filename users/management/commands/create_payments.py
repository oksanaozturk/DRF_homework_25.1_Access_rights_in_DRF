import datetime

from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    """Класс для создания кастомной команды по заполнению таблицы модели Payment"""

    def handle(self, *args, **options):
        # Очищаем таблицу, если есть старые данные
        Payment.objects.all().delete()

        # Для связанных полей модели проверяем наличие или создаем данные
        user1, created = User.objects.get_or_create(email='admin@sky.pro')
        # user2, created = User.objects.get_or_create(email='skypro.mytest@yandex.ru')

        course1, created = Course.objects.get_or_create(name='Подготовка в школе')
        course2, created = Course.objects.get_or_create(name='Общее развитие детей дошкольного возраста')

        lesson1, created = Lesson.objects.get_or_create(name='Гимнастика', course=course2)
        lesson2, created = Lesson.objects.get_or_create(name='Музыка', course=course2)

        # Создание платежей
        payment1 = Payment.objects.create(
            user=user1,
            date_payment=datetime.datetime.now().date(),
            course=course1,
            amount=15000,
            payment_method='cash',
        )

        payment2 = Payment.objects.create(
            user=user1,
            date_payment=datetime.datetime.now().date(),
            lesson=lesson1,
            amount=3000,
            payment_method='transfer to account',
        )

        payment3 = Payment.objects.create(
            user=user1,
            date_payment=datetime.datetime.now().date(),
            lesson=lesson2,
            amount=5000,
            payment_method='transfer to account',
        )
