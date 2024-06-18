from src.processing import filter_operations_list, sort_operations_list


def test_filter_operations_list(zero_list):
    assert filter_operations_list(zero_list) == []


def test_find_key_value(item_in_list):
    assert filter_operations_list(item_in_list, "value") == item_in_list


def test_zero_dict(zero_list_func_2):
    assert sort_operations_list(zero_list_func_2) == []


def test_right_sorted(right_sorted):
    assert sort_operations_list(right_sorted)
