from prettytable import PrettyTable

row = [" "]
for i in range(13):
    row.append(i)

t = PrettyTable(row)

for i in range(13):
    row = []
    row.append(i)
    for j in range(13):
        row.append(i * j)
    t.add_row(row)

print(t)
