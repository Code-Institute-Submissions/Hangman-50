# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    print(word)

get_word()