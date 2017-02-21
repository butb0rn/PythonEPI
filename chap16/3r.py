def getPermutations(l):
    if len(l) < 1: return []
    res = []
    for i in range(len(l)):
        partialResult = getPermutations(l[:i] + l[i+1:])
        res += map(lambda x: [l[i]]+x,partialResult) or [[l[i]]]
    return res

print getPermutations([2,3,4])
