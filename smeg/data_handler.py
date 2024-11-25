import re
import html
import bcrypt

def replace_characters(input_string: str) -> str:
    to_replace = ["<", ">", ";"]
    replacements = ["%3C", "%3E", "%3B"]
    char_list = list(input_string)
    for i in range(len(char_list)):
        if char_list[i] in to_replace:
            index = to_replace.index(char_list[i])
            char_list[i] = replacements[index]

def check_password(password: str) -> bytes:
    if not issubclass(type(password), str):
        raise TypeError("Expected a string")
    if len(password) < 9:
        raise ValueError("less than 9 characters")
    if len(password) > 12:
        raise ValueError("more than 12 characters")
    if re.search(r"[@$!%*?&]", password):
        raise ValueError("contains one of '@$!%*?&' special characters")
    if re.findall(r"[a-z]", password) + (r"[A-Z]", password)< 4:
        raise ValueError("Has less than 4 Alpha")
    if re.findall(r"[0-9]", password) < 3:
        raise ValueError("Has less than 3 Numbers")

    return password.encode