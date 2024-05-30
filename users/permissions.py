from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """Проверка принадлежности пользователя к группе "Модератор"
    Если Пользователь Модератор, то будет возвращаться True"""

    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moders').exists()
        # if request.user.groups.filter(name='moderator').exists():
        #     return True
        # return False


class IsOwner(permissions.BasePermission):
    """
   Класс для проверки является ли Пользователь Владельцем.
   Разрешение на уровне объекта, позволяющее редактировать его только владельцам объекта.
   Предполагается, что экземпляр модели имеет атрибут «владелец».
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if obj.owner == request.user:
            return True
        return False
