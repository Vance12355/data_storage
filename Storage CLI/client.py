import requests
import os

# URL-адрес сервера
SERVER_URL = 'http://127.0.0.1:8000/api/'


#Сессия для клиента
session = requests.Session()
IS_AUTH = False

def register(username, password):
    """Регистрация нового пользователя"""
    response = session.post(f'{SERVER_URL}register/', data={'username': username, 'password': password})
    if response.status_code == 201:
        print("Пользователь успешно зарегистрирован.")
    else:
        print(f"Ошибка регистрации: {response.json()}")

def login(username, password):
    """Авторизация пользователя"""
    response = session.post(f'{SERVER_URL}login/', data={'username': username, 'password': password})
    if response.status_code == 200:
        print("Вход выполнен успешно.")
    else:
        print(f"Ошибка входа: {response.json()}")

def upload_file(filepath):
    """Загрузка файла на сервер"""
    try:
        with open(filepath, 'rb') as file:
            response = session.post(f'{SERVER_URL}upload/', files={'file': file}, stream=True)

        print(f"Status code: {response.status_code}")
        print(f"Response content: {response.content.decode('utf-8')}")

        if response.status_code == 201:
            print(f"Файл '{filepath}' успешно загружен.")
        else:
            print(f"Ошибка при загрузке файла: {response.json()}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def download_file(filename, destination):
    """Скачивание файла с сервера"""
    try:
        response = session.get(f'{SERVER_URL}download/{filename}/')
        if response.status_code == 200:
            with open(os.path.join(destination, filename), 'wb') as file:
                file.write(response.content)
            print(f"Файл '{filename}' успешно скачан в '{destination}'.")
        else:
            print(f"Ошибка при скачивании файла: {response.json()}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def main():
    while True:
        action = input(
            "Введите 'register' для регистрации, 'login' для входа, 'upload' для загрузки файла, 'download' для скачивания файла, 'exit' для выхода: ").strip().lower()

        if action == 'register':
            username = input("Введите имя пользователя: ").strip()
            password = input("Введите пароль: ").strip()
            register(username, password)

        elif action == 'login':
            username = input("Введите имя пользователя: ").strip()
            password = input("Введите пароль: ").strip()
            login(username, password)

        elif action == 'upload':
            filepath = input("Введите путь к файлу для загрузки: ").strip()
            if os.path.isfile(filepath):
                upload_file(filepath)
            else:
                print("Указанный файл не существует.")

        elif action == 'download':
            filename = input("Введите имя файла для скачивания: ").strip()
            destination = input("Введите путь к папке для сохранения файла: ").strip()
            if os.path.isdir(destination):
                download_file(filename, destination)
            else:
                print("Указанная папка не существует.")

        elif action == 'exit':
            break

        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
