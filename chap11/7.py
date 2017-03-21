from heapq import *

class Entry(object):
    def __init__(self, value, rank):
        self.value = value
        self.rank = rank

    def __lt__(self, other):
        return self.rank < other.rank

class Stack(object):
    def __init__(self):
        self.timestamp = 0
        self.maxHeap = []

    def push(self, value):
        heappush(self.maxHeap, Entry(value, self.timestamp))
        self.timestamp -= 1

    def pop(self):
        return heappop(self.maxHeap)

    def peek(self):
        return self.maxHeap[0]


s = Stack()
s.push(5)
s.push(15)
s.push(19)
s.push(7)
print s.pop().value
print s.pop().value
print s.pop().value
print s.pop().value
