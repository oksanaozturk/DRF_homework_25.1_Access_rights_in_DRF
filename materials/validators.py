from rest_framework import serializers

allowed_resource = 'youtube.com'


class ValidateURLResource:
    """Класс валидации добавляемой ссылки"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """Метод проверки ссылки на соответсвие заданным параметрам"""
        url = value.get(self.field)
        if url and not url.startswith('https://www.youtube.com/'):
            raise serializers.ValidationError('Ссылка возможна только на сайт youtube.com. Введите правильный URL.')
