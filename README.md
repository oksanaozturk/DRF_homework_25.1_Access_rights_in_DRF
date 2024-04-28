# DRF_homework_24.2_Serializers

# Это продолжение DRF_homework_24.1 (Вьюсеты и дженерики)

# Для разворачивания проекта потребуется создать и заполнить файл .env  по шаблону файла .env.sample

* Задание 1
Для модели курса добавьте в сериализатор поле вывода количества уроков. Поле реализуйте с помощью 
SerializerMethodField()

* Задание 2
Добавьте новую модель в приложение users:

Платежи

пользователь,
дата оплаты,
оплаченный курс или урок,
сумма оплаты,
способ оплаты: наличные или перевод на счет.

Поля пользователь, оплаченный курс и отдельно оплаченный урок должны быть ссылками на соответствующие модели.

Запишите в таблицу, соответствующую этой модели данные через инструмент фикстур или кастомную команду.

Если вы забыли как работать с фикстурами или кастомной командой - 
можете вернуться к уроку 20.1 Работа с ORM в Django чтобы вспомнить материал.

* Задание 3
Для сериализатора для модели курса реализуйте поле вывода уроков. 
Вывод реализуйте с помощью сериализатора для связанной модели.

Один сериализатор должен выдавать и количество уроков курса и информацию по всем урокам курса одновременно.

* Задание 4
Настроить фильтрацию для эндпоинта вывода списка платежей с возможностями:

менять порядок сортировки по дате оплаты,
фильтровать по курсу или уроку,
фильтровать по способу оплаты.



# Последовательность действий:

1) Добавляем новый class CourseDetailSerializer в serislezer.py

2) Добавляем в views.py/class CourseViewSet метод get_serializer_class для выбора Serializer 
при условии выведении листа со всеми курсами или отдельно один курс

3) Добавлена модель Payment в Приложение users
4) Выполнены миграции

python manage.py makemigrations 
python manage.py migrate   

5) В admin.py добавлены настройки для модели Payment

6) Добавлена кастомная команда create_payments в user.management.commands для заполненая таблицы платежей

7) Созданы фикстуры для приложений  таблиц

python -Xutf8 manage.py dumpdata materials -o data_materials.json
python -Xutf8 manage.py dumpdata users -o data_users.json  

8) Настраиваем фильтры. Для этого заходим на сайт https://www.django-rest-framework.org/, 
выбираем там в APIGuide раздел filtering

устанавливаем django-filter: pip install django-filter

!!! заносим в requirements.txt 
+ прописываем её в config/settings.py в INSTALLED_APPS как django-filters (с s  на конце)!!!

+ Добавление настроек REST_FRAMEWORK в config/settings.py

9)  Настройка сортировки в users/views.py
     Переопределяем backends так как для ordering и search нужен filters.OrderingFilter,
     который импортируем из rest_framework/filters, а для filterset нужен только DjangoFilterBackend, который из django-filters

     filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
     ordering_fields = ('date_payment',)
 
     Чтобы фильтровать нужно добавить ?ordering=date_payment (можно сочетать и фильтрацию, и сортировку одновременно)
     http://127.0.0.1:8000/users/payments?ordering=date_payment

10) Настраиваем фильтрацию в в users/views.py, список меняем на кортеж, как более защищенный
    
    filterset_fields = ('lesson', 'course', 'payment_method')


Чтобы фильтровать нужно добавить - ?payment_method=transfer
    
    http://127.0.0.1:8000/users/payments?payment_method=transfer
