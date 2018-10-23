employees = ["Filip", "Misa", "Visnja", "Andrija", "Aleksa"]

print("There are %d employees: " % len(employees))
for employee in employees:
    print(employee)
print("")

while True:
    employee = input("Enter an employee name to remove: ")
    try:
        employees.remove(employee)
    except ValueError:
        print("There is no such employee!")
        print("")
        continue
    if not employees:
        print("There are no more employees.")
        break
    else:
        print("There are %d employees: " % len(employees))
        for employee in employees:
            print(employee)
        print("")
