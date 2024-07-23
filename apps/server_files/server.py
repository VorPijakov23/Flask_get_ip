from flask import Flask, request, jsonify
from logging import getLogger
from apps.server_files.pages import home
from apps.config import host, port, debug


class Server:
    """Класс для управления сервером Flask"""

    def __init__(self):
        self.app = Flask(__name__)
        self.app.logger.disabled = True
        log = getLogger('werkzeug')
        log.disabled = True

    def setup_routes(self, path, title, func):
        self.app.add_url_rule(path, title, func)

    async def start_server(self):
        """Функция запускающая сервер"""
        self.setup_routes(path="/", title="home", func=home)
        await self.app.run(host=host, port=port, debug=debug)