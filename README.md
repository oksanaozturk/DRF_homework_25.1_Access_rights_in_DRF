# DRF_homework_24.1

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



