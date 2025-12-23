import string
import random
import hashlib


def generate_password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    char = list(char)
    pwd=""

    for i in range(length):
        pwd += random.choice(char)
    return pwd

def hash_password(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()

while True:
    try:
        print("-------------------------------------------------")
        length = int(input("Choose a length for your password: "))
        print("-------------------------------------------------")
    except ValueError:
        print("Invlaid! ONLY Number allowed!!!")
        continue

    pwd = generate_password(length)
    print("generate_password:", pwd)
    hash = hash_password(pwd)
    print("Hash:", hash)
    break
