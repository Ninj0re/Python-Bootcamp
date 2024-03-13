with open("invited_names.txt") as invited_names:
    names = invited_names.readlines()

    count = 0
    for name in names:
        names[count] = name.strip()
        count += 1

with open("starting_letter.txt", "r") as letter:
    my_letter = letter.read()

for name in names:
    with open(f"Ready To Send/letter to {name}.txt", "w") as final_letter:
        final_letter.write(my_letter.replace("[name]", name))
