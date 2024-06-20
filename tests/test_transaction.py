import unittest
from io import StringIO
from unittest.mock import mock_open, patch

import pandas as pd

from src.transaction import get_transactions_csv, get_transactions_excel


class TestTransactionsFunctions(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="""id;state;date;amount;currency_name;currency_code;from;to;description
4137938;EXECUTED;2023-01-04T13:13:34Z;15560;Real;BRL;;Счет 38164279390569873521;Открытие вклада
4699552;EXECUTED;2022-03-23T08:29:37Z;23423;Peso;PHP;Discover 7269000803370165;American Express 1963030970727681;Перевод с карты на карту""",
    )
    def test_get_transactions_csv(self, mock_open):
        expected_output = [
            [
                "4137938",
                "EXECUTED",
                "2023-01-04T13:13:34Z",
                "15560",
                "Real",
                "BRL",
                "",
                "Счет 38164279390569873521",
                "Открытие вклада",
            ],
            [
                "4699552",
                "EXECUTED",
                "2022-03-23T08:29:37Z",
                "23423",
                "Peso",
                "PHP",
                "Discover 7269000803370165",
                "American Express 1963030970727681",
                "Перевод с карты на карту",
            ],
        ]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            result = get_transactions_csv("dummy.csv")
            self.assertEqual(result, expected_output)
            self.assertIn(
                "['4137938', 'EXECUTED', '2023-01-04T13:13:34Z', '15560', 'Real', 'BRL', '', "
                "'Счет 38164279390569873521', 'Открытие вклада']",
                fake_out.getvalue(),
            )
            self.assertIn(
                "['4699552', 'EXECUTED', '2022-03-23T08:29:37Z', '23423', 'Peso', 'PHP', "
                "'Discover 7269000803370165', 'American Express 1963030970727681',"
                " 'Перевод с карты на карту']",
                fake_out.getvalue(),
            )

    @patch("pandas.read_excel")
    def test_get_transactions_excel(self, mock_read_excel):
        data = {
            "id": [4137938, 4699552],
            "state": ["EXECUTED", "EXECUTED"],
            "date": ["2023-01-04T13:13:34Z", "2022-03-23T08:29:37Z"],
            "amount": [15560, 23423],
            "currency_name": ["Real", "Peso"],
            "currency_code": ["BRL", "PHP"],
            "from": ["", "Discover 7269000803370165"],
            "to": ["Счет 38164279390569873521", "American Express 1963030970727681"],
            "description": ["Открытие вклада", "Перевод с карты на карту"],
        }
        df = pd.DataFrame(data)
        mock_read_excel.return_value = df

        with patch("sys.stdout", new=StringIO()) as fake_out:
            result = get_transactions_excel("dummy.xlsx")
            pd.testing.assert_frame_equal(result, df)
            self.assertIn("4137938", fake_out.getvalue())
            self.assertIn("4699552", fake_out.getvalue())
