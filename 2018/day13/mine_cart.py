# https://adventofcode.com/2018/day/13
# --- Day 13: Mine Cart Madness ---

from functools import reduce
from itertools import groupby, chain

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
        self.crashed = False

    def move(self, grid):
        track = grid.trackAt(self.x, self.y)
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

        self.x += dx
        self.y += dy
    

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

    @staticmethod
    def verifyCartMove(c, cartsByStartPosition):
        oc = cartsByStartPosition.get((c.x, c.y), None)
        if oc and oc.x == c.x and oc.y == c.y:
            c.crashed = True
            oc.crashed = True
            for c in [c, oc]:
                print('Captured crash at (' + str(c.x) + ', ' + str(c.y) + ')')

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
        cartsByStartPosition = { (c.x, c.y): c for c in self.carts }
        groupedByRow = groupby(self.carts, key=lambda c: c.x)
        for _, carts in groupedByRow:
            carts = sorted(carts, key=lambda c: c.y)
            for c in carts:
                c.move(self)
                Grid.verifyCartMove(c, cartsByStartPosition)

        self.updateCrashes()
        self.removeCarts()

    def updateCrashes(self):
        cartsByPoints = {}
        for c in self.carts:
            carts = cartsByPoints.get((c.x, c.y), [])
            carts.append(c)
            cartsByPoints[(c.x, c.y)] = carts

        for c in chain.from_iterable(map(lambda t: t[1], filter(lambda t: len(t[1]) > 1, cartsByPoints.items()))):
            print('Captured crash at (' + str(c.x) + ', ' + str(c.y) + ')')
            c.crashed = True

    def removeCarts(self):
        self.carts = list(filter(lambda c: not c.crashed, self.carts))

    def cartsLeft(self):
        return len(self.carts)


def readSpecification(filename):
    g = Grid()
    with open(filename) as f:
        for line in f:
            g.addRow(line)

    g.processCarts()
    return g

def printSimulation(filename):
    g = readSpecification(filename)
    
    while g.cartsLeft() > 1:
        g.move()
    
    if g.cartsLeft() == 1:
        c = g.carts[0]
        print('Position of last remaining cart is (' + str(c.x) + ', ' + str(c.y) + ')')
    else:
        print('Uh Oh! all carts crashed')
    

#for filename in ['production.input', 'sample3.input', 'sample2.input', 'sample.input']:
for filename in ['test.input', 'test1.input', 'test2.input', 'production.input']:
    print('----------------------   Running ' + filename + '   --------------------------')
    printSimulation(filename)
