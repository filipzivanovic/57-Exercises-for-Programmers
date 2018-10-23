def inputNumber(what, which):
    while True:
        try:
            if(what == "price"):
                userInput = float(input("Enter the %s of item %d: $" % (what, which)))
            else:
                userInput = int(input("Enter the %s of item %d: " % (what, which)))
            if (userInput <= 0):
                print("Not a positive number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return userInput
            break

subtotal = 0
i = 1

while True:
    price = inputNumber("price", i)
    quantity = inputNumber("quantity", i)
    subtotal += price * quantity
    i += 1
    if(input("End of the shopping? (Y for yes): ") == "Y"):
        break

tax = subtotal * 0.055
total = subtotal + tax

print("Subtotal: $%.2f" % subtotal)
print("Tax: $%.2f" % tax)
print("Total: $%.2f" % total)
