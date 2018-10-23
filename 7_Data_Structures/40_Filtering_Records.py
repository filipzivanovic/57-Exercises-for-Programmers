import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="python"
)

cursor = db.cursor()

while True:
    rule = input("Filter employees by:\n(1) Last Name,\n(2) Position,\n(3) Separation Date.\n")
    if rule == "1":
        filter_by = "last_name"
        break
    elif rule == "2":
        filter_by = "position"
        break
    elif rule == "3":
        filter_by = "separation_date"
        break
    else:
        print("No such option for sorting. Try again:")
        continue

if rule == "3":
    cursor.execute("SELECT * FROM employees WHERE TIMESTAMPDIFF(month, separation_date, NOW()) > 6")
else:
    string = input("Enter a search string: ")
    cursor.execute("SELECT * FROM employees WHERE %s LIKE \'%%%s%%\'" % (filter_by, string))

result = cursor.fetchall()

print('Name                | Position          | Separation Date')
print('--------------------|-------------------|----------------')
for x in result:
    name = x[0] + ' ' + x[1]
    print('{name:19} | {position:17} | {separation_date}'.format(name=name, position=x[2], separation_date=x[3]))
