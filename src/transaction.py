import csv

import pandas as pd


def get_transactions_csv(file_path: str) -> list[list[str]]:
    """Функция открывает и выводит в консоль csv файл"""
    rows = []
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            print(row)
            rows.append(row)

        return rows


def get_transactions_excel(file_path: str) -> pd.DataFrame:
    """Функция открывает и выводит в консоль excel файл"""
    df = pd.read_excel(file_path)
    df = df[df["id"].notnull()]
    print(df)
    return df


if __name__ == "__main__":
    file_path = '../data/transactions.csv'
    get_transactions_csv(file_path)

    file_path = '../data/transactions_excel.xlsx'
    get_transactions_excel(file_path)
