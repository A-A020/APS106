##############################
# APS106 Winter 2021 - Lab 5 #
##############################

import random
from itertools import combinations

#####################################
# HELPER FUNCTIONS TO HELP PLAY THE
# GAME - NO NEED TO EDIT THESE
#####################################

def generate_deck():
    """
    (None) -> [[suit, number],[suit,number], ...]

    Create a standard deck of cards with which to play our game.
    Suits are: spades, clubs, diamonds, hearts
    Numbers are: 1 -13 where the numbers represent the following cards:
        1  - Ace
        11 - Jack
        12 - Queen
        13 - King
        2-10 - Number cards
    """

    deck = []
    suits = ['spades','clubs','diamonds','hearts']

    for suit in suits:
        for number in range(1,14):
            deck.append([suit,number])

    return deck

def shuffle(deck):
    """
    (list) -> list

    Produce a shuffled version of a deck of cards. This should shuffle a deck
    containing any positive number of cards.

    Note, this function should return a new list containing the shuffled deck
    and not directly reorder the elements in the input list. That is, the
    list contained in 'deck' should be unchanged after the function returns.
    """

    shuffled_deck = random.sample(deck,len(deck))

    return shuffled_deck

#############################
# PART 1 - Deal card
#############################

def deal_card(deck,hand):
    """
    (list,list) -> None

    Deal a card from the first element in the deck list and add it to the list
    representing the player's hand. Both list input parameters
    are nested lists with each element in the list being a two-element
    list representing a card.
    
    Note that this function returns nothing! It modifies the two lists that 
    are passed in as parameters in place.

    """

    new_hand = hand.append(deal.card[0])
    return new_hand


#############################
# PART 2 - Score Hand
#############################

def score_hand(hand):
    """
    (list) -> int

    Calculate the cribbage score for a hand of five cards. The input parametercount
    is a nested list of length 5 with each element being a two-element list
    representing a card. The first element for each card is a string defining
    the suit of the card and the second element is an int representing the 
    number of the card.
    """
    

score_hand=[['hearts',10],['hearts',2],['hearts',3],['hearts',6],['diamonds',3]]

num_list = []
for sublist in socre_hand:
    for char in sublist:
        num_list = num_list.append[char[1]]
print(num_list)
        


################################
# PART 3 - PLAY
################################

def play(shuffled_deck):
    """
    (list) -> [str, int, int]
    
    Function deals cards to players, computes player scores, and
    determines winner.
    
    Function retuns a three-element list where the first element is a string
    indicating the winner, the second element is an int specifying player 1\'s
    score, and the third element is an int specifying player2\'s score.
    """
    player1_hand = []
    player2_hand = []
    
    # TODO complete the function
    
