# https://adventofcode.com/2018/day/11
# --- Day 11: Chronal Charge ---
import math

def cellPower(x, y, sno):
    rid = x + 10
    pl = rid * y
    pl = pl + sno
    pl = pl * rid

    if pl < 99 or math.floor(pl / 100) == 0:
        pl = 0
    else:
        pl = math.floor(pl / 100) % 10

    return pl - 5

def gridPower(x, y, sno):
    gp = 0
    for xs in range(x, x + 3):
        for ys in range(y, y + 3):
            cp = cellPower(xs, ys, sno)
            #print('(X,Y) =  (' + str(xs) + ',' + str(ys) + ') Power = ' + str(cp))
            gp += cp

    return gp

def findBestGrid(sno):
    gp = gridPower(0, 0, sno)
    cellPosition = (0, 0)
    for x in range(1, 298):
        for y in range(1, 298):
            cgp = gridPower(x, y, sno)
            if cgp > gp:
                gp = cgp
                cellPosition = (x, y)

    return (gp, cellPosition)


#print('-- Grid power --')
#print(gridPower(33, 45, 18))
#print(gridPower(21, 61, 42))

gp, cellPosition = findBestGrid(18)
x, y = cellPosition
print('(X,Y) =  (' + str(x) + ',' + str(y) + ') Power = ' + str(gp))

gp, cellPosition = findBestGrid(42)
x, y = cellPosition
print('(X,Y) =  (' + str(x) + ',' + str(y) + ') Power = ' + str(gp))

gp, cellPosition = findBestGrid(8561)
x, y = cellPosition
print('(X,Y) =  (' + str(x) + ',' + str(y) + ') Power = ' + str(gp))

