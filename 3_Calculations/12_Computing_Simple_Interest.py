def inputNumber(what):
    while True:
        try:
            userInput = float(input("Enter the %s: " % what))
            if(userInput <= 0):
                print("Not a positive number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return userInput
            break

P = inputNumber("principal")
r = inputNumber("interest")
t = inputNumber("number of years")

def calculateSimpleInterest(P, r, t):
    A = P * (1 + r / 100 * t)
    return A

A = calculateSimpleInterest(P, r, t)
print("After %d years at %.2f%%, the investment of $%.2f will be worth $%.2f." % (t, r, P, A))

print("By years:")
for i in range(int(t)):
    A = calculateSimpleInterest(P, r, i+1)
    print("After %d. year at %.2f%%, the investment of $%.2f will be worth $%.2f." % (i+1, r, P, A))