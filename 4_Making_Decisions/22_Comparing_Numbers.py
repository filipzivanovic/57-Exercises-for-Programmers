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


num_of_nums = inputNumber("How many number do you want to enter? ")

numbers = []

input_num = inputNumber("Enter the 1. number: ")
numbers.append(input_num)
largest = numbers[0]

for i in range(2, num_of_nums + 1):
    input_num = inputNumber("Enter the %d. number: " % i)
    while True:
        found = 0
        for num in numbers:
            if input_num == num:
                print("The same number already exists.")
                input_num = inputNumber("Enter the %d. number: " % i)
                found = 1
                break
        if found == 0:
            break
    numbers.append(input_num)
    if input_num > largest:
        largest = input_num

for num in numbers:
    print(num)

print("The largest number is %d." % largest)
