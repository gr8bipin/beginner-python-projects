# Generate a random number guessing game in Python
# until the user guesses the correct number
# The user will be prompted to guess a number between 1 and 100
# The program will provide feedback on whether the guess is too high or too low
# and will continue until the user guesses correctly.

# Generate a random number 
# Loop
    # Ask the user to guess a number
    # If not a valid random_number
       # Print an error  
    # If number < guess
        # Print too low
    # If number > guess
        # Print too high
    # Else  
        # Print well done  

import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
    
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            break

    except ValueError:
        print("Please enter a valid integer.")

