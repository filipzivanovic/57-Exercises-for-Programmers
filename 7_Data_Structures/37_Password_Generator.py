import string
import random
import pyperclip


def input_number(message):
    while True:
        try:
            user_input = int(input(message))
            if user_input < 0:
                print("Not a positive number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return user_input


def generate_password(length, special, numbers):
    letters = length - special - numbers
    password = []
    for i in range(letters):
        password.append(random.choice(string.ascii_letters))
    for i in range(special):
        password.append(random.choice(string.punctuation))
    for i in range(numbers):
        password.append(random.choice(string.digits))
    random.shuffle(password)
    return password


length = input_number("What's the minimum length? ")
special = input_number("How many special characters? ")
numbers = input_number("How many numbers? ")

password = generate_password(length, special, numbers)
password = ''.join(password)
pyperclip.copy(password)
