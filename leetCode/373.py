from heapq import *

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = start+end

    def __lt__(self, other):
        return not self.sum < other.sum

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        minHeap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if len(minHeap) < k:
                    heappush(minHeap, Interval(nums1[i], nums2[j]))
                elif (nums1[i]+nums2[j]) < minHeap[0].sum:
                    heappush(minHeap, Interval(nums1[i], nums2[j]))
                    heappop(minHeap)

        return [[i.start, i.end] for i in minHeap]



'''
def kSmallestPairs(self, nums1, nums2, k):
    queue = []
    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
    push(0, 0)
    pairs = []
    while queue and len(pairs) < k:
        _, i, j = heapq.heappop(queue)
        pairs.append([nums1[i], nums2[j]])
        push(i, j + 1)
        if j == 0:
            push(i + 1, 0)
    return pairs
'''
