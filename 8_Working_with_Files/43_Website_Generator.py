import os


def input_answer(what):
    while True:
        answer = input("Do you want a folder for %s? " % what).lower()
        if answer != "y" and answer != "n":
            print("Please answer with y or n!")
            continue
        return answer


def make_dir(addition, root):
    path = root_path + "/" + addition
    if not os.path.exists(path):
        os.makedirs(path)


def make_file(root_path, site_name, author):
    with open("./%s/index.html" % root_path, "w") as file:
        message = "<html>" \
                  "<head><title>%s</title></head>" \
                  "<body>Author: %s</body>" \
                  "</html>" % (site_name, author)
        print(message, file=file)


site_name = input("Site name: ")
author = input("Author: ")
js = input_answer("JavaScript")
css = input_answer("CSS")

root_path = "./%s" % site_name
make_dir("", root_path)

if js == "y":
    make_dir("js", root_path)

if css == "y":
    make_dir("css", root_path)

make_file(root_path, site_name, author)
