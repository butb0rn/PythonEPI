from heapq import *
import math

class Star(object):
    def __init__(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        self.distance = self.distance(x,y,z)

    def distance(self, x,y,z):
        return math.sqrt(x*x + y*y + z*z)

    def __le__(self, other):
        return not self.distance < other.distance


def findClosestKStarts(k, starts):
    maxHeap = []
    idx = 0
    while idx < len(starts):
        heappush(maxHeap, starts[idx])
        if len(maxHeap) > k:
            heappop(maxHeap)
        idx += 1
    maxHeap.sort()
    return maxHeap

s = [Star(1,1,1),Star(2,2,2), Star(3,3,3), Star(4,4,4), Star(5,5,5), Star(6,6,6), Star(7,7,7)]
print [x.distance for x in findClosestKStarts(4, s)]
