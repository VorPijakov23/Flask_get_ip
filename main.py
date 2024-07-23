from asyncio import create_task, gather, run  # Библиотека для асинхронного программмирования
from apps.server import start_server  # Функция для запуска сервера Flask
from apps.domain import get_domain  # Функция для получения домена


async def main():
    """Главная функция программы"""
    domain = create_task(get_domain())  # Запуск функции get_domain как процесс
    server = create_task(start_server())  # Запуск функции start_server как процесс (оба процесса работают параллельно)
    await gather(domain, server)  # Ожидание завершения процессов


if __name__ == '__main__':  # Точка входа в программу
    try:
        run(main())  # Асинхронный запуск функции main()
    except KeyboardInterrupt:  # Исключение KeyboardInterrupt
        print("Exit")  # Печатает "Exit" при завершении программы через ^C
    except Exception as e:  # Обработчик всех ошибок
        print(f"Error: {e}")
