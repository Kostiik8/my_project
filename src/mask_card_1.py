from typing import Any


def card_numbers(user_input: Any) -> str:
    """Функция запрашивает у пользователя номер карты
    и возвращает номер с засекренной частью.
    """
    user_input = user_input.replace(" ", "")
    masks_card = []
    block_size = 4
    for num in range(0, len(user_input), block_size):
        masks_card.append(user_input[num: num + block_size])
    result = " ".join(masks_card)
    result = result[:7] + "*" * 2 + " " + "*" * 4 + result[14:]
    return result
