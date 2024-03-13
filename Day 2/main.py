import random


def main():
    x_axis = ["O", "O", "O"]
    treasure_map1 = [x_axis.copy(), x_axis.copy(), x_axis.copy()]
    treasure_map = [x_axis.copy(), x_axis.copy(), x_axis.copy()]
    x_loc = random.randint(0, 2)
    y_loc = random.randint(0, 2)
    x_finder = ["a", "b", "c"]
    treasure_map[x_loc][y_loc] = "X"

    while True:
        x_loc_player = 0
        y_loc_player = 0
        for i in treasure_map1:
            print(i)

        treasure_loc = input()

        f = 0
        for i in x_finder:
            if i == treasure_loc[0].lower():
                x_loc_player = f
                break
            f += 1
        for i in range(3):
            if i == int(treasure_loc[1]) - 1:
                y_loc_player = i
                break
        if treasure_map[x_loc_player][y_loc_player] == "X":
            print("You win!")
            break


main()
