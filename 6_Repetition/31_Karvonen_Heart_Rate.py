def input_number(message):
    while True:
        try:
            user_input = int(input(message))
            if user_input <= 0:
                print("Not a positive number! Try again.")
                continue
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return user_input


age = input_number("What is your age? ")
resting_pulse = input_number("What is your resting pulse? ")

print("Intensity\t| Rate")
print("------------|--------")
for intensity in range(55, 100, 5):
    rate = (((220 - age) - resting_pulse) * intensity / 100) + resting_pulse
    print("%d%%\t\t\t| %d bpm" % (intensity, rate))
