from apps.config import port, host, time_temp, debug, url_ip_info  # Импортируем данные из config.py
from flask import Flask, request, jsonify  # Импортируем экземпляр класса Flask и функции для работы с json, ip
from logging import getLogger  # Импорт функции для получения логгера
from json import dump  # Функция необходимая для красивого вывода json
from datetime import datetime  # Функция для работы со временем
from requests import get, exceptions  # Функции для get запросса к сервису с данными url


app = Flask(__name__)  # Экземпляр класса Flask

app.logger.disabled = True  # Выключение логов flask
log = getLogger('werkzeug')  # Получение логгера Werkzeug, который отвечает за регистрацию событий и ошибок
log.disabled = True  # Отключает логи для Werkzeug


def get_current_time():
    """Функция для вывода текущего времени"""
    return datetime.now().strftime(time_temp)


def get_client_ip():
    """Функция для получения IP пользователя"""
    return request.environ.get('HTTP_X_REAL_IP', request.access_route[-1])


def get_ip_info(ip):
    """Функция для получения информации об IP"""
    try:
        response = get(f"{url_ip_info}{ip}")
        if response.status_code == 200:
            return response.json()
        else:
            print("GET request failed. Status code:", response.status_code)
    except exceptions.RequestException as e:
        print("Error sending GET request:", e)


def get_client_info():
    """Функция для составления json файла с данными пользователя"""
    client_ip = get_client_ip()  # Получаем IP пользователя
    ip_info = get_ip_info(client_ip)  # Получение данных об IP
    return {
        'ip_info': dict(ip_info),                 # Подробная информация об IP
        'headers': dict(request.headers),         # Заголовки https запросса
        'user_agent': request.user_agent.string,  # Информация о браузере
        'method': request.method,                 # Методы
        'path': request.path,                     # Страница (Всегда /)
        'url': request.url,                       # Url запросса
        "time": get_current_time()                # Текущее время
    }


def log_client_info(client_info):
    """Функция для записи в лог файлы"""
    with open("ips", "a+") as files:  # Запись в файл ips
        files.seek(0)
        existing_ips = files.read()
        if client_info['ip_info']["ip"] not in existing_ips:
            files.write(client_info['ip_info']["ip"] + "\n")
            files.truncate()

    with open('ips_info', 'a+') as f:  # Запись в фалй ips_info
        if client_info['ip_info']["ip"] not in existing_ips:
            dump(client_info, f, indent=4)
            f.write("\n")
        else:
            f.write(f"[ * ] {get_current_time()}    {client_info['ip_info']['ip']}\n")


@app.route("/")
async def home():
    """Асинхронная функция запуска flask сервера"""
    client_info = get_client_info()  # Компановка данных пользователя в json
    log_client_info(client_info)  # Запись в лог файлы
    return jsonify(client_info)  # Вывод json файла на главную страницу


async def start_server():
    """Асинхронная функция запускающая сервер"""
    app.run(host=host, port=port, debug=debug)
