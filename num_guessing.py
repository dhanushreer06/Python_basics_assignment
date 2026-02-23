#Q17. Number Guessing Game

import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("   Welcome to the Number Guessing Game!")
    print("***************************************")
    print("I have chosen a number between 1 and 100.")
    
    # Start the loop
    while True:
        # input guess
        guess = int(input("Enter your guess: "))
        attempts += 1 # Increase attempt count by 1
        
        # Check if the guess is too low
        if guess < secret_number:
            print("Too low! Try again.")
            
        # Check if the guess is too high
        elif guess > secret_number:
            print("Too high! Try again.")
            
        # If the guess is correct, exit the loop
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

# Run the game
number_guessing_game()