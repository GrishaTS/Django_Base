# Django Homework
## ![flake8 test]( https://github.com/GrishaTS/Django_Base/actions/workflows/python-package.yml/badge.svg) 

### Клонируем репозиторию
```commandline 
git clone https://github.com/GrishaTS/Django_Base.git
```

### Переходим в папку Django_Base
```commandline 
cd Django_Base
```

### Устанавливаем виртуальное окружение и все зависимости
| Windows | MacOs + Linux                            |Обозначение|
| :--------------- | :------------------------------ |:--------------- |
|`python -m venv venv`|`python3 -m venv venv`|Добавлем вирутальное окружение|
|`.\venv\Scripts\activate`|`source venv/bin/activate`| Активируем вирутальное окружение|
|`pip install -r requirements.txt`|`pip3 install -r requirements.txt`| Устанавливаем все зависимости в вирутальное окружение|

### Переходим в папку lyceum
```commandline 
cd lyceum
```

### Запускаем сайт
| Windows | MacOs + Linux                            |
| :--------------- | :------------------------------ |
|`python manage.py runserver`|`python3 manage.py runserver`|


## Доп задание:
### Устанавливаем библиотеку для переменных окружения
| Windows | MacOs + Linux                            |Обозначение|
| :--------------- | :------------------------------ |:--------------- |
|`pip install python-dotenv`|`pip3 install python-dotenv`|Добавляем библиотеку|
### Создаем файл .env, прописываем туда все секретные данные: 
```commandline 
SECRET_KEY=django-insecure-#ob)5wygi#bi1z&qs=z1cacv-mjh%fs+di)i+2tw49#e6c#9+)
DEBUG=True
```

### Чтобы забрать переменные из файла .env: 
#### 1) Импортируем os и dotenv.load_dotenv
```commandline 
import os
from dotenv import load_dotenv
```

#### 2) Забираем переменные окружения и присваиваем переменным в коде
```commandline 
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
```

#### 3) Используем функцию eval для определения DEBAG, так как все переменные окружения хранятся в строках, а переменная DEBAG имеет булевое значение
```commandline 
DEBUG = os.getenv('DEBUG', "False") == “True”
```

