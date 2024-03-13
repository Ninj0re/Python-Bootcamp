# Bar yaş kontrol sistemi
age = -1

while age <= 0:
    age = int(input("What is your age: "))
    if age >= 18:
        print("Girebilirsiniz")
    elif 18 > age > 0:
        print("Giremezsin!")
