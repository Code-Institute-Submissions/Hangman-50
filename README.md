

 # Hangman - python project

<img width="743" alt="Screenshot 2022-05-18 at 00 13 40" src="https://user-images.githubusercontent.com/7358665/168927580-7b0a199f-b97d-4059-84e1-33958c7decc7.png">

[Game deployed on Heroku](https://hangman-word-guesser.herokuapp.com/)

[Link to Github repository](https://github.com/SJCooper/Hangman)

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
  - Titles and welcome messages prompt the player for input
  - Accepts user input

<img width="743" alt="Screenshot 2022-05-18 at 00 13 40" src="https://user-images.githubusercontent.com/7358665/168927605-b901cf62-4a5a-499c-a488-37ab2df3f39b.png">

- Input validation and error checking
  - All input strings and randomly chosen words are uppercased to aid comparisons.
  - Player input can only be individual letters of the alphabet or words of equal length to the chosen random word also only using characters from the alphabet.
  - If the player makes an invalid input, the game notifies them and no lives are removed

<img width="743" alt="Screenshot 2022-05-18 at 00 14 22" src="https://user-images.githubusercontent.com/7358665/168927781-2135c3b8-5653-4b4b-a9a1-f4b7b788a5ba.png">

  - If the player makes a repeat guess, either single letter or full word, then the player is notified of the invalid guess and no lives are removed
 
 <img width="743" alt="Screenshot 2022-05-18 at 00 14 02" src="https://user-images.githubusercontent.com/7358665/168927713-aeadeecd-eda6-4763-bc93-ddedfab43b85.png">

  - If the player makes a valid guess that is incorrect they are informed that they have lost a life and the art is progressed by adding one body part to the hangman character.

<img width="743" alt="Screenshot 2022-05-18 at 00 14 13" src="https://user-images.githubusercontent.com/7358665/168927759-22faedeb-8b32-4a4d-98c6-e17c6b5077b8.png">

  - If the player makes a valid correct guess of an individual letter then they are congratulated, the letter is show in it's correct position in the word and no lives are lost.
  
  <img width="743" alt="Screenshot 2022-05-18 at 00 13 48" src="https://user-images.githubusercontent.com/7358665/168927688-1caa6149-01fc-4970-9cfa-032fca217850.png">

  - If the player runs out of lives then the game over text is shown and the correct word is displayed to the player
 
  <img width="743" alt="Screenshot 2022-05-18 at 00 14 33" src="https://user-images.githubusercontent.com/7358665/168927921-72805354-b254-4cba-97f0-deeffa857170.png">

  - If the player makes a valid correct guess of the complete word or the final outstanding single letter, then the winning game message is displayed and the full random word is shown.

<img width="743" alt="Screenshot 2022-05-18 at 00 14 43" src="https://user-images.githubusercontent.com/7358665/168927853-4ff2380f-553f-4f18-86a1-0af2ecd7ce7f.png">

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

<img width="989" alt="Screenshot 2022-05-17 at 22 22 16" src="https://user-images.githubusercontent.com/7358665/168928110-9ea75e3e-6c3a-44f8-8363-d3c4e9f57004.png">
<img width="989" alt="Screenshot 2022-05-17 at 22 21 25" src="https://user-images.githubusercontent.com/7358665/168928113-2b9f329e-d7a5-4d77-a82b-d331e47e17f1.png">


## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.
  - Steps for deplyment were outlined by the love-sandwiches project guidelines. These had been updated as Heroku has recently discontinued direct Github links due to a security issue. All steps followed can be found here at [Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/e3b664e16366444c8d722c5d8340b340/).

[Game deployed on Heroku](https://hangman-word-guesser.herokuapp.com/)

[Link to Github repository](https://github.com/SJCooper/Hangman)



