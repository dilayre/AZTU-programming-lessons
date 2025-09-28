import itertools, random   # import modules

# card values with names
values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
suits = ['Spade', 'Heart', 'Diamond', 'Club']

# make a deck (52 cards)
deck = list(itertools.product(values, suits))

# shuffle the deck
random.shuffle(deck)

# function to convert number to card name
def card_name(value):
    if value == 1:
        return "Ace"
    elif value == 11:
        return "Jack"
    elif value == 12:
        return "Queen"
    elif value == 13:
        return "King"
    else:
        return str(value)

# draw 5 cards
print("You got:")
for i in range(5):
    val, suit = deck[i]
    print(card_name(val), "of", suit)
