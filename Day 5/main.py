for i in range(1, 101):
    printed_value = ""
    if(i % 3 == 0):
        printed_value += "Fizz"
    if(i % 5 == 0):
        printed_value += "Buzz"
    if printed_value == "":
        print(i)
        continue
    print(printed_value)
