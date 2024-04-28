from rest_framework.serializers import ModelSerializer

from users.models import Payment


class PaymentSerializer(ModelSerializer):
    """Класс создания скриализатора для модели Payment"""

    class Meta:
        model = Payment
        fields = "__all__"  # Или кортеж полей, которые необходимо вывести
