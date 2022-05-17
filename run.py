# import modules and py files used

import random
import pyfiglet
from constants import WORD_LIST, STAGES


class Hangman:
    """
    creates an instance of the Hangman game
    sets up variables
    """

    def __init__(self):
        self.word = random.choice(WORD_LIST).upper()
        self.word_completion = "-" * len(self.word)
        self.guessed_letters = []
        self.guessed_words = []
        self.lives = 6

    def welcome_message(self):
        """
        creates a welcome message
        uses pyfiglet font
        """
        print("Let's play a game of...")
        print(pyfiglet.figlet_format("Hangman!"))

    def display_hangman(self):
        """
        adds visual ASCII art to player to indicate
        how many lives the player has used/left
        """
        print(STAGES[self.lives])
        print(self.word_completion)

    def play_hangman(self):
        """
        checks for player input and validates for:
        repeat single letter guess
        incorrect single letter guess
        correct single letter guess
        repeat full word guess
        incorrect full word guess
        correct full word guess.
        updates guess lists as required and gives feedback to player
        """
        self.display_hangman()
        guessed = False
        while not guessed and self.lives > 0:
            guess = input("Please guess a letter or word: \n").upper().strip()
            if len(guess) == 1 and guess.isalpha():
                if guess in self.guessed_letters:
                    print("You already guessed", guess)
                elif guess not in self.word:
                    print(guess, "is not in the word.")
                    self.lives -= 1
                    self.guessed_letters.append(guess)
                    print("You have: " + str(self.lives) + " lives remaining")
                else:
                    print("Awesome,", guess, "is in the word!")
                    self.guessed_letters.append(guess)
                    # convert word string to list, allow correct letters to show  # noqa
                    word_as_list = list(self.word_completion)
                    # find letters in list that have been guessed using list
                    indices = [i for i, letter in enumerate(
                        self.word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    # convert back to string
                    self.word_completion = "".join(word_as_list)
                    # check for win condition
                    if "-" not in self.word_completion:
                        guessed = True

            elif len(guess) == len(self.word) and guess.isalpha():
                if guess in self.guessed_words:
                    print("You already guessed the word", guess)
                elif guess != self.word:
                    print(guess, "is not the right word")
                    self.lives -= 1
                    self.guessed_words.append(guess)
                    print("You have: " + str(self.lives) + " lives remaining")
                # a full word guess is valid and correct
                else:
                    guessed = True
                    self.word_completion = self.word
            else:
                print("That is not a valid guess. Please guess a letter or word.")  # noqa
            self.display_hangman()
            print("\n")
        # if player wins the game
        if guessed:
            print("Congrats, you guessed the word!", self.word)
        # if player runs out of lives
        else:
            print("Sorry, you ran out of lives. The word was " +
                  self.word + ". Maybe next time!")


def get_word():
    """
    Picks a random word from word list
    Returns the word as all uppercase
    Sets it for use in current game
    """
    word = random.choice(WORD_LIST)
    return word.upper()


def main():
    hangman_game = Hangman()
    hangman_game.welcome_message()
    hangman_game.play_hangman()
    # player input to start new games or quit playing
    while input("Play Again? (Y/N) \n").upper() == "Y":
        hangman_game = Hangman()
        hangman_game.play_hangman()


if __name__ == "__main__":
    main()
