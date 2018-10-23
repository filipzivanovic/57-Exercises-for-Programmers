def inputNumber(message):
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return userInput
            break

def convert(scale, temp):
    out_temps = []
    if(scale == "c"):
        out_temps.append((in_temp * 9 / 5) + 32)
        out_temps.append(in_temp + 273.15)
    elif(scale == "f"):
        out_temps.append((in_temp - 32) * 5 / 9)
        out_temps.append((in_temp + 459.67) * 5 / 9)
    else:
        out_temps.append(in_temp - 273.15)
        out_temps.append(in_temp * 9 / 5 - 459.67)
    return out_temps

print("Press C to convert from Celsius to Fahrenheit and Kelvin.")
print("Press F to convert from Fahrenheit to Celsius and Kelvin.")
print("Press K to convert from Kelvin to Celsius and Fahrenheit.")
conversion = input("Your choice: ")

while True:
    if(conversion.lower() == "c"):
        input_scale = "Celsius"
        output_scale1 = "Fahrenheit"
        output_scale2 = "Kelvin"
        break
    elif(conversion.lower() == "f"):
        input_scale = "Fahrenheit"
        output_scale1 = "Celsius"
        output_scale2 = "Kelvin"
        break
    elif(conversion.lower() == "k"):
        input_scale = "Kelvin"
        output_scale1 = "Celsius"
        output_scale2 = "Fahrenheit"
        break
    conversion = input("There is no such conversion. Try again: ")

in_temp = inputNumber("Please enter the temperature in %s: " % input_scale)

out_temps = convert(conversion.lower(), in_temp)

print("The temperature in %s is %.2f, and in %s is %.2f" % (output_scale1, out_temps[0], output_scale2, out_temps[1]))