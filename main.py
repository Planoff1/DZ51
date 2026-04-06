import string
import keyword


def is_valid_variable_name(name: str) -> bool:

    if not name:
        return False

    if name[0].isdigit():
        return False

    allowed_chars = string.ascii_lowercase + "_"
    for char in name:
        if char not in allowed_chars:
            return False

    if name in keyword.kwlist:
        return False

    if "__" in name:
        return False

    return True

user_input = input("Введіть ім'я змінної: ")
result = is_valid_variable_name(user_input)
print(result)
