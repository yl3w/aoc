# https://adventofcode.com/2018/day/14
# --- Day 14: Chocolate Charts ---

def makeRcps(score):
    rcps = []
    for d in str(score):
        rcps.append(int(d))
    return rcps

def scoresFrom(scoreStartIndex, outlook=10):
    rscores = [3, 7]
    e1 = 0
    e2 = 1
    
    while len(rscores) < scoreStartIndex + outlook:
        combined = rscores[e1] + rscores[e2]
        rscores.extend(makeRcps(combined))
        sl = len(rscores)
        te1 = (rscores[e1] + 1) % sl
        te2 = (rscores[e2] + 1) % sl
        if e1 + te1 > sl - 1:
            e1 = (e1 + te1) - sl 
        else:
            e1 = (e1 + te1)
    
        if (e2 + te2) > sl - 1:
            e2 = (e2 + te2) - sl
        else:
            e2 = (e2 + te2)


    return rscores[scoreStartIndex:scoreStartIndex+outlook]

def findPatternInScores(rscores, pattern, ci):
    if len(rscores) < len(pattern):
        return -1

    for i in range(ci, len(rscores)):
        cp = ''.join(map(str, rscores[i-len(pattern): i]))
        if cp == pattern:
            return i - 1

    return -1

def findPattern(pattern):
    rscores = [3, 7]
    e1 = 0
    e2 = 1
    checkIndex = 0

    patternIndex = findPatternInScores(rscores, pattern, checkIndex)
    while patternIndex == -1:
        checkIndex = len(rscores) - 1
        combined = rscores[e1] + rscores[e2]
        rscores.extend(makeRcps(combined))
        sl = len(rscores)
        te1 = (rscores[e1] + 1) % sl
        te2 = (rscores[e2] + 1) % sl
        if e1 + te1 > sl - 1:
            e1 = (e1 + te1) - sl 
        else:
            e1 = (e1 + te1)
    
        if (e2 + te2) > sl - 1:
            e2 = (e2 + te2) - sl
        else:
            e2 = (e2 + te2)
    
        patternIndex = findPatternInScores(rscores, pattern, checkIndex)


    return patternIndex - len(pattern) + 1

for ssi in [9, 5, 18, 2018, 209231]:
    print(''.join(map(str,scoresFrom(ssi))))

for p in ['51589', '01245', '92510', '59414', '209231']:
    print('Found pattern ' + p + ' after ' + str(findPattern(p)) + ' recipies')
