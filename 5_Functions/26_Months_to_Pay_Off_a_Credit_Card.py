from math import log10 as log


def inputNumber(message):
    while True:
        try:
            userInput = float(input(message))
            if userInput < 0:
                print("Not a positive number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return userInput
            break


def calculateMonthsUntilPaidOff(b, apr, p):
    i = apr / 100.0 / 365
    n = -1.0 / 30.0 * (log(1 + b / p * (1 - (1 + i) ** 30)) / log(1 + i))
    return n


b = inputNumber("What is your balance? ")
apr = inputNumber("What is the APR on the card (as a percent)? ")
p = inputNumber("What is the monthly payment you can make? ")

n = calculateMonthsUntilPaidOff(b, apr, p)
print("It will take you %d months to pay off this card." % n)
