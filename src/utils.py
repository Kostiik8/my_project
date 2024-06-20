import json
import os
import re
from collections import Counter
from typing import Any

from src.logger import setup_logging

logger = setup_logging("utils", "logs/utils.log")


def read_json_transactions(path: str) -> Any:
    """Функция загружает данные из файла в формате Json"""
    if not os.path.exists(path):
        logger.info("Файл не найден.")
        return []

    try:
        logger.info("Открываем json файл")
        with open(path, "r", encoding="utf-8") as file:
            repos = json.load(file)
            logger.info(f"Проверяем что {path} не пустой")
            if isinstance(repos, list):
                logger.info("Возвращаем объект python repos")
                return repos
            else:
                logger.info(f"Возвращаем пустой словарь если файл {path} пустой")
                return []
    except Exception as e:
        logger.error(f"Произошла ошибка при чтении файла: {e}")
        return []


def search_transactions(transactions: list, search_string: str) -> list[Any]:
    """функция которая фильтруем список словарей по заданной строке поиска"""
    filtered_transactions = []
    for transaction in transactions:
        if "description" in transaction and re.search(search_string, transaction["description"], re.IGNORECASE):
            filtered_transactions.append(transaction)
    return filtered_transactions


def get_counter_categories(transactions: list, list_categories: list) -> dict:
    """Функция которая подсчитывает количество операций в категории"""
    operations_categories = []
    for transaction in transactions:
        for category in list_categories:
            if "description" in transaction and category in transaction["description"]:
                operations_categories.append(category)
    return dict(Counter(operations_categories))


def transactions_filter_by_rub(transactions: list, search_key: str) -> list:
    """Функция фильтрации транзакций по коду валюты"""
    result = []
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and re.search(search_key, transaction["operationAmount"]["currency"]["code"], re.IGNORECASE)
        ):
            result.append(transaction)
    return result


# base_dir = os.path.abspath('..')
# file_name = 'data/operations.json'
# current_dir = os.path.join(base_dir, file_name)
# transactions = read_json_transactions(current_dir)
#
# list_categories = ['Перевод с карты на карту']
# counter_categories = get_counter_categories(transactions, list_categories)
# # #
# # # filter_transactions = search_transactions(transactions, 'Перевод с карты на карту')
# # # for transaction in filter_transactions:
# # #     print(transaction)
# print(counter_categories)
