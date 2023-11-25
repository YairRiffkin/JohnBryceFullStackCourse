import cards
import scores

players = ["Dan", "Eddie", "Susan", "Bob", "Lucy"]
table = dict.fromkeys(players)
# print(table)
deck = cards.create_deck()
# print(deck)
number_of_players = len(players)
# print(len(players))
for i in range(0, number_of_players):
    hand = cards.deal_cards(deck, 5)
    table[players[i]] = hand

cards.print_hand(table, number_of_players)


# names = list(table.keys())
# for i in range(0, number_of_players):
#     print(names[i])