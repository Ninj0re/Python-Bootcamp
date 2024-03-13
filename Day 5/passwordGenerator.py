import random

symbol_list = []
num_list = []
letter_list = []
for i in range(33, 48):
    symbol_list.append(str(chr(i)))
for i in range(0, 10):
    num_list.append(str(i))
for i in range(65, 91):
    letter_list.append(str(chr(i)))
for i in range(97, 123):
    letter_list.append(str(chr(i)))

num_of_letters = int(input("Num of letters?"))
num_of_symbols = int(input("Num of Symbols?"))
num_of_nums = int(input("Num of Nums?"))
password = ""

for i in range(num_of_letters):
    if num_of_symbols > 0:
        password = password + symbol_list[random.randint(0, len(symbol_list) - 1)]
        num_of_symbols -= 1
    elif num_of_nums > 0:
        password = password + num_list[random.randint(0, len(num_list) - 1)]
        num_of_nums -= 1
    else:
        password = password + letter_list[random.randint(0, len(letter_list) - 1)]

    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)

print("Your password is: "+ password)