import functools
from typing import Any, Callable, Optional, Union


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор логирующий вызов функции в файл или консоль."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, 'a') as file:
                        message = f"{func.__name__} ok\n"
                        file.write(message)
                else:
                    print(f"{func.__name__} ok")
                return result
            except ZeroDivisionError as e:
                if filename:
                    with open(filename, 'a') as file:
                        message = f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}\n"
                        file.write(message)
                else:
                    print(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """Функция складывает числа и выводит в файл """
    return x + y


my_function(1, 2)


@log(filename="mylog.txt")
def my_error_function(x: int, y: int) -> Union[int, float, None]:
    """Функция делит числа одно на другое с ошибкой
       и выводит в файл
    """
    return x / y


my_error_function(5, 0)


@log()
def my_function_not_file(x: int, y: int) -> Union[int, float, None]:
    """Функция складывает числа одно на другое
       и выводит в консоль
    """
    return x + y


my_function_not_file(4, 2)


@log()
def my_function_not_file_with_error(x: int, y: int) -> Union[int, float, None]:
    """Функция делит числа одно на другое
           и выводит в консоль
        """
    return x / y


my_function_not_file_with_error(3, 0)
