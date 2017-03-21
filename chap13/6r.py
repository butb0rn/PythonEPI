import sys

def findNearestRepetition(l):
    nearestRep = sys.maxint
    rep = {}
    for i in range(len(l)):
        if l[i] in rep.keys():
            nearestRep = min(nearestRep, i - rep[l[i]])
        rep[l[i]] = i

    return nearestRep


s = ["all", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "result"]
print findNearestRepetition(s)
