from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def block_user():
    """Функция по блокированию пользователя, если он не заходил более 30 дней."""

    # Получаем сегодняшнюю дату
    # today = timezone.now().today().date()
    active_users = User.objects.filter(is_active=True)
    for user in active_users:
        if user.last_login.date() < timezone.now().date() - timezone.timedelta(days=30):
            user.is_active = False
            user.save()

# Ещё один вариант функции
# @shared_task
# def user_blocking():
#     '''Функция блокирования пользователя, если он не заходил более месяца.'''
#     user_is_active = User.objects.filter(is_active=True)
#     today = datetime.now().date()
#     for user in user_is_active:
#         if user.last_login and (today - user.last_login.date()) > timedelta(days=30):
#             user.is_active = False
#             user.save()
