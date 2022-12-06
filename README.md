# Django Homework
![flake8 test]( https://github.com/GrishaTS/Django_Base/actions/workflows/python-package.yml/badge.svg) 

## Клонируем репозиторий
```commandline 
git clone https://github.com/GrishaTS/Django_Base.git
```

## Переходим в папку Django_Base
```commandline 
cd Django_Base
```

## Устанавливаем виртуальное окружение и все зависимости
| Windows | MacOs + Linux                            |Обозначение|
| :--------------- | :------------------------------ |:--------------- |
|`python -m venv venv`|`python3 -m venv venv`|Добавлем вирутальное окружение|
|`.\venv\Scripts\activate`|`source venv/bin/activate`| Активируем вирутальное окружение|
|`pip install -r requirements.txt`|`pip3 install -r requirements.txt`| Устанавливаем все зависимости в вирутальное окружение|

## Переходим в папку lyceum
```commandline 
cd lyceum
```

## Запускаем сайт
| Windows | MacOs + Linux                            |
| :--------------- | :------------------------------ |
|`python manage.py runserver`|`python3 manage.py runserver`|


## Настройка .env:
##### Примечание: это необязательно
### Создаем файл .env в корневой директории, прописываем туда секретные данные (пример - .env_example):
```commandline
SECRET_KEY=secret_key_1234567890
DEBUG=boolean_value
```

## Данные тестового админа:

```commandline
email: admin@gmail.com
Password: admin
```

## Структура базы данных
#### В проекте находится тесовая база данных (db.sqlite), для ознакомления с ее структурой и админкой
### Для наглядности структуры можете посмотреть ER-диаграмму:
![image](https://user-images.githubusercontent.com/69619529/202220165-2c5f11d2-e1c9-401f-ad1a-c5338c4a1ca7.png)
### Другие таблицы:
![image](https://user-images.githubusercontent.com/69619529/205300568-9c10b5b2-1bf2-46a6-822f-cf257e288af4.png)
![image](https://user-images.githubusercontent.com/69619529/206010202-df4225b7-57cc-4634-9556-8868e80873cd.png)

