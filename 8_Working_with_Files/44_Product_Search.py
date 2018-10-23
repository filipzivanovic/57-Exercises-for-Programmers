import json


def input_answer(message):
    while True:
        answer = input(message).lower()
        if answer != "y" and answer != "n":
            print("Please answer with y or n!")
            continue
        return answer


def add_product(file, name, price, quantity):
    with open(file, "w") as f:
        entry = {"name": name, "price": price, "quantity": quantity}
        data["products"].append(entry)
        json.dump(data, f)


json_file = "44_products.json"

found = 0
while True:
    with open(json_file, "r") as file:
        data = json.load(file)
    input_product = input("What is the product name? ")
    for product in data["products"]:
        if input_product.lower() == product["name"].lower():
            found = 1
            print("Name: %s" % product["name"])
            print("Price: $%.2f" % product["price"])
            print("Quantity: %d" % product["quantity"])
    if found == 1:
        break
    print("Sorry, that product was not found in our inventory.")
    added = input_answer("Does this product should be added? ")
    if added == "y":
        price = float(input("What is the product price? "))
        quantity = int(input("What is the product quantity? "))
        add_product(json_file, input_product, price, quantity)
