import csv
from typing import Any

import pandas as pd


def get_transactions_csv(file_path: str) -> list[dict[str, Any]]:
    """Функция открывает и выводит в консоль csv файл"""
    with open(file_path, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        csv_transactions = []
        for row in reader:
            transactions = {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": row["amount"],
                    "currency": {"name": row["currency_name"], "code": row["currency_name"]},
                },
                "description": row["description"],
                "from": row["from"],
                "to": row["to"],
            }
            csv_transactions.append(transactions)
        return csv_transactions


def get_transactions_excel(file_path: str) -> list[dict[str, Any]]:
    """Функция открывает и выводит в консоль excel файл"""
    df = pd.read_excel(file_path)
    xlsx_transactions = []
    for index, row in df.iterrows():
        transactions = {
            "id": row["id"],
            "state": row["state"],
            "date": row["date"],
            "operationAmount": {
                "amount": row["amount"],
                "currency": {"name": row["currency_name"], "code": row["currency_name"]},
            },
            "description": row["description"],
            "from": row["from"],
            "to": row["to"],
        }
        xlsx_transactions.append(transactions)
    return xlsx_transactions
