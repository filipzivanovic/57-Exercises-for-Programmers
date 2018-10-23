string = input("What is the input string? ")

while(len(string) == 0):
    print("Input is empty! Please enter something!")
    string = input("What is the input string? ")

print(string + " has " + str(len(string)) + " characters.")