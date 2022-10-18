# Django Homework
## ![flake8 test]( https://github.com/GrishaTS/Django_Base/actions/workflows/python-package.yml/badge.svg) 

## Клонируем репозиторию
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
##### Примечание: это необязательно, проект будет запускаться и без этого
### Создаем файл .env в корневой директории, прописываем туда секретные данные (пример - .env_example):
```commandline
SECRET_KEY=???
DEBUG=???
```
