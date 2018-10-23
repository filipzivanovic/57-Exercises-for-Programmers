import re


def checkName(which, name):
    if name == "":
        print("The %s name must be filled in." % which)
        return 1
    if len(name) < 2:
        print("\"%s\" is not a valid %s name. It is too short." % (name, which))
        return 1
    else:
        matchObj = re.match('^[a-zA-Z]+$', name)
        if not matchObj:
            print("\"%s\" is not a valid %s name. It should only consist of letters." % (name, which))
            return 1
        else:
            return 0


def checkZIP(zip):
    if zip == "":
        print("The zip must be filled in.")
        return 1
    matchObj = re.match('^\d+$', zip)
    if not matchObj:
        print("The ZIP code must be numeric.")
        return 1
    else:
        return 0


def checkID(id):
    if id == "":
        print("The id must be filled in.")
        return 1
    matchObj = re.match('^[a-zA-Z]{2}-\d{4}$', id)
    if not matchObj:
        print("%s is not a valid ID." % id)
        return 1
    else:
        return 0


def validateInput(first_name, last_name, zip_code, employee_id):
    fn = checkName("first", first_name)
    ln = checkName("last", last_name)
    cz = checkZIP(zip_code)
    ci = checkID(employee_id)
    return fn + ln + cz + ci


vi = -1

while vi != 0:
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    zip_code = input("Enter the ZIP code: ")
    employee_id = input("Enter the employee ID: ")
    vi = validateInput(first_name, last_name, zip_code, employee_id)

print("There were no errors found.")
