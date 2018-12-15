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

def score(gen, init):
    score = 0
    for i in range(len(gen)):
        if gen[i] == '#':
            score += (i + init)

    return score


filename = 'sample.input'
#filename = 'production.input'
gen, notes = readSpecification(filename)

print(str(0) + ': ' + gen)
firstPotvalue = gen.index('#')
for i in range(20):
    gen = nextGeneration(gen, notes)
    lh = gen.index('#')
    firstPotvalue += lh - 4
    rh = gen.rindex('#')
    gen = gen[lh:rh+1]
    value = score(gen, firstPotvalue)
    print(str(i + 1) + ':(' + str(value) + ') ' + gen)


