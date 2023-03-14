"""Main file for hangman game"""

#Step 5

import random
import hangman_words
import hangman_art


word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

guess_list = []


print(hangman_art.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print("The word is this long:")
print(f"{' '.join(display)}")

while not end_of_game:
    print(f"So far you have incorrectly guessed: {' '.join(guess_list)}")
    guess = input("Guess a letter: ").lower()
    #guess_list.append(guess)
    #guess_list.sort()
    #print(guess_list)
    
    if guess in display:
        print(f"You've already gussed this letter {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        guess_list.append(guess)
        guess_list.sort()
        if lives == 0:
            end_of_game = True
            print(f"The word was: {chosen_word}")
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
    #print("So fare you have guessed:")