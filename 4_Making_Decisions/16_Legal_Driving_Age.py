import sys

def inputNumber():
    while True:
        try:
            userInput = int(input("What is your age? "))
            if(userInput < 0):
                print("Not a valid age number! Try again.")
                continue
        except ValueError:
            print("Not a valid age number! Try again.")
            continue
        else:
            return userInput
            break

user_age = inputNumber()
# print("You are old enough to legally drive") if (user_age >= 16) else print("You are not old enough to legally drive")

if(user_age >= 18):
    print("You can legally drive in every country.")
    sys.exit(0)

ages = []
ages.append({"age": 15, "country": "El Salvador"})
ages.append({"age": 15, "country": "Australia"})
ages.append({"age": 15, "country": "Northern Mariana Island"})
ages.append({"age": 16, "country": "Cameroon"})
ages.append({"age": 16, "country": "Canada"})
ages.append({"age": 16, "country": "Israel"})
ages.append({"age": 17, "country": "South Africa"})
ages.append({"age": 17, "country": "Argentina"})
ages.append({"age": 17, "country": "Indonesia"})

countries = []

for age in ages:
    if(user_age >= age["age"]):
        countries.append(age["country"])

if(len(countries) != 0):
    print("Countries that you can legally drive in:")
    for country in countries:
        if(countries.index(country) == len(countries) - 1):
            print(country + ".")
        else:
            print(country + ",")
else:
    print("There is no country that you can legally drive in.")



