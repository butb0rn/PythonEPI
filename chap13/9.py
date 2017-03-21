def longestSub(l):
    d = {}
    longestDupFreeStartIdx = 0
    result = 0
    dupIdx = -1
    for i in range(len(l)):
        if l[i] in d.keys():
            dupIdx = d[l[i]]
        else:
            d[l[i]] = i
            dupIdx = -1
        if dupIdx != -1 and dupIdx >= longestDupFreeStartIdx:
            result = max(result, i - longestDupFreeStartIdx)
            longestDupFreeStartIdx = dupIdx + 1

    return max(result, len(l) - longestDupFreeStartIdx)

#
print longestSub(["f","s","f","e","t","w","e","n","w","e"])
