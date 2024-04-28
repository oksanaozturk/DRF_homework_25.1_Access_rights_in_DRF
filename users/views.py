from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from users.models import Payment
from users.serializer import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    """Класс для настройки CRUD для модели Payment с помощью метеда ViewSet
    Create, Update, Retrieve, Delete."""
    serializer_class = PaymentSerializer
    # Получаем все данне из БД
    queryset = Payment.objects.all()

    # Спмсок меняем на кортеж, так как это более защищенная форма данных (указываем то, по чему хотим фильтровать)
    filterset_fields = ('lesson', 'course', 'payment_method')

    # Настройка сортировки
    # Переопределяем backends так как для ordering и search нужен filters.OrderingFilter,
    # который импортируем из rest_framework, а для filterset нужен только DjangoFilterBackend, который из django-filters
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('date_payment',)
