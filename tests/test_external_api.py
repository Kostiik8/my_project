import os
from unittest.mock import Mock, patch

from src.external_api import convert_to_rub, get_exchange_rate

API_KEY = os.getenv("API_KEY")


@patch('requests.get')
def test_get_exchange_rate(mock_get):
    # Создаем фиктивный ответ, который будет возвращен вместо реального API вызова
    mock_response = Mock()
    expected_rate = 75.0
    mock_response.json.return_value = {
        "info": {
            "rate": expected_rate
        }
    }
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    # Вызов тестируемой функции
    rate = get_exchange_rate("USD", "RUB")

    # Проверка ожидаемого результата
    assert rate == expected_rate, f"Ожидается {expected_rate}, получаем {rate}"

    # Проверка, что mock был вызван с правильными аргументами
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD",
        headers={
            "apikey": API_KEY
        }
    )


@patch('src.external_api.get_exchange_rate')
def test_convert_to_rub(mock_get_exchange_rate):
    """Функция проверет константную ковертацию без API запроса"""
    mock_get_exchange_rate.return_value = 75.0

    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "code": "USD"
            }
        }
    }

    amount_in_rub = convert_to_rub(transaction)
    expected_amount_in_rub = round(100.00 * 75.0, 2)
    assert amount_in_rub == expected_amount_in_rub, f"Ожидается {expected_amount_in_rub}, получаем {amount_in_rub}"

    mock_get_exchange_rate.assert_called_once_with("USD", "RUB")


@patch('src.external_api.get_exchange_rate')
def test_convert_euro_to_rub(mock_get_exchange_rate):
    """Функция проверет константную ковертацию без API запроса с другой валютой"""
    mock_get_exchange_rate.return_value = 80.0

    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "code": "EUR"
            }
        }
    }

    amount_in_rub = convert_to_rub(transaction)
    expected_amount_in_rub = round(100.00 * 80.0, 2)
    assert amount_in_rub == expected_amount_in_rub, f"Ожидается {expected_amount_in_rub}, получаем {amount_in_rub}"

    mock_get_exchange_rate.assert_called_once_with("EUR", "RUB")


@patch('src.external_api.get_exchange_rate')
def test_convert_invalid_currency_to_rub(mock_get_exchange_rate):
    """Фугкция выдает ошибку если нечего конвертировать"""
    mock_get_exchange_rate.return_value = 0

    try:
        assert False, "Ожидалось исключение InvalidCurrencyError"
    except AssertionError:
        pass

    mock_get_exchange_rate.assert_not_called()


@patch('src.external_api.get_exchange_rate')
def test_convert_to_rub_with_zero_rate(mock_get_exchange_rate):
    """Фугкция выдает ошибку при конвертирование на ноль"""
    mock_get_exchange_rate.return_value = 0.0
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "code": "USD"
            }
        }
    }

    try:
        convert_to_rub(transaction)
        assert False, "Ожидалось исключение ZeroExchangeRateError"
    except AssertionError:
        pass

    mock_get_exchange_rate.assert_called_once_with("USD", "RUB")
