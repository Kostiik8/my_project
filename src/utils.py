import json
import os
from typing import Any

from src.logger import setup_logging

logger = setup_logging('utils', 'logs/utils.log')


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
