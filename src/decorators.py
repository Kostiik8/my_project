import functools
from typing import Any, Callable, Optional


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
            except Exception as e:
                if filename:
                    with open(filename, 'a') as file:
                        message = f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}\n"
                        file.write(message)
                else:
                    print(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}")
        return wrapper
    return decorator
