# Number Guessing Game

Welcome to the **Number Guessing Game**! This is a Python-based console game where the computer selects a random number between 1 and 100, and you must guess the number. You can request hints during the game to help you narrow down your guesses.

## Features

- The game generates a random number between 1 and 100.
- You can guess numbers until you find the correct one.
- The game provides feedback after each guess, telling you if your guess is too high or too low.
- You can request a hint by typing `hint`. Hints include:
  - Whether the number is a **multiple of 5**.
  - Whether the number is a **prime number**.
  - Whether the number is a **perfect square**.

## How to Play

1. **Start the game**: When you run the script, the game will inform you that it has selected a number between 1 and 100.
2. **Make a guess**: Type your guess (a number between 1 and 100) and press Enter.
3. **Feedback**: After each guess, the game will tell you if the guess is too low, too high, or correct.
4. **Request a hint**: If you're stuck, type `hint` to get helpful clues. You can request multiple hints during the game.

## Example Interaction

```
Welcome to the Number Guessing Game!
I have selected a number between 1 and 100. Try to guess it!

Enter your guess or type 'hint' for a hint: 50
Your guess is too low. Try again!

Enter your guess or type 'hint' for a hint: hint
Hint: The number is a multiple of 5.

Enter your guess or type 'hint' for a hint: 55
Your guess is too high. Try again!

Enter your guess or type 'hint' for a hint: 50
Congratulations! You've guessed the number in 3 attempts.
```

## Functions

### 1. `is_prime(n)`
This function checks if a number `n` is a prime number. A prime number is a number greater than 1 that is divisible only by 1 and itself.

### 2. `is_perfect_square(n)`
This function checks if a number `n` is a perfect square. A perfect square is a number that is the square of an integer.

### 3. `is_multiple_of(n, m)`
This function checks if a number `n` is a multiple of another number `m`.

### 4. `number_guessing_game()`
This is the main function that runs the Number Guessing Game. It generates a random number, handles user input, provides feedback, and gives hints when requested.

## Requirements

- Python 3.x or higher
- No external libraries are required as it uses Python's built-in libraries `random` and `math`.

## How to Run

1. Copy the code into a Python file, for example `number_guessing_game.py`.
2. Run the file from the command line:
   ```bash
   python number_guessing_game.py
   ```
3. Follow the on-screen instructions to play the game.

## License

This project is open-source and available under the MIT License.

---
