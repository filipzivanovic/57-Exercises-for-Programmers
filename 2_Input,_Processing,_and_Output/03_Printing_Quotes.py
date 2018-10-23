# These aren't the droids you're looking for. - Obi-Wan Kenobi
# These aren't the tables you're looking for. - Dobrivoje Kasikovic
# These aren't the guns you're looking for. - Usama Bin Ladin
# These aren't the people you're looking for. - Zoran Djindjic

num = input("Number of quotations: ")

quotations = []

for i in range(int(num)):
    quotation = input("What is the " + str(i+1) + ". quotation? ")
    author = input("Who's the author of " + str(i+1) + ". quotation? ")
    quotations.append({"quotation": quotation, "author": author})

for quotation in quotations:
    print(quotation["author"] + " says, \"" + quotation["quotation"] + "\"")

