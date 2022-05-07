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
    print(word.upper())
    

get_word()
