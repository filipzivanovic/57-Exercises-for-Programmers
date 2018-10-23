import string

def passwordValidator(password):
    if password.isnumeric() and len(password) <= 8:
        return 1
    elif password.isalpha() and len(password) <= 8:
        return 2
    elif password.isalnum() and not password.isalpha() and not password.isnumeric() and len(password) >= 8:
        return 3
    elif any(char in (string.punctuation) for char in password) and \
         any(char in (string.digits) for char in password) and \
         any(char in (string.ascii_letters) for char in password):
        return 4
    else:
        return 5


password = input("Please enter your password: ")

if (passwordValidator(password) == 1):
    valid = "very weak"
elif (passwordValidator(password) == 2):
    valid = "weak"
elif (passwordValidator(password) == 3):
    valid = "strong"
elif (passwordValidator(password) == 4):
    valid = "very strong"
else:
    valid = "unknown strength"

print("The password \"%s\" is %s password." % (password, valid))
