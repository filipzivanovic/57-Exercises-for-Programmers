import random


def input_number(message):
    while True:
        try:
            user_input = int(input(message))
            if user_input <= 0:
                print("Not a positive number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return user_input


def generate_random():
    print("Let's play Guess the Number.")
    while True:
        difficulty = input_number('Pick a difficulty level (1 - 10, 2 - 100, or 3 - 1000): ')
        if difficulty not in (1, 2, 3):
            print("Not an existing difficulty! Try again.")
            continue
        break
    difficulties = {1: 10, 2: 100, 3: 1000}
    diff = difficulties[difficulty]
    random_number = random.randint(1, diff)
    return random_number


def guess_number(random_number):
    guessed = []
    guess = input_number("I have my number. What's your guess? ")
    count = 1
    while guess != random_number:
        already = 0
        for number in guessed:
            if guess == number:
                print("You have already guessed that number.")
                already = 1
        if guess < random_number:
            if already == 0:
                guessed.append(guess)
            guess = input_number("Too low. Guess again: ")
        elif guess > random_number:
            if already == 0:
                guessed.append(guess)
            guess = input_number("Too high. Guess again: ")
        count += 1

        continue
    return count


def print_output(count):
    count_s = "es"
    if count == 1:
        count_s = ""
        addition = "You're a mind reader!"
    elif 2 <= count <= 3:
        addition = "Most impressive."
    elif 4 <= count <= 6:
        addition = "You can do it better than that."
    else:
        addition = "Better luck next time."
    return "Bravo! You got it in %d guess%s! %s" % (count, count_s, addition)

while True:
    random_number = generate_random()
    count = guess_number(random_number)
    print(print_output(count))
    if input("Play again? y/n : ").lower() == "n":
        print("Bye Bye !!!")
        break

