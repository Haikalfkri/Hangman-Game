#Step 5
import random
from hangman_art import stages, logo
from hangman_word import word_list
import os


choosen_word = random.choice(word_list)
lives = 6

print(logo)

print(f"Pssst, the solution is {choosen_word}")

display = []
for _ in range(len(choosen_word)):
    display+="_"


end_of_game = False
while not end_of_game:
    guess = input("Guess the letter: ").lower()
    
    os.systme("cls")
    
    if guess in display:
        print(f"You've already guessed {guess}")
        

    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
            
    if guess not in choosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose") 
    
    print(f"{''.join(display)}")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")
    
    print(stages[lives])