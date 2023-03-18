############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Code #####################

from art import logo 
import os 
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    #print(card)
    return card

def total_score(hand):
   return  sum(hand)

def determine_winner(hand1, hand2):
    if sum(hand1) > 21:
        print("You bust, you lost")
    elif sum(hand2) > 21:
        print("The deal bust, you win!")
    elif sum(hand1) > sum(hand2):
        print("You win!")
    elif sum(hand1) < sum(hand2):
        print("You lose")
    elif sum(hand1) == sum(hand2):
        print("It's a draw")


play = True
play_q = input("Do you want to play Blackjack? ")

#print(logo)
while play:
    print(logo)
    user_cards = []
    comp_cards = []
    action = ""
    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())
    
    print(f"Your cards: {user_cards}, current score: {total_score(user_cards)}") 
    print(f"Computer's first card: {comp_cards[0]}")
    while action != "n" or total_score(user_cards) > 21: 
        action = input("Type 'y' to get another card, type 'n' to pass: ")

        if action == "y":
            user_cards.append(deal_card())
        print(f"Your cards: {user_cards}, current score: {total_score(user_cards)}") 
        print(f"Computer's first card: {comp_cards[0]}")
    #print(user_cards)
    #print(comp_cards)
    while total_score(comp_cards) < 17 and total_score(user_cards) > total_score(comp_cards):
        comp_cards.append(deal_card())
    
    print(f"Your final hand: {user_cards}, final score {total_score(user_cards)}")
    print(f"Computer's final hand: {comp_cards}, final score {total_score(comp_cards)}")
    determine_winner(user_cards, comp_cards)
    
    play_q = input("Do you want to play Blackjack? Type 'y' for yes 'n' for no ")
    if play_q == "y":
        play = True
        os.system('clear')
    else:
        play = False