import time

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

current_age = inputNumber("What is your current age? ")
retire_age = inputNumber("At what age would you like to retire? ")

diff = retire_age - current_age

current_year = int(time.strftime("%Y"))
retire_year = current_year + diff

if(diff < 0):
    print("You can retire anytime! You passed retirement boundary %d years ago" % abs(diff))
else:
    print("You have %d years left until you can retire." % diff)
    print("It's %d, so you can retire in %d." % (current_year, retire_year))