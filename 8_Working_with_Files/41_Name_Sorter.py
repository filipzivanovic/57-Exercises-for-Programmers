from operator import itemgetter

with open("41_input_names", "r") as file:
    lines = file.readlines()
names = []
for line in lines:
    names.append({"last_name": line.strip().split(", ")[0], "first_name": line.strip().split(", ")[1]})

with open("41_output_names", "w") as file:
    print("Total of %d names" % len(lines), file=file)
    print("-----------------", file=file)
    sorted_names = sorted(names, key=itemgetter("last_name", "first_name"))
    for name in sorted_names:
        print(name["last_name"] + ", " + name["first_name"], file=file)
