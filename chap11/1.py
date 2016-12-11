from heapq import *

class ArrayEntry:
    def __init__(self, value, arrayId):
        self.value = value
        self.arrayId = arrayId


def mergeSortedArrays(sortedArrays):
    minHeap = []
    heads = {}
    for i in range(len(sortedArrays)):
        if len(sortedArrays[i]) > 0:
            heappush(minHeap, ArrayEntry(sortedArrays[i][0], i))
            heads[i] = 1

    print " ".join(str(item.value) for item in minHeap)
    heappush(minHeap, ArrayEntry(-1, -1))
    heapify(minHeap)
    print " ".join(str(item.value) for item in minHeap)

    #
    # result = []
    # for _ in range(sum(map(len, l))):
    #     x = heappop(minHeap)
    #     result.append(x.value)
    #     smallestArray = sortedArrays[x.arrayId]
    #     smallestArrayHead = heads[x.arrayId]
    #     if smallestArrayHead < len(smallestArray):
    #         heappush(minHeap, ArrayEntry(smallestArray[smallestArrayHead], x.arrayId))
    #         heads[x.arrayId] = heads[x.arrayId] + 1
    #
    # return result

l = [[3,5,7], [0,6], [0,6,28]]
print mergeSortedArrays(l)
