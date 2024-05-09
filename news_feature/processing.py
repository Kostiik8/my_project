from typing import Any, Dict


def dict_list(list_of_dicts: list[dict[str, Any]], state_value: Any = 'EXECUTED') -> list[dict[str, Any]]:
    """Функция принимает список словарей и возвращает
       отсортированный по значению список словарей
    """

    new_list = []
    for dict_ in list_of_dicts:
        if state_value in dict_.values():
            new_list.append(dict_)
    return new_list


def dictionary(sort_dictionaries: list[Dict[str, Any]], reverse: bool = True) -> list[Dict[str, Any]]:
    """Функция принимает список словарей и возвращает
       список словарей
    """

    new_list = sorted(sort_dictionaries, key=lambda x: x['date'], reverse=True)
    return new_list
