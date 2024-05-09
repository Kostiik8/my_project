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


list_of_dicts = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def dictionary(sort_dictionaries: list[Dict[str, Any]], reverse: bool = True) -> list[Dict[str, Any]]:
    """Функция принимает список словарей и возвращает
       отсортированный список по убыванию дат
    """

    new_list = sorted(sort_dictionaries, key=lambda x: x['date'], reverse=True)
    return new_list


sort_dictionaries = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
