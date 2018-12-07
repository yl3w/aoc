# --- Day 6: Chronal Coordinates ---
# https://adventofcode.com/2018/day/6

import pprint
import random

def readSpecification(filename):
    coordinates = []
    with open(filename) as f:
        for line in f:
            coordinates.append(tuple(map(int, line.split(','))))

    return coordinates

def computeGrid(coordinates):
    lx = min(map(lambda t: t[0], coordinates))
    ly = min(map(lambda t: t[1], coordinates))
    rx = max(map(lambda t: t[0], coordinates))
    ry = max(map(lambda t: t[1], coordinates))

    return (lx, ly, rx, ry)

def setOrigin(coordinates, lx, ly):
    return list(map(lambda t: (t[0]-lx, t[1]-lx), coordinates))

def findClosest(point, coordinates):
    x, y = point
    distances = list(map(lambda t: abs(t[0] - x) + abs(t[1] - y), coordinates))
    minimum = min(distances)
    pointsAtMinimum = distances.count(minimum)
    if pointsAtMinimum == 1:
        index = distances.index(minimum)
        return coordinates[index]

    return None

def computeOwnership(point, coordinates, rx, ry):
    area = 0
    for i in range(rx + 1):
        for j in range(ry + 1):
            if point == findClosest((i,j), coordinates):
                area = area + 1

    return area

def findLargestArea(coordinates, rx, ry):
    def isPointBoxedIn(coordinate):
        x, y = coordinate
        return x > 0 and x < rx and y > 0 and y < ry

    def doesPointEscape(coordinate):
        x, y = coordinate
        edgeCoordinates = [(0, y), (x, 0), (rx, y), (x, ry)]
        closest = [findClosest(c, coordinates) for c in edgeCoordinates]
        return coordinate in closest

    boxedInCoordinates = filter(lambda t: not doesPointEscape(t), filter(isPointBoxedIn, coordinates))
    areas = [computeOwnership(c, coordinates, rx, ry) for c in boxedInCoordinates]
    return max(areas)


coordinates = readSpecification('production.input')
print('Total coordinates is ' + str(len(coordinates)))
lx, ly, rx, ry = computeGrid(coordinates)
coordinates = setOrigin(coordinates, lx, ly)
rx, ry = (rx-lx, ry-ly)
print('Found largest area with size ' + str(findLargestArea(coordinates, rx, ry)))

