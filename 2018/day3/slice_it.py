# day 3 : no matter how you slice it
# https://adventofcode.com/2018/day/3
import re
import functools

def readSpecification(filename):
    """return a list of 3-tuple's, where each tuple is (identifier, (row, column), (width, height))"""
    specs = []
    pattern = re.compile(r"#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)$")
    with open(filename) as f:
        for line in f:
            m = pattern.match(line)
            if m:
                specs.append((int(m.group(1)), (int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5)))))

    return specs

# keep track of number of times a cell has been used
# we'll keep track of the identifier of the specification for each cell
# (2,3) -> [77,14,65] : in this instance the cell (2,3) is associated with 3 identifiers

def assignIdentifier(assignments, spec):
    identifier = spec[0]
    #print('Working with spec ' + str(spec))
    for row in range(spec[1][0], spec[1][0] + spec[2][0]):
        for col in range(spec[1][1], spec[1][1] + spec[2][1]):
            ids = assignments.get((row, col), [])
            ids.append(identifier)
            assignments[(row, col)] = ids
            #print('Assignments for ' + str((row, col)) + ' are ' + str(ids))


def assignIdentifiers(specs):
    assignments = {}
    for spec in specs:
        assignIdentifier(assignments, spec)
        #print('Assignments updates to ' + str(assignments))

    return assignments

def countMultiUseCells(assignments):
    return functools.reduce(lambda x, y: x + y, map(lambda t: 0 if len(t[1]) == 1 else 1, assignments.items()))

#specs = readSpecification("sample.input")
specs = readSpecification("production.input")
print('Total number of specifications is ' + str(len(specs)))
assignments = assignIdentifiers(specs)
print(countMultiUseCells(assignments))
