import getpass
import bcrypt

def define_hash(password):
    hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    return hashed_password

usps = []
usps.append({"username": "filip", "password": define_hash('asd123')})
usps.append({"username": "pera", "password": define_hash('zxc456')})
usps.append({"username": "birca", "password": define_hash('qwe789')})

found = 0

input_user = input("Username: ")
input_password = getpass.getpass()

for up in usps:
    hashed_password = up["password"]
    if(input_user == up["username"]):
        if(bcrypt.checkpw(input_password.encode('utf8'), hashed_password)):
            found = 1
            break

if(found == 1):
    print("Welcome!")
else:
    print("I don't know you.")