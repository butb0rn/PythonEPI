class LinkedList(object):
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode


def hasOverLappingLists(l1, l2):
    def getLen(p):
        count = 0
        while p:
            p = p.next
            count += 1
        return count

    def jumpToNode(l, count):
        while count > 0:
            l = l.next
            count -= 1
        return l

    if not l1 or not l2: return None
    p1 = l1
    p2 = l2
    p1Len = getLen(p1)
    p2Len = getLen(p2)

    if p1Len > p2Len:
        count = p1Len - p2Len
    else:
        count = p2Len - p1Len

    #assume p1 is larger LinkedList
    p1 = jumpToNode(p1, count)
    p2 = l2
    while p1 and p2 and p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1


a = LinkedList("a")
b = LinkedList("b")
c = LinkedList("c")
d = LinkedList("d")
e = LinkedList("e")
a.next = b
b.next = d
c.next = d
d.next = e

l1 = LinkedList(0, a)
l2 = LinkedList(0, c)
# print hasOverLappingLists(l1, l2).data
