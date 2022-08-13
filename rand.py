import string
from random import choice, shuffle

def randomPass():
    lower = list(string.ascli_lowercase)
    upper = list(string.ascli_uppercase)
    digits = list(string.digits)

    all = lower + upper + digits
    shuffle(all)

    length = int(input("How long is the password?: "))
    password = ''

    for i in range(length):
        password += choice(all)
        print(password)

    randomPass()