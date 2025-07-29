

# 📘 Assignment: Games in Python – Hangman

## 🎯 Objective

You will build the classic Hangman game in Python, practicing string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️  Create the Hangman Game

#### Description
Write a program that randomly selects a word from a list and lets the user guess letters. The player has a limited number of attempts to guess the whole word.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept single letters as user guesses
- Display current progress in the format _ _ _ (underscores for unguessed letters)
- Track the number of incorrect guesses remaining
- End when the word is guessed or attempts run out
- Display win/lose messages

##### Example
```
Welcome to Hangman!
Word: _ _ _ _ _
Attempts left: 6
Guess a letter: a
Word: _ a _ _ a
Attempts left: 5
...
Congratulations! You guessed the word: panda
```

### 🛠️  Add Your Own Word List

#### Description
Extend the game to allow easy editing of the word list (e.g., by changing a variable in the code or loading from a file).

#### Requirements
Completed program should:

- Allow easy modification of the word list used for random selection
- Support a list of at least 10 different words
- Work correctly regardless of word length
