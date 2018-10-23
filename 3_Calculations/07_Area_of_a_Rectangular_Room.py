factor = 0.09290304

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
        scale_num = float(input("Would you like to use feet or meters? Press 1 for feet, 2 for meters. "))
        if (scale_num != 1) and (scale_num != 2):
            print("You can only choose between 1 and 2! Try again.")
            continue
    except ValueError:
        print("Not a number! Try again.")
        continue
    else:
        scale = 0
        if (scale_num == 1):
            scale = "feet"
        else:
            scale = "meters"
        break

length = inputNumber("What is the length of the room in %s? " % scale)
width = inputNumber("What is the width of the room in %s? " % scale)

if(scale_num == 1):
    area_imperial = length * width
    area_metric = area_imperial * factor
else:
    area_metric = length * width
    area_imperial = area_metric / factor

print("You entered dimensions of %.2f by %.2f %s." % (length, width, scale))

print("The area is: \n%.2f square feet, \n%.2f square meters." % (area_imperial, area_metric))