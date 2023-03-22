# A higher or lower game. 
# The goal of the game is to guess who has more followers 

from game_data import data
from art import logo, vs
import random
import os

os.system('clear')

wrong = False
first_guess = True
score = 0

while not wrong:
    print(logo)
    if first_guess:
        a = random.choice(data) 
        first_guess = False
    else:
        print(f"You're right! Current Score: {score}.")
    name_a = a["name"]   
    discription_a = a["description"]
    country_a = a["country"]
    followers_a = a["follower_count"]
    print(f"Compare A: {name_a}, a {discription_a}, from {country_a}")
    print(vs)
    b = random.choice(data) 
    name_b = b["name"]   
    discription_b = b["description"]
    country_b = b["country"]
    followers_b = b["follower_count"]
    print(f"Compare B: {name_b}, a {discription_b}, from {country_b}")
    AorB = input("Who has more followers? Type 'A' or 'B': ")
    if followers_a > followers_b and AorB == "A":
        os.system('clear')
        guess = True
        score+= 1
    elif followers_a < followers_b and AorB == "B":
        os.system('clear')
        guess = True
        score += 1
        a = b # We set a to the one with the most followers
    else: 
        os.system('clear')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}.")
        wrong = True
        