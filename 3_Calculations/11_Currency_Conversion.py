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

countries = []
countries.append({"currency": "EUR", "rate": 118.196})
countries.append({"currency": "USD", "rate": 100.601})
countries.append({"currency": "CHF", "rate": 104.840})

dinars = inputNumber("How many dinars are you exchanging? ")
exchange_currency = input("What is the exchange currency? ")
found = 0

while True:
    for country in countries:
        if(exchange_currency == country["currency"]):
            exchange_rate = country["rate"]
            found = 1
            break
    if (found == 1):
        break
    exchange_currency = input("There is no such exchange currency. Enter again: ")

balance = dinars / exchange_rate

print("%.2f RSD at an exchange rate of %.2f is %.2f %s." % (dinars, exchange_rate, balance, exchange_currency))