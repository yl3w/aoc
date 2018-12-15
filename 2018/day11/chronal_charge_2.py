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

def networkCellPower(sno, size):
    cells = {}
    for xs in range(1 + size):
        for ys in range(1 + size):
            cells[(xs, ys)] = cellPower(xs, ys, sno)

    return cells

def powerForGridAt(x, y, size, baselinePower, ncp):
    gp = baselinePower[(x, y)] - ncp[x+size - 1 , y+size - 1]
    for ys in range(y, y + size):
        gp += ncp[(x + size - 1, ys)]

    for xs in range(x, x + size):
        gp += ncp[(xs, y + size - 1)]

    return gp


def gridPower(size, baselinePower, ncp):
    power = {}
    for xs in range(1, 301 - size + 1):
        for ys in range(1, 301 - size + 1):
            power[(xs, ys)] = powerForGridAt(xs, ys, size, baselinePower, ncp)

    return power

def findBestGrid(sno):
    baselinePower = ncp = networkCellPower(sno, 300)
    (pt, gp) = max(ncp.items(), key=lambda t: t[1])
    bs = 1
    for size in range(2, 301):
        baselinePower = gridPower(size, baselinePower, ncp)
        (cpt, cgp) = max(baselinePower.items(), key=lambda t: t[1])
        if cgp > gp:
            pt = cpt
            gp = cgp
            bs = size
        else:
            break

    return (pt, gp, bs)

for sno in [18, 42, 8561]:
    cellPosition, gp, size = findBestGrid(sno)
    x, y = cellPosition
    print('Grid serial number ' + str(sno) + ' BEST (X,Y) =  (' + str(x) + ',' + str(y) + ') Power = ' + str(gp) + ' size is ' + str(size))

