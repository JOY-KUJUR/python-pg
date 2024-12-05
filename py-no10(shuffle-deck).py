import random

# Define the suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


deck = []


for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}' 
        deck.append(card)  

random.shuffle(deck)

print(deck)

for card in deck[:4]:
    print(card)
