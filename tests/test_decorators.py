from typing import Union
from src.decorators import log


@log(filename="../mylog.txt")
def my_function(x: int, y: int) -> int:
    """Функция складывает числа"""
    return x + y


my_function(1, 2)


@log(filename="../mylog.txt")
def my_error_function(x:int, y:int) -> Union[int, float, None]:
    """Функция делит числа одно на другое с ошибкой"""
    return x / y


my_error_function(0, 2)


@log()
def my_function_not_file(x:int, y:int) -> Union[int, float, None]:
    """Функция делит числа одно на другое
       с ошибкой и выводит в консоль
    """
    return x / y


my_function_not_file(0, 3)


@log()
def my_function_not_file_with_error(x:int, y:int) -> Union[int, float, None]:
    """Функция делит числа одно на другое
           без вывода в файл
        """
    return x / y


my_function_not_file_with_error(0, 3)
