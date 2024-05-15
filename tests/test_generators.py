from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, transactions
import pytest


def test_empty_transactions(zero_list_for_generator):
    descriptions = list(transaction_descriptions(zero_list_for_generator))
    assert descriptions == zero_list_for_generator


def test_transaction_descriptions():
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_filter_by_currency():
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268


def test_filter_by_another_currency():
    usd_transactions = filter_by_currency(transactions, "RUB")
    assert next(usd_transactions)["id"] == 873106923
    assert next(usd_transactions)["id"] == 594226727


def test_filter_by_currency_currency_not_found(zero_list_for_generator):
    usd_transactions = list(filter_by_currency(transactions, "EURO"))
    assert usd_transactions == zero_list_for_generator


def test_filter_by_currency_empty_transactions(zero_list_for_generator):
    usd_transactions = list(filter_by_currency([], "USD"))
    assert usd_transactions == zero_list_for_generator


def test_filter_by_currency_zero_string(zero_list_for_generator):
    usd_transactions = list(filter_by_currency(transactions, ""))
    assert usd_transactions == zero_list_for_generator


def test_card_number_generator():
    cards = list(card_number_generator(1, 3))
    assert cards == ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003']


def test_card_number_generator_start_end_values():
    cards = list(card_number_generator(10, 12))
    assert cards == ['0000 0000 0000 0010', '0000 0000 0000 0011', '0000 0000 0000 0012']


@pytest.mark.parametrize("special_char", ['@', '%', '!', ':', '#', '$', '^', '&', '*', '-', '.', ','])
def test_no_special_characters_in_card_numbers(special_char):
    card_number = card_number_generator(1, 3)
    assert special_char not in card_number


def test_card_number_generator_length():
    cards = list(card_number_generator(1, 5))
    assert len(cards) == 5


def test_card_number_generator_unique_cards():
    cards = list(card_number_generator(1, 10))
    assert len(cards) == len(set(cards))


def test_card_number_generator_invalid_range():
    cards = list(card_number_generator(5, 3))
    assert len(cards) == 0


def test_card_number_generator_card_length():
    card_length = 19
    card_number = next(card_number_generator(1, 10))
    assert len(card_number) == card_length


@pytest.mark.parametrize("card_number", card_number_generator(1, 3))
def test_only_digits_in_card_numbers(card_number):
    assert card_number.replace(" ", "").isdigit()


@pytest.mark.parametrize("card_number", card_number_generator(1, 3))
def test_no_extra_spaces_in_card_numbers(card_number):
    assert " " in card_number


@pytest.mark.parametrize("card_number", card_number_generator(1, 3))
def test_correct_separator_in_card_numbers(card_number):
    assert card_number[4] == " " and card_number[9] == " " and card_number[14] == " "
