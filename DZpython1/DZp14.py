import re


def validate_password(password):
    return re.findall(r"^[A-Za-z0-9@_-]{6,18}$", password)


print(validate_password("ma-p@sswOrd"))
