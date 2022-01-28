# Author: Youri van der Meulen

# Import function 'random'
import random 
# Define function named 'computer_guess' because the computer is gonna guess our number, x = parameter
def computer_guess(x):
    guess = 0
    # Computer needs to have a range of number to guess out, minimum and maximum
    lowest = 1
    highest = x
    # Feedback given by user, empty string
    feedback = ''
    # While loop over our feedback expression
    while feedback != 'c':
        # If statement to avoid that low and high are the same number, otherwise 'randint' will give us an error
        if lowest != highest:
            # First random guess by the computer between low and high, 'random.randint' returns a random integer
            guess = random.randint(lowest, highest)
        else:
            guess = lowest
        # The computer needs to 'ask' the user for feedback on whether his guess was correct or wrong. The 'f' string allows me to put a variable in my string.
        feedback = input(f'Is the number {guess} too high (press H), too low (press L), or correct (press C)?').lower()
        # If statement for our different types of feedback to the computer.
        if feedback == 'h':
            highest = guess - 1
        elif feedback == 'l':
            lowest = guess + 1
    # Feedback when the computer guessed our number correctly
    print(f'The computer guessed your number {guess} correctly! Next time, make up a more difficult number!')

# Call the 'computer_guess' function
computer_guess(100)