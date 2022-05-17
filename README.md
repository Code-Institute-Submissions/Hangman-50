

 # Hangman - python project

## How to play the game

Hangman is a word guessing game in which the player guesses letters or whole words to try and guess a word chosen at random by the computer.

A word is chosen at random by the computer and is initially hidden from the player with the only information the player recieves being how many letters the words contains.

The player then has limited guesses to choose individual letters or to attempt to guess the whole word.

Any succesful letters guessed are then shown to the player in their correct position in the word.

If the player runs out of guesses then they lose.

If the playes correctly guesses the word or correctly guesses all letters in the word individually before running out of guesses, the player wins the game.

Progression is shown visually by a simple hangman gallows slowly adding part of a man to the noose until the head, arms and legs are all added at which point it is game over.

## Features

### Existing features

- Game Start
  - A random word is chosen by the computer from a list
  - Player plays against the computer
  - Tiltles and welcome messages prompt the player for input
  - Accepts user input

- Input validation and error checking
  - All input strings and randomly chosen words are uppercased to aid comparisons.
  - Player input can only be individual letters of the alphabet or words of equal length to the chosen random word also only using characters from the alphabet.
  - If the player makes an invalid input, the game notifies them and no lives are removed
  - If the player makes a repeat guess, either single letter or full word, then the player is notified of the invalid guess and no lives are removed
  - If the player makes a valid guess that is incorrect they are informed that they have lost a life and the art is progressed by adding one body part to the hangman character.
  - If the player makes a valid correct guess of an individual letter then they are congratulated, the letter is show in it's correct position in the word and no lives are lost.
  - If the plyer makes a valid correct guess of the complete word or the final outstanding single letter, then the winning game message is displayed and the full random word is shown.

### Future Features

- scoring system
    - local or signed in storage of players historical scores.
- color added
    - use of packages to add color to the text. red for lives lost and green when the game is won etc
- two player mode
    - functionality for two players to play against each other taking it in turns to enter a word for the other player to guess.
- Multiple word catagories
    - multiple word lists grouped by catagory that the player can chose from at the start of the game.
- Difficulty ranges
    - Mulitple words, phrases or words of longer length could be grouped in specific list that can be chosen through initial menu options at the start of the game.

## Testing

I have manually tested this project by doing the following:
  - Passed the code through a PEP8 checker and confirmed that there are no issues
  - Purposfully repeated inputs for single and full word guesses, purposefully guessed incorrectly and created win and lose conditions.
  - Tested in my local IDE and Heroku python environment fset up by Code Institute.

### Bugs

Bugs and their solutions have been documented in the issues page of the Github repository for this project.
There are currently no bugs that are unresolved.

### Validator testing

No validator errors were returned from [PEP8online](PEP8online.com)

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.
  - Steps for deplyment were outlined by the love-sandwiches project guidelines. These had been updated as Heroku has recently discontinued direct Github links due to a security issue. All steps followed can be found here at [Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/e3b664e16366444c8d722c5d8340b340/).



