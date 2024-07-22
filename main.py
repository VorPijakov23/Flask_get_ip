from multiprocessing import Process  # Импортируем класс Process из модуля multiprocessing для запуска нескольких процесоов
from apps.server import start_server  # Импортируем функцию start_server из модуля apps.server для запуска сервера
from apps.domain import get_domain  # Импортируем функцию get_domain из модуля apps.domain для запуска домена сервера


def main():
    # Создаем два отдельных процесса
    p1 = Process(target=get_domain)  # Процесс p1 будет запускать функцию get_domain
    p2 = Process(target=start_server)  # Процесс p2 будет запускать функцию start_server

    # Запускаем оба процесса
    p1.start()
    p2.start()

    # Ожидаем завершения обоих процессов
    p1.join()
    p2.join()


if __name__ == '__main__':  # Это основная точка входа в скрипт
    try:
        main()  # Вызываем функцию main
    except KeyboardInterrupt:
        print("Exit")  # Печатаем "Exit" если скрипт был прерван с помощью Ctrl+C
