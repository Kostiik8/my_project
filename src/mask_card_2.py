from typing import Union


def score_numbers(user_input: Union[str]) -> str:
    """Функция запрашивает у пользователя номер счета
    и возвращает последние 4 цифры счета.
    """
    masks_score = []
    for num in range(len(user_input)):
        masks_score.append(user_input[num:num])
    result = "*" * 2 + user_input[-4:]
    return result
