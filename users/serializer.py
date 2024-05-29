from rest_framework.serializers import ModelSerializer

from users.models import Payment, User


class PaymentSerializer(ModelSerializer):
    """Класс создания сериализатора для модели Payment"""

    class Meta:
        model = Payment
        fields = "__all__"  # Или кортеж полей, которые необходимо вывести


class UserSerializer(ModelSerializer):
    """Класс создания сериализатора для модели User"""

    class Meta:
        model = User
        fields = "__all__"  # Или кортеж полей, которые необходимо вывести
