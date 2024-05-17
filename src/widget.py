from datetime import datetime
from typing import Any


def information(card_numbers: Any, score_numbers: Any, user_input: Any) -> str:
    """Функция принимает из результат выполнения из других функций
       и строку пользователя после чего возвращает обьдинив их
    """

    type_card = ""
    number_card = ""
    for i in user_input:
        if i.isalpha():
            type_card += i
        elif i.isdigit():
            number_card += i
    if "Счет" in type_card:
        return f"{type_card} {score_numbers(number_card)}"
    else:
        return f"{type_card} {card_numbers(number_card)}"


def convert_date(input_date: str) -> str:
    """Функция берет из библиотеки данные для работы с данными,
       принимает на вход строку с временем и возвращает в выбранном формате
    """

    date_obj = datetime.strptime(input_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
