import cards
import scores
from collections import Counter

deck = cards.create_deck()
test_hand = cards.deal_cards(deck, 5)
test_hand = [('D', '3'), ('C', '3'), ('S', '3'), ('H', '3'), ('C', '2')]
# test_hand = [('D', '4'), ('D', '3'), ('D', '5'), ('D', 'A'), ('D', '2')]
print(test_hand)

# x = scores.test_straight(test_hand)
# print(x)

# x = scores.test_flush(test_hand)
# print(x)


num_iterations = scores.give_value(test_hand)
result = Counter(num_iterations)
print(result)
value = list(result.keys())
repeat = list(result.values())
print(value, repeat)
result_data = [[], [], [0, 0], []] # 0:hand, 1:score, 2:highest 3:card in hand, 4:rest of cards


if max(repeat) == 1:
    result_data[0] = "EMPTY"
    result_data[1] = 0
if max(repeat) == 2:
    pair = repeat.count(2)
    position1 = repeat.index(2)
    if pair == 2:
        result_data[0] = "TWO PAIR"
        result_data[1] = 2
        position2 = repeat[position1 + 1:].index(2) + position1 + 1
        result_data[2] = [value[position1], value[position2]]
        result_data[2].sort(reverse=True)
    else:
        result_data[0] = "PAIR"
        result_data[1] = 1
        result_data[2][0] = value[position1]
if max(repeat) == 3:
    result_data[0] = "THREE"
    result_data[1] = 3
    position1 = repeat.index(3)
    result_data[2][0] = value[position1]
    if repeat.count(2):
        result_data[0] = "FULL HOUSE"
        result_data[1] = 6
        position2 = repeat.index(2)
        result_data[2][1] = value[position2]
if max(repeat) == 4:
    result_data[0] = "FOUR"
    result_data[1] = 7
    position1 = repeat.index(4)
    result_data[2][0] = value[position1]

print(result_data)



       




    

