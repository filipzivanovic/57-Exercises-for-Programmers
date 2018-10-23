from operator import itemgetter
from babel.numbers import format_currency


with open("42_values", "r") as file:
    lines = file.readlines()
salaries = []
for line in lines:
    salaries.append({"last_name": line.strip().split(",")[0], "first_name": line.strip().split(",")[1],
                     "salary": int(line.strip().split(",")[2])})

last_name_lengths = []
first_name_lengths = []
salaries_lengths = []
for salary in salaries:
    last_name_lengths.append(salary["last_name"])
    first_name_lengths.append(salary["first_name"])
    salaries_lengths.append(salary["salary"])
last_name_length = str(len(max(last_name_lengths, key=len)) + 1)
first_name_length = str(len(max(last_name_lengths, key=len)) + 1)
salary_length = str(len(max(last_name_lengths, key=len)) + 1)

sorted_by_salary = sorted(salaries, key=itemgetter("salary"))

print(("{Last:" + last_name_length + "}"
       "{First:" + first_name_length + "}"
       "{Salary:" + salary_length + "}")
       .format(Last="Last", First="First", Salary="Salary"))

total_length = int(last_name_length) + int(first_name_length) + int(salary_length) + 1
print('-' * total_length)

for salary in sorted_by_salary:
    formatted_salary = format_currency(salary["salary"], 'USD', locale='en_US')
    print(("{last_name_val:" + last_name_length + "}"
           "{first_name_val:" + first_name_length + "}"
           "{salary_val:" + salary_length + "}")
           .format(last_name_val=salary["last_name"], first_name_val=salary["first_name"], salary_val=formatted_salary))
