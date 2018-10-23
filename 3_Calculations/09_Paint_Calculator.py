import math

def inputNumber(message):
    while True:
        try:
            userInput = float(input(message))
            if (userInput <= 0):
                print("Not a positive number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return userInput
            break

while True:
    try:
        shape_num = float(input("Is your room squared or rounded? Press 1 for square, 2 for round. "))
        if (shape_num != 1) and (shape_num != 2):
            print("You can only choose between 1 and 2! Try again.")
            continue
    except ValueError:
        print("Not a number! Try again.")
        continue
    else:
        shape = 0
        if (shape_num == 1):
            shape = "square"
        else:
            shape = "round"
        break

def ifPlural(whats):
    if (whats == 1):
        what_s = ""
    else:
        what_s = "s"
    return what_s

if(shape_num == 1):
    length = inputNumber("What is the length of the room? ")
    width = inputNumber("What is the width of the room? ")
    area = length * width
else:
    radius = inputNumber("What is the radius of the room? ")
    area = math.pow(radius, 2) * math.pi

gallons = math.ceil(area / 350)
gallon_s = ifPlural(gallons)

print("You will need to purchase %d gallon%s of paint to cover %d square meters." % (gallons, gallon_s, area))