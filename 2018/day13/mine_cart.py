# https://adventofcode.com/2018/day/13
# --- Day 13: Mine Cart Madness ---

from functools import reduce
from itertools import groupby

class Cart:
    trackAndDirection = { '/' : {
                '^': '>',
                '<': 'v',
                '>': '^',
                'v': '<'
            }, '\\' : {
                '^': '<',
                '<': '^',
                '>': 'v',
                'v': '>'
            }
        }

    intersectionAndMove = { 'L' : {
                '^': (0, -1, '<'),
                '<': (1, 0, 'v'),
                'v': (0, 1, '>'),
                '>': (-1, 0, '^')
            }, 'S': {
                '^': (-1, 0, '^'),
                '<': (0, -1, '<'),
                '>': (0, 1, '>'),
                'v': (1, 0, 'v')
            }, 'R': {
                '^': (0, 1, '>'),
                '<': (-1, 0, '^'),
                '>': (1, 0, 'v'),
                'v': (0, -1, '<')
            }
        }

    directionAndMove = { '^' : (-1, 0), '<': (0, -1), '>': (0, 1), 'v': (1, 0) }
    intersectionOrder = 'LSR'

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.turnNext = 'L'

    def updateCart(self, grid):
        track = grid.trackAt(self.x, self.y)
        #print(track + ' '  + self.direction)
        if track == '+':
            dx, dy, direction = Cart.intersectionAndMove[self.turnNext][self.direction]
            self.direction = direction
            ti = Cart.intersectionOrder.index(self.turnNext)
            if ti == len(Cart.intersectionOrder) - 1:
                self.turnNext = Cart.intersectionOrder[0]
            else:
                self.turnNext = Cart.intersectionOrder[ti + 1]
        else:
            if track in Cart.trackAndDirection:
                self.direction = Cart.trackAndDirection[track][self.direction]

            dx, dy = Cart.directionAndMove[self.direction]

        #print(str(self.x) + ',' + str(self.y) + ' : ' + str(dx) + ',' + str(dy))
       
        self.x += dx
        self.y += dy

        #print(grid.trackAt(self.x, self.y))
    

    def position(self):
        return (self.x, self.y)

class Grid:
    cartsAndDirections = {'>': '-', '<': '-', '^': '|', 'v': '|'}

    def __init__(self):
        self.grid = []
        self.carts = []

    @staticmethod
    def cartsFacingDirection(direction, row):
        ys = []
        for i in range(len(row)):
            if row[i] == direction:
                ys.append(i)

        return (direction, ys)

    @staticmethod
    def makeCart(x, direction, ys):
        return list(map(lambda y: Cart(x, y, direction), ys))

    def processCarts(self):
        for x in range(len(self.grid)):
            cartsFacingDirection = map(lambda d: Grid.cartsFacingDirection(d, self.grid[x]), Grid.cartsAndDirections.keys())
            carts = map(lambda t: Grid.makeCart(x, t[0], t[1]), cartsFacingDirection)
            for cs in carts:
                self.carts.extend(cs)

    def addRow(self, r):
        self.grid.append(r)

    def trackAt(self, x, y):
        track = self.grid[x][y]
        if track in Grid.cartsAndDirections:
            return Grid.cartsAndDirections[track]

        return track

    def move(self):
        groupedByRow = groupby(self.carts, key=lambda c: c.x)
        for _, carts in groupedByRow:
            carts = sorted(carts, key=lambda c: c.y)
            for c in carts:
                c.updateCart(self)

    def collision(self):
        coordinates = set()
        for c in self.carts:
            pair = (c.x, c.y)
            if pair not in coordinates:
                coordinates.add(pair)
            else:
                return pair

        return None


def readSpecification(filename):
    g = Grid()
    with open(filename) as f:
        for line in f:
            g.addRow(line)

    g.processCarts()
    return g


#filename = 'sample.input'
filename = 'production.input'
g = readSpecification(filename)
while not g.collision():
    g.move()

print(g.collision())
