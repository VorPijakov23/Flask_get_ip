"""Файл конфигурации"""

port = 35123                                        # Порт для работы сервера
host = "0.0.0.0"                                    # Хост для работы сервера
command = f"ssh -R 80:localhost:{port} serveo.net"  # Команда для получения домена
time_temp = "%H:%M:%S"                              # Шаблон для времени
debug = False                                       # Показ ошибок Flask (False по дефолту)
url_ip_info = "https://ipwho.is/"                   # Сервис для информации об IP
