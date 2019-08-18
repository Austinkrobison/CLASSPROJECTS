"""
Solve a jumble (anagram) by checking against each word in a dictionary
Authors: Austin Robison

Usage: python3 jumbler.py jumbleword wordlist.txt
"""

import argparse

def jumbler(jumble, dict_file_name):
    """
    takes a group letters and sorts it into words in
    inputs:
        jumble : a bunch of letters that may be arranged into a word
        dict_file_name: file name of an english(or any language) dictionary
    effects:
        prints a word that can be "un-scrambled" from jumble
        also prints how many words can be unscrambled out of the
entire dictionary
    """
    dict_file = open(dict_file_name, "r")
    matches = 0
    word_amt = 0
    jumb_key = ''.join(sorted(jumble))
    for word_raw in dict_file:
        word = word_raw.strip()
        word_key = ''.join(sorted(word))
        word_amt += 1
        if jumb_key ==  word_key:
            print(word)
            matches += 1
    if matches >= 1:
        print(matches, "matches in", word_amt, "lines")
    if matches == 0:
        print('No matches')
    dict_file.close()

def main():
    """
    collect command arguments and invoke jumbler()
    inputs:
        none, fetches arguments using argparse
    effects:
        calls jumbler()
    """
    parser = argparse.ArgumentParser(description="Solve a jumble (anagram)")
    parser.add_argument("jumble", type=str, help="Jumbled word (anagram)")
    parser.add_argument('wordlist', type=str, help="A text file containing dictionary words, one word per line.")
    args = parser.parse_args()  # gets arguments from command line
    jumble = args.jumble
    wordlist = args.wordlist
    jumbler(jumble, wordlist)

if __name__ == "__main__":
    main()
