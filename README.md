# DRF_homework_24.1

# Для разворачивания проекта потребуется создать и заполнить файл .env  по шаблону файла .env.sample

* Задание 1
Создайте новый Django-проект, подключите DRF в настройках проекта.

* Задание 2
Создайте следующие модели:

Пользователь:
все поля от обычного пользователя, но авторизацию заменить на email;
телефон;
город;
аватарка.
Модель пользователя разместите в приложении users

Курс:
название,
превью (картинка),
описание.

Урок:
название,
описание,
превью (картинка),
ссылка на видео.

* Задание 3
Опишите CRUD для моделей курса и урока. Для реализации CRUD для курса используйте Viewsets, а для урока - Generic-классы.

Для работы контроллеров опишите простейшие сериализаторы.


* Для начала работы над задачей выполните первые шаги:
Настройте виртуальное окружение. 
Создайте новый Django-проект.

mkdir project — создаем новую директорию для проекта.

cd project — переходим в созданную директорию.

python3 -m venv env — создаем виртуальное окружение.

pip3 install django — устанавливаем пакет Django.

pip3 freeze > requirements.txt — сохраняем список зависимостей. 
После создания виртуального окружения создайте проект с помощью команды:

django-admin startproject config .

* После успешного создания проекта сделайте первую настройку. Для этого:
Создайте первое приложение с названием catalog

python manage.py startapp catalog . Внесите начальные настройки проекта. 
Сделайте настройку урлов (URL-файлов) для нового приложения.

* Установка дополнения для Django:

pip install djangorestframework + Внести новый пакет в 
INSTALLED_APPS - 'rest_framework'

pip install psycopg2-binary

pip install pillow

* В лучших практиках сразу добавляем приложение User + Внести новый пакет в 
INSTALLED_APPS + 
AUTH_USER_MODEL = "users.User")
 
python manage.py startapp users 

* Настройка DATABASES в settings.py + создаем базу  drf_hw в pgAdmin

* Только после этого делаем первые миграции

python manage.py makemigrations

python manage.py migrate

* Добавляем в корень проекта файл medis  и настройки для него в settings.py

* Создаем приложение materials

python manage.py startapp materials

* Создание в приложении materials моделей Курс и Урок + миграции + регистрация их в Админке

* Для реализации CRUD для модели Курса используем Viewsets
 
Внесены изменения 1) в views.py - CourseViewSet, 
                  2) создан файл materials/serializer.py и в нем CourseSerializer
                  3) создан файл materials/urls.py, в нем создан router (маршрутизатор для CRUD при использовании способа ViewSet)
                  4) Добавлены настройки в config/urls.py

* Для реализации CRUD для модели урока - использованы Generic-классы

Внесены изменения 1) в views.py - LessonCreateAPIView, LessonDestroyAPIView, LessonUpdateAPIView,
                             LessonRetrieveAPIView, LessonListAPIView
                  2) в файл materials/serializer.py и в нем LessonSerializer
                  3) в файле materials/urls.py добавлены пути для каждого дейставия из механизмов CRUD
