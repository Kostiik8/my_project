import os

import pandas as pd

from src.processing import filter_operations_list, sort_operations_list
from src.transaction import get_transactions_csv, get_transactions_excel
from src.utils import read_json_transactions, search_transactions, transactions_filter_by_rub
from src.widget import convert_date, information


def main():
    while True:
        print(
            """Программа: Привет! Добро пожаловать в программу работы\nс банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
        )
        user_input = input("Выберите формат файла 1/2/3: ")
        if user_input == "1":
            file_name = "data/operations.json"
            current_dir_json = os.path.join("..", file_name)
            transactions = read_json_transactions(current_dir_json)
            break
        elif user_input == "2":
            base_dir = os.path.abspath("..")
            file_name = "data/transactions.csv"
            current_dir_csv = os.path.join(base_dir, file_name)
            transactions = get_transactions_csv(current_dir_csv)
            break
        elif user_input == "3":
            current_dir_csv = "../data/transactions_excel.xlsx"
            transactions = get_transactions_excel(current_dir_csv)
            break
        else:
            print("НЕ ПРАВИЛЬНЫЙ ФОРМАТ ВВОДА!!! ВВЕДИТЕ 1, 2 или 3")
            continue

    while True:
        print("""Программа: Введите статус, по которому необходимо выполнить фильтрацию.""")
        user_input = input("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING ").upper()
        if user_input == "EXECUTED":
            filter_transactions = filter_operations_list(transactions, "EXECUTED")
            print(f"Программа: Операции отфильтрованны по статусу '{user_input}'")
            break

        elif user_input == "CANCELED":
            filter_transactions = filter_operations_list(transactions, "CANCELED")
            print(f"Программа: Операции отфильтрованны по статусу '{user_input}'")
            break

        elif user_input == "PENDING":
            filter_transactions = filter_operations_list(transactions, "PENDING")
            print(f"Операции отфильтрованны по статусу '{user_input}'")
            break

        else:
            print(f'Статус операции "{user_input}" недоступен.')
            continue

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            user_input = input("Отсортировать по возрастанию или по убыванию? ").lower()
            if user_input == "по убыванию":
                sort_operations_list_data = sort_operations_list(filter_transactions, reverse=True)
                break
            elif user_input == "по возрастанию":
                sort_operations_list_data = sort_operations_list(filter_transactions, reverse=False)
                break
        elif user_input == "нет":
            sort_operations_list_data = filter_transactions
            break

        else:
            print("Неверный ответ, введите да/нет")
            continue

    while True:
        print("Выводить только рублевые тразакции?")
        input_currency = input("Да/Нет:  ").lower()
        if input_currency == "да":
            filter_currency = transactions_filter_by_rub(sort_operations_list_data, "RUB")
            break
        elif input_currency == "нет":
            filter_currency = sort_operations_list_data
            break
        else:
            print(f"{input_currency} не верный ввод")
            continue

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            user_input_word = input("Введите ключевое слово ").lower()
            sort_operations_list_word = search_transactions(filter_currency, user_input_word)
            break
        elif user_input == "нет":
            sort_operations_list_word = filter_currency
            break
        else:
            print("Неверный ответ. Введите Да/Нет")
            continue

    if transactions == []:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    elif len(transactions) > 0:
        print(f"Всего банковских операций в выборке: {len(sort_operations_list_word)}")

    for transaction in transactions:
        convert_date_str = transaction.get("date")
        if isinstance(convert_date_str, str):
            try:
                date = convert_date(convert_date_str)
            except ValueError:
                print(f"Неверный формат даты: {convert_date_str}")
                continue
        else:
            print(f"Дата не является строкой или отсутствует: {convert_date_str}")
            continue

        from_account = transaction.get("from")
        to_account = transaction.get("to")

        if from_account and pd.notnull(from_account):
            from_ = information(from_account)
        else:
            from_ = "0"

        if to_account and pd.notnull(to_account):
            to_ = information(to_account)
        else:
            to_ = "0"

        description = transaction.get("description", "Описание отсутствует")
        amount = transaction.get("operationAmount", {}).get("amount", "Сумма отсутствует")
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", "Валюта отсутствует")
        print("Распечатываю итоговый список транзакций...")
        print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
