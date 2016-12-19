def findSubs(n, k):
    return getSubK(n, 1, k)

def getSubK(n, idx, k):
    if k < 1: return [[]]
    p = []
    for i in range(idx,n+1):
        p += [[i]+x for x in getSubK(n, i+1, k-1)]
    return p

print findSubs(5,3)
