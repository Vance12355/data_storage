# Data Storage
Клиент-серверное приложение для хранилища данных

## Установка
```bash
git clone https://github.com/Vance12355/data_storage.git
cd data_storage
pip install -r requirements.txt
```

## Запуск сервера
```bash
python manage.py runserver
```

## API сервера:
### GET /api/upload/
Загружает файл на сервер
```bash
http://127.0.0.1:8000/api/upload/
```
### GET /api/download/
Позволяет скачать файл с сервера
```bash
http://127.0.0.1:8000/api/download/
```
### GET /api/list/
Возвращает список всех файлов, хранящихся на сервере
```bash
http://127.0.0.1:8000/api/list/
```


## Использование клиентского CLI
Клиентское приложение представляет собой скрипт на Python (`client.py`), который взаимодействует с сервером через API

### Запуск клиентского приложения:
```bash
cd 'Storage CLI'
python client.py
```

После запуска `client.py` необходимо зарегистрироваться (если нет аккаунта) c помощью команды `register`, затем авторизоваться под своим логином, паролем с помощью команды `login`

### Доступные команды `client.py`


- `upload` — загрузка файла на сервер
- `download` — скачивание файла с сервера
- `list` - получения списка файлов на сервере
- `exit` — выход из клиентского приложения

### Пример загрузки файла на сервер

```bash
<<<upload
Введите путь к файлу для загрузки: path/to/your/file.jpg
Файл 'file.jpg' успешно загружен.
```

### Пример скачивания файла с сервера

```bash
<<<download
Введите имя файла для скачивания: file.jpg
Введите путь к папке для сохранения файла: path/to/download/directory
Файл 'file.jpg' успешно скачан в 'path/to/download/directory'
```

