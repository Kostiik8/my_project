
def user_str(user_input: list[str]) -> list[str]:
    """функция принимает строку и возвращает слова если первая
       и последняя буква совпадает, а так же пустые строки или списки"""

    result = []
    for text in user_input:
        if text == "" or text[0] == text[-1]:
            result.append(text)
    return result


user_input = ["", "madam", "racecar", "noon", "level", ""]
print(user_str(user_input))
