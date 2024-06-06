## Продолжение домашних работ по курсу Django REST framework (DRF)

### Представлены работы: 
1) DRF_homework_25.1_Access_rights_in_DRF (Права доступа в DRF)  
2) DRF_homework_25.2_Validators_pagination_tests (Валидаторы, пагинация и тесты)
3) DRF_homework_26.1_Documentation_and_Security (Документирование и безопасность)
4) DRF_homework_26.2_Celery (Celery)

### Документация находится по адресу: 
    ```
    https://pypi.org/project/django-apscheduler/
    ```

    ````                                   
    https://drf-yasg.readthedocs.io/en/stable/ (для настройки документации)
    ````

### Используемые технологии:

 - Python
 - Django
 - PostgerSQL
 - Django REST framework
 - celery
 - celery-beat
 - redis
 - stripe

### Параметры по работе в БД с Пользователями:

 - Email Пользователя
 - Номер телефона Пользователя
 - Город проживания Пользователя
 - Аватар Пользователя

### Параметры по работе в БД с Курсами:

 - Наименование курса
 - Превью курса
 - Описание
 - Автор курса

### Параметры по работе в БД с Уроками:

 - Наименование урока
 - Наименование курса, к которому привязан урок 
 - Превью урока
 - Описание
 - Ссылка на видео урока
 - Автор урока

### Параметры по работе в БД с Подпиской на обновление курса:

 - Пользователь подписки
 - Курс в подписке

### Параметры по работе в БД с Платежами:

 - Плательщик (Пользователь курса)
 - Дата оплаты курса/урока
 - Указание курса/урока, который был оплачен
 - Сумма оплаты
 - Способ оплаты
 - Ссылка на оплату
 - ID Сессии

<details>
<summary> Инструкция по развертыванию проекта</summary>


* ### Для разворачивания проекта потребуется создать и заполнить файл .env  по шаблону файла env.sample
#### Добавьте секретный ключ Вашего проекта
SECRET_KEY=

#### Добавте настройки для подключения к базе данных (ДБ должна быть создана)
- POSTGRES_DB=
- POSTGRES_USER=
- POSTGRES_HOST=
- POSTGRES_PORT=
- POSTGRES_PASSWORD=

#### Напишите Вашу почту
EMAIL_HOST_USER=
#### Напишите пароль для Приложения Яндекс, а не пароль входа на Почту
EMAIL_HOST_PASSWORD=

####  Добавьте секретный ключ из Личного кабинета на Stripe
STRIPE_API_KEY=

####  Добавьте настройки для celery
- CELERY_BROKER_URL=
- CELERY_RESULT_BACKEND=)


### Используется виртуальное окружение - venv, зависимости записаны в файл requirements.txt
  - pip install -r requirements.txt

### Команда для запуска Приложения: 
  - python manage.py runserver

### Команда для запуска celery-bea и celery worker одной командой:
  - celery -A condig worker --beat --scheduler django --loglevel=info

</details>


### Автор проекта https://github.com/oksanaozturk

