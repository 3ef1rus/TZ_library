# TZ_library
Приложение для создания и управления персональной библиотекой книг

# Функционал:

1. Добавление книги:
Для добавления новой книги в библиотеку необходимо предоставить следующую информацию:
    Название: Строка, обязательное поле.
    Автор: Строка, обязательное поле.
    Год издания: Целое число, обязательное поле.
При успешном добавлении книге автоматически присваивается уникальный идентификатор и статус "В наличии".
Система проводит валидацию введенных данных.
При обнаружении ошибок пользователю предоставляется три попытки для исправления некорректных данных.

2. Удаление книги:
Чтобы удалить книгу из библиотеки, укажите ее уникальный идентификатор.
После подтверждения операции книга будет безвозвратно удалена.

3. Поиск книг:
Для поиска книг можно использовать следующие критерии:
    Название: Точный поиск по названию книги.
    Автор: Точный поиск по имени автора.
    Год издания: Точный поиск по году издания.
Результаты поиска отображаются в виде списка, содержащего идентификатор, название, автора и год издания найденных книг.

4. Отображение книг:
Список всех книг отображается в виде списка, содержащей следующую информацию:
    ID: Уникальный идентификатор книги.
    Название: Название книги.
    Автор: Автор книги.
    Год издания: Год издания книги.
    Статус: Текущий статус книги (в наличии или выдана).

5. Изменение статуса книги:
Для изменения статуса книги необходимо:
    Выбрать пункт меню "Изменить статус".
    Указать идентификатор книги, статус которой требуется изменить.
    Ввести новый статус книги из доступных вариантов: "В наличии" или "Выдана".

6. Загрузка/сохранение данных:
Загрузка данных:
Поддерживается загрузка данных из JSON-файла.
Файл должен содержать массив объектов, где каждый объект описывает книгу с полями: id, title, author, year, status.
Если в файле найдутся книги с уже существующими ID, то они будут пропущены.

Пример:
[
  {
    "id": "3d81c71221a64bdea25a816a39826a7c",
    "title": "Сто лет одиночества",
    "author": "Габриэль Гарсиа Маркес",
    "year": 1967,
    "status": true
  },
  {
    "id": "456789abcde12345678901234567890",
    "title": "Преступление и наказание",
    "author": "Фёдор Достоевский",
    "year": 1866,
    "status": false
  }
]

Сохранение данных:
Данные о книгах автоматически сохраняются в формате JSON при каждом изменении в библиотеке (добавление, удаление, изменение книги).
Файл с данными сохраняется в указанной директории.

# **Клонировать репозиторий:**
git clone https://github.com/3ef1rus/TZ_library