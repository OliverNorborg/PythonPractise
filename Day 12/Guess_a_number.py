#Number guessing game
import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

play_game = True
number = random.randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst the nunber if: {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5


while play_game:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        #guess = int(input("Make a guess: "))
        print("Too high.")
        lives -= 1
    elif guess < number:
        #guess = int(input("Make a guess: "))
        print("Too low.")
        lives -= 1
        
    if lives == 0:
        play_game = False
        print("You've run out of guesses, you lose.")
    else: 
        print("Guess again.")
    
    if number == guess:
        play_game = False
        print(f"You got it! The answer was {number}.")

    
    
