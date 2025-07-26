# dice_rolling_game.py
# A simple dice rolling game where the user can roll two dice and get a random result between
# the values of the two dice.
# Ask: roll two dice and return a random number between the two values.
# If user chooses to roll, display the result.
# If user chooses not to roll, thank them for playing.
# If user enters an invalid choice, display an error message.

# Loop
    # Ask: roll the dice?
    # If user enters y 
    #  Generate two random numbers
    #  Print them
    # If user enters n
    #  Print a thank you message
    #  Terminate
    # Else
    #  Print invalid choice

import random
playing = True
while playing:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == 'y':   
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1}, {dice2})')
    elif choice == 'n':
        print("Thanks for playing!")
        break # playing = False
    else:
        print("Invalid choice!")