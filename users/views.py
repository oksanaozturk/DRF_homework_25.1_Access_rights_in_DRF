from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import Payment, User
from users.serializer import PaymentSerializer, UserSerializer


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


class UserCreateAPIView(CreateAPIView):
    """Класс для создания экземпляра модели User (CRUD)"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # Делаем разрешение для этого контроллера, чтобы незарегистрированный пользователь имел доступ к регистрации
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Данный метод необходим для того, чтобы нам не мешала настройка 'username = None',
        указанная нами в модели User в models.py"""
        user = serializer.save(is_active=True)
        # Кешируем обязательно пароль Пользователя
        user.set_password(user.password)
        user.save()


class UserUpdateAPIView(UpdateAPIView):
    """Класс для редактирования экземпляра модели User (CRUD)"""
    serializer_class = UserSerializer
    # Получаем все данне из БД
    queryset = User.objects.all()


class UserDestroyAPIView(DestroyAPIView):
    """Класс для удаления экземпляра модели User (CRUD)"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(ListAPIView):
    """Класс для выведения всех экземпляров модели User (CRUD)"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(RetrieveAPIView):
    """Класс для выведения одного экземпляра модели User (CRUD)"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
