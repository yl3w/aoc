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

for ssi in [9, 5, 18, 2018, 209231]:
    print(''.join(map(str,scoresFrom(ssi))))
