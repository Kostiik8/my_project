from typing import Any, Union

from src.logger import setup_logging

logger = setup_logging('masks', 'logs/masks.log')


def card_numbers(user_input: Any) -> str:
    """Функция запрашивает у пользователя номер карты
    и возвращает номер с засекренной частью.
    """
    user_input = user_input.replace(" ", "")
    masks_card = []
    block_size = 4
    logger.info('Делаем отступы согласно заданию')
    for num in range(0, len(user_input), block_size):
        masks_card.append(user_input[num: num + block_size])
    result = " ".join(masks_card)
    logger.info('Маскируем карту согласно заданию')
    result = result[:7] + "*" * 2 + " " + "*" * 4 + result[14:]
    logger.info('Выводим замаскированный результат')
    return result


def score_numbers(user_input: Union[str]) -> str:
    """Функция запрашивает у пользователя номер счета
    и возвращает последние 4 цифры счета.
    """
    masks_score = []
    logger.info('Проверяем длину ввода пользователя')
    for num in range(len(user_input)):
        masks_score.append(user_input[num:num])
    logger.info('Маскируем карту согласно заданию')
    result = "*" * 2 + user_input[-4:]
    logger.info('Выводим замаскированный результат')
    return result
