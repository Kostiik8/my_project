import logging
import os


def setup_logging(name: str, log_file: str, level=logging.DEBUG) -> logging.Logger:
    """Фунция для обработки модулей с помощью логирования, фиксит ошибку с путем"""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.FileHandler(log_file, mode='w')
    handler.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
