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
    return functools.reduce(lambda s, u: s if not s else dissimilarUnits(u), zip(p1, p2), True)

def printPolymer(polymer):
    print('Resulting polymer is ' + polymer)
    print('Length of resulting polymer is ' + str(len(polymer)))
    print('Verifying polymer, Is polymer good? ' + str(verifyPolymer(polymer)))

def reactOnAllPolymers(filename):
    with open(filename) as f:
        for polymer in f:
            printPolymer(doReaction(polymer.strip()))


polymer = "bbbBBBcC"

#printPolymer(doReaction(polymer))
reactOnAllPolymers('production.input')
