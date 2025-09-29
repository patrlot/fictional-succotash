import random

def gen_pass(n):
    character = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQSTUVWXYZ1234567890"
    password = ""

    for i in range(n):
        password += random.choice(character)

    return password

n = int(input('panjang password:'))
print("password:", gen_pass(n))