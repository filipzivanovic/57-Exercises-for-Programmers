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

def calculateTip(bill_amount, tip_rate):
    tip = float(bill_amount) * float(tip_rate) / 100
    return tip

def calculateTotalAmount(bill_amount, tip):
    total_amount = float(bill_amount) + float(tip)
    return total_amount

bill_amount = inputNumber("What is the bill? ")
tip_rate = inputNumber("What is the tip percentage? ")

tip = calculateTip(bill_amount, tip_rate)
print("The tip is ${0:.2f}".format(tip))

total_amount = calculateTotalAmount(bill_amount, tip)
print("The total is ${0:.2f}".format(total_amount))