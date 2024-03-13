import random


def game():
    life = 5
    word_list = ["apple", "phone", "baboon"]
    word = word_list[random.randint(0, len(word_list) - 1)]
    player_word = []
    for _ in word:
        player_word.append("_")

    while life > 0:
        print(player_word)
        letter_in_word = False
        char = guess()

        c = 0
        for letter in word:
            if char == letter:
                letter_in_word = True
                player_word[c] = char
            c += 1
        if not letter_in_word:
            life -= 1
            print(f"Life: {life}")

        game_ended = True
        for letter in player_word:
            if letter == "_":
                game_ended = False
        if game_ended:
            print("You win!!")
            print("------------------------------------")
            return
    print("You lose :(")
    print("------------------------------------")


def guess():
    while True:
        input_string = input("What's your guess?")
        if (ord(input_string) >= 65 and ord(input_string) <= 90) or (ord(input_string) >= 97 and ord(input_string) <= 122):
            return input_string.lower()
        print("Wrong input try again!")


while True:
    game()
