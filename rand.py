import string
from random import choice


def randomPass():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    charset = lowercase + uppercase + digits

    length = int(input("How long is the password?: "))
    password = "".join(choice(charset) for _ in range(length))
    print(password)


randomPass()