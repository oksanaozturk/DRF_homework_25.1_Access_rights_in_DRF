from celery import shared_task
from django.core.mail import send_mail

from config import settings
from materials.models import Course, SubscriptionCourse


@shared_task
def send_message_about_update_course(course_id):
    """
    Функция отправки письма на почту Подписчику об обновлениях по курсу.
    """
    print("Отправка письма ...")
    course = Course.objects.get(pk=course_id)
    course_users = SubscriptionCourse.objects.filter(course=course_id)
    # При условии, что course_users у нас не пустой будет формироваться email_list
    email_list = []
    for user in course_users:
        email_list.append(user.email)
    # При условии, что email_list у нас не пустой будет производится отправка писем
    if email_list:
        send_mail(
            subject=f'Обновление по курсу {course.name}',
            message=f'Вы подписаны на обновления курса, вышла новая информция. Рекомендуем Вас ознакомиться с ней"',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=email_list,
            fail_silently=True
            )
# #
# @shared_task
# def send_message_for_update(course_id):
#     '''Отправка уведомления об обновлениях по подписке.'''
#     subs_update = Subscription.objects.filter(course=course_id)
#     subject = 'Обновление'
#     message = 'Вы подписаны на обновления курса, вышла новая информция.'
#     if subs_update:
#         email_list = []
#         for subscr in subs_update:
#             email_list.append(subscr.user.email)
#         send_mail(
#             subject=subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=email_list,
#             fail_silently=True
#         )
