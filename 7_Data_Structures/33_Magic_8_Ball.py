import random

answers = ["Yes", "No", "Maybe", "Ask again later"]

while True:
    input("What's your question? ")
    print(random.choice(answers))
    if input("Play again? y/n : ").lower() == "n":
        print("Bye Bye !!!")
        break