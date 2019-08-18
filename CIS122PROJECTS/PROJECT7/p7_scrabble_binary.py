# p7_scrabble_binary.py
import urllib.request
info_url = "http://www.cs.uoregon.edu/Classes/15F/cis122/data/sowpods.txt"
word_list = []
ask = 'Enter L to Look for a word, or Q to Quit: '
prompt = 'Enter a word to search for: '
def binary_search(item, alist):
    left = 0
    right = len(word_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if word_list[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    if left >=0 and left < len(alist) and alist[left] == item:
        print(alist[left], 'was found', item)
        return True
    else:
        return False    
with urllib.request.urlopen(info_url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode("utf-8")
        if line[0] != '#':
            word_list.append(line)
    ask_inp = input(ask)
    while ask_inp != 'Q':
        word_inp = input(prompt).lower()
        word_out = word_inp.title()
        print()
        if ask_inp == 'L' or 'l':
            found = False
        if binary_search(word_inp, word_list) == True:
            print(word_out, "was found!")
            found = True
        if not found:
            print(word_out, "was not found! Please try again.")
