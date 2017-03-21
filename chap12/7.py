class MinMax(object):

    def __init__(self, minVal=None, maxVal=None):
        self.minVal = minVal
        self.maxVal = maxVal

    def buildMinMax(self, minVal, maxVal):
        if minVal < maxVal:
            return MinMax(minVal, maxVal)
        else:
            return MinMax(maxVal, minVal)

def findMinMax(arr):
    if len(arr) <= 1:
        return MinMax().buildMinMax(arr[0], arr[0])


    globalMinMax = MinMax().buildMinMax(arr[0], arr[1])
    for i in range(2, len(arr), 2):
        if i+1 < len(arr):
            localMinMax = MinMax().buildMinMax(arr[i], arr[i+1])
            globalMinMax = MinMax().buildMinMax(min(localMinMax.minVal, globalMinMax.minVal), max(localMinMax.maxVal, globalMinMax.maxVal))


    if len(arr) % 2 != 0:
        globalMinMax = MinMax(min(localMinMax.minVal, globalMinMax.minVal), max(localMinMax.minVal, globalMinMax.maxVal))

    return globalMinMax


arr = [3,12,19,5,1,-2,4]
res = findMinMax(arr)
print res.minVal, res.maxVal
