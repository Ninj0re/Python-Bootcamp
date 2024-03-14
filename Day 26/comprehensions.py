l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
l2 = []

for n in l:
    result = n*n
    if result % 2 == 1:
        l2.append(result)
# print(l2)

# print([n*2 for n in range(1, 5)])

#names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#short_names = [name for name in names if len(name) < 5]
#print(short_names)

with open("file_1") as file1:
    list1 = file1.readlines()
with open("file_2") as file2:
    result = [int(line) for line in file2.readlines() if list1.__contains__(line)]

print(result)
