from random import choice
from string import ascii_uppercase # Uppercase alphabet

words = ["testa", "testb", "testc", "testd", "teste", "testf"] # Random word array ( to let the user test this code )


# Choose a random word out of all the word options
def get_word(words):
    word = choice(words).upper()  # Choose a random word

    return word # Returns the word


# Show te score after the game ended
def show_score(word: str, fails: int, max_fails: int):
    word = word.lower() # Make all the letters of the word lowercase

    if fails < max_fails:
        print(f"You won, the word was: {word}")
    
    else:
        print(f"You lost, the word was: {word}")


# The hangman game itself
def hangman(word: str):
    word_letters = list(word) # Make an array of the word
    guessed_letters = [] # Make an array where the users guesses gets stored
    word_characters = ['-'] * len(word) # Make an array to show the length of the word, and the characters if the users guessed 1

    game_ended = False # Check if the game has ended
    fails = 0 # The fails the user has made
    max_fails = 5 # Max fails the user can make

    
    while not game_ended and fails < max_fails:
        print("You have already used this letters: " + ' '.join(guessed_letters)) # Shows which letters the user has guessed
        print("Word: " + ' '.join(word_characters).lower()) # Shows the letter or "-" when the letter is not guessed

        guess = input("Guess a letter: ").upper() # Ask the users letter

        # If the guess is not in the word
        if not guess in word_letters:

            # If the user guessed a single letter
            if guess in ascii_uppercase:
                # If the user guessed a new letter
                if guess not in guessed_letters:
                    print("You guessed a wrong letter")
                    fails += 1  # Add 1 fail to the user
                
                # If the user guessed a letter that was already guessed
                else:
                    print("You already guessed this letter, the fails were not increased")
            
            # If the user did not guess an letter
            else:
                print("Choose 1 letter, the fails were not increased") 
        
        # If the user guessed a letter thats in the word
        else:
            # Run this check if there are 1 or more of the letter in the word
            while guess in word_letters:
                index = word_letters.index(guess) # Get the positon of the letter
                word_characters[index] = guess # Add the letter to the word (that gets shown to the user)
                word_letters[index] = "-" # Change the positon of the letter to "-" in the word
            
            # If all the letters are guessed
            if not "-" in word_characters:
                game_ended = True # Ends the game

        # Add the guessed letter to all the guessed letters
        if guess in ascii_uppercase and guess not in guessed_letters:
            guessed_letters.append(guess) # Add the guesses letter to the guessed letters

    # If the game ended
    else:
        show_score(word, fails, max_fails) # Shows the board with the information


word = get_word(words) # Get a random word
hangman(word) # Starts the game