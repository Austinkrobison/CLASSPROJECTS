#p7_dictionary
import urllib.request

bird_to_counts = {}

url = 'http://www.cs.uoregon.edu/Classes/15F/cis122/data/birds2.txt'

with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        bird = line.decode('utf-8')
        if bird in bird_to_counts:
##            count = bird_to_counts[bird]
##            count = count + 1
##            bird_to_counts[bird] = count
            #or
            bird_to_counts[bird] += 1
        else:
            bird_to_counts[bird] = 1
div1 = '='*53
print(div1)
print(' '*22, 'Fowl Count\n')
print(div1)
print(' Species',' '* 13,' Count', ' '*5, ' % of sightings')
print('-'*53)
total_birds = sum(bird_to_counts.values())
#print(total_birds)
for bird in sorted(bird_to_counts):
    show_bird = format(bird.title(), '15s')
    count = bird_to_counts[bird]
    show_count = format(count, '10,d')
    percent = float((count / total_birds)*100)
    nice_percent = format(percent, '15,.2f')
    
    print(show_bird, show_count, nice_percent, '%')
print('\n\nData gathered from: ', url)
