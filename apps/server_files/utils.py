from datetime import datetime
from requests import get, exceptions
from json import dumps
from apps.config import time_temp, url_ip_info
from apps.server_files.server import request, jsonify


def get_current_time():
    """Функция для вывода текущего времени"""
    return datetime.now().strftime(time_temp)


def get_client_ip():
    """Функция для получения IP пользователя"""
    from flask import request
    return request.environ.get('HTTP_X_REAL_IP', request.access_route[-1])


def get_ip_info(ip):
    """Функция для получения информации об IP"""
    try:
        response = get(f"{url_ip_info}{ip}")
        if response.status_code == 200:
            return response.json()
        else:
            print("GET request failed. Status code:", response.status_code)
            return {}
    except exceptions.RequestException as e:
        print("Error sending GET request:", e)
        return {}


def log_client_info():
    """Функция для записи в лог файлы"""
    client_info = get_client_info()
    with open("ips", "a+") as files:
        files.seek(0)
        existing_ips = files.read()
        if client_info['ip_info'].get("ip") not in existing_ips:
            files.write(client_info['ip_info'].get("ip", "") + "\n")
            files.truncate()
    with open('ips_info', 'a+') as f:
        if client_info['ip_info'].get("ip") not in existing_ips:
            f.write(dumps(client_info, indent=4) + "\n")
        else:
            f.write(f"[ * ] {get_current_time()}    {client_info['ip_info'].get('ip', '')}\n")


def get_client_info():
    """Функция для составления json файла с данными пользователя"""
    client_ip = get_client_ip()
    ip_info = get_ip_info(client_ip)
    info = {
        'ip_info': ip_info,
        'headers': dict(request.headers),
        'user_agent': request.user_agent.string,
        'method': request.method,
        'path': request.path,
        'url': request.url,
        "time": get_current_time()
    }
    return info


def jsonify_response(info):
    return jsonify(info)