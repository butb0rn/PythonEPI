def getMaxLenInterval(l):
    idx = 0
    maxLen = -1
    l.sort()
    for i in range(1,len(l)):
        if l[i] - l[i-1] > 1:
            maxLen = max(maxLen, i - idx)
            idx = i
    return max(maxLen, len(l)-idx)

# l = [3,-2,7,9,8,1,2,0,-1,5,8]
l = [3,-2,5,5,5,1,2,0,-1,5,5,5,6,7,8,10,11,4,9]
print getMaxLenInterval(l)
