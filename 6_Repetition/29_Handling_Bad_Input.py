def input_number(message):
    while True:
        try:
            user_input = int(input(message))
            if user_input < 0:
                print("Not a positive number! Try again.")
                continue
            elif user_input == 0:
                print("Cannot divide with zero! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return user_input


rate = input_number("What is the rate of return? ")

years = 72 / rate

print("It will take %d years to double your initial investment." % years)
