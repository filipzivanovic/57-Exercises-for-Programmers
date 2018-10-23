import math

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
n = inputNumber("number of times the interest is compounded per year")

def calculateCompoundInterest(P, r, t, n):
    A = P * pow((1 + r / 100 / n), n * t)
    return A

A = calculateCompoundInterest(P, r, t, n)
print("$%.2f invested at at %.2f%% for %d years compounded %d times per year is $%.2f." % (P, r, t, n, A))

print("By years:")
for i in range(int(t)):
    A = calculateCompoundInterest(P, r, i+1, n)
    print("After %d. year at %.2f%%, the investment of $%.2f will be worth $%.2f." % (i+1, r, P, A))