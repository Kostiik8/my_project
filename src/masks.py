from src.logger import setup_logging

logger = setup_logging("masks", "logs/masks.log")


def card_numbers(string_number: str) -> str:
    """Функция запрашивает у пользователя номер карты
    и возвращает номер с засекренной частью.
    """
    string_number = string_number.replace(" ", "")
    masks_card = []
    block_size = 4
    logger.info("Делаем отступы согласно заданию")
    for num in range(0, len(string_number), block_size):
        masks_card.append(string_number[num: num + block_size])
    result = " ".join(masks_card)
    logger.info("Маскируем карту согласно заданию")
    result = result[:7] + "*" * 2 + " " + "*" * 4 + result[14:]
    logger.info("Выводим замаскированный результат")
    return result


def score_numbers(string_number: str) -> str:
    """Функция запрашивает у пользователя номер счета
    и возвращает последние 4 цифры счета.
    """
    masks_score = []
    logger.info("Проверяем длину ввода пользователя")
    for num in range(len(string_number)):
        masks_score.append(string_number[num:num])
    logger.info("Маскируем карту согласно заданию")
    result = "*" * 2 + string_number[-4:]
    logger.info("Выводим замаскированный результат")
    return result
