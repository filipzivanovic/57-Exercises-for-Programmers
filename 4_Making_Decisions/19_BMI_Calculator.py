def inputNumber(what):
    while True:
        try:
            userInput = float(input("What's your %s? " % what))
            if userInput < 0:
                print("Not a positive number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return userInput
            break


weight = inputNumber("weight")
height = inputNumber("height")

BMI = weight / (height ** 2)

print("Your BMI is %.1f" % BMI)

if(BMI < 18.5):
    print("You are underweight. You should see your doctor.")
elif(BMI > 25):
    print("You are overweight. You should see your doctor.")
else:
    print("You are within the ideal weight range.")