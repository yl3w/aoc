# Day 9
# https://adventofcode.com/2018/day/9

def insert(circle, current, marble):
    if marble % 23 == 0:
        score = marble + circle[current - 7]
        del circle[current - 7]
        if current - 7 > -1:
            return (current - 7, score)
        elif current - 7 == -1:
            return (0, score)
        else:
            return (len(circle) + current - 6, score)
    elif current == len(circle) - 1:
        circle.insert(1, marble)
        return (1, 0)
    else:
        circle.insert(current + 2, marble)
        return (current + 2, 0)

def play(playerCount, marbleCount):
    scores = [0]*playerCount
    circle = [0]
    current = 0
    for marble in range(1, marbleCount + 1):
        current, score = insert(circle, current, marble)
        if False:
            lp = [circle[i] if i != current else '(' + str(circle[i]) + ')' for i in range(0, len(circle))]
            print('------------------------------')
            print('After marble ' + str(marble) + ' current is ' + str(current))
            print(lp)
        if marble % playerCount == 0:
            scores[-1] += score
        else:
            scores[(marble % playerCount) - 1] += score

    return scores

for playerCount, marbleCount in [(9, 25), (10, 1618), (13, 7999), (17, 1104), (21, 6111), (30, 5807), (411, 71058)]:
    scores = play(playerCount, marbleCount)
    print('Winning score for ' + str(playerCount) + ' and turns ' + str(marbleCount) + ' is ' + str(max(scores)))
