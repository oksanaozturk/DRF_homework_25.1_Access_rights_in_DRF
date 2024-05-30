from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """Проверка принадлежности пользователя к группе "Модератор"
    Если Пользователь Модератор, то будет возвращаться True"""
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator').exists():
            return True
        return False
