import datetime

from src.masks import card_numbers, score_numbers


def information(string_number: str) -> str:
    """Функция принимает из результат выполнения из других функций
    и строку пользователя после чего возвращает обьдинив их
    """

    type_card = ""
    number_card = ""
    for i in string_number:
        if i.isalpha():
            type_card += i
        elif i.isdigit():
            number_card += i
    if "Счет" in type_card:
        return f"{type_card} {score_numbers(number_card)}"
    else:
        return f"{type_card} {card_numbers(number_card)}"


def convert_date(encrypted_date: str) -> str:
    """Функция принимает дату в формате ISO 8601 и возвращает её в формате дд.мм.гггг"""
    if not encrypted_date:  # Проверка на пустую строку
        raise ValueError("Пустая строка даты")
    if encrypted_date[-1].isdigit():
        date_time_obj = datetime.datetime.strptime(encrypted_date, "%Y-%m-%dT%H:%M:%S.%f")
    else:
        date_time_obj = datetime.datetime.strptime(encrypted_date, "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = date_time_obj.strftime("%d.%m.%Y")
    return formatted_date
