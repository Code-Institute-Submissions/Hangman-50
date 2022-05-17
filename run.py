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
        self.word_completion = "_" * len(self.word)
        self.guessed_letters = []
        self.guessed_words = []
        self.lives = 6
        self.games_played = 0
        self.games_won = 0
        self.games_lost = 0

    def welcome_message(self):
        print("Let's play a game of...")
        print(pyfiglet.figlet_format("Hangman!"))

    def display_hangman(self):
        """
        adds visual ASCII art to player to indicate
        how many lives they have used/left
        """

        print(STAGES[self.lives])
        print(self.word_completion)

    def play_hangman(self):
        self.display_hangman()
        guessed = False
        while not guessed and self.lives > 0:
            guess = input("Please guess a letter or word: ").upper().strip()
            # ..if guess is one letter
            if len(guess) == 1 and guess.isalpha():
                # checking to see if letter has already been guessed
                if guess in self.guessed_letters:
                    print("You already guessed", guess)
                # if letter guessed is not correct
                elif guess not in self.word:
                    print(guess, "is not in the word.")
                    self.lives -= 1
                    self.guessed_letters.append(guess)
                # if guessed letter is in the current games word
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
                    if "_" not in self.word_completion:
                        guessed = True

            # ..if guess is the same length of the chosen word and all letters
            elif len(guess) == len(self.word) and guess.isalpha():
                # if a full word guess has already been tried with the same word  # noqa
                if guess in self.guessed_words:
                    print("You already guessed the word", guess)
                # if a full word guess is valid but not correct
                elif guess != self.word:
                    print(guess, "is not the right word")
                    self.lives -= 1
                    self.guessed_words.append(guess)
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
    # player input to start new games or not
    while input("Play Again? (Y/N) ").upper() == "Y":
        hangman_game = Hangman()
        hangman_game.play_hangman()

# code snippet to make game play in command line, not sure if needs to be removed once uploaded to Heroku?!  # noqa


if __name__ == "__main__":
    main()
