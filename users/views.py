from rest_framework.viewsets import ModelViewSet

from users.models import Payment
from users.serializer import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    """Класс для настройки CRUD для модели Payment с помощью метеда ViewSet
    Create, Update, Retrieve, Delete."""
    serializer_class = PaymentSerializer
    # Получаем все данне из БД
    queryset = Payment.objects.all()
