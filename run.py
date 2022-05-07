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
    print("Let's play a game of Hangman!")
    
def display_hangman(lives):
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






    ]