
# 📘 Assignment: Games in Python

## 🎯 Objective

In this assignment, you will build a simple text-based Hangman game in Python. You will practice using loops, conditionals, strings, and user input to create an interactive game experience.

## 📝 Tasks

### 🛠️	Build the Core Game Loop

#### Description
Create the main game loop for Hangman. The program should choose a hidden word and repeatedly ask the player to guess letters until they win or run out of attempts.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list of words.
- Display the hidden word progress using underscores for unguessed letters (for example: `_ _ _ _`).
- Prompt the user to enter one letter per turn.
- Continue running until all letters are guessed or attempts reach zero.


### 🛠️	Track Guesses and Game Outcome

#### Description
Add game logic for correct and incorrect guesses. Show useful feedback after each turn and print a final result message when the game ends.

#### Requirements
Completed program should:

- Update the displayed word progress when a correct letter is guessed.
- Decrease remaining attempts when the guessed letter is not in the word.
- Prevent duplicate guesses from counting as new attempts.
- Display a clear win message if the player guesses the full word.
- Display a clear lose message with the correct word if attempts run out.
