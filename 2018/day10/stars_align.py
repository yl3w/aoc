# day 10 - stars align
# https://adventofcode.com/2018/day/10

import re
from itertools import groupby, tee

def readSpecification(filename):
    with open(filename) as f:
        pattern = re.compile(r"position=<(.*),(.*)> velocity=<(.*),(.*)>")
        return list(map(lambda m:
            (int(m[1].strip()), int(m[2].strip()), int(m[3].strip()), int(m[4].strip())), [pattern.match(line) for line in f]))

def splitPointsAndVelocity(pandv):
    return (list(map(lambda pv: (pv[0], pv[1]), pandv)), list(map(lambda pv: (pv[2], pv[3]), pandv)))

def transition(points, velocity, duration):
    return list(map(lambda pv: (pv[0][0]+pv[1][0]*duration, pv[0][1]+pv[1][1]*duration), zip(points, velocity)))

def area(points):
    minx = min(map(lambda p: p[0], points))
    maxx = max(map(lambda p: p[0], points))
    
    miny = min(map(lambda p: p[1], points))
    maxy = max(map(lambda p: p[1], points))

    return (maxx - minx) * (maxy - miny)

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def printPoints(points):
    points.sort(key=lambda p: p[1])
    groupedByY = {k:list(v) for k, v in groupby(points, key=lambda p: p[1])}
    miny = min(map(lambda p: p[1], points))
    maxy = max(map(lambda p: p[1], points))
    minx = min(map(lambda p: p[0], points))

    for y in range(miny, maxy + 1):
        xs = list(sorted(set(map(lambda p: p[0], groupedByY[y]))))
        xs.insert(0, minx)
        for s, e in pairwise(xs):
            if s != e:
                print(' ' * (e - s - 1), end='')
            print('#', end='')
        print('')

#fname='sample.input'
fname='production.input'
points, velocity = splitPointsAndVelocity(readSpecification(fname))
duration = 0
currentArea = area(points)
minArea = currentArea
while minArea >= currentArea:
    duration += 1
    minArea = currentArea
    currentArea = area(transition(points, velocity, duration))

print('Found time, it is ' + str(duration - 1))
result = transition(points, velocity, duration - 1)
print('Result Area ' + str(area(result)))
printPoints(result)



