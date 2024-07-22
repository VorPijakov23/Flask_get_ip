from os import system  # Импорт функции system для ввода команды в shell системы
from apps.config import command  # Импорт команды для получания домена


def get_domain():
    """Функция для ввода команды"""
    system(command)
