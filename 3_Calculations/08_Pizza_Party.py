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
pizzas = inputNumber("pizzas")
slices = inputNumber("slices")

pizza_s = ifPlural(pizzas)
slice_s = ifPlural(slices)

total_slices = pizzas * slices
total_slice_s = ifPlural(total_slices)

slices_per_person = int(total_slices / people)
slice_s_per_person = ifPlural(slices_per_person)

leftovers = total_slices % people
leftover_s = ifPlural(leftovers)

print("%d people with %d pizza%s, each with %d slice%s, with total of %d slice%s.\n" % (people, pizzas, pizza_s, slices, slice_s_per_person, total_slices, total_slice_s))
print("Each person gets %d slice%s of pizza.\n" % (slices_per_person, slice_s))
print("There are %d leftover piece%s." % (leftovers, leftover_s))
