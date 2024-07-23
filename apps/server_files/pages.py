from apps.server_files.utils import get_client_info, log_client_info, jsonify_response


def home():
    """Функция запуска flask сервера"""
    log_client_info()
    return jsonify_response(get_client_info())
