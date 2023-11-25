import itertools
import random

def create_deck():
    pack = ()
    suits = "HDCS"
    values = "23456789TJQKA"
    pack = list(itertools.product(suits, values))
    random.shuffle(pack)
    return pack

def deal_cards(deck, number):
    player_cards = [deck.pop() for i in range(0, number)]
    return player_cards

def print_hand(hand, number):
    letter = ["H", "D", "C", "S"]
    names = list(hand.keys())
    for i in range(0, number):
        print(names[i], end="\t")
        for_print = hand[names[i]]
        for one_card in for_print:
            char = (letter.index(one_card[0])) + 3
            print(chr(char), one_card[1], end="\t")
        print("\n")

        

