from os import system            # Импортируем функцию system из модуля os, для ввода команды в shell
from apps.config import command  # Импортируем команду для получения url
from asyncio import to_thread    # Импортируем функцию для создания отдельного потока для system


async def get_domain():
    """Асинхронная функция для вызова синхронной функции system с аргументом command в отдельном потоке"""
    await to_thread(system, command)
