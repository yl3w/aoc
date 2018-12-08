# --- Day 8: Memory Maneuver ---
# https://adventofcode.com/2018/day/8

def readSpecification(filename):
    with open(filename) as f:
        return list(map(int, f.readline().split()))


class Node:
    def __init__(self, input, index):
        self.__children__ = []
        self.__metadata__ = []
        self.__startIndex__ = index
        childrenCount = input[index]
        metadataCount = input[index + 1]
        cp = index + 2
        if childrenCount != 0:
            for child in range(childrenCount):
                child = Node(input, cp)
                cp = child.__lastIndex__
                self.__children__.append(child)
        
        if metadataCount != 0:
            self.__metadata__ = input[cp:cp + metadataCount]

        self.__lastIndex__ = cp + metadataCount

    def print(self, depth=0):
        print('Depth ' + str(depth))
        print('Children ' + str(len(self.__children__)))
        print('Metadata ' + str(self.__metadata__))
        print('---------')
        for child in self.__children__:
            child.print(depth + 1)

    def sumMetadata(self):
        totalMetadata = sum(self.__metadata__)
        for child in self.__children__:
            totalMetadata += child.sumMetadata()

        return totalMetadata



#specs = readSpecification('sample.input')
specs = readSpecification('production.input')

root = Node(specs, 0)
#root.print()
print('Total meta data is ' + str(root.sumMetadata()))

