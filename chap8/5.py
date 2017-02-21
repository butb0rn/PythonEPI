from r4 import hasOverLappingLists
from r3 import *

def overlappingLists(l1,l2):
    def getLen(node, fNode):
        count = 0
        while node != fNode:
            node = node.next
            count += 1
        return count

    def jumpToNode(l, count):
        while count > 0:
            l = l.next
            count -= 1
        return l

    r1 = hasCycle(l1)
    r2 = hasCycle(l2)

    if not r1 and not r2:
        return hasOverLappingLists(l1,l2)
    elif (not r1 and r2) or (r1 and not r2):
        return None

    temp = r2

    while True:
        temp = temp.next
        if (temp == r1 or temp == r2): break

    if temp != r1: return None


    l1Len = getLen(l1, r1)
    l2Len = getLen(l2, r2)
    
    if l1Len > l2Len:
        l1 = jumpToNode(l1, l1Len - l2Len)
    else:
        l2 = jumpToNode(l2, l2Len - l1Len)


    while l1 != l2 and l1 != r1 and l2 != r2:
        l1 = l1.next
        l2 = l2.next

    if l1 == l2: return l1

    return r1


a = LinkedList("a")
b = LinkedList("b")
c = LinkedList("c")
d = LinkedList("d")
e = LinkedList("e")
f = LinkedList("f")
a.next = b
b.next = d
c.next = d
d.next = e
e.next = f
f.next = e

l1 = LinkedList(0, a)
l2 = LinkedList(0, c)

print overlappingLists(l1,l2).data
