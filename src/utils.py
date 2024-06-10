import json
import os
import logging
from typing import Any


logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('..//logs/utils.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_transactions(path: str) -> Any:
    """Функция загружает данные из файла в формате Json"""
    if not os.path.exists(path):
        logger.info("Файл не найден.")
        return []

    try:
        logger.info('Открываем json файл')
        with open(path) as file:
            try:
                transactions = json.load(file)
                logger.info('Проверка содержимого в файле')
                return transactions
            except json.JSONDecodeError:
                logger.error("Ошибка при декодировании JSON.")
                return []
    except Exception as e:
        logger.error(f"Произошла ошибка при чтении файла: {e}")
        return []
