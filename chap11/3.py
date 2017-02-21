from heapq import *

def sortAlmostSortedArray(s, k):
    minHeap = []
    for i in range(k):
        heappush(minHeap, s[i])

    idx = k
    while idx < len(s):
        heappush(minHeap, s[idx])
        print heappop(minHeap)
        idx += 1

    while minHeap:
        print heappop(minHeap)



sortAlmostSortedArray([3,-1,2,6,5,4,8],2)
