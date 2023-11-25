from collections import Counter

def give_value(hand): # set numerical values to the cards in the hand
    values = []
    convert = ["T", "J", "Q", "K", "A"] # Ace = 14 for this game
    for card in hand:
        single_card = card[1]
        if single_card in convert:
            card_value = (convert.index(single_card)) + 10
        else:
            card_value = int(single_card)
        values.append(card_value)
    return values

def test_straight(hand): # checks hand for straight
    values = give_value(hand)
    values.sort()
    if min(values) == 2 and max(values) == 14: # check for straight with ACE in the middle
        gap = 0
        i = 0
        while i <= len(values)-1:
            gap = values[i+1] - values[i]
            if gap > 1: 
                for n in range(i+1):
                    values[n] = values[n] + 13
                break
            i += 1
    straight_sum = len(values) * 0.5 * (max(values) + min(values)) # formula for series
    if sum(values) == straight_sum:
        return "STRAIGHT"
    
def test_flush(hand): # check for flush in hand
    signs = []
    for sign in hand:
        signs.append(sign[0])
    result = Counter(signs)
    result = result.values()
    result = int(list(result)[0])
    if result == 5: # all signs are the same
        return "FLUSH"
    
def test_other(hand):
    num_iterations = give_value(hand)
    result = Counter(num_iterations).values()

