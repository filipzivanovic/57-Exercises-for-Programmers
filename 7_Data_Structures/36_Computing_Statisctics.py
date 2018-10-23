import statistics

# def input_number(message):
#     while True:
#         user_input = input(message)
#         if user_input == "done":
#             return user_input
#         try:
#             user_input = int(user_input)
#             if user_input == 0:
#                 print("Not a positive number! Try again.")
#                 continue
#         except ValueError:
#             print("Not a number! Try again.")
#             continue
#         else:
#             return user_input
#
#
# 36_numbers = []
#
# while True:
#     number = input_number("Enter a number: ")
#     if number == "done":
#         break
#     36_numbers.append(str(number))

file = open("36_numbers", "r")
lines = file.readlines()
numbers = [line.strip() for line in lines]
print("Numbers: " + ', '.join(numbers) + '.')

numbers = [float(i) for i in numbers]
print("The average is %.2f" % statistics.mean(numbers))
print("The minimum is %.2f" % min(numbers))
print("The maximum is %.2f" % max(numbers))
print("The standard deviation is %.2f" % statistics.stdev(numbers))
