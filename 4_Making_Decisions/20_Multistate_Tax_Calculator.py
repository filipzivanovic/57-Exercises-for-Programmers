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


states = []
states.append({"state": "wisconsin", "basic_tax_rate": 0.05, "additional_tax_rate": 1})
states.append({"state": "illinois", "basic_tax_rate": 0.08, "additional_tax_rate": 0})

countries = []
countries.append({"state": "wisconsin", "country": "eau claire", "additional_tax_rate": 0.005})
countries.append({"state": "wisconsin", "country": "dunn", "additional_tax_rate": 0.004})

amount = inputNumber("What is the order amount? ")
input_state = input("What state do you live in? ").lower()

tax_rate = 0
for state in states:
    if(input_state == state["state"]):
        tax_rate = state["basic_tax_rate"]
        if(state["additional_tax_rate"] == 1):
           input_country = input("What country do you live in? ").lower()
           for country in countries:
                if(input_state == country["state"] and input_country == country["country"]):
                    tax_rate += country["additional_tax_rate"]

tax = amount * tax_rate
total = amount + tax
print("The tax is $%.2f." % tax)
print("The total is $%.2f." % total)