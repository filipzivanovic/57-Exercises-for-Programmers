from os import listdir
from os.path import isfile, join

path = "./Sentences/"
files = [f for f in listdir(path) if isfile(join(path, f))]

for file in files:
    print("File: %s" % file)
    with open(path + file, "r") as f:
        lines = f.readlines()

    for line in lines:
        print(line.strip())

    new_lines = []

    good_words = [{"bad": "a", "good": "1"}, {"bad": "e", "good": "2"}, {"bad": "i", "good": "3"},
                  {"bad": "o", "good": "4"}, {"bad": "u", "good": "5"}]

    for word in good_words:
        new_lines = []
        for line in lines:
            new_line = line.strip().replace(word["bad"], word["good"])
            new_lines.append(new_line)
        lines = new_lines

    for line in lines:
        print(line)
    print()
