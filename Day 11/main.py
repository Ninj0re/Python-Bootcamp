import random
import time


def game():
    list_deck = create_deck()
    random.shuffle(list_deck)
    hand_player = [list_deck.pop(0), list_deck.pop(0)]
    hand_bot = [list_deck.pop(0)]

    score_bot = print_hand("Bot ", hand_bot)
    score_player = print_hand("Your ", hand_player)

    go_on = 1

    while go_on != 0:
        go_on = int(input("If you want card press 1 else press 0."))
        if go_on == 1:
            hand_player.append(list_deck.pop(0))
            score_player = print_hand("Your ", hand_player)
            if score_player > 21:
                end_screen("You lose!!")
                return
    while score_bot < 17:
        hand_bot.append(list_deck.pop(0))
        score_bot = print_hand("Bot ", hand_bot)
        if score_bot < 17:
            time.sleep(2)
        if score_bot > 21:
            end_screen("You win!!")
            return
    if score_player > score_bot:
        end_screen("You win!!")
    elif score_bot > score_player:
        end_screen("You lose!!")
    else:
        end_screen("TIE!!")


def create_deck():
    list_cards = []
    list_suits = ["♠", "♥", "♣", "♦"]
    list_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

    for suit in list_suits:
        for number in list_numbers:
            dict_card = {}
            string = suit + number
            if number == "A":
                dict_card["value"] = [string, 1, 11]
            elif number == "T" or number == "J" or number == "Q" or number == "K":
                dict_card["value"] = [string, 10]
            else:
                dict_card["value"] = [string, int(number)]
            list_cards.append(dict_card)

    return list_cards


def deal_card(deck):
    return list(deck).pop(0)


def print_hand(who, hand):
    print(str(who) + "hand ")
    score = 0
    list_ace = []
    for card in hand:
        print(card["value"][0], end="")
        if card["value"][0][1] == "A":
            list_ace.append(card)
        else:
            score += int(card["value"][1])
    for ace in list_ace:
        score += int(ace["value"][2])
        if score > 21:
            score -= int(ace["value"][2] - ace["value"][1])

    print(f"\nScore: {score}")
    return score


def end_screen(condition):
    print(str(condition))
    print("----------------------------\n")


while True:
    game()
