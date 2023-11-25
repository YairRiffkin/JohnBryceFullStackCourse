from cards import create_deck, deal_cards

players = ["Dan", "Eddie", "Susan", "Bob", "Lucy"]
table = dict.fromkeys(players)
deck = create_deck()
print(deck)
number_of_players = len(players)
print(len(players))
for i in range(0, number_of_players):
    hand = deal_cards(deck, 5)
    table[players[i]] = hand

# cards.print_hand(table, number_of_players)

print(table)