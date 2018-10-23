def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
            if (userInput <= 0):
                print("Not a positive number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return userInput
            break


num_of_itter = inputNumber("How many 36_numbers do you want to add? ")
sum = 0
for i in range(num_of_itter):
    num = input("Enter %d. number: " % (i + 1))
    try:
        val = int(num)
    except ValueError:
        continue
    sum += val

print("The total is %d " % sum)
