# project6-states.py
import urllib.request
info_url = 'http://www.cs.uoregon.edu/Classes/15F/cis122/data/state_data.txt'
info_list = []
total_area = 0
total_pop = 0
##-------------------formating-----------------------
divider1 = '-' * 52
divider2 = '=' * 53
header_s = format('State', '15s')
header_c = format('Capital', '18s')
header_a = format('Area', '7s')
header_p = format('Population (Million)')
print('-' * 21, 'State Data','-' * 21, '\n')
print(header_s, header_c, header_a, header_p)
print(divider2, '\n')
def nice_data(state, capital, area, pop):
    '''Data -> format
       Makes data look presentable
    '''
    nice_state = format(state.title(), '15s')
    nice_capital = format(capital.title(), '15s')
    if type(area) == int:
        nice_area = format(area, '10,d')
    else:
        nice_area = format(area, '>10s')
    if type(pop) == float:
        nice_pop = format(pop, '10,.1f')
    else:
        nice_pop = format(pop, '>10s')
    print(nice_state, nice_capital, nice_area, nice_pop)
    return None
##-------------------state data-----------------------
with urllib.request.urlopen(info_url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode("utf-8")
        if line[0] != '#':
            item_list = line.split(',')
            state = item_list[0].lower()
            capital = item_list[1].lower()
            area = int(item_list[2])
            pop = float(item_list[3])
            info_list.append([state, capital, area, pop])
            nice_data(state, capital, area, pop)
            total_area = int(total_area + area)
            show_total_area = format(total_area, '34,d')
            total_pop = float(total_pop + pop)
            show_total_pop = format(total_pop, '10,.1f')
#----------------------formatting-----------------------
print('\n', divider1, '\n')
print('Totals:', show_total_area, show_total_pop, '\n')
print(divider2)
