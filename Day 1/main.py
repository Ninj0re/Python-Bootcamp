# # işareti olan satırlar command line
# print("--------------------------------") olan satırlar file runlandığında console daha düzenli olsun diye

# 1. print

# print function prints the things inside () to the console. Be careful about ""
x = 2+3
print("2+3")
print(2+3)
print("--------------------------------")
print("x")
print(x)
print("--------------------------------")

# 2. Variable Types (Data Types)

# Text Type: str
# Numeric Type int, float
# Boolean Type(True or False): bool

# We can convert data types to other data types.
# For example data type of input function is str but if we want to do math operation with user input
# we have to convert it to numerical type(int or float)
# in 3. part I explain it with an example

# 3. input

# getting personal information from user via input function
# \n means the new line ('n' stand for new)
age = input("What is your age?\n")
name = input("What is your name?\n")

print(name + "'s age is " + age)

# average age finder program
age1 = int(input("1: What is your age: "))
age2 = int(input("2: What is your age: "))
avr = (age1 + age2)/2
print("Average age is: " + str(avr))


# 4. If statement

x = True
if x:
    print("1")
print("--------------------------------")

x = 2
if x == 2:
    print("2")
print("--------------------------------")

x = "fatma"
if x == "cu":
    print(3)
if x == "fatma":
    print(4)
