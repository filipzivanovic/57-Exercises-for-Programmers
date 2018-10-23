import math

def inputNumber(what):
    while True:
        try:
            userInput = int(input("How many %s? " % what))
            if (userInput <= 0):
                print("Not a positive number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return userInput
            break

def ifPlural(whats):
    if (whats == 1):
        what_s = ""
    else:
        what_s = "s"
    return what_s

people = inputNumber("people")
total_slices = 0

for i in range(people):
    tmp = inputNumber("slices for %s." % str(i+1))
    total_slices += tmp

slices_per_pizza = inputNumber("slices per pizza")

pizzas = total_slices / slices_per_pizza

pizzas = math.ceil(pizzas)

pizza_s = ifPlural(pizzas)

print("We need to order %d pizza%s." % (pizzas, pizza_s))