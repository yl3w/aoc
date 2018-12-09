# Day 9
# https://adventofcode.com/2018/day/9

class Node:
    def __init__(self, marble):
        self.marble = marble
        self._left = self
        self._right = self

    def insert(self, node):
        self._left._right = node
        node._left = self._left
        node._right = self
        self._left = node

    def remove(self):
        self._left._right = self._right
        self._right._left = self._left

    def moveBack(self, positions):
        if positions == 0:
            return self

        return self._left.moveBack(positions - 1)

    def moveForward(self, positions):
        if positions == 0:
            return self

        return self._right.moveForward(positions - 1)


def insert(current, marble):
    if marble % 23 == 0:
        nodeToRemove = current.moveBack(7)
        nodeToRemove.remove()
        score = marble + nodeToRemove.marble
        del nodeToRemove
        return (current.moveBack(6), score)
    else:
        insertAtNode = current.moveForward(2)
        nc = Node(marble)
        insertAtNode.insert(nc)
        return (nc, 0)

def play(playerCount, marbleCount):
    scores = [0]*playerCount
    current = Node(0)
    for marble in range(1, marbleCount + 1):
        current, score = insert(current, marble)
        if marble % playerCount == 0:
            scores[-1] += score
        else:
            scores[(marble % playerCount) - 1] += score

    return scores

for playerCount, marbleCount in [(9, 25), (10, 1618), (13, 7999), (17, 1104), (21, 6111), (30, 5807), (411, 71058), (411, 7105800)]:
    scores = play(playerCount, marbleCount)
    print('Winning score for ' + str(playerCount) + ' and turns ' + str(marbleCount) + ' is ' + str(max(scores)))
