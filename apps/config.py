"""Файл конфигурации"""

## Url для возможного перенаправления
# url = "https://blank.page/"

port = 35123  # Порт для работы сервера
host = "0.0.0.0"  # Хост для работы сервера
command = f"ssh -R 80:localhost:{port} serveo.net"  # Команда для получения домена
