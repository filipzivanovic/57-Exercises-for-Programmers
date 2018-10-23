import random

names = []

while True:
    name = input("Enter a name: ")
    if name == "":
        break
    names.append(name)

while True:
    if not names:
        print("\nAll names have been chosen.")
        break
    else:
        winner = random.choice(names)
        print("\nThe winner is... %s" % winner)
        names.remove(winner)
