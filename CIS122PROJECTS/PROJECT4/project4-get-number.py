# project-get_int.py
prompt = 'Enter a number between 1 and 100: '
def get_int(prompt, minval, maxval):
    """ Takes the user input value as an integer
        between 1 and 100, if the number is not between
        1 and 100, asks for another attempt.
    """
    try_again = True
    while try_again:
        my_number = int(input(prompt))
        if my_number < minval:
            print('That number is less than 1, \n Please, try again')
        elif my_number > maxval:
            print('That number is greater than 100,\n Please, try again')
        else:
            try_again = False
    return my_number
print('Success,', get_int(prompt, 1, 100), 'is a good number')
