from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from materials.models import Course, Lesson, SubscriptionCourse
from users.models import User


class CourseTestCase(APITestCase):
    """
    Класс для тестирования CRUD модели Course (контролер был создан с помощью метода ViewSet)
    """

    def setUp(self):
        """Метод для предоставления тестового объекта."""
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@test.ru',
            password='test',
        )
        self.course = Course.objects.create(name='Тест курса', description='Тестирование CRUD модели модели Course',
                                            owner=self.user)
        self.lesson = Lesson.objects.create(name='Тест урока', course=self.course, video='https://www.youtube.com/123',
                                            owner=self.user)
        # принудительная аутентификация клиента с помощь метода force_authenticate
        # (так как только авторизованные Пользователи могут работать в системе)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        """
        Тест для проверки работы retrieve(GET) - получение данных курса по указанию pk(id) курса в запросе.
        """
        # Получаем url
        url = reverse('materials:course-detail', args=(self.course.pk,))
        # После находжения url делаем запрос (GET), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.get(url)
        # Полученные в response данные преобразуем в json
        data = response.json()
        # Далее проводим сравнение двух значений с использованием метода GET (data.get)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.course.name    # Второе значение можно написать как "Тест курса"
        )

    def test_course_create(self):
        """
        Тест для проверки работы create(POST) - Создание нового курса.
        """
        # Получаем url для create. Для create указываем course-list!!! (ТАК КАК это было создано методом ViewSet)
        url = reverse('materials:course-list')
        # Задаем данные для создания курса:
        data = {
            "name": "Test",
        }
        # После находжения url делаем запрос (POST), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        ),
        self.assertEqual(
            Course.objects.all().count(), 2   # Так как в базе данных у нас сейчас создалось 2 объекта (+ setUp)
        )

    def test_course_update(self):
        """
        Тест для проверки работы update(PUT/PATCH) -
        внесение изменений в данные курса по указанию pk(id) курса в запросе.
        """
        # Получаем url. Для update указываем course-detail!!! (ТАК КАК это было создано методом ViewSet)
        url = reverse('materials:course-detail', args=(self.course.pk,))
        # Задаем данные для внесение изменений в данные курса:
        data = {
            "name": "Test",
        }
        # После находжения url делаем запрос (PATCH), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.patch(url)
        # Далее проводим сравнение двух значений с использованием метода GET (data.get)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), "Test"    # Так как были внесены изменения "Тест курса" поменялся на "Test"
        )

    def test_course_delete(self):
        """
        Тест для проверки работы delete/destroy(DELETE) - удаление курса по указанию pk(id) курса в запросе.
        """
        # Получаем url. Для delete указываем course-detail!!! (ТАК КАК это было создано методом ViewSet)
        url = reverse('materials:course-detail', args=(self.course.pk,))
        # После находжения url делаем запрос (DELETE), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.delete(url)
        # Далее проводим сравнение двух значений с использованием метода GET (data.get)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0  # Так как из базы данных был удален объект
        )

    def test_course_list(self):
        """
        Тест на проверку работы настройки Пагинации (выведение заданного колочества сущностей на страницу).
        """
        # Получаем url для вывода всех курсов
        url = reverse('materials:course-list')
        # После находжения url делаем запрос (GET), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.get(url)
        data = response.json()
        print(data)  # Выводим, чтобы визуально сравнить данные
        # Берем пример данных, которые у нас будут выдаваться из Postman, меняя на значения, которые у нас будут
        result = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.course.pk,
                        "name": self.course.name,
                        "preview": None,
                        "description": self.course.description,
                        "owner": self.user.pk
                        }
                        ]
                }

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        ),
        self.assertEqual(
            data, result   # Сравниваем эти 2 значения
        )


class LessonTestCase(APITestCase):
    """
    Класс для тестирования CRUD модели Lesson (контролеры были созданы с помощью дженериков)
    """

    def setUp(self):
        """Метод для предоставления тестового объекта."""
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@test.ru',
            password='test',
        )
        self.course = Course.objects.create(name='Тест курса', description='Тестирование CRUD модели модели Course',
                                            owner=self.user)
        self.lesson = Lesson.objects.create(name='Тест урока', course=self.course, video='https://www.youtube.com/123',
                                            owner=self.user)
        # принудительная аутентификация клиента с помощь метода force_authenticate
        # (так как только авторизованные Пользователи могут работать в системе)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """
        Тест для проверки работы retrieve(GET) - получение данных курса по указанию pk(id) курса в запросе.
        """
        # Получаем url
        url = reverse('materials:lessons-retrieve', args=(self.lesson.pk,))
        # После находжения url делаем запрос (GET), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.get(url)
        # Полученные в response данные преобразуем в json
        data = response.json()
        # Далее проводим сравнение двух значений с использованием метода GET (data.get)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.lesson.name    # Второе значение можно написать как "Тест урока"
        )

    def test_lesson_create(self):
        """
        Тест для проверки работы create(POST) - Создание нового урока.
        """
        # Получаем url для create.
        url = reverse('materials:lessons-create')
        # Задаем данные для создания курса:
        data = {
            "name": "Test",
        }
        # После находжения url делаем запрос (POST), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        ),
        self.assertEqual(
            Lesson.objects.all().count(), 2   # Так как в базе данных у нас сейчас создалось 2 объекта (+ setUp)
        )

    def test_lesson_update(self):
        """
        Тест для проверки работы update(PUT/PATCH) -
        внесение изменений в данные урока по указанию pk(id) курса в запросе.
        """
        # Получаем url
        url = reverse('materials:lessons-update', args=(self.lesson.pk,))
        # Задаем данные для внесение изменений в данные урока:
        data = {
            "name": "Test",
        }
        # После находжения url делаем запрос (PATCH), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.patch(url)
        # Далее проводим сравнение двух значений с использованием метода GET (data.get)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), "Test"  # Так как были внесены изменения "Тест урока" поменялся на "Test"
        )

    def test_lesson_delete(self):
        """
        Тест для проверки работы delete/destroy(DELETE) - удаление урока по указанию pk(id) курса в запросе.
        """
        # Получаем url.
        url = reverse('materials:lessons-destroy', args=(self.lesson.pk,))
        # После находжения url делаем запрос (DELETE), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.delete(url)
        # Далее проводим сравнение двух значений с использованием метода GET (data.get)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0  # Так как из базы данных был удален объект
        )

    def test_lesson_list(self):
        """
        Тест на проверку работы настройки Пагинации (выведение заданного количества сущностей на страницу).
        """
        # Получаем url для вывода всех курсов
        url = reverse('materials:lessons-list')
        # После находжения url делаем запрос (GET), ответ которого запишем в переменную response,
        # чтобы потом его можно было сравнить
        response = self.client.get(url)
        data = response.json()
        print(data)  # Выводим, чтобы визуально сравнить данные
        # Берем пример данных, которые у нас будут выдаваться из Postman, меняя на значения, которые у нас будут
        result = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.lesson.pk,
                        "name": self.lesson.name,
                        "preview": None,
                        "description": self.lesson.description,
                        "video": self.lesson.video,
                        "course": self.course.pk,
                        "owner": self.user.pk

                        }
                        ]
                }

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        ),
        self.assertEqual(
            data, result   # Сравниваем эти 2 значения
        )


class SubscriptionCourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test_admin@sky.pro')
        self.course = Course.objects.create(name='C++', description='Язык программирования общего назначения',
                                            owner=self.user)
        self.lesson = Lesson.objects.create(name='Test_Modul', course=self.course, owner=self.user)
        self.subscription = SubscriptionCourse.objects.create(course=self.course, user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_is_subscription(self):
        url = reverse('materials:subscription')
        data = {
            "user": self.user.id,
            "course": self.course.pk,
        }

        response = self.client.post(url, data)
        result = response.json()
        print(result)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            result.get('message'), 'подписка удалена'
        )
