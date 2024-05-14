import pytest


@pytest.fixture
def zero_list():
    return []


@pytest.fixture
def zero_list_func_2():
    return []


@pytest.fixture
def item_in_list():
    return [{'key': 'value'}]


@pytest.fixture
def right_sorted():
    return [
        {'date': '2024-05-10', 'value': 5},
        {'date': '2024-05-09', 'value': 4},
        {'date': '2024-05-08', 'value': 3}]


@pytest.fixture
def uncorrect_symbols():
    return '@'


@pytest.fixture
def input_date():
    return "2018-07-11T02:26:18.671407"
