def inputNumber(message):
    while True:
        try:
            userInput = float(input(message))
            if(userInput < 0):
                print("Not a positive number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return userInput
            break

countries = []
countries.append({"country": "Australia", "limit": 0})
countries.append({"country": "Israel", "limit": 0.01})
countries.append({"country": "Costa Rica", "limit": 0.02})
countries.append({"country": "Serbia", "limit": 0.03})
countries.append({"country": "Russia", "limit": 0.04})
countries.append({"country": "Thailand", "limit": 0.05})
countries.append({"country": "Angola", "limit": 0.06})
countries.append({"country": "Honduras", "limit": 0.07})
countries.append({"country": "Nigeria", "limit": 0.08})
countries.append({"country": "Palau", "limit": 0.1})

A = inputNumber("Total alcohol consumed: ")
W = inputNumber("Body weight: ")
H = inputNumber("Hours since the last drink: ")

g = inputNumber("Male (1) or female (2): ")
if(g == 1):
    r = 0.73
else:
    r = 0.63

c = input("Country: ")
while True:
    for country in countries:
        if(c == country["country"]):
            limit = country["limit"]
            found = 1
            break
    if (found == 1):
        break
    exchange_currency = input("There is no such country. Enter again: ")

A = A * 33.814
W = W / 0.045359
BAC = (A * 5.14 / W * r) - 0.015 * H

print("Your BAC is %.2f." % BAC)

if(BAC >= limit):
    print("It is not legal for you to drive.")
else:
    print("It is safe for you to drive.")