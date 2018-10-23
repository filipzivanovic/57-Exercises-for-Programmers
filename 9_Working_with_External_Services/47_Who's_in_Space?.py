import requests
from operator import itemgetter


def sort_names(data):
    names = []
    for row in data:
        first_name = row["name"].split()[0]
        last_name = row["name"].split()[1]
        names.append({"first_name": first_name, "last_name": last_name, "craft": row["craft"]})

    sorted_names_list = sorted(names, key=itemgetter("last_name", "first_name"))
    sorted_names = []
    for name in sorted_names_list:
        sorted_names.append({"name": name["first_name"] + " " + name["last_name"], "craft": name["craft"]})
    return sorted_names


url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
data = response.json()

col_name_width = str(max(len(row["name"]) for row in data["people"]) + 1)
col_craft_width = str(max(len(row["craft"]) for row in data["people"]) + 1)
if int(col_craft_width) < 6:
    col_craft_width = 6

people = len(data["people"])

sorted_names = sort_names(data["people"])

print("There are %d people in space right now:\n" % people)
print(("{name:" + col_name_width + "} | Craft").format(name="Name"))
print("-" * int(col_name_width) + "-|-" + "-" * int(col_craft_width))
for row in sorted_names:
    print(("{name:" + col_name_width + "} | {craft:25}").format(name=row["name"], craft=row["craft"]))

# from itertools import groupby
#
# for k, v in groupby(sorted_names, key=lambda x: x["craft"]):
#     print(k, list(v))
