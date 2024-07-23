from os import system
from asyncio import to_thread
from apps.config import command


class Domain:
    """Класс для управления доменом"""

    async def get_domain(self):
        """Асинхронная функция для вызова синхронной функции system с аргументом command в отдельном потоке"""
        await to_thread(system, command)
