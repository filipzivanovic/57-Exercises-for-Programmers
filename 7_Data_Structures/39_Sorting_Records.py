import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="python"
)

cursor = db.cursor()

while True:
    rule = input("Sort employees by:\n(1) Name,\n(2) Position,\n(3) Separation Date.\n")
    if rule == "1":
        order_by = "last_name, first_name"
        break
    elif rule == "2":
        order_by = "position"
        break
    elif rule == "3":
        order_by = "separation_date"
        break
    else:
        print("No such option for sorting. Try again:")
        continue

cursor.execute("SELECT * FROM employees ORDER BY %s" % order_by)

result = cursor.fetchall()

print('Name                | Position          | Separation Date')
print('--------------------|-------------------|----------------')
for x in result:
    name = x[0] + ' ' + x[1]
    print('{name:19} | {position:17} | {separation_date}'.format(name=name, position=x[2], separation_date=x[3]))
