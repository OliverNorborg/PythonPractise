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
    cards = [11,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #An 11 is an Ace
    card = random.choice(cards)
    return card

def total_score(hand):
    if len(hand) == 2 and sum(hand) == 21:
        return 0 #Will be used to check for blackjack 
    if 11 in hand and sum(hand) > 21:
      hand.remove(11)
      hand.append(1)
    return sum(hand)

def update_hand(hand):
    if sum(hand) > 21:
        for i in range(len(hand)):
            if hand[i] == 11:
                hand[i] = 1
                return hand
    else:
        return hand
    

def determine_winner(hand1, hand2):
    user_score = total_score(hand1)
    comp_score = total_score(hand2)
    if user_score == 0:
        print("BLACKJACK, Congratulations")
    elif user_score > 21:
        print("You bust, you lost")
    elif comp_score > 21:
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
    if total_score(user_cards) == 0:
        game_over = True
        #determine_winner(user_cards, comp_cards)
    else:
        game_over = False
        print(f"Your cards: {user_cards}, current score: {total_score(user_cards)}") 
        print(f"Computer's first card: {comp_cards[0]}")

    #while action != "n" or total_score(user_cards) > 21: 
    while not game_over:
        action = input("Type 'y' to get another card, type 'n' to pass: ")

        if action == "y":
            user_cards.append(deal_card())
        # We update the hand incase the user has an 11 and have gone over 21 
        user_cards = update_hand(user_cards)
        comp_cards = update_hand(comp_cards)

        print(f"Your cards: {user_cards}, current score: {total_score(user_cards)}") 
        print(f"Computer's first card: {comp_cards[0]}")
        if action == "n":
            game_over = True
        elif total_score(user_cards) > 21:
            game_over = True


    # This while function will add cards to the computers hand if it is below 17 
    while total_score(comp_cards) < 17 and total_score(user_cards) > total_score(comp_cards):
        comp_cards.append(deal_card())
        comp_cards = update_hand(comp_cards)
    
    #Here we print the final hand for each user 
    print(f"Your final hand: {user_cards}, final score {sum(user_cards)}")
    print(f"Computer's final hand: {comp_cards}, final score {sum(comp_cards)}")
    determine_winner(user_cards, comp_cards)
    
    play_q = input("Do you want to play Blackjack? Type 'y' for yes 'n' for no ")
    if play_q == "y":
        play = True
        os.system('clear')
    else:
        play = False
        
        
