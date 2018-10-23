def filter_even_numbers(source, input_numbers):
    if source == "n":
        input_numbers = input_numbers.split(sep=" ")
    output_numbers = []
    for number in input_numbers:
        if int(number) % 2 == 0:
            output_numbers.append(number)
    return output_numbers


source = input("Are numbers coming from the file (y/n)? ")
if source == "n":
    input_numbers = input("Enter a list of numbers, separated by spaces: ")
    output_numbers = filter_even_numbers(source, input_numbers)
else:
    file = open("38_numbers", "r")
    lines = file.readlines()
    input_numbers = [line.strip() for line in lines]
    output_numbers = filter_even_numbers(source, input_numbers)

output_numbers = ' '.join(output_numbers)
print("The even numbers are: %s." % output_numbers)
