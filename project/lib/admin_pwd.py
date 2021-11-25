import string
from random import randint
import random


def generate_password():
    # Random string with a combination of lower, uppercase and numbers
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(7))
    num = randint(10, 99)
    password = result_str + str(num)
    return password

