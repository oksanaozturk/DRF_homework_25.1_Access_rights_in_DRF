from django.urls import path
from rest_framework.permissions import AllowAny
# Используем SimpleRouter так как с ним можно создать несколько экземпляров класса, а с DefaultRouter только один
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import PaymentViewSet, UserListAPIView, UserRetrieveAPIView, UserCreateAPIView, UserUpdateAPIView, \
    UserDestroyAPIView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

# Создаем экземпляр класса SimpleRouter(), он обеспечивает маршрутизацию всех путей CRUD
router = SimpleRouter()
router.register("payments", PaymentViewSet)

urlpatterns = [
    # Путь для вывода страницы со всеми объектами модели User
    path("users-list/", UserListAPIView.as_view(), name="users-list"),
    # Путь для вывода страницы с одним объектом модели User
    path("user-view/<int:pk>/", UserRetrieveAPIView.as_view(), name="users-retrieve"),
    # Путь для вывода страницы при создании нового объекта модели User
    path("user-create/", UserCreateAPIView.as_view(), name="users-create"),
    # Путь для редактирования объекта модели User
    path("user-update/<int:pk>/", UserUpdateAPIView.as_view(), name="users-update"),
    # Путь для удаления объекта модели User
    path("user-destroy/<int:pk>/", UserDestroyAPIView.as_view(), name="users-destroy"),

    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

    ] + router.urls

# Другой вариант добавления
# urlpatterns += router.urls
