# project4-buildings.py

buildings = []
prompt = 'Name an interesting building or type QUIT to stop: '
name = input(prompt)
while name != 'QUIT':
    buildings.append(name)
    name = input(prompt)
for building in buildings:
    print(building)
