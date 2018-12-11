# day 10 - stars align
# https://adventofcode.com/2018/day/10

import re

def readSpecification(filename):
    with open(filename) as f:
        pattern = re.compile(r"position=<(.*),(.*)> velocity=<(.*),(.*)>")
        return list(map(lambda m:
            (int(m[1].strip()), int(m[2].strip()), int(m[3].strip()), int(m[4].strip())), [pattern.match(line) for line in f]))

def splitPointsAndVelocity(pandv):
    return (list(map(lambda pv: (pv[0], pv[1]), pandv)), list(map(lambda pv: (pv[2], pv[3]), pandv)))

def transition(points, velocity):
    return list(map(lambda pv: (pv[0][0]+pv[1][0], pv[0][1]+pv[1][1]), zip(points, velocity)))

def isValidText(points):
    return all([any([(x-1,y) in points, (x+1,y) in points, (x,y-1) in points, (x, y+1) in points]) for x, y in points])

def printPoints(points):
    miny = min(map(lambda p: p[1], points))
    maxy = max(map(lambda p: p[1], points))

    for r in range(miny, maxy + 1):
        positions = list(map(lambda p: p[0], sorted(filter(lambda p: p[1] == r, points), key=lambda p: p[0])))
        if len(positions) > 0:
            row = [' '] * (max(positions) + 1)
            for position in positions:
                row[position] = '#'
            print("".join(row))

fname='sample.input'
#fname='production.input'
points, velocity = splitPointsAndVelocity(readSpecification(fname))

index = 0
while index < 5 or isValidText(points):
    points = transition(points, velocity)
    index += 1


printPoints(points)


