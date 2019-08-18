# p8_Count_Words.py

import urllib.request
word_to_counts = {}
url = 'http://www.cs.uoregon.edu/Classes/15F/cis122/data/alice1.txt'
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        line = line.lower()
        #print('Line:', line)
        if len(line) > 0:
            line_list = line.split(' ')
            #print('Line list: ', line_list)
            for word in line_list:
                if word in word_to_counts:
                    word_to_counts[word] += 1
                else:
                    word_to_counts[word] = 1
        #input('Press Enter to Continue ')
for word in sorted(word_to_counts):
    count = word_to_counts[word]
    show_word = format(word.capitalize(), '<18s')
    show_count = format(count, '6,d')
    print(show_word, count)
