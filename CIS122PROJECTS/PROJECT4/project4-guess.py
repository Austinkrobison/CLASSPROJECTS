# project4-guess.py
prompt = 'Guess a number between 1 and 100: '
def get_int(prompt, minval, maxval):
    """ Takes the user input value as an integer
        between minval and maxval, if the number is not between
        minval and maxval, asks for another attempt.
    """
    try_again = True
    while try_again:
        my_number = int(input(prompt))
        if my_number < minval:
            print('That number is less than 1, \nPlease, try again')
        elif my_number > maxval:
            print('That number is greater than 100,\nPlease, try again')
        else:
            try_again = False
    return my_number
import random as r
answer = r.randint(1, 100)
def guessing_game(prompt, answer):
    try_again = True
    while try_again:
        my_guess = get_int(prompt, 1, 100)
        if my_guess > answer:
            print('That guess was greater than the answer,\nPlease try again')
        elif my_guess < answer:
            print('That guess was less than the answer,\nPlease try again')
        else:
            try_again = False
    return my_guess
print('Nice Guess!\n', guessing_game(prompt, answer),'is the correct number!')
