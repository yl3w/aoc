# --- Day 12: Subterranean Sustainability ---
# https://adventofcode.com/2018/day/12

from pprint import pprint

def readInitialState(f):
    line = f.readline()
    return line[line.index(': ') + len(': '):].strip()

def readNotes(f):
    notes = {}
    for line in f:
        sepIndex = line.index(' => ')
        pattern = line[:sepIndex].strip()
        post = line[sepIndex + len(' => ')].strip()
        notes[pattern] = post

    return notes

def readSpecification(filename):
    with open(filename) as f:
        initial = readInitialState(f)
        f.readline()
        notes = readNotes(f)

        return (initial, notes)

def nextGeneration(cg, notes):
    ng = '..'
    cg = '....' + cg + '....'
    for i in range(2, len(cg) - 2):
        pattern = cg[i-2:i+3]
        if pattern in notes:
            ng += notes[pattern]
        else:
            ng += '.'

    return ng

def score(garden, init):
    score = 0
    for i in range(len(garden)):
        if garden[i] == '#':
            score += (i + init)

    return score

def skipGenerations(pvd, ig, cg, mg):
    gd = cg - ig
    gl = mg - cg
    tailGenerations = gl % gd
    generationsToSkip = gl - tailGenerations

    return (pvd * generationsToSkip, tailGenerations)

def compact(potvalue, garden):
    lh = garden.index('#')
    rh = garden.rindex('#')
    potvalue += lh - 4
    garden = garden[lh:rh+1]
    return (potvalue, garden)

def performGenerations(garden, count):
    """Simulates generations until a cycle is found. Once the cycle is found, does some basic math to advance
    as many cycles as possible before simulating any remaining generations. Computes the first index of a live
    pot by keeping track of changes in live pot offset between first and last generation in cycle

    TODO: Turns out I wrote the code more generally than is necessary and the input I've results in a cycle of
    only 1. Is this generally true? Revisit a confirm"""

    history = {}

    currentFirstLivepot = garden.index('#')

    generation = 0
    # continue while not cycle is found
    while garden not in history and generation < count:
        history[garden] = (generation, currentFirstLivepot)
        currentFirstLivepot, garden = compact(currentFirstLivepot, nextGeneration(garden, notes))
        generation += 1

    remainingGenerations = count - generation
    if remainingGenerations > 0:
        # process the cycle quickly
        seeng, legacyFirstLivepot = history[garden]
        # TODO : Is this always 1?
        noOfGenerationsInCycle = (generation - seeng)

        countOfCycleRepetitions = remainingGenerations // noOfGenerationsInCycle
        # how far ahead can we go?
        if countOfCycleRepetitions > 0:
            # keep track of first live pot offset
            firstLivepotDelta = currentFirstLivepot - legacyFirstLivepot
            currentFirstLivepot += (firstLivepotDelta * countOfCycleRepetitions)
            remainingGenerations = remainingGenerations % noOfGenerationsInCycle

        for i in range(remainingGenerations):
            currentFirstLivepot, garden = compact(currentFirstLivepot, nextGeneration(garden, notes))

    return score(garden, currentFirstLivepot)


def mapByGeneration(generationByGarden):
    gardenByGeneration = {}
    return { generation : (garden, firstlivepot) for garden, (generation, firstlivepot) in generationByGarden.items() }


#filename = 'sample.input'
filename = 'production.input'
garden, notes = readSpecification(filename)

score = performGenerations(garden, 50000000000)
print('Score after 50000000000 generations is ' + str(score))

