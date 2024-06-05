import unittest.mock
from src.utils import read_json_transactions


@unittest.mock.patch('os.path.exists')
def test_read_json_transactions_file_exists(mock_exists):
    mock_exists.return_value = True
    path = 'existing_file.json'
    result = read_json_transactions(path)
    assert result is not None
    assert isinstance(result, list)


@unittest.mock.patch('os.path.exists')
def test_read_json_transactions_file_not_found(mock_exists):
    mock_exists.return_value = False
    path = 'non_existing_file.json'
    result = read_json_transactions(path)
    assert result == []


@unittest.mock.patch('os.path.exists')
def test_read_json_transactions_invalid_json_format(mock_exists):
    mock_exists.return_value = True
    path = 'invalid_json_format.json'
    result = read_json_transactions(path)
    assert result == []
