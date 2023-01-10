# Blackjack

MAX = 21
import random

def main():
    hand1 = 0
    hand2 = 0
    deck = create_deck()

    while hand1 <= MAX and hand2 <= MAX:
        #player1
        card1 = random.choice(list(deck.items()))
        value1 = card1[1]
        del deck[card1[0]]
        hand1 = update_hand_value(hand1,value1,card1)

        #player2
        card2 = random.choice(list(deck.items()))
        value2 = card2[1]
        del deck[card2[0]]
        hand2 = update_hand_value(hand2,value2,card2)

        print("Player 1 was dealt", card1)
        print("Player 2 was dealt", card2)

    print("Player 1: ", hand1, "Player 2: ",hand2)

    if hand1 > MAX and hand2 > MAX:
        print("There is no winner...")
    #'Player 1 wins' or
    elif hand1 < MAX:
        print("Player 1 wins!")
    #'Player 2 wins'
    else:
        print("Player 2 wins!")


# The create_deck function creates a deck of cards and returns the deck.
def create_deck():
    # Set up local variables
    suits = ['Spades','Hearts','Clubs','Diamonds']
    special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}

    # Create list of all the card values
    numbers = ['Ace', 'King', 'Queen', 'Jack']
    for i in range(2,11):
        numbers.append(str(i))

    # Initialize deck
    deck = {}
    for suit in suits:
        for num in numbers:
            #TODO Add the numbers 2-10 to the deck [Hint: you will need to check if the value is numeric]
            if num == '2' or num == '3' or num == '4' or num == '5' or num == '6' or num == '7' or num == '8' or num == '9' or num == '10':
                deck.update({num +' of '+ suit:int(num)})
            
            #TODO Add the Ace, King, Queen, or Jack values to the deck using the dictionary special_values.
            else:
                deck.update({num + ' of ' + suit:special_values[num]})

    return deck

#Given the player's current hand, the value of the card they were just dealt
# and the name of the card they were just dealt, return the new value of their hand 
# Remember: If a player is dealt an ace, the program should decide the value by:
# The ace will be worth 11 points, unless that makes the player's hand exceed 21 points.
# In that case the ace will be worth 1 point.
def update_hand_value(hand, value, card):
    if card != 'Ace':
        if type(value) == int: #number cards
            hand += value
            return hand

        elif type(value) == str: #face cards
            hand += 10
            return hand

    else:
        if hand + 11 == 21:
            hand += 11
            return hand

        elif hand + 11 > 21:
            hand += 1
            return hand

# Call the main function
main()

