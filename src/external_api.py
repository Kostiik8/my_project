import os
import time
from typing import Any

import requests
from dotenv import load_dotenv
from src.utils import read_json_transactions

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_exchange_rate(from_currency: str, to_currency: str) -> Any:
    """Функция делает API запрос для получения актуальных данных о валюте"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}"
    headers = {
        "apikey": API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["info"]["rate"]
    else:
        raise Exception(f"Не удалось получить курсы валют: {response.status_code}")


def convert_to_rub(transaction: dict) -> Any:
    """Функция получает список транзакций далее и валюту в рубли"""
    if not isinstance(transaction, dict):
        raise TypeError("Транзакция должна быть словарем")

    if "operationAmount" not in transaction or "amount" not in transaction["operationAmount"] or "currency" not in \
            transaction["operationAmount"]:
        raise KeyError('Транзакция должна содержать \'operationAmount\' c \'суммой\' и \'валютой\' ')

    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return round(float(amount), 2)

    try:
        exchange_rate = get_exchange_rate(currency, "RUB")
    except Exception as e:
        print(f"Ошибка при получении обменного курса.: {e}")
        return None

    return round(float(amount) * exchange_rate, 2)


if __name__ == '__main__':
    transactions_path = '../data/operations.json'
    transactions = read_json_transactions(transactions_path)

    for transaction in transactions:
        try:
            amount_in_rub = convert_to_rub(transaction)
            if amount_in_rub is not None:
                print(f"Сумма сделки в рублях: {amount_in_rub}")
        except (TypeError, KeyError) as e:
            print(f"Ошибка обработки транзакции: {e}")
        time.sleep(1)
