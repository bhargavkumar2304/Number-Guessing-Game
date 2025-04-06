import random
import math

# Helper function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Helper function to check if a number is a perfect square
def is_perfect_square(n):
    return int(math.sqrt(n)) ** 2 == n

# Helper function to check if a number is a multiple of a given number
def is_multiple_of(n, m):
    return n % m == 0

def number_guessing_game():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        # Ask for the user's guess or request for a hint
        user_input = input("Enter your guess or type 'hint' for a hint: ").strip().lower()

        if user_input == "hint":
            # Provide a hint only when asked
            if is_multiple_of(random_number, 5):
                print("Hint: The number is a multiple of 5.")
            if is_prime(random_number):
                print("Hint: The number is a prime number.")
            if is_perfect_square(random_number):
                print("Hint: The number is a perfect square.")
        else:
            try:
                user_guess = int(user_input)
                attempts += 1  # Increment attempts on each guess
                # Provide feedback based on the guess
                if user_guess < random_number:
                    print("Your guess is too low. Try again!")
                elif user_guess > random_number:
                    print("Your guess is too high. Try again!")
                else:
                    print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                    break  # Exit the loop if the guess is correct

            except ValueError:
                print("Invalid input. Please enter a valid number or type 'hint' to get a hint.")

# Run the game
number_guessing_game()