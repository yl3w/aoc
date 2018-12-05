import functools
import itertools

def causeReaction(polymer, unit):
    if len(polymer) == 0:
        return unit

    lu = polymer[len(polymer) - 1]
    if unit != lu and unit.lower() == lu.lower():
            return polymer[:-1]

    return polymer + unit

def doReaction(polymer):
    return functools.reduce(causeReaction, polymer)

def dissimilarUnits(ut):
    lu = ut[0]
    ru = ut[1]
    if lu != ru and lu.upper() == ru.upper():
        return (lu.islower() and ru.isupper()) or (lu.isupper() and ru.islower())

    return True

def verifyPolymer(polymer):
    p1, p2 = itertools.tee(polymer)
    next(p2, None)
    if not functools.reduce(lambda s, u: s if not s else dissimilarUnits(u), zip(p1, p2), True):
        raise Exception('Found a bad polymer ' + polymer)

def removeUnit(polymer, unit):
    return polymer.replace(unit, '').replace(unit.upper(), '')

def doReactionWithBadUnit(polymer, unit):
    polymer = doReaction(removeUnit(polymer, unit))
    #printPolymer(polymer)
    return polymer

def printPolymer(polymer):
    print('Resulting polymer is ' + polymer)
    print('Length of resulting polymer is ' + str(len(polymer)))

def reactOnAllPolymers(filename):
    with open(filename) as f:
        for polymer in f:
            print('Length of polymer originally presented after reactions ' + str(len(doReaction(polymer.strip()))))
            length = min(map(lambda u: len(doReactionWithBadUnit(polymer.strip(), u)), 'abcdefghijklmnopqrstuvwxyz'))
            print('Found shortest polymer with length ' + str(length) + ' after eliminating bad unit')
 

polymer = "bbbBBBcC"

#printPolymer(doReaction(polymer))
reactOnAllPolymers('production.input')
