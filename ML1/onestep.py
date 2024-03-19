import sys
l = sys.argv
l.pop(0)
w= int(l.pop(0))
h = int(l.pop(0))
bars = int(l.pop(0))
rewards = int(l.pop(bars*2))

def printgrid(g):
    for x in range(h):
        s = ""
        for a in g[x]:
            if a == "block":
                s += "----"
            else:
                s += "{:.2f}".format(a)
            s += " "
        print(s)

grid = []
for x in range(h):
    f = []
    for y in range(w):
        f.append(0.00)
    grid.append(f)

for a in range(bars):
    tempx = int(l.pop(0))
    tempy = int(l.pop(0))
    grid[tempx][tempy] = "block"


for a in range(rewards):
    tempx = int(l.pop(0))
    tempy = int(l.pop(0))
    tempval = float(l.pop(0))
    grid[tempx][tempy] = tempval

printgrid(grid)