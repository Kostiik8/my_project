import json
import os
from typing import Any


def read_json_transactions(path: str) -> Any:
    """Функция загружает данные из файла в формате Json"""
    if not os.path.exists(path):
        print("Файл не найден.")
        return []

    try:
        with open(path) as file:
            try:
                transactions = json.load(file)
                return transactions
            except json.JSONDecodeError:
                print("Ошибка при декодировании JSON.")
                return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []
