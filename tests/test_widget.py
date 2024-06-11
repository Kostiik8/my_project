import pytest

from src.masks import score_numbers, card_numbers
from src.widget import convert_date, information


@pytest.mark.parametrize('user_input, expected_output', [
    ('Visa Platinum 7000 7922 8960 6361', 'VisaPlatinum 7000 79** **** 6361'),
    ('Счет 73654108430135874305', 'Счет **4305')

])
def test_information(user_input, expected_output):
    result = information(card_numbers, score_numbers, user_input)
    assert result == expected_output


def test_convert_date(input_date):
    output_date = convert_date(input_date)
    assert output_date == "11.07.2018"
