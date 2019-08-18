# project6-sowpods.py
import urllib.request
info_url = 'http://www.cs.uoregon.edu/Classes/15F/cis122/data/sowpods.txt'
word_list = []
ask = 'Enter L to Look for a word, or Q to Quit: '
prompt = 'Enter a word to search for: '

def Search(alist, item):
    pos = 0
    found = False    
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found


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
        if Search(word_list, word_inp) == True:
            print(word_out, "was found!")
            found = True
        if not found:
            print(word_out, "was not found! Please try again.")
print(word_list)
