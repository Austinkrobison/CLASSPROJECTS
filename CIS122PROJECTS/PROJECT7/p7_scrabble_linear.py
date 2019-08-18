# p7_scrabble_linear.py
import urllib.request
import time as t
info_url = 'http://www.cs.uoregon.edu/Classes/15F/cis122/data/sowpods_short.txt'
word_list = []
menu_ask = 'Enter S to search or Q to quit: '
prompt = 'Type a word to search: '
def linear_search(item, the_list):
    index = 0
    for word in the_list:
        if word == item:
            return True, index
        elif word > item:
            return False, -1
        else:
            index = index + 1
    return True
with urllib.request.urlopen(info_url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode("utf-8")
        if line[0] != '#':
            word_list.append(line)
    print(word_list)
    menu_inp = input(menu_ask)
    while menu_inp != 'Q' and menu_inp == 'S' or 's':
        word_inp = input(prompt)
        word_out = word_inp.title()
        found = False
        if linear_search(word_inp, word_list) == True:
            print(word_out, 'was found')
            found = True
        if not found:
            print(word_out, 'was not found! please try again')





























#look at the second character
#look at the third character
#look at the forth character
#look at the fifth character
#look at the sixth character
##ask_inp = input(ask)
##current_char_place = 0
##for word in word_list:
##    start = t.time()
##    if word == ask_inp:
##        print('word found')
##    while ask_inp[current_char_place] == word[current_char_place]: 
##        current_char_place += 1
##    if
##    break
##end_time = t.time() - start
##print(end_time)

