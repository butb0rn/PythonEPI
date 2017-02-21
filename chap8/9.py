class Node(object):
    def __init__(self, data, ne=None):
        self.data = data
        self.next = ne

def cyclicallyRightShiftList(l, k):
    if not l: return None
    tail = l
    lenList = 1

    while tail.next:
        lenList += 1
        tail = tail.next

    if (k % lenList == 0): return l

    tail.next = l
    shift = lenList - k
    while shift > 1:
        l = l.next
        shift -= 1

    newHead = l.next
    l.next = None

    return newHead

l = Node("a", Node("b", Node("c", Node("d", Node("e")))))
res = cyclicallyRightShiftList(l, 2)
while res:
    print res.data
    res = res.next
