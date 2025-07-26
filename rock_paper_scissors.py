# Ask the user to make a choice
# If choice is not valid
#  Print an error 
# Let the computer make a choice
# Print choices (emojis)
# Determine the winner
# Ask the user if they want to continue
# If not
#  Terminate  

import random
choices = ['r', 'p', 's']

while True:

    user_choice = input("Enter rock, paper, or scissors: (r/p/s) ").lower()
    if user_choice not in choices:
        print("Invalid choice.")
        continue

    computer_choice = random.choice(choices)

    if user_choice == 'r':
        print("You chose Rock 🪨")
    elif user_choice == 's':
        print("You chose Scissors ✂️")  
    else:
        print("You chose Paper 📄")

    print(f"You chose: {user_choice}, Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie! 🤝")
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')):
        print("You win! 🎉")
    else:
        print("You lose! 😢")

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break