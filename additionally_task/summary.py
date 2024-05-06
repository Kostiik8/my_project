def multiplication(list_numbers: list[int]) -> int:
    """функция принимает список чисел и возвращает перемноженное
       максимальное значение
    """

    if len(list_numbers) < 2:
        return 0
    max1 = list_numbers[-1]
    max2 = list_numbers[-2]
    multi_max = max1 * max2
    return multi_max


list_numbers = [2, 3, 5, 7, 11]
print(multiplication(list_numbers))
