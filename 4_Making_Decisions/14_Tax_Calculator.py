def inputNumber(message):
    while True:
        try:
            userInput = float(input(message))
            if(userInput <= 0):
                print("Not a positive number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return userInput
            break

amount = inputNumber("What is the order amount? ")
state = input("What is the state? ")
st = 0

while True:
    if(state.lower() == "wi" or  state.lower() == "wisconsin"):
        st = 1
    if(state.lower() == "mn" or  state.lower() == "minnesota"):
        st = 2
    if(st == 0):
        state = input("There is no such state. Enter again: ")
        continue
    break

tax = 0

if(st == 1):
    tax_rate = 5.5
    tax = amount / 100 * tax_rate
    print("The subtotal is $%.2f." % amount)
    print("The tax is $%.2f." % tax)

total = amount + tax
print("The total is $%.2f." % total)