def inputNumber():
    while True:
        try:
            userInput = int(input("Please enter the number of the month: "))
            if userInput < 1 or userInput > 12:
                print("Not a month number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return userInput
            break

def switch_demo(month, language):
    if language == "en":
        switcher = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
    elif language == "fr":
        switcher = {
            1: "Janvier",
            2: "Février",
            3: "Mars",
            4: "Avril",
            5: "Mai",
            6: "Juin",
            7: "Juillet",
            8: "Août",
            9: "Septembre",
            10: "Octobre",
            11: "Novembre",
            12: "Décembre"
        }
    elif language == "sr":
        switcher = {
            1: "Januar",
            2: "Februar",
            3: "Mart",
            4: "April",
            5: "Maj",
            6: "Jun",
            7: "Jul",
            8: "Avgust",
            9: "Septembar",
            10: "Oktobar",
            11: "Novembar",
            12: "Decembar"
        }
    print(switcher.get(month, "Invalid month"))

language = input("What is your language? ")
month = inputNumber()
switch_demo(month, language)