from math import inf, floor
class Item:
    def __init__(self, name):
        self.name = name;
        self.cals = inf
        self.cost = inf
        self.costPerCal = 0

    def __repr__(self):
        return "%s" %(self.name)
    def setCals(self, newCals):
        self.cals = newCals

    def setCost(self,newCost):
        self.cost = newCost
class Menu:
    def __init__(self):
        self.items = []
        self.numItems = 0
    def addItem(self, item):
        self.items.append(item)
        self.numItems += 1

order = {}
n = input().strip()
w = input().strip()
menu = Menu()
for i in range(int(n)):
    V, C, S = input().strip().split()
    Y = Item(S)
    Y.setCals(int(C))
    Y.setCost(int(V))
    Y.costPerCal = int(V) / int(C)
    menu.addItem(Y)

def minCalSolve(capacity, Amenu):
    minCals = [[0 for i in range(capacity+1)] for j in range(Amenu.numItems +1)]
    for p in range(capacity +1):
        minCals[0][p] = inf
    for q in range(1, Amenu.numItems +1):
        minCals[q][0] = 0
    for i in range(1, Amenu.numItems +1):
        for j in range(1, capacity +1):
            if Amenu.items[i-1].cost > j:
                minCals[i][j] = minCals[i-1][j]
            else:
                minCals[i][j] = min(minCals[i-1][j],
                                    minCals[i][j - Amenu.items[i-1].cost] + Amenu.items[i-1].cals)

    if minCals[Amenu.numItems][capacity] == inf:
        print("Not possible to spend exactly:", capacity)
        return None
    else:
        print("Possible to spend exactly:", capacity)
        print("Minimum calories:", minCals[Amenu.numItems][capacity])
        TARGETVAL = capacity
        i = Amenu.numItems

        while(i >= 0 and TARGETVAL != 0):
            if(minCals[i][TARGETVAL] == minCals[i-1][TARGETVAL]):
                i -= 1

            if(minCals[i][TARGETVAL] != minCals[i-1][TARGETVAL]):
                if(Amenu.items[i-1] in order):
                    order[Amenu.items[i-1]] += 1
                else:
                    order[Amenu.items[i-1]] = 1

                TARGETVAL -= Amenu.items[i-1].cost
        for i in order:
            print(i, order.get(i))

minCalSolve(int(w), menu)



