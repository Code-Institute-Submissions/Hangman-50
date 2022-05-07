#import modules and py files used

import random
from words import word_list

def get_word():
    """
    Picks a random word from word list
    Returns the word as all uppercase
    Sets it for use in current game
    """
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """
    Set up initial play variables    
    set up the correct number of underscores for the word length
    """
    word_completion = "_" * len(word)
    # initial state of has the word been correctly guessed is set to False
    guessed = False
    # list to add letters that have been guessed to
    guessed_letters = []
    # list to add full words that have been guessed to
    guessed_words = []
    # number of guesses left before game is lost, (head, torso, left and right arms, left and right legs)
    lives = 6
    # prints welcome message, ASCII art and current word status
    print("Let's play a game of Hangman!")
    print(display_hangman(lives))
    print(word_completion)
    print("\n")
    #loop for game logic
    while not guessed and lives > 0:
        guess = input("Please guess a letter or word: ").upper()
        # ..if guess is one letter
        if len(guess) == 1 and guess.isalpha():
            # checking to see if letter has already been guessed
            if guess in guessed_letters:
                print("You already guessed", guess)
            # if letter guessed is not correct
            elif guess not in word:
                print(guess, "is not in the word.")
                lives -= 1
                guessed_letters.append(guess)
            # if guessed letter is in the current games word
            else:
                print("Awesome,", guess, "is in the word!")
                guessed_letters.append(guess)
                # convert word string to list to allow correct letters to be shown to player
                word_as_list = list(word_completion)
                # find letters in list that have been guessed using index numbers in list
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                # convert back to string
                word_completion = "".join(word_as_list)

        #..if guess is the same length of the chosen word and all letters
        elif len(guess) == len(word) and guess.isalpha()

        else:
            print("That is not a valid guess. Please try again.")
        print(display_hangman(lives))
        print(word_completion)
        print("\n")
        










def display_hangman(lives):
    """
    adds visual ASCII art to player to indicate
    how many lives they have used/left
    """
    stages = [
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -
                """,
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                    -
                """,
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     
                    -
                """,
                """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
                    -
                """,
                """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -
                """,
                """
                    --------
                    |      |
                    |      O
                    |     
                    |    
                    |     
                    -
                """,
                """
                    --------
                    |      |
                    |      
                    |    
                    |     
                    |     
                    -
                """,
    ]
    return stages[lives]