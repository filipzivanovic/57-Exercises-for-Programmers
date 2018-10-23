def inputNumber(message):
    while True:
        try:
            userInput = float(input("What is the " + message + " number? "))
            if(userInput <= 0):
                print("Not a positive number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return userInput
            break

def sum(a, b):
    return a + b

def diff(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

first = inputNumber("first")
second = inputNumber("second")

print("%s + %s = %.2f" % (first, second, sum(first, second)))
print("%s - %s = %.2f" % (first, second, diff(first, second)))
print("%s * %s = %.2f" % (first, second, mul(first, second)))
print("%s / %s = %.2f" % (first, second, div(first, second)))