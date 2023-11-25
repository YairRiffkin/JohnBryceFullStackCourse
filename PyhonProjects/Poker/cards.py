import itertools
import random

def create_deck():
    suits = "HDCS"
    values = "23456789TJQKA"
    deck = list(itertools.product(values, suits))
    return random.shuffle(deck)

def deal_cards(deck, number):
    player_cards = [deck.pop() for i in range(0, number)]
    return player_cards

def print_hand(hand, number):
    names = list(hand.keys(0))
    for i in range(0, number):
        print(names(i), "\n")
        

