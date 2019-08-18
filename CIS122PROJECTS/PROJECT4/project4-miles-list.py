# project4-miles-list.py
prompt = 'Type many miles have you rode your bike each day this week,\n then press Enter, when you are done enter 0 '
miles = [ ]
def get_float(prompt, minval, maxval):
    """ Takes the user input value as a float value
        between minval and maxval, if the number is not between
        minval and maxval, asks for another attempt.
    """
    try_again = True
    while try_again:
        my_number = float(input(prompt))
        if my_number < minval:
            print('That number is less than 0, \nPlease, try again')
        elif my_number > maxval:
            print('That number is greater than 100,\nPlease, try again')
        elif my_number == 0:
            try_again = False
        else:
            try_again = False
    return my_number

distance = get_float(prompt, 0, 100)
counter = 0
while distance != 0:
    if counter == 0:
        miles.append(distance)
        counter += 1
    distance = get_float(prompt, 0, 100)
    miles.append(distance)

total_distance = sum(miles)
print('Total distance rode this week', total_distance)
