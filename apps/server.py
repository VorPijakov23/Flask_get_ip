from apps.config import port, host  # Импортируем порт и хост для запуска
from flask import Flask, request, jsonify  # Импортируем классы для работы
from logging import getLogger  # Импортируем класс для отключения логов Flask
from json import dump # Импортируем библиотеку для

app = Flask(__name__)  # Создаём эксемпляр класса Flask с указанием имени

app.logger.disabled = True  # Выключаем логи Flask
log = getLogger('werkzeug')
log.disabled = True


def get_client_ip():
    """Функция для получения IP пользователя"""
    return request.environ.get('HTTP_X_REAL_IP', request.access_route[-1])


def get_client_info():
    """Функция для компановки данных пользователя в json"""
    client_ip = get_client_ip()

    #  TODO: Сделать сканет ip адреса: https://ipdb.ipcalc.co/ipdata/
    return {
        'ip': client_ip,
        'headers': dict(request.headers),
        'args': dict(request.args),
        'form': dict(request.form),
        'files': dict(request.files),
        'user_agent': request.user_agent.string,
        'method': request.method,
        'path': request.path,
        'url': request.url
    }


def log_client_info(client_info):
    """Функция для записи данных пользователя в файлы"""
    with open("ips", "a+") as files:
        files.seek(0)
        existing_ips = files.read()
        if client_info['ip'] not in existing_ips:
            files.write(client_info['ip'] + "\n")
            files.truncate()

    with open('ips_info', 'a+') as f:
        if client_info['ip'] not in existing_ips:
            dump(client_info, f, indent=4)
            f.write("\n")
        else:
            f.write(client_info['ip'] + "\n")


@app.route("/")
def home():
    """Функция рендера главной страницы с данными пользователя"""
    client_info = get_client_info()
    log_client_info(client_info)
    return jsonify(client_info)


def start_server():
    """Функция запуска сервера"""
    app.run(host=host, port=port, debug=False)
